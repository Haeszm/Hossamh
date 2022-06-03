# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 👋🏻\n
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 ↤ بعد ترقيتي ، اكتب «تحديث» او /reload مجموعة لتحديث بيانات المشرفين
 3 ↤ أضف  @{ASSISTANT_NAME} إلى مجموعتك أو اكتب او «انضم»  /userbotjoin لدعوة حساب المساعد
 4 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 5 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر «تحديث» او /reload في إصلاح بعض المشكلات
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب «غادر» /userbotleave ثم اكتب «انضم» او /userbotjoin مرة أخرى

💡 إذا كان لديك أسئلة متابعة حول هذا الروبوت، يمكنك أن تقول ذلك على دردشة الدعم بلدي هنا: @{GROUP_SUPPORT}.
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

 **⇦ قم بالضغط علي الزر الذي تريده لمعرفه الاوامر  !**

يمكن استخدام جميع الأوامر مع (! / .) معالج""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⌯  الاوامر بالانجليزي ⌯", callback_data="cbadmin"),
                    InlineKeyboardButton("⌯ اوامــر المطــور ⌯", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("⌯  الاوامر بالعربي ⌯", callback_data="cbvamp")                    
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""• 📮 ¦ قائمة الأوامر الأساسيه:

» /play (اسم الأغنية / رابط) - تشغيل الموسيقى على دردشة الفيديو 
» /stream (m3u8/youtube live link) - play youtube/m3u8 live stream music
» /vplay (اسم / رابط الفيديو) - تشغيل الفيديو على دردشة الفيديو
» /vstream - تشغيل فيديو مباشر من yt live / m3u8
» /playlist - تظهر لك قائمة التشغيل 
» /lyric (استعلام) - قص الأغنية الغنائية 
» /video (استعلام) - تنزيل الفيديو من youtube 
» /song (استعلام) - تنزيل أغنية من youtube  
» /search (استعلام) - ابحث عن رابط فيديو youtube 
» /ping - إظهار حالة البوت بينغ
» /uptime - إظهار حالة وقت تشغيل الروبوت
» /alive - عرض معلومات الروبوت على قيد الحياة (في مجموعة)  
» /help - لإظهار رسالة المساعدة (دليل البوت الكامل)
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  
 ⌯ ها هي الأوامر بالانجليزي ⌯

 »/mplay   او «تشغيل» 「اسم الأغنية / رابط」تشغيل الصوت mp3
 » /vplay او «فديو» 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
 » /stream «او«تشغيل» 「رابط 」تشغيل صوت
 » /vstream «او «فيديو» 「رابط」 تشغيل فيديو مباشر من اليوتيوب
 » /stop  «او «ايقاف» لايقاف التشغيل
 » /resume «او لاستئناف التشغيل«مواصله  
 » /skip   «او «تقدم» تخطي الئ التالي
 » /pause «او «وقف» ايقاف التشغيل موقتآ    
 » /vmute «لكتم البوت او «كتم
 » /vunmute  « او «الغاء الكتم لرفع الكتم عن البوت
 » /playlist  «او «تحكم» ↤ تظهر لك قائمة التشغيل
 » /video  «او «تنزيل» + الاسم  تنزيل فيديو من youtube
 » /song +  « او« تحميل» الاسم تنزيل صوت من youtube
 » /volume  «او «الصوت»+ الرقم لضبط مستوئ الصوت
 » /reload  «او «تحديث» لتحديث البوت و قائمة المشرفين
 » /userbotjoin  «او «انضم» لاستدعاء حساب المساعد
 » /userbotleave « او «غادر» لطرد حساب المساعد 
 » /ping «او«تيست» - إظهار حالة البوت بينغ
 » /alive   او «السورس» إظهار معلومات البوت  (في المجموعه) 
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⌯ ها هي الاوامر  للمطور ⌯

» /rmw  »او «مسح- clean all raw files
» /rmd  » او «تنظيف- clean all downloaded files
» /sysinfo»او «معلومات- show the system information
» /update»او «ترقيه - update your bot to latest version
» /restart «او «ريستارت - restart your bot
» /leaveall»او «غادرالجميع - order userbot to leave from all group
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbvamp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""• ♥ ¦ قائمة الأوامر الأساسيه متعربه :

💣 ¦ اوامر الاستخدام الكامله الاوامر تكتب كما هي بدون شرط قبلها
━━━━━━━━━━━━
『تشغيل』 「اسم الأغنية او / رابط تشغيل الصوت mp3
『شغل』 「اسم الأغنية او / رابط تشغيل الصوت mp3
『فديو』「رابط」
『ايقاف او قف او توقف او اسكت』لايقاف التشغيل
 『انضم』لانضمام المساعد
『بحث』لي البحث عن اغاني 
『تنزيل』«اسم الفديو» لتنزيل فديو من اليوتيوب
『تحميل』«اسم الاغنيه»لتحميل اغنيه من اليوتيوب
━━━━━━━━━━━━
📬 ¦ قناة البوت @MusicElkeatib""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )
           

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("⌯ اغلاق ⌯", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
