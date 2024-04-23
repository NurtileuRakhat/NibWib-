# Generated by Django 5.0.4 on 2024-04-22 14:43

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Adres ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(choices=[('1', 'ADANA'), ('2', 'ADIYAMAN'), ('3', 'AFYONKARAHД°SAR'), ('4', 'AДћRI'), ('5', 'AMASYA'), ('6', 'ANKARA'), ('7', 'ANTALYA'), ('8', 'ARTVД°N'), ('9', 'AYDIN'), ('10', 'BALIKESД°R'), ('11', 'BД°LECД°KK'), ('12', 'BД°NGГ–L'), ('13', 'BД°TLД°S'), ('14', 'BOLU'), ('15', 'BURDUR'), ('16', 'BURSA'), ('17', 'Г‡ANAKKALE'), ('18', 'Г‡ANKIRI'), ('19', 'Г‡ORUM'), ('20', 'DENД°ZLД°'), ('21', 'DД°YARBAKIR'), ('22', 'EDД°RNE'), ('23', 'ELAZIДћ'), ('24', 'ERZД°NCAN'), ('25', 'ERZURUM'), ('26', 'ESKД°ЕћEHД°R'), ('27', 'GAZД°ANTEP'), ('28', 'GД°RESUN'), ('29', 'GГњMГњЕћHANE'), ('30', 'HAKKARД°'), ('31', 'HATAY'), ('32', 'ISPARTA'), ('33', 'MERSД°N'), ('34', 'Д°STANBUL'), ('35', 'Д°ZMД°R'), ('36', 'KARS'), ('37', 'KASTAMONU'), ('38', 'KAYSERД°'), ('39', 'KIRKLARELД°'), ('40', 'KIRЕћEHД°R'), ('41', 'KOCAELД°'), ('42', 'KONYA'), ('43', 'KГњTAHYA'), ('44', 'MALATYA'), ('45', 'MANД°SA'), ('46', 'KAHRAMANMARAЕћ'), ('47', 'MARDД°N'), ('48', 'MUДћLA'), ('49', 'MUЕћ'), ('50', 'NEVЕћEHД°R'), ('51', 'NД°ДћDE'), ('52', 'ORDU'), ('53', 'RД°ZE'), ('54', 'SAKARYA'), ('55', 'SAMSUN'), ('56', 'SД°Д°RT'), ('57', 'SД°NOP'), ('58', 'SД°VAS'), ('59', 'TEKД°RDAДћ'), ('60', 'TOKAT'), ('61', 'TRABZON'), ('62', 'TUNCELД°'), ('63', 'ЕћANLIURFA'), ('64', 'UЕћAK'), ('65', 'VAN'), ('66', 'YOZGAT'), ('67', 'ZONGULDAK'), ('68', 'AKSARAY'), ('69', 'BAYBURT'), ('70', 'KARAMAN'), ('71', 'KIRIKKALE'), ('72', 'BATMAN'), ('73', 'ЕћIRNAK'), ('74', 'BARTIN'), ('75', 'ARDAHAN'), ('76', 'IДћDIR'), ('77', 'YALOVA'), ('78', 'KARABГјK'), ('79', 'KД°LД°S'), ('80', 'OSMANД°YE'), ('81', 'DГњZCE')], max_length=50)),
                ('street', models.CharField(max_length=150)),
                ('address', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ModelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, default='1640528661_1-abrakadabra-fun-p-serii-chelovek-na-avu-1.png', upload_to='avatar/')),
                ('isCustomer', models.BooleanField(default=True)),
                ('address', models.ManyToManyField(blank=True, related_name='user_addresses', to='UserApp.modeladdress')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]