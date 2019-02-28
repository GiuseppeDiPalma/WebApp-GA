import array
import random
import sys
import numpy
import json


from deap import algorithms
from deap import base
from deap import benchmarks
from deap import creator
from deap import tools


import FitnessEAltre


# sys.argv[0] #nome eseguibile
# sys.argv[1] # nome file json
# sys.argv[2] #tipo algoritmo da usare
# sys.argv[3] #tipo dati da usare
Obs_T = [
    [60.2222, 38.1111, 35.8889, 43.6667, 55.7778, 68.2222],
    [28.1667, 15.2222, 8.1111, 13.6667, 13.4444, 19.5556],
    [12.1667, 7, 4.1111, 3.8889, 5.6667, 12.2222]
]

Obs_L50 = [
    [9.4444, 17.7778, 14, 5.5556, 11.6667, 4.2222],
    [3.1111, 5.2222, 2, 2.2222, 6.3333, 1.7778],
    [1.2222, 1.4444, 1.4444, 1.6667, 2.1111, 0.5556]
]

Obs_L100 = [
    [17.6667, 11.2222, 8.8889, 11.1111, 6.4444, 1.4444],
    [3.5556, 5, 2.5556, 3.2222, 1.7778, 1.2222],
    [1.1111, 1.4444, 1.5556, 1.6667, 0.7778, 0]
]


with open(sys.argv[1], 'r') as f:
    data = json.load(f)

tmp = data["dati"]

if tmp == 'T':
    print("DATI: "+ tmp)
    zeroBs = Obs_T
elif tmp == 'L50':
    print("DATI: "+ tmp)
    zeroBs = Obs_L50
elif tmp == 'L100':
    print("DATI: "+ tmp)
    zeroBs = Obs_L100
else:
    print("MANCA IL SET DI DATI ---> T | L50 | L100 ")

MIN_VALUE = int(data["min_value"])
MAX_VALUE = int(data["max_value"])
MIN_STRATEGY = float(data["min_strategy"])
MAX_STRATEGY = float(data["max_strategy"])
MU = int(data["mutation"]) # Mutazioni
cx_pb = float(data["cxpb"])  # CXPB  is the probability with which two individuals are crossed
mut_pb = float(data["mutpb"]) # MUTPB is the probability for mutating an individual
valureSelectTournSize = int(data["value_tournSize"]) # numero individui che partecipano a ciascuna selezione.
num_gen = int(data["pop_size"]) # numero di individui in una generazione

tipoAlgoritmo = data["tipoAlgoritmo"]
# # numeri dei valori da ottenere
IND_SIZE = 7
LAMBDA = 100
valueMateAlpha = 0.1
valueMutateC = 1.0 # parametro di apprendimento
valueMutateIndpb = 0.03 # Probabilità indipendente per ogni attributo da scambiare a un'altra posizione.

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# passaggio di individui
creator.create("Individual", array.array, typecode="d",
               fitness=creator.FitnessMin, strategy=None)
creator.create("Strategy", array.array, typecode="d")

# Generatore di individui
# La funzione di inizializzazione per una strategia di evoluzione 
# non è definita da DEAP. 
# La funzione di generazione seguente prende come argomento la 
# classe di individuo per istanziare, icls. Prende anche la classe 
# di strategia da utilizzare come strategia, scls. Gli argomenti 
# successivi sono i valori minimi e massimi per gli attributi 
# individuali e strategici. La strategia viene aggiunta nel 
# membro della strategia dell'individuo restituito.


def generateES(icls, scls, size, imin, imax, smin, smax):
    ind = icls(random.uniform(imin, imax) for _ in range(size))
    ind.strategy = scls(random.uniform(smin, smax) for _ in range(size))
    return ind

# La strategia controlla la deviazione standard della mutazione. 
# E' comune avere un limite inferiore sui valori in modo che 
# l'algoritmo non cada solo nello sfruttamento. Questo limite 
# inferiore viene aggiunto all'operatore di variazione dal seguente 
# decoratore.
def checkStrategy(minstrategy):
    def decorator(func):
        def wrappper(*args, **kargs):
            children = func(*args, **kargs)
            for child in children:
                for i, s in enumerate(child.strategy):
                    if s < minstrategy:
                        child.strategy[i] = minstrategy
            return children
        return wrappper
    return decorator


toolbox = base.Toolbox()

toolbox.register("individual", generateES, creator.Individual, creator.Strategy,
                 IND_SIZE, MIN_VALUE, MAX_VALUE, MIN_STRATEGY, MAX_STRATEGY)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Estensione dell'intervallo in cui è possibile attribuire i nuovi valori
# per ogni attributo su entrambi i lati degli attributi dei genitori.


toolbox.register("mate", tools.cxESBlend, alpha=valueMateAlpha)

toolbox.register("mutate", tools.mutESLogNormal, c=valueMutateC, indpb=valueMutateIndpb)

toolbox.register("select", tools.selTournament, tournsize=valureSelectTournSize)

# funzione per valutare
toolbox.register(
    "evaluate", lambda x: FitnessEAltre.Function_Fitness(x, zeroBs))

# l'inizializzatore viene decorato con i minimi della strategia
# per evitare di scendere troppo al di sotto di quel valore
toolbox.decorate("mate", checkStrategy(MIN_STRATEGY))
toolbox.decorate("mutate", checkStrategy(MIN_STRATEGY))


def main():
    print("nome dell'eseguibile: ", sys.argv[0])
    print("tipo di algoritmo da utilizzare: ", tipoAlgoritmo)
    random.seed()
    MU, LAMBDA = 10, 100
    pop = toolbox.population(n=MU)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    if tipoAlgoritmo == 'eaSimple':
        '''
eaSimple:
L'algoritmo prende in considerazione una popolazione e la evolve al suo posto usando il metodo varAnd()*

Parte di un algoritmo evolutivo che applica solo la parte di variazione(crossover e mutazione)Gli individui modificati
hanno la loro idoneità invalidata. Gli individui sono clonati, quindi la popolazione resituita è indipendente
dalla popolazione di input.

1. valuta gli individui con un fitness non valido
2. entra nel ciclo generazionale dove viene applicata la procedura di selezione per
   sostituire interamente la popolazione parentale. Il rapporto di sostituzione 1:1 di questo algoritmo
   richiede che la procedura di selezione sia stocastica e di selezionare più volte lo stesso individui

3. applica la funzione varAnd per produrre la popolazione di prossima generazione.
4. valuta i nuovi individui e calcola le statistiche su questa popolazione.
5 restituisce una tupla con la popolazione finale e un Logbook dell'evoluzione.
'''
        print("Sto eseguendo algoritmo eaSimple")
        pop, logbook = algorithms.eaSimple(
            pop, toolbox, cxpb=cx_pb, mutpb=mut_pb, ngen=num_gen, stats=stats, halloffame=hof)

    elif tipoAlgoritmo == 'eaMuPlusLambda':
        '''
eaMuPlusLambda:
l'algoritmo prende in considerazione una popolazione e la evolve al suo posto utilizzando la funzione varOr()*
come sopra solo che usa(crossover, mutazione o riproduzione)

La variazione procede in questo modo:
lambda_ iterazione, seleziona una delle tre operazione: crossover, mutazione o riproduzione.
Nel caso di un crossover, due individui sono selezionati a caso dalla popolazione parentale P_\mathrm{p}
quest individui sono clonati usando il metodo toolbox.clone() e poi accoppiati usando il metodo toolbox.mate().
SOlo il primo figlio viene aggiunto alla popolazione proble P_\mathrm{o}
il secondo figlio viene scartato.
Nel caso di una mutazione, un individuo viene selezionato a caso da P_\mathrm{r}
viene clonato e poi mutato usando il metodo toolbox.mutate().
Nel caso di una riproduzione, un individuo è selezionato a caso da P_\mathrm{p}
clonato e aggiunto a P_\mathrm{o}.

Questa variazione si chiama Or perchè una prole non risulterà mai da entrambe le operazioni 
crossover e mutazione
la somma di entrambe le probabilità deve essere in [0,1], la probabilita di riproduzione è 1 -cxpb -mutpb

1. vengono valutate le persone che hanno un'idonetà non valida.
2. il ciclo evolutivo inizia producendo i figli della popolazione, i figli sono generati dalla funzione varOr().
3. la prole viene poi valutata e la popolazione di nuova generazione viene selezionata
sia dalla prole che dalla popolazione.
'''
        print("Sto eseguendo algoritmo eaMuCommaLambda")
        pop, logbook = algorithms.eaMuCommaLambda(
            pop, toolbox, mu=MU, lambda_=LAMBDA, cxpb=cx_pb, mutpb=mut_pb, ngen=num_gen, stats=stats, halloffame=hof)

    elif tipoAlgoritmo == 'eaMuCommaLambda':
        '''
eaMuCommaLambda ( usa varOr() ):
1. vengono valutate le generazioni che hanno un'idonèta 
2. il ciclo evolutivo inizia producendo i figli della popolazione, i figli 
sono generati dalla funzione varOr(). La prole viene poi valutata e la nuova generazione
di popolazione viene solezionata solo dalla prole
3. quando vengono fatte le generazioni ngen, l'algoritmo restituisce una tupla con la
popolazione finale e un logbook del'evoluzione.

NOTA: è necessario tenere d'occhio il rapporto lambda:mu è di 1:!, poichè una selezione
non elastica non comporta lacuna selezione in quanto l'operatore seleziona gli individui labda da un pool di mu.
'''
        print("Sto eseguendo algoritmo eaMuPlusLambda")
        pop, logbook = algorithms.eaMuPlusLambda(
            pop, toolbox, mu=MU, lambda_=LAMBDA, cxpb=cx_pb, mutpb=mut_pb, ngen=num_gen, stats=stats, halloffame=hof)
    else:
        print("valore dell'algoritmo sbagliato")


    # print("HALL OF FAME:\n", hof)

    listaProva = []
    listaProva.append(hof)
    arrayHOF = []
    for i in range(0, 7):
        arrayHOF.append(listaProva[0][0][i])

    # print(arrayHOF)
    avg_list = []
    avg_list.append(logbook)
    
    arrayGen = []
    arrayNevals = []
    arrayAvg = []
    arrayStd = []
    arrayMin = []
    arrayMax = []

    for i in range(0,len(logbook)):
        arrayGen.append(avg_list[0][i]["gen"])
        arrayNevals.append(avg_list[0][i]["nevals"])
        arrayAvg.append(avg_list[0][i]["avg"])
        arrayStd.append(avg_list[0][i]["std"])
        arrayMin.append(avg_list[0][i]["min"])
        arrayMax.append(avg_list[0][i]["max"])
    
    with open('risultato.json', 'w') as f:
        json.dump(arrayGen, f, ensure_ascii=True, indent=4)
    
    print(arrayHOF)
    # for i in range(0,len(arrayMax)):
    #     print("{x: ",i ,",y: ", arrayMax[i],"},")
    # sono già ordinati come escono dal logbook
    # FitnessEAltre.stampaGrafico(arrayGen, arrayHOF)
    # FitnessEAltre.stampaTuttiGrafici(arrayGen, arrayNevals, arrayAvg, arrayStd, arrayMin, arrayMax)

    return pop, logbook, hof


if __name__ == "__main__":
    main()


# salvare i risutati contenuti in list python in risultati.json
# eseguire lo script python da server.js

# in server js deve prendere il rile risultato.json e mandarlo all'app
# il codicejava sull'app deve generare il grafico