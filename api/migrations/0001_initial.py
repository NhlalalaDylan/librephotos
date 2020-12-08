# Generated by Django 2.1.2 on 2020-11-15 18:49

import api.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('scan_directory', models.CharField(db_index=True, max_length=512)),
                ('avatar', models.ImageField(null=True, upload_to='avatars')),
                ('nextcloud_server_address', models.CharField(default=None, max_length=200, null=True)),
                ('nextcloud_username', models.CharField(default=None, max_length=64, null=True)),
                ('nextcloud_app_password', django_cryptography.fields.encrypt(models.CharField(default=None, max_length=64, null=True))),
                ('nextcloud_scan_directory', models.CharField(db_index=True, max_length=512, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='AlbumAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('created_on', models.DateTimeField(db_index=True)),
                ('gps_lat', models.FloatField(blank=True, null=True)),
                ('gps_lon', models.FloatField(blank=True, null=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
                ('owner', models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=512, null=True)),
                ('date', models.DateField(db_index=True, null=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
                ('location', django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_index=True, null=True)),
                ('owner', models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=512)),
                ('geolocation_level', models.IntegerField(db_index=True, null=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=512)),
                ('thing_type', models.CharField(db_index=True, max_length=512, null=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('created_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
                ('public', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='faces')),
                ('image_path', models.FilePathField()),
                ('person_label_is_inferred', models.NullBooleanField(db_index=True)),
                ('person_label_probability', models.FloatField(db_index=True, default=0.0)),
                ('location_top', models.IntegerField()),
                ('location_bottom', models.IntegerField()),
                ('location_left', models.IntegerField()),
                ('location_right', models.IntegerField()),
                ('encoding', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LongRunningJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.PositiveIntegerField(choices=[(1, 'Scan Photos'), (2, 'Generate Event Albums'), (3, 'Regenerate Event Titles'), (4, 'Train Faces')])),
                ('finished', models.BooleanField(default=False)),
                ('failed', models.BooleanField(default=False)),
                ('job_id', models.CharField(db_index=True, max_length=36, unique=True)),
                ('queued_at', models.DateTimeField(default=datetime.datetime.now)),
                ('started_at', models.DateTimeField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(default=api.models.get_default_longrunningjob_result)),
                ('started_by', models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('kind', models.CharField(choices=[('USER', 'User Labelled'), ('CLUSTER', 'Cluster ID'), ('UNKNOWN', 'Unknown Person')], max_length=10)),
                ('mean_face_encoding', models.TextField()),
                ('cluster_id', models.IntegerField(null=True)),
                ('account', models.OneToOneField(default=None, null=True, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('image_path', models.CharField(db_index=True, max_length=512)),
                ('image_hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('thumbnail_tiny', models.ImageField(upload_to='thumbnails_tiny')),
                ('thumbnail_small', models.ImageField(upload_to='thumbnails_small')),
                ('thumbnail_big', models.ImageField(upload_to='thumbnails_big')),
                ('square_thumbnail', models.ImageField(upload_to='square_thumbnails')),
                ('square_thumbnail_tiny', models.ImageField(upload_to='square_thumbnails_tiny')),
                ('square_thumbnail_small', models.ImageField(upload_to='square_thumbnails_small')),
                ('square_thumbnail_big', models.ImageField(upload_to='square_thumbnails_big')),
                ('image', models.ImageField(upload_to='photos')),
                ('added_on', models.DateTimeField(db_index=True)),
                ('exif_gps_lat', models.FloatField(blank=True, null=True)),
                ('exif_gps_lon', models.FloatField(blank=True, null=True)),
                ('exif_timestamp', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('exif_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('geolocation_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_index=True, null=True)),
                ('captions_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_index=True, null=True)),
                ('search_captions', models.TextField(blank=True, db_index=True, null=True)),
                ('search_location', models.TextField(blank=True, db_index=True, null=True)),
                ('favorited', models.BooleanField(db_index=True, default=False)),
                ('hidden', models.BooleanField(db_index=True, default=False)),
                ('public', models.BooleanField(db_index=True, default=False)),
                ('encoding', models.TextField(default=None, null=True)),
                ('owner', models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
                ('shared_to', models.ManyToManyField(related_name='photo_shared_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='face',
            name='person',
            field=models.ForeignKey(on_delete=models.SET(api.models.get_unknown_person), related_name='faces', to='api.Person'),
        ),
        migrations.AddField(
            model_name='face',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=models.SET(api.models.get_unknown_person), related_name='faces', to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumuser',
            name='cover_photos',
            field=models.ManyToManyField(related_name='album_user_cover_photos', to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumuser',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumuser',
            name='photos',
            field=models.ManyToManyField(to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumuser',
            name='shared_to',
            field=models.ManyToManyField(related_name='album_user_shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumthing',
            name='cover_photos',
            field=models.ManyToManyField(related_name='album_thing_cover_photos', to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumthing',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumthing',
            name='photos',
            field=models.ManyToManyField(to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumthing',
            name='shared_to',
            field=models.ManyToManyField(related_name='album_thing_shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumplace',
            name='cover_photos',
            field=models.ManyToManyField(related_name='album_place_cover_photos', to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumplace',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=models.SET(api.models.get_deleted_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumplace',
            name='photos',
            field=models.ManyToManyField(to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumplace',
            name='shared_to',
            field=models.ManyToManyField(related_name='album_place_shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumdate',
            name='photos',
            field=models.ManyToManyField(to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumdate',
            name='shared_to',
            field=models.ManyToManyField(related_name='album_date_shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumauto',
            name='photos',
            field=models.ManyToManyField(to='api.Photo'),
        ),
        migrations.AddField(
            model_name='albumauto',
            name='shared_to',
            field=models.ManyToManyField(related_name='album_auto_shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='albumuser',
            unique_together={('title', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='albumthing',
            unique_together={('title', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='albumplace',
            unique_together={('title', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='albumdate',
            unique_together={('date', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='albumauto',
            unique_together={('timestamp', 'owner')},
        ),
        migrations.RemoveField(
            model_name='albumplace',
            name='cover_photos'
        ),
        migrations.RemoveField(
            model_name='albumthing',
            name='cover_photos'
        ),
        migrations.RemoveField(
            model_name='albumuser',
            name='cover_photos'
        )
    ]
