# Generated by Django 4.2.11 on 2024-05-07 13:36

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('fullName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='offline', max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('createdBy', models.CharField(max_length=100)),
                ('modifiedBy', models.CharField(max_length=100)),
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
        migrations.CreateModel(
            name='Message',
            fields=[
                ('chatId', models.BigAutoField(primary_key=True, serialize=False)),
                ('chats', models.TextField(blank=True, max_length=1024, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(choices=[('read', 'read'), ('unread', 'unread'), ('delivered', 'delivered'), ('typing', 'typing')], max_length=10)),
                ('createdBy', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
                ('fromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('toUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagId', models.UUIDField(default=uuid.uuid4)),
                ('tagged', models.SlugField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('threadId', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=1024, null=True)),
                ('fileComment', models.FileField(upload_to='')),
                ('imageComment', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied', to='whatsappServiceApi.message')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('statusId', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomId', models.BigAutoField(primary_key=True, serialize=False)),
                ('roomName', models.CharField(max_length=100)),
                ('icon', models.ImageField(null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_admin', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldPassword', models.CharField(max_length=150)),
                ('newPassword', models.CharField(max_length=150)),
                ('confirmPassword', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=100)),
                ('resetUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
