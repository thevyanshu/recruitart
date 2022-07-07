# Generated by Django 4.0.5 on 2022-07-06 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('job_title', models.ManyToManyField(to='app1.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('remuneration', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_designation', models.CharField(max_length=255)),
                ('current_location', models.CharField(max_length=255)),
                ('preferred_designation', models.CharField(max_length=255)),
                ('preferred_location', models.CharField(max_length=255)),
                ('current_salary', models.CharField(max_length=255)),
                ('expected_salary', models.CharField(max_length=255)),
                ('can_join', models.CharField(choices=[('Immediately', 'Immediately'), ('15 Days', '15 Days'), ('1 Month', '1 Month'), ('2 Month', '2 Months'), ('3 Month', '3 months')], default='1', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('alternate_mobile', models.IntegerField()),
                ('total_experience', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('pg_name', models.CharField(max_length=255)),
                ('ug_name', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('resume', models.FileField(upload_to='resume')),
                ('jobpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.jobpost')),
            ],
        ),
    ]