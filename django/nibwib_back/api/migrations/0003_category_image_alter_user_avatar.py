# Generated by Django 5.0.4 on 2024-04-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_bio_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='catgory/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='1640528661_1-abrakadabra-fun-p-serii-chelovek-na-avu-1.png', upload_to='avatar/'),
        ),
    ]