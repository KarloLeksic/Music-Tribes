# Generated by Django 4.0.3 on 2022-05-08 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_tribe_chieftain'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tribe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.tribe'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Chatbox',
        ),
    ]