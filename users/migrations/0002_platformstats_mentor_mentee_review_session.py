# Generated by Django 5.1.5 on 2025-02-15 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_enhanced', models.IntegerField(default=0)),
                ('empowered_mentors', models.IntegerField(default=0)),
                ('global_community', models.IntegerField(default=0)),
                ('connections_built', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('attendance', models.CharField(max_length=10)),
                ('top_rated', models.BooleanField(default=False)),
                ('available_asap', models.BooleanField(default=False)),
                ('coaching', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='mentor_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.TextField()),
                ('goals', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
                ('assigned_mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('feedback', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mentee')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateTimeField()),
                ('session_notes', models.TextField(blank=True, null=True)),
                ('session_type', models.CharField(choices=[('1on1', '1-on-1'), ('group', 'Group')], max_length=50)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mentee')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mentor')),
            ],
        ),
    ]
