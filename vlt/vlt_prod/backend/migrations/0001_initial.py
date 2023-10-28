# Generated by Django 3.2.20 on 2023-09-04 12:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('brand_id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('categories_id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('order_quantity', models.PositiveIntegerField(max_length=10)),
                ('total_price', models.PositiveIntegerField()),
                ('order_status', models.CharField(max_length=10)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.brand')),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categories')),
            ],
        ),
        migrations.CreateModel(
            name='reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_id', models.PositiveIntegerField(max_length=100)),
                ('reminder_type', models.CharField(max_length=10)),
                ('comment', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=10)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.PositiveIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tracking',
            fields=[
                ('tracking_id', models.PositiveIntegerField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categories')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.order')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('purchase_id', models.PositiveIntegerField(max_length=100, primary_key=True, serialize=False)),
                ('total_price', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=10)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.brand')),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categories')),
                ('order_quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('payment_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('modified_date', models.DateField(default=datetime.date(2023, 9, 4))),
                ('amount_paid', models.PositiveSmallIntegerField()),
                ('next_date', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.order')),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.purchase')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user'),
        ),
        migrations.AddField(
            model_name='brand',
            name='categories_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categories'),
        ),
    ]
