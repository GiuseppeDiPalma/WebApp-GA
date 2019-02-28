import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

def Function_Fitness(x, zeroBs):

    mat = np.array([
        [x[1], 0, x[2]],
        [x[3], x[4], 0],
        [0, x[5], x[6]]
    ])
    # crea matrice 3x6 e la riempie con 0
    proj = np.zeros((3, 6))
    # Ad ogni prima colonna della matrice creata in precedenza
    # la sostituisce con i nostri dati
    proj[:1] = zeroBs[:1]

    for i in range(1, 6):
        proj[:, i] = mat.dot(proj[:, i-1])
        # proj[:i] = mat * proj[:,i-1]
    y = sum(sum(abs(proj-zeroBs)))

    return y,


# def starmap(function, iterable):
    # for args in iterable:
    # yield function(*args)

def stampaGrafico(gen, valueArray):
    a = np.array(gen)
    b = np.array(valueArray)
    plt.title('Grafico fval')
    plt.xlabel('')
    plt.ylabel('fval')
    plt.plot(a, b)
    plt.grid(True)
    plt.show()


def stampaTuttiGrafici(gen, nevals, avg, std, minn, maxx):
    a = np.array(gen)
    b = np.array(nevals)
    c = np.array(avg)
    d = np.array(std)
    e = np.array(minn)
    f = np.array(maxx)

    plt.figure(1)
    # nevals
    plt.plot()
    plt.plot(a, b, color='red', marker='o')
    plt.xlabel('Num Generazione')
    plt.ylabel('Valore Nevals')
    plt.title('Nevals')
    plt.grid(True)

    plt.figure(2)
    # avg
    plt.plot()
    plt.xlabel('Num Generazione')
    plt.ylabel('Valore Media')
    plt.title('Avg')
    plt.plot(a, c)
    plt.grid(True)

    plt.figure(3)
    # std
    plt.plot()
    plt.xlabel('Num Generazione')
    plt.ylabel('Valore Std')
    plt.title('Std')
    plt.plot(a, d)
    plt.grid(True)


    plt.figure(4)
    # min
    plt.plot()
    plt.xlabel('Num Generazione')
    plt.ylabel('Valore Minimi')
    plt.title('Min')
    plt.plot(a, e)
    plt.grid(True)

    plt.figure(5)
    # max
    plt.plot()
    plt.xlabel('Num Generazione')
    plt.ylabel('Valore Massimi')
    plt.title('Max')
    plt.plot(a, f)
    plt.grid(True)

    plt.show()