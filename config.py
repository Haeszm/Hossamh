import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "lido")
ALIVE_NAME = getenv("ALIVE_NAME", "lido")
BOT_USERNAME = getenv("BOT_USERNAME", "joker7x_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lido")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "br_selva")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SO_SELVA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ف ب غ س ك و م ا ت / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/10bfc5e7d6ab441832a65.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Mrlido99/Selvamic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/10bfc5e7d6ab441832a65.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/10bfc5e7d6ab441832a65.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/10bfc5e7d6ab441832a65.jpg")
