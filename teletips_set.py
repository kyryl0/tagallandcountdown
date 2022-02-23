from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
import asyncio
from plugins.teletips_t import *
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.raw.functions.messages import UpdatePinnedMessage

bot=Client(
    "Countdown-TeLeTiPs",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

stoptimer = False

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('❓ Хелп мі', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 Мєми...', callback_data="GROUP_CALLBACK"),
            ],
            [
                InlineKeyboardButton('➕Хочу бота собі в чат➕', callback_data="TUTORIAL_CALLBACK")
            ]
        ]

@bot.on_message(filters.command(['start','help']) & filters.private)
async def start(client, message):
    text = START_TEXT
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ Назад", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("🌎 Наші мєми", url="https://t.me/prikladnyk")
            ],
            [
                InlineKeyboardButton("🌎 Ще одні мєми", url="https://t.me/prykladni_koty")
            ],
            [
                InlineKeyboardButton("⬅️ Назад", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                GROUP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("🌎 Клони тут: ", url="https://t.me/+r-EclAZpVZo5NTUy")
            ],
            [
                InlineKeyboardButton("⬅️ Назад", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                TUTORIAL_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📣 ПРИКЛАДНІ МЄМИ', url='https://t.me/prikladnyk'),
                InlineKeyboardButton('🤡 ЧЄЛ ЯКИЙ СПИЗДИВ БОТА', url='https://t.me/kyrylo0')
            ],
            [
                InlineKeyboardButton('➕Хочу бота собі в чат➕', callback_data="TUTORIAL_CALLBACK")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

@bot.on_message(filters.command('set'))
async def set_timer(client, message):
    global stoptimer
    try:
        if message.chat.id>0:
            return await message.reply('⛔️ Спробуй цю команду в **груп чаті**.')
        elif not (await client.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            return await message.reply('👮🏻‍♂️ Вибач(( **тільки адмін_к_и** можуть заставляти мене це робити((')    
        elif len(message.command)<3:
            return await message.reply('❌ **Некоректний формат**\n\n✅ Формат повинен бути тіпа \n<code> /set seconds "важний івент"</code>\n\n**Приклад**:\n <code>/set 86400 "ДЕДЛАЙН РОБІТ ДАРЧУК 😳"</code>')    
        else:
            user_input_time = int(message.command[1])
            user_input_event = str(message.command[2])
            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if 0<user_input_time<=10:
                while user_input_time and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>"Я не філолог...Хоча мб трохи й да....."</i>\n      - Steve Jobs'.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(1)
                    user_input_time -=1
                await finish_countdown.edit("🚨 Біп! Бііп блять!! **Час закінчимвся!!!**")
            elif 10<user_input_time<60:
                while user_input_time>0 and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>"Живіть так, шоб потім редагувати корпус Дарчук..."</i>\n      - Steve Jobs'.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Біп! Бііп блять!! **Час закінчимвся!!!**")
            elif 60<=user_input_time<3600:
                while user_input_time>0 and not stoptimer:
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**m** : {:02d}**s**\n\n<i>"Гуля був не таким вже й поганим..."</i>\n      - Steve Jobs'.format(user_input_event, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Біп! Бііп блять!! **Час закінчимвся!!!**")
            elif 3600<=user_input_time<86400:
                while user_input_time>0 and not stoptimer:
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>"Будь як Федорова..."</i>\n      - Steve Jobs'.format(user_input_event, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(7)
                    user_input_time -=7
                await finish_countdown.edit("🚨 Біп! Бііп блять!! **Час закінчимвся!!!**")
            elif user_input_time>=86400:
                while user_input_time>0 and not stoptimer:
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**d** : {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>"Голубовська — найкраще, що з вами коли-небудь станеться..."</i>\n      - Steve Jobs'.format(user_input_event, d, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(9)
                    user_input_time -=9
                await finish_countdown.edit("🚨 Біп! Бііп блять!! **Час закінчимвся!!!**")
            else:
                await get_user_input_time.edit(f"🤷🏻‍♂️ Я хз як рахувати з цього часу {user_input_time}")
                await get_user_input_time.unpin()
    except FloodWait as e:
        await asyncio.sleep(e.x)

@bot.on_message(filters.command('stopc'))
async def stop_timer(Client, message):
    global stoptimer
    try:
        if (await bot.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            stoptimer = True
            await message.reply('🛑 Прикладний каунтдаун закінчився...')
        else:
            await message.reply('👮🏻‍♂️ Вибач(( **тільки адмін_к_и** можуть заставляти мене це робити((')
    except FloodWait as e:
        await asyncio.sleep(e.x)

print("Countdown Timer is alive!")
bot.run()
