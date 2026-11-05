# sqlite-isolation-replay

## Français

Rejouer lectures et écritures concurrentes WAL SQLite.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sqlite_isolation_replay examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Deux connexions réelles sur un fichier WAL ; étapes contrôlées sans sommeil : lecture, écriture non validée, commit concurrent, échec de promotion puis nouvelle lecture.

### Limites

Scénario local mono-processus déterministe ; ni cluster ni benchmark de contention.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Replay concurrent SQLite WAL reads and writes.

Synthetic data; no network access or secret required.

```sh
python -m sqlite_isolation_replay examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Two actual connections on a WAL file; controlled steps without sleeps: read, uncommitted write, concurrent commit, failed upgrade, fresh read.

### Limits

Deterministic local single-process scenario; no cluster or contention benchmark.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir lecturas y escrituras concurrentes WAL SQLite.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sqlite_isolation_replay examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Dos conexiones reales a archivo WAL; pasos controlados sin esperas: lectura, escritura no confirmada, commit concurrente, promoción fallida y nueva lectura.

### Límites

Escenario local determinista de un proceso; sin clúster ni benchmark de contención.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/isolation.html
