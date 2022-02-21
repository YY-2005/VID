# Copyright (C) 2021 By VeezMusicProject

from driver.core import me_bot
from driver.decorators import check_blacklist
from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("home start")
    await query.edit_message_text(
        f"""✨ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 [{BOT_NAME}] (https://t.me/ {BOT_USERNAME}) ** هو روبوت لتشغيل الموسيقى والفيديو في مجموعات ، من خلال دردشة الفيديو Telegram Group! **

💡 ** اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر على زر »📚 الأوامر! **

🔖 ** لمعرفة كيفية استخدام هذا الروبوت ، يرجى النقر فوق »❓ زر الدليل الأساسي! **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني الي مجموعتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ الدليل الاساسي", callback_data="user_guide")],
                [
                    InlineKeyboardButton("📚 الاوامر", callback_data="command_list"),
                    InlineKeyboardButton("❤ المالك", url=f"https://t.me/{OWNER_USERNAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 المجموعه الرسمية", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 القناة الرسمية", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""ℹ️ Quick use Guide bot, please read fully !

👩🏻‍💼 » شغل - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

👩🏻‍💼 » فيديو - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

👩🏻‍💼 » لايف - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

❓ هل لديك أسئلة؟ اتصل بنا في [مجموعه الدعم] (https://t.me/ {GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="user_guide")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    ass_uname = me_bot.first_name
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to use this Bot ?, read the Guide below !

1.) أولاً ، أضف هذا الروبوت إلى مجموعتك.
2.) بعد ذلك ، قم بترقية هذا الروبوت كمسؤول في المجموعة ، وقم أيضًا بإعطاء جميع الأذونات باستثناء المسؤول المجهول.
3.) بعد ترقية هذا الروبوت ، اكتب ريلود المجموعة لتحديث بيانات المسؤول.
3.) قم بدعوة @ {ass_uname} إلى مجموعتك أو اكتب "انضم" لدعوتها ، لسوء الحظ سينضم userbot بنفسه عندما تكتب `` شغل (اسم الاغنية) 'أو `` فيديو (اسم الفيديو) `.
4.) قم بتشغيل / بدء محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو / الموسيقى.
`-النهاية ، تم إعداد كل شيء -`

💡 إذا كانت لديك أسئلة متابعة حول هذا الروبوت ، فيمكنك إخبارها في دردشة الدعم هنا: @ {GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("»دليل الاستخدام السريع«", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👮🏻‍♀️ اوامر الادمن", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("👩🏻‍💼 اوامر جميع المستخدمين", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("اوامر سودو", callback_data="sudo_command"),
                    InlineKeyboardButton("اوامر المالك", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("رجوع", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» شغل (اسم الاغنيه/اللينك) - لتشغيل الاغاني في المكالمه
» فيديو (اسم الفيديو/اللينك) - لتشغيل الفيديو في المكالمه
» لايف (m3u8/رابط اللايف من يوتيوب) - لتشغيل البث في المكالمه
» /playlist - see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in Group only)

⚡️ __ بدعم من {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""✏️ قائمة الأوامر لمسؤول المجموعة.
» وقف - إيقاف تشغيل المسار الحالي مؤقتًا
» كمل - تشغيل المسار المتوقف مؤقتًا مسبقًا
» تخطي - يذهب إلى المسار التالي
» ايقاف - ايقاف تشغيل المسار ومسح الطابور
» كتم - كتم صوت userbot المتدفق في مكالمة جماعية
» الغاء الكتم - قم بإلغاء كتم صوت userbot المتدفق في مكالمة جماعية
» الصوت `1-200` - ضبط مستوى صوت الموسيقى (يجب أن يكون userbot مسؤولاً)
» ريلود - لاعادة تصحيح اخطاء ورفع الادمنين الجدد
» انضم - لادعوه الحساب المساعد للمجموعه
» اخرج - لخروج الحساب المساعد من المجموعه

⚡️ __بالدعم من  {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system information
» /eval - execute any code (`developer stuff`)
» /sh - run any command (`developer stuff`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» حظر عام (`username` or `user_id`) - for global banned people, can be used only in group
» الغاء العام (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» اعادة التشغيل - restart your bot directly
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» تثبيت (`message`) - send a broadcast message to all groups in bot database
» التثبيت (`message`) - send a broadcast message to all groups in bot database with the chat pin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
