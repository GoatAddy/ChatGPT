from flask import Flask
import threading
import bot  # tumhara telegram bot yaha import hoga

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    bot.main()  # bot start karne ka function call karo (agar direct run hota hai to bot.py ki code copy karna padega)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
