import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
import threading
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Flask app pour garder le bot actif
app = Flask(__name__)

@app.route('/')
def home():
    return f"Bot actif et opérationnel depuis {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Token du bot (sécurisé via les variables d'environnement)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Médias
INTRO_VIDEO = "https://drive.google.com/uc?export=download&id=1NREjyyYDfdgGtx4r-Lna-sKgpCHIC1ia"
MAIN_IMAGE = "https://i.ytimg.com/vi/KolFup7TxOM/hq720.jpg"
BOTTOM_IMAGE = "https://aviator.com.in/wp-content/uploads/2024/04/Aviator-Predictor-in-India.png"

PAYMENT_PROOF_IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Circle_sign_2.svg/1024px-Circle_sign_2.svg.png"
] * 5

INFO_IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Circle_sign_2.svg/1024px-Circle_sign_2.svg.png"
] * 5

def create_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎯 Informations sur les bots", callback_data='info_bots')],
        [InlineKeyboardButton("💰 Retrait du casino", callback_data='casino_withdrawal')],
        [InlineKeyboardButton("📱 Contacter l'expert", url="https://t.me/judespronos")]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_program_button():
    keyboard = [[InlineKeyboardButton("🚀 OBTENIR LE PROGRAMME MAINTENANT", url="https://t.me/judespronos")]]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=INTRO_VIDEO,
            caption="🎮 Découvrez notre méthode révolutionnaire ! 🎰"
        )

        message = f"""🎯 BILL GATES, BONJOUR ❗️

Je suis un programmeur vénézuélien et je connais la combine pour retirer l'argent du jeu des casinos.

✅ 1800 personnes ont déjà gagné avec moi. Et je peux vous garantir en toute confiance que vous gagnerez.

💫 Vous pouvez gagner de l'argent sans rien faire, car j'ai déjà fait tout le programme pour vous.

🔥 Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y')}"""

        await update.message.reply_photo(
            photo=MAIN_IMAGE,
            caption=message,
            reply_markup=create_keyboard()
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=BOTTOM_IMAGE,
            caption="🏆 Rejoignez les gagnants dès aujourd'hui !"
        )

        logger.info(f"Nouvel utilisateur: {update.effective_user.id}")

    except Exception as e:
        logger.error(f"Erreur lors du démarrage: {e}")

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        if query.data == 'casino_withdrawal':
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="""🎰 PREUVES DE PAIEMENT RÉCENTES 🎰

💎 Ces retraits ont été effectués dans les dernières 24 heures
✨ Nos utilisateurs gagnent en moyenne 500€ par jour
⚡️ Méthode 100% automatisée et garantie
🔒 Aucun risque de perte

👇 Voici les preuves en images 👇"""
            )
            
            media_group = [InputMediaPhoto(media=url) for url in PAYMENT_PROOF_IMAGES]
            await context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
            
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="🌟 Prêt à commencer votre succès ?",
                reply_markup=create_program_button()
            )

        elif query.data == 'info_bots':
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="""🤖 NOTRE TECHNOLOGIE UNIQUE 🤖

✅ Intelligence artificielle avancée
🎯 Taux de réussite de 98.7%
💫 Mise à jour quotidienne des algorithmes
⚡️ Plus de 1800 utilisateurs satisfaits

👇 Découvrez notre système en images 👇"""
            )
            
            media_group = [InputMediaPhoto(media=url) for url in INFO_IMAGES]
            await context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
            
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="🚀 Prêt à révolutionner vos gains ?",
                reply_markup=create_program_button()
            )

        logger.info(f"Bouton {query.data} cliqué par l'utilisateur {update.effective_user.id}")

    except Exception as e:
        logger.error(f"Erreur lors du traitement du bouton: {e}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Une erreur est survenue. Veuillez réessayer."
        )

def keep_alive():
    def run():
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
    thread = threading.Thread(target=run)
    thread.start()

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_button))
        keep_alive()
        logger.info("Bot démarré avec succès!")
        application.run_polling()
    except Exception as e:
        logger.critical(f"Erreur fatale: {e}")
        raise

if __name__ == '__main__':
    main()
