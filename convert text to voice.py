import os
from gtts import gTTS
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext



TOKEN = "" # Insert token of your bot



async def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message when the user starts the bot."""
    await update.message.reply_text("Hello! Send me any text, and I will convert it into speech.")

async def text_to_speech(update: Update, context: CallbackContext) -> None:
    """Converts received text into an audio file and sends it back."""
    text = update.message.text
    tts = gTTS(text, lang='en')  # Set default language to English
    tts.save("output.mp3")
    
    # Send the audio file back to the user
    with open("output.mp3", "rb") as audio:
        await update.message.reply_audio(audio)
    
    # Remove the file after sending
    os.remove("output.mp3")

def main():
    """Main function to run the bot."""
    app = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_speech))

    # Run the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
