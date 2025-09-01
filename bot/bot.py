from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from utils import weekly_summary, some_stats
import db
# from database import db


TOKEN = "telegram-token"

# ----------------- Bot Commands -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 *Hello, and welcome to WakaTrackr!*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "I'm here to help you track your coding habits effortlessly.\n"
        "By connecting your WakaTime account, I’ll send you:\n\n"
        "📅 *Daily & Weekly Summaries*\n"
        "💻 *Languages You've Used*\n"
        "⏱️ *Time Spent Coding*\n"
        "📈 *Productivity Trends*\n\n"
        "Use /setkey <your_wakatime_api> to store your API key and get started! 🫡"
    )

    await update.message.reply_text(welcome_message, parse_mode="Markdown")

    keyboard = [
        ["📅 Daily Summaries", "📊 Last 7 Day Summaries"],
        ["📈 Some Stats", "ℹ️ About"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👇 Choose an option:", reply_markup=reply_markup)

async def setkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not context.args:
        await update.message.reply_text("❌ Please provide your API key. Example: /setkey waka_xxx")
        return

    api_key = context.args[0]
    try:
        db.save_api_key(user_id, api_key)
        await update.message.reply_text("✅ Your API key has been saved successfully!")
    except Exception as e:
        print(f"Error saving API key: {e}")
        await update.message.reply_text("❌ Failed to save your API key. Please try again.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🤖 *WakaTrackr Info*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "👤 Creator: llyas\n"
        "🔗 GitHub: [github.com/llyas36](https://github.com/llyas36)\n"
        "🔗 Twitter: [x.com/llyas__](https://x.com/llyas__)\n\n"
        "System integrity: stable.\n"
        "Purpose: track code. stay consistent.\n"
        "Enjoyment: optional.\n"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

# ----------------- Stats Commands -----------------
async def some(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    api_key = db.get_api_key(user_id)
    if not api_key:
        await update.message.reply_text("❌ You must set your API key first using /setkey")
        return

    machines, editors, os = some_stats(api_key)  # accept api_key

    message = "📊 *Your Coding Stats*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    message += "🖥️ *Machines Used:*\n"
    for m in machines:
        message += f"• `{m['name']}` → {m['text']} 🔸 *Usage:* {m['percent']}%\n"

    message += "\n📝 *Editors:*\n"
    for e in editors:
        message += f"• `{e['name']}` → {e['text']} 🔸 *Usage:* {e['percent']}%\n"

    message += "\n🧠 *Operating Systems:*\n"
    for o in os:
        message += f"• `{o['name']}` → {o['text']} 🔸 *Usage:* {o['percent']}%\n"

    await update.message.reply_text(message, parse_mode="Markdown")

async def day7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    api_key = db.get_api_key(user_id)
    if not api_key:
        await update.message.reply_text("❌ You must set your API key first using /setkey")
        return

    activity, languages, projects = weekly_summary(api_key)  # to accept api_key

    message = "📅 *Weekly Summary*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    message += "📈 *Activity Overview:*\n"
    for a in activity:
        message += f"• `{a['name']}` → {a['text']} 🔸 *Usage:* {a['percent']}%\n"

    message += "\n🗣️ *Languages Used:*\n"
    for l in languages:
        message += f"• `{l['name']}` → {l['text']} ({l['percent']}%)\n"

    message += "\n📁 *Projects Worked On:*\n"
    for p in projects:
        message += f"• `{p['name']}` → {p['text']} ({p['percent']}%)\n"

    await update.message.reply_text(message, parse_mode="Markdown")

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You’ve discovered a premium feature!")

# ----------------- Main -----------------
if __name__ == "__main__":
    db.init_db()

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setkey", setkey))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^ℹ️ About$"), about))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📊 Last 7 Day Summaries$"), day7))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📅 Daily Summaries$"), daily))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📈 Some Stats$"), some))

    print("Bot running...")
    app.run_polling()
