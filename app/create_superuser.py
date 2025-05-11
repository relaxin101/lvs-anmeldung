import os
import django
from django.contrib.auth import get_user_model
#from anmeldung.models import Verbindung

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

User = get_user_model()

email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

if not User.objects.filter(email=email).exists():
    #Verbindung.objects.create(kuerzel='HES', name='K.Ö.St.V. Herulia Stockerau')
    User.objects.create_superuser(email=email, password=password, couleurname='Admin')#,verbindung=Verbindung.objects.first())
    print(f"Superuser '{email}' created.")
else:
    print(f"Superuser '{email}' already exists.")
