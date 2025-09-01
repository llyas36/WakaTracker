
---

# WakaTrackr Bot 🖥️📊

**WakaTrackr** is a Telegram bot that helps you track your coding habits effortlessly using your WakaTime account. Get daily and weekly summaries, view languages, projects, and coding activity — all directly in Telegram!

---

## Features

* Store your WakaTime API key securely.
* View your **daily coding stats** (premium feature placeholder).
* Get **weekly summaries** with activity, languages, and projects.
* Track **machines, editors, and operating systems** used.
* Easy-to-use buttons and commands in Telegram.

---

## Commands

* `/start` – Welcome message and instructions.
* `/setkey <your_wakatime_api>` – Save your WakaTime API key.
* `/about` – Info about the bot and creator.
* Inline buttons:

  * 📅 Daily Summaries
  * 📊 Last 7 Day Summaries
  * 📈 Some Stats
  * ℹ️ About

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/llyas36/wakatrackr-bot.git
cd wakatrackr-bot
```

2. Create a virtual environment:

```bash
python3 -m venv botEnv
source botEnv/bin/activate  # Linux/macOS
botEnv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set your Telegram Bot token as an environment variable:

```bash
export TELEGRAM_TOKEN="YOUR_BOT_TOKEN"
```

5. (Optional) Set up PostgreSQL on Railway for persistent storage:

```bash
export DATABASE_URL="your_railway_postgresql_url"
```

---

## Running the Bot

```bash
python bot.py
```

The bot will start and respond to commands in Telegram.

---

## Database

* By default, uses **SQLite** for local development.
* For production, recommended to use **PostgreSQL** (Railway add-on) to avoid losing user API keys on redeploy.

---

## Security

* WakaTime API keys are **encrypted** before storing.
* The bot only stores keys needed to fetch user stats.
* No keys are shared or exposed publicly.

---

## Contributing

* Fork the repo and create a branch for your feature/bugfix.
* Submit a pull request for review.
* Please follow Python best practices and keep the code clean.

---

## License

MIT License © 2025 [llyas](https://github.com/llyas36)

---

