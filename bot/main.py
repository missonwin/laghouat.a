from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# دالة الترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 أهلاً بك في *Max Trade Bot* 💹\n"
        "🚀 هذا البوت يساعدك في الحصول على إشارات تداول دقيقة.\n"
        "📊 استخدم الأزرار أو الأوامر للبدء.\n\n"
        "💬 تذكر: التداول مسؤوليتك الشخصية."
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

# تشغيل البوت
app = Application.builder().token("").build()
app.add_handler(CommandHandler("start", start))

print("✅ البوت يعمل الآن...")
app.run_polling()