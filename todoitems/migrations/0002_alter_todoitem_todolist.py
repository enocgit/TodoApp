# Generated by Django 4.1.4 on 2022-12-17 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_icon_color'),
        ('todoitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todolist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist.todolist'),
        ),
    ]