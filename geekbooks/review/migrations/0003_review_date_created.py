# Generated by Django 4.0.6 on 2022-11-02 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_book_user_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]