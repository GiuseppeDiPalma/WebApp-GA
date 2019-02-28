from django.db import models

# Create your models here.

class Stats(models.Model):
    POP_SIZE = (
        ('100','100'),
        ('200','200'),
        ('300','300'),
        ('400','400'),
        ('500','500'),
        ('600','600'),
        ('700','700'),
        ('800','800'),
        ('900','900'),
    )

    MUTATION_RATE = (
        ('0%','0%'),
        ('1%','1%'),
        ('2%','2%'),
        ('3%','3%'),
        ('4%','4%'),
        ('5%','5%'),
        ('10%','10%'),
        ('20%','20%'),
        ('30%','30%'),
        ('40%','40%'),
        ('50%','50%'),
        ('75%','75%'),
        ('100%','100%'),
    )

    MUTATION_SIZE = (
        ('0%','0%'),
        ('1%','1%'),
        ('2%','2%'),
        ('3%','3%'),
        ('4%','4%'),
        ('5%','5%'),
        ('10%','10%'),
        ('20%','20%'),
        ('30%','30%'),
        ('40%','40%'),
        ('50%','50%'),
        ('75%','75%'),
        ('100%','100%'),
    )

    popSize = models.CharField(max_length=3, choices=POP_SIZE)
    mutationRate = models.CharField(max_length=4, choices=MUTATION_RATE)
    mutationSize = models.CharField(max_length=4, choices=MUTATION_SIZE)

    data = models.DateTimeField(auto_now=False, auto_now_add=True)