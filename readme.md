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