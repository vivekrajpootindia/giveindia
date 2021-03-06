# Generated by Django 3.1 on 2020-08-04 14:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000000)])),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current'), ('BasicSavings', 'BasicSavings')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TransferAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_amount', models.IntegerField(default=0)),
                ('transfered_at', models.DateTimeField()),
                ('transfer_from_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_account', to='giveindiaapi.account')),
                ('transfer_to_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_account', to='giveindiaapi.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='type_of',
            field=models.ManyToManyField(to='giveindiaapi.AccountType'),
        ),
    ]
