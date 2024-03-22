from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9db6ae360e0a7b833abff.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/3d0d7d23d3a7fb86b442e.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/varmasarkar")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/varmasarkar")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "VARMA SARKAR")  

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
