# Telegram Casino Bot

Un bot Telegram pour la gestion automatisée de gains casino.

## Configuration Requise

- Python 3.11+
- Un token de bot Telegram
- Un compte Render

## Installation

1. Clonez le repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Créez un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances
```bash
pip install -r requirements.txt
```

4. Configurez les variables d'environnement
```bash
cp .env.example .env
# Modifiez le fichier .env avec vos propres valeurs
```

## Déploiement sur Render

1. Connectez-vous à votre compte Render
2. Créez un nouveau Web Service
3. Connectez votre repository GitHub
4. Configurez le service :
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `python main.py`
5. Ajoutez les variables d'environnement dans Render :
   - `TELEGRAM_TOKEN`
   - `PORT`

## Développement Local

```bash
python main.py
```

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
