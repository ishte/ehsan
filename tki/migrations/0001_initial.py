# Generated by Django 4.0.6 on 2022-07-18 06:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tki.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('fullname', models.CharField(blank=True, max_length=60, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('id', models.CharField(default=tki.models.customer_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('mobile_no', models.CharField(max_length=13)),
                ('otp', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('project_id', models.CharField(default=tki.models.project_detail_id, editable=False, help_text='This is The Project Id', max_length=10, primary_key=True, serialize=False)),
                ('project_detail', models.CharField(help_text='Enter Type (like website /app)', max_length=100)),
                ('booking_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Enter Booking amount', max_digits=10)),
                ('total_project_value', models.DecimalField(decimal_places=2, default=0.0, help_text='Enter Total Project Value (in ₹)', max_digits=10)),
                ('project_booking_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.CharField(default=tki.models.team_name_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('designation', models.CharField(blank=True, max_length=80, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image/')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Teamsa', to='tki.projectdetail')),
                ('team', models.ManyToManyField(blank=True, related_name='team_lista', to='tki.teamname')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Teama', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_meeting', models.CharField(blank=True, max_length=250, null=True)),
                ('planning', models.CharField(blank=True, max_length=250, null=True)),
                ('requirements', models.CharField(blank=True, max_length=250, null=True)),
                ('design_ui_ux', models.CharField(blank=True, max_length=250, null=True)),
                ('framework', models.CharField(blank=True, max_length=250, null=True)),
                ('approval', models.CharField(blank=True, max_length=250, null=True)),
                ('development', models.CharField(blank=True, max_length=250, null=True)),
                ('testing', models.CharField(blank=True, max_length=250, null=True)),
                ('release', models.CharField(blank=True, max_length=250, null=True)),
                ('handover', models.CharField(blank=True, max_length=250, null=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_tacker', to='tki.projectdetail')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_project_value', models.DecimalField(blank=True, decimal_places=2, help_text='Enter remaing amount', max_digits=10, null=True)),
                ('booking_amount', models.DecimalField(blank=True, decimal_places=2, help_text='Enter remaing amount', max_digits=10, null=True)),
                ('total_paid', models.DecimalField(blank=True, decimal_places=2, help_text='Enter Total Paid Amount (in ₹)', max_digits=10, null=True)),
                ('enter_amount', models.DecimalField(blank=True, decimal_places=2, help_text='Enter remaing amount', max_digits=10, null=True)),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pd', to='tki.projectdetail')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pi', to='tki.projectdetail')),
            ],
        ),
    ]