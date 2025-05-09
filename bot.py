
import os
from telegram import Update, Poll, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

# تحميل الأسئلة من ملف
def load_questions_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
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

# عند استلام ملف
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_path = "received_questions.txt"
    await file.download_to_drive(file_path)
    await update.message.reply_text("📥 تم استلام الملف، جاري معالجة الأسئلة...")

    questions = load_questions_from_file(file_path)
    for q, opts, correct in questions:
        await context.bot.send_poll(
            chat_id=update.effective_chat.id,
            question=q,
            options=opts,
            type=Poll.QUIZ,
            correct_option_id=correct,
            is_anonymous=False
        )
        await asyncio.sleep(2)

# أمر البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أرسل لي ملف نصي (.txt) يحتوي على الأسئلة بالتنسيق المناسب، وسأحوّله لاختبار تفاعلي.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.FILE_EXTENSION("txt"), handle_document))
app.run_polling()

