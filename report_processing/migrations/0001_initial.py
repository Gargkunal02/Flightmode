# Generated by Django 4.0.4 on 2022-04-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentValidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_report', models.FileField(blank=True, null=True, upload_to='reports_PDF')),
                ('send_message', models.CharField(blank=True, max_length=250, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]