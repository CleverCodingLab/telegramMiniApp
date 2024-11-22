from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

WEBAPP_URL = "https://clevercodinglab.github.io/telegramMiniApp/"  # Replace with your GitHub Pages URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle referral
    if context.args and context.args[0].startswith('ref_'):
        referrer_id = context.args[0].split('ref_')[1]
        # Store referral info in context.bot_data or a database
        
    # Create WebApp button
    keyboard = [
        [InlineKeyboardButton("🎮 Play Game", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎮 Welcome to Point Tracker!\n\n"
        "Click the button below to start playing and earning points!",
        reply_markup=reply_markup
    )

async def main():
    # Initialize bot with your token
    application = Application.builder().token('7825902112:AAG-ht_9DsAjHkft47vQ2-3aInrOQxHlctw').build()
    
    # Add handlers
    application.add_handler(CommandHandler('start', start))
    
    # Start the bot
    print("Bot is running...")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())