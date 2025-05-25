# NovaBot 🤖

NovaBot is a fully modular, customizable Discord bot designed for community moderation, logging, and user engagement. Built with scalability and clarity in mind, NovaBot simplifies server management while offering features users actually care about.

---

## 🌟 Features

- 🔨 **Moderation Tools**: Easily kick, ban, and warn members with permission checks.
- 📝 **Message Logging**: Automatically logs messages, users, channels, and timestamps.
- 🔗 **Firebase Integration**: Store logs and activity securely in Firestore.
- 🔄 **Extensible Commands**: Add your own cogs or commands using the `discord.py` extension system.

---

## 🧠 Tech Stack

- **Python 3.11+**
- **[discord.py](https://discordpy.readthedocs.io/en/stable/)** – For Discord bot integration
- **[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)** – For logging and data storage
- **Amazon EC2** or local hosting

---

## 📁 Folder Structure

```
NovaBot/
├── bot.py                     # Bot entry point
├── cogs/                      # Modular bot commands
│   ├── moderation.py          # Kick, Ban, Warn commands
│   └── logging.py             # Logs user messages to Firebase
├── utils/
│   └── firebase.py            # Firebase helper functions
├── config/
│   └── config.json            # Bot token and prefix
├── requirements.txt           # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/NovaBot.git
cd NovaBot
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Firebase

- Create a Firebase project
- Download your `serviceAccountKey.json`
- Replace the path in `utils/firebase.py` with your JSON path

```python
cred = credentials.Certificate('path/to/your/firebase/credentials.json')
```

### 4. Update Config

In `config/config.json`:

```json
{
    "prefix": "!",
    "token": "YOUR_DISCORD_BOT_TOKEN"
}
```

### 5. Run NovaBot

```bash
python bot.py
```

---

## 🧩 Adding New Features

Add your own commands or functionalities as new Python files inside the `cogs/` directory. Just follow the `discord.ext.commands.Cog` pattern.

---

## 🛡️ Permissions

Ensure your bot has the following Discord permissions:

- Manage Messages
- Kick Members
- Ban Members
- Read Message History

---

## 📜 License

NovaBot is released under the MIT License. Feel free to fork, customize, and improve.

---
