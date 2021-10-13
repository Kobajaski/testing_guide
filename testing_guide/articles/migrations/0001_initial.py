# Generated by Django 3.2.8 on 2021-10-13 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('category', models.TextField(choices=[('Dev', 'Dev'), ('DevOps', 'DevOps'), ('Feel Good', 'Feel Good'), ('BIM', 'BIM'), ('Makers', 'Makers'), ('Agile', 'Agile'), ('UX/UI', 'UX/UI'), ('Data', 'Data'), ('SSI', 'SSI'), ('Industrie', 'Industrie')], verbose_name='Category')),
                ('content', models.BinaryField(verbose_name='Content')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
