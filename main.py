import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# Initialisation de l'application Flask
app = Flask(__name__)

# Token du bot (ajout du token fourni)
TELEGRAM_TOKEN = '7184666905:AAFd2arfmIFZ86cp9NNVp57dKkH6hAVi4iM'
bot = Bot(token=TELEGRAM_TOKEN)

# Correction de l'avertissement en ajoutant un worker
dispatcher = Dispatcher(bot, None, workers=1)

# Commande /start
def start(update, context):
    message = (
        "Bonjour. Je m'appelle Mustafa Zulu 💻\n"
        "Mon équipe et moi-même avons développé un algorithme de programme "
        "qui calcule le prochain coef dans le jeu Aviator avec une précision de 99,997% ✅\n"
        "Nous vous apprendrons à utiliser ce programme pour gagner 120 000 dès aujourd'hui 💰💰\n"
        "Écrivez-moi et je vous donnerai le programme 🎁\n"
        "👉@moustaphalux👈"
    )
    update.message.reply_text(message)

# Gérer les messages texte
def echo(update, context):
    update.message.reply_text("Merci de votre message ! Utilisez /start pour en savoir plus.")

# Ajout des handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Route pour la racine afin d'éviter les erreurs 404
@app.route('/', methods=['GET'])
def home():
    return 'Bot Telegram est en ligne !'

# Route pour recevoir les mises à jour Telegram
@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Point d'entrée principal
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT)
