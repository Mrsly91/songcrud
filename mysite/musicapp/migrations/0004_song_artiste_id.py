# Generated by Django 4.1.2 on 2022-10-29 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_remove_song_artiste_alter_lyric_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
    ]
