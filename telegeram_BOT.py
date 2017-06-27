import telegram
import os
import sys
import persian
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
CHAT_ID = 177255930
bot = telegram.Bot(token='341875004:AAE4K7VqEcVHONT2aEdPGce8iRClTIEfCCg')
updater = Updater(token='341875004:AAE4K7VqEcVHONT2aEdPGce8iRClTIEfCCg')
dispatcher = updater.dispatcher
#################################################################################################################
tx = persian.arToPersianChar("""در حال ارسال پیام ناشناس به AmirHossein هستی. می‌تونی انتقاد یا هر حرفی که تو دلت هست رو بفرستی چون پیامت به صورت کاملا ناشناس ارسال می‌شه.

منتظر گرفتن متن پیام ازت هستیم... ضمنا اگه عضو VIP باشی می‌تونی تصویر، ویدیو، موزیک یا وویس ناشناس هم بفرستی. فعالسازی با لمس: /upgrade""")
#################################################################################################################
from telegram.ext import CommandHandler

custom_keyboard1 = [['📩 لینک من برای دریافت پیام ناشناس'],['🖋 ارسال ناشناس', '📪 پیام‌های دریافت شده'],['⚙️ تنظیمات', '🤔 راهنما']]
custom_keyboard2 = [['حله بفرست'],['بی خیال','از اول مینویسم']]
reply_markup1 = telegram.ReplyKeyboardMarkup(custom_keyboard1)
reply_markup2 = telegram.ReplyKeyboardMarkup(custom_keyboard2)
reply_markup1.resize_keyboard = True
reply_markup2.resize_keyboard = True
def start(bot, update):
    update.message.reply_text(tx)
    #bot.send_message(update.message.from_user.id,text="چه کاری برات انجام بدم؟",reply_markup=reply_markup1)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#################################################################################################################
def echo(bot, update):
    if update.message.text == 'حله بفرست':
        sent = ("با موفقیت ارسال شد 😊" + "\n\n" + "چه کاری برات انجام بدم؟")
        bot.send_message(update.message.from_user.id,text=sent,reply_markup=reply_markup1)
        return 1
    elif update.message.text == 'از اول مینویسم':
        sent = "اوکی، پیام‌های قبلی حذف شد. از اول بنویس:"
        bot.send_message(update.message.from_user.id,text=sent,reply_markup=reply_markup1)
        return 1
    elif update.message.text == 'بی خیال':
        sent = "چه کاری برات انجام بدم؟"
        bot.send_message(update.message.from_user.id,text=sent,reply_markup=reply_markup1)
    elif update.message.text == '📩 لینک من برای دریافت پیام ناشناس':
        name = update.message.from_user.first_name
        sent  = """سلام """ + name + """ """ + """هستم 😉
لینک زیر رو لمس کن و هر انتقادی که نسبت به من داری یا حرفی که تو دلت هست رو با خیال راحت بنویس و بفرست. بدون اینکه از اسمت باخبر بشم پیامت به من می‌رسه. خودتم می‌تونی امتحان کنی و از همه بخوای راحت و ناشناس بهت پیام بفرستن، حرفای خیلی جالبی می‌شنوی:

👇👇👇
https://telegram.me/harfbemanbot?start=MTIwOTE5Mj"""
        update.message.reply_text(sent)
        sent = """✅ پیام بالا رو به دوستات و گروه‌هایی که می‌شناسی فوروارد کن یا لینک داخلش رو تو شبکه‌های اجتماعی بذار تا بقیه بتونن بهت پیام ناشناس بفرستن. پیام‌ها از طریق همین برنامه بهت می‌رسه.

اینستاگرام داری؟ دریافت لینک مخصوص اینستاگرام: /instagram"""
        update.message.reply_text(sent)
        return 1
    elif update.message.text == '🖋 ارسال ناشناس':
        sent = """نیاز به فعال کردن نسخه VIP داری!

با داشتن عضویت VIP می‌تونی:

🔸 به فرستنده پیام‌های ناشناسی که برات میاد به صورت ناشناس یا با معرفی خودت جواب بفرستی.

🔸به همه کاربران برنامه (بیشتر از ۵ میلیون نفر) بدون داشتن لینک اختصاصیشون پیام ناشناس بفرستی.

🔸و علاوه بر متن، تصویر، ویدیو، موزیک، وویس یا گیف به صورت ناشناس بفرستی.

عضویت VIP محدودیت زمانی نداره و می‌تونی برای همیشه از همه امکانات خاص برنامه که روز به روز هم بیشتر میشن استفاده کنی. همین الان با فقط ۵ هزار تومن برای خودت VIP فعال کن و لذت ببر:

فعالسازی آنلاین از طریق درگاه بانکی:
https://sakkoo.me/hbm/?u=120919218

فعالسازی از طریق USSD:
‏لمس دستور /USSD"""
        update.message.reply_text(sent)
        return 1
    elif update.message.text == '📪 پیام‌های دریافت شده':
        sent = """در حال حاضر پیامی نداری. چطوره با زدن دستور /link لینک خودت رو بگیری و به دوستات و گروه‌ها بفرستی تا بتونند بهت پیام ناشناس بفرستند؟"""
        update.message.reply_text(sent)
        return 1
    elif update.message.text == '🤔 راهنما':
        sent = """من اینجام که کمکت کنم! برای دریافت راهنمایی در مورد هر موضوع، کافیه دستور آبی رنگی که مقابل اون سوال هست رو لمس کنی:

🔹این برنامه چیه اصلا؟ به چه درد می‌خوره؟ /faq1

🔹چطوری پیام ناشناس دریافت کنم؟ /faq2

🔹لینک اختصاصیم رو می‌ذارم اینستاگرام اما کار نمیکنه /faq3

🔹پیام‌های ناشناس من کجا به دستم می‌رسه؟ /faq4

🔹چطوری یه نفر رو آنبلاک کنم؟ /faq8

🔹چطور می‌تونم پیام ناشناس بفرستم؟ /faq5

🔹چطور می‌تونم پیام‌های دریافتی رو یکجا ببینم و به هر کدوم که می‌خوام جواب بدم؟  /faq6

🔹این فعال کردن نسخه VIP یعنی چی؟ آیا باید اپلیکیشن دانلود کنم؟  /faq7

🔹من می‌خوام بدونم چه کسی بهم پیام فرستاده /faq12

🔹قوانین استفاده از این سرویس چیه؟ /faq13"""
        update.message.reply_text(sent)
        return 1
    elif update.message.text == '⚙️ تنظیمات':
        sent = """تنطیمات در دسترس نمیباشد"""
        #bot.send_message(update.message.from_user.id,text=sent,reply_markup=reply_markup1)
        update.message.reply_text(sent)
        return 1
    temp = update.message.text + "\n\n☝️ ثبت شد. همین رو بفرستیم یا ادامه داره؟ اگه ادامه داره ادامه شو بنویس و بفرست."
    bot.send_message(chat_id = update.message.from_user.id,text=temp,reply_markup=reply_markup2)
    bot.send_message(CHAT_ID, text = update.message.from_user.to_json() , reply_markup = reply_markup1)
    bot.send_message(CHAT_ID, text = update.message.text , reply_markup = reply_markup1)
    file = open("foo.txt", "a")
    file.write(update.message.from_user.to_json() + '\n\n')
    file.write(" : " + update.message.to_json() + '\n')
    file.write("***********************************************************************************************************************************************\n");
#################################################################################################################
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
