# Generated by Django 4.1 on 2022-09-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=225)),
                ('company', models.CharField(max_length=225)),
                ('total_modules', models.IntegerField()),
            ],
            options={
                'unique_together': {('course_name', 'company')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('manager_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCourseActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('completed_modules', models.IntegerField(default=0)),
                ('is_started', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('quiz_completed', models.BooleanField(default=False)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.person')),
            ],
            options={
                'unique_together': {('user', 'course')},
            },
        ),
    ]
