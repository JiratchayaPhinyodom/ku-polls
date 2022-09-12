from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='the ending date for voting.'
                                       , blank=True, null=True)
        )
    ]
