from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')
                 ),
                ('title', models.TextField()),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
