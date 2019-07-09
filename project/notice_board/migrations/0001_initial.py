# Generated by Django 2.2.1 on 2019-07-08 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication', models.CharField(choices=[('1', 'Best'), ('2', 'Good'), ('3', 'Could be better'), ('4', 'Bad')], default=None, max_length=2)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=3)),
                ('additional_care', models.BooleanField(default=False, null=True)),
                ('sociability_to_human', models.CharField(max_length=30)),
                ('sociability_to_pets', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localization', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=6)),
                ('active', models.BooleanField(default=True, null=True)),
                ('pet_kind', models.CharField(max_length=5)),
                ('contact_number', models.CharField(max_length=11)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('localization',),
            },
        ),
    ]
