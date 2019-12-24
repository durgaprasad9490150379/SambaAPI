# Generated by Django 2.2.1 on 2019-12-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('expiry_days', models.PositiveIntegerField()),
                ('no_expiry', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('dn', models.CharField(max_length=255)),
                ('objectClass', models.CharField(max_length=255)),
                ('cn', models.CharField(max_length=255)),
                ('sn', models.CharField(max_length=255)),
                ('givenName', models.CharField(max_length=255)),
                ('instanceType', models.CharField(max_length=255)),
                ('whenCreated', models.CharField(max_length=255)),
                ('whenChanged', models.CharField(max_length=255)),
                ('displayName', models.CharField(max_length=255)),
                ('uSNCreated', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('badPwdCount', models.CharField(max_length=255)),
                ('codePage', models.CharField(max_length=255)),
                ('countryCode', models.CharField(max_length=255)),
                ('badPasswordTime', models.CharField(max_length=255)),
                ('lastLogoff', models.CharField(max_length=255)),
                ('lastLogon', models.CharField(max_length=255)),
                ('primaryGroupID', models.CharField(max_length=255)),
                ('accountExpires', models.CharField(max_length=255)),
                ('logonCount', models.CharField(max_length=255)),
                ('sAMAccountName', models.CharField(max_length=255)),
                ('sAMAccountType', models.CharField(max_length=255)),
                ('userPrincipalName', models.CharField(max_length=255)),
                ('objectCategory', models.CharField(max_length=255)),
                ('pwdLastSet', models.CharField(max_length=255)),
                ('userAccountControl', models.CharField(max_length=255)),
                ('uSNChanged', models.CharField(max_length=255)),
                ('memberOf', models.CharField(max_length=255)),
                ('distinguishedName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('userou', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('mail_address', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
            ],
        ),
    ]
