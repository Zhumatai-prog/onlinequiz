# Generated by Django 3.2.4 on 2021-06-20 21:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210620_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'), ('Option5', 'Option5')], max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
