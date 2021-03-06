# Generated by Django 2.1.4 on 2018-12-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popSize', models.CharField(choices=[('100', ''), ('200', ''), ('300', ''), ('400', ''), ('500', ''), ('600', ''), ('700', ''), ('800', ''), ('900', '')], max_length=3)),
                ('mutationRate', models.CharField(choices=[('0%', ''), ('1%', ''), ('2%', ''), ('3%', ''), ('4%', ''), ('5%', ''), ('10%', ''), ('20%', ''), ('30%', ''), ('40%', ''), ('50%', ''), ('75%', ''), ('100%', '')], max_length=4)),
                ('mutationSize', models.CharField(choices=[('0%', ''), ('1%', ''), ('2%', ''), ('3%', ''), ('4%', ''), ('5%', ''), ('10%', ''), ('20%', ''), ('30%', ''), ('40%', ''), ('50%', ''), ('75%', ''), ('100%', '')], max_length=4)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
