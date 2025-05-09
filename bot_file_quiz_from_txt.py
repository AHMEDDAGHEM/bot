
import os
from telegram import Update, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

# تحميل الأسئلة من ملف نصي
def load_questions(filename="questions.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read().strip().split("\n\n")
        questions = []
        for block in raw:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                q = lines[0]
                opts = [line[3:].strip() for line in lines[1:5]]
                correct = int(lines[5].split()[-1]) - 1
                questions.append((q, opts, correct))
        return questions

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("جارٍ إرسال الأسئلة...")

    questions = load_questions()
    chat_id = update.message.chat_id

    for q, options, correct in questions:
        await context.bot.send_poll(
            chat_id=chat_id,
            question=q,
            options=options,
            type=Poll.QUIZ,
            correct_option_id=correct,
            is_anonymous=False
        )
        await asyncio.sleep(2)  # مهلة بين كل سؤال والتالي

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
