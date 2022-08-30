# Generated by Django 2.2.16 on 2022-08-29 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220829_1407'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
    ]
