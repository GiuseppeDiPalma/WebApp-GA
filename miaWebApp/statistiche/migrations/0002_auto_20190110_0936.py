# Generated by Django 2.1.4 on 2019-01-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistiche', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='mutationRate',
            field=models.CharField(choices=[('0%', '0%'), ('1%', '1%'), ('2%', '2%'), ('3%', '3%'), ('4%', '4%'), ('5%', '5%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], max_length=4),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mutationSize',
            field=models.CharField(choices=[('0%', '0%'), ('1%', '1%'), ('2%', '2%'), ('3%', '3%'), ('4%', '4%'), ('5%', '5%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], max_length=4),
        ),
        migrations.AlterField(
            model_name='stats',
            name='popSize',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('700', '700'), ('800', '800'), ('900', '900')], max_length=3),
        ),
    ]
