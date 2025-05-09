
import os
from telegram import Update, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا! أرسل لي سؤال اختيار من متعدد بهذا التنسيق:\n"
        "السؤال؟\nA) اختيار أول\nB) اختيار ثاني\nC) اختيار ثالث\nD) اختيار رابع\n*الصحيح 2"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    try:
        lines = text.split('\n')
        question = lines[0]
        options = [line[3:].strip() for line in lines[1:5]]
        correct = int(lines[5].split()[-1]) - 1

        await update.message.reply_poll(
            question=question,
            options=options,
            type=Poll.QUIZ,
            correct_option_id=correct,
            is_anonymous=False
        )
    except Exception as e:
        await update.message.reply_text(
            "⚠️ تأكد من تنسيق السؤال بهذا الشكل:\n"
            "السؤال؟\nA) ...\nB) ...\nC) ...\nD) ...\n*الصحيح 2"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
