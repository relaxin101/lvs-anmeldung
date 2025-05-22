# Setup
1. Env file kopieren und aufsetzen
    ```bash
    cp .env.example .env
    ```

2. .env anpassen (z.B. email zeug, admin user, etc.)


3. Docker-Compose starten
    ```bash
    docker compose up -d
    ````

4. Browser öffnen

    - Basic form [localhost:8000](localhost:8000)
    - Admin panel [localhost:8000/admin](localhost:8000/admin)


# Prod Setup
Wiederhole 1. & 2. (statt `.env` -> `.env.prod`)

> ![Warning] **kryptographisch garantiert zufälligen SECRET_KEY benutzen**
> Bspw. so`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

```bash
docker-compose -f docker-compose.prod.yml up --build
```
