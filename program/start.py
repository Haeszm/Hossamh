from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    ASSISTANT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["/start", f"/start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""مرحبا {message.from_user.mention()} 👋🏻\n
💭 [𝆥 𝑴𝒚_𝑷𝒚𝒕𝑯𝒐𝒏_𝑩𝒐𝑻 ›](https://t.me/{ASSISTANT_NAME}) يتـيـح لـك تـشـغيل الـموسـيقى والفـيديـو فـي مجـموعـات مـن خـلال محـادثـات الـفيديـو الجـديـدة في Telegram!

📜 ¦ اكتــشف جـميـع أوامـر الـروبـوت وكيـفية عـملها مـن خـلال الـنقر علـى زار »  📜 ¦ الـأوامــر

🔖  لمـعرفة كـيفية اسـتخـدام هـذا الـروبـوت ، يـرجى النـقر فـوق زار » 🕊︙دليـل الـاسـتخـدام
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اضفني لي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("دلـيل الاسـتخـدام", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton("🖥 ¦ الأوامــر", callback_data="cbcmds"),
                    InlineKeyboardButton("المـطــور", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton("الـدعـم", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton("الـسورس", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(" 😈 ¦ المـطوريـن", url=f"https://t.me/")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )




@Client.on_message(
    command(["/alive", f"/alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- 𝐆𝐑𝐎𝐔𝐏 -", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "- 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 -", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, I'm {me_bot.first_name}**\n\n🧑🏼‍💻 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n👾 Bot Version: `v{__version__}`\n🔥 Pyrogram Version: `{pyrover}`\n🐍 Python Version: `{__python_version__}`\n✨ PyTgCalls Version: `{pytover.__version__}`\n🆙 Uptime Status: `{uptime}`\n\n❤ **Thanks for Adding me here, for playing video & music on your Group's video chat**"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )



@Client.on_message(command(["الاوامر", "اوامر", "الاوامر", "مم"]) & filters.group & ~filters.edited)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/b135aeb1ac54ce83a493a.jpg",
        caption=f"""🌀 ها هي الاوامر :
الاوامر تكتب كما هي بدون شرط او اي شيء
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『  تشغيل 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『  فديو 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『  تشغيل 』✪➢ ➕  「رابط 」تشغيل صوت
 ⇦ ✪『  فديو 』✪➢ ➕  「رابط」 تشغيل فيديو مباشر من اليوتيوب
⇦ ✪『 ايقاف او انهاء』✪➢ ☆ لايقاف التشغيل
⇦ ✪『  وقف 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 تقدم 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『   مواصله  』✪➢ ☆ استئناف التشغيل 
⇦ ✪『   كتم او سكوت 』✪➢ ☆ لكتم البوت
⇦ ✪『 الغاء الكتم』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『   تحكم 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『   تنزيل 』✪➢ ➕ «اسم الفديو» لتنزيل فديو من اليوتيوب 
⇦ ✪『   تحميل 』✪➢ ➕ «اسم الاغنيه» لتحميل اغنيه من اليوتيوب 
⇦ ✪『   بحث 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『   الصوت 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『   تحديث 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『   انضم 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『   غادر 』✪➢ ☆ لطرد حساب المساعد 
⇦ ✪『   بينج 』✪➢ ☆ - إظهار حالة البوت بينغ
⇦ ✪『   الوقت 』✪➢ ☆ - اظهار الوقت
⇦ ✪『   السورس 』✪➢ ☆  إظهار معلومات البوت  (في المجموعة)
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『   مسح  』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『   تنظيف  』✪➢ ☆ لتنظيف جميع الملفات المحمله
⇦ ✪『   معلومات  』✪➢ ☆ لرؤيه معلومات النظام 
⇦ ✪『  ترقيه 』✪➢ ☆ لترقيه البوت لاخر اصدار من السورس
⇦ ✪『  تنصيب 』✪➢ ☆ لاعاده التشغيل من هيركو
⇦ ✪『  غادرالجميع 』✪➢ ☆ لمغادره الحساب المساعد لجميع الدردشات
━━━━━━━━━━━━━━
 ⚡️ ??قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝆥 𝑴𝒚_𝑷𝒚𝒕𝑯𝒐𝒏_𝑩𝒐𝑻 ›", url=f"https://t.me/M_Python_1"),
                ],
            ]
        ),
    )


@Client.on_message(command(["/ping", "ينج", "يست", f"/ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["/uptime","لوقت", f"/uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )

