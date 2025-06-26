
from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@example.com',
            password=make_password('GaXtNaBaR.15'),
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
