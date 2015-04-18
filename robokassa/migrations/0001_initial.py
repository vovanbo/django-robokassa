# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('InvId', models.IntegerField(db_index=True, verbose_name='Номер заказа')),
                ('OutSum', models.CharField(verbose_name='Сумма', max_length=15)),
                ('created_at', models.DateTimeField(verbose_name='Дата и время получения уведомления', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Уведомление об успешном платеже',
                'verbose_name_plural': 'Уведомления об успешных платежах (ROBOKASSA)',
            },
        ),
    ]
