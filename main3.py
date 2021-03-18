# dmosk.ru
import imaplib, mymodule
import email
import telebot
password = mymodule.my_password
# Создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('dervoed.brest@gmail.com', password)
# Выводим список папок в почтовом ящике и выбираем для работы папку входящие (inbox)
mail.list()
mail.select("inbox")
# ========= Поиск нужного письма ==========
result, data = mail.search(None, "ALL") # Получаем массив со списком найденных почтовых сообщений
ids = data[0] # Сохраняем в переменную ids строку с номерами писем
id_list = ids.split() # Получаем массив номеров писем
latest_email_id = id_list[-1] # Задаем переменную latest_email_id, значением которой будет номер последнего письма
result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем письмо с идентиф. latest_email_id (посл. письмо)
raw_email = data[0][1] # В переменную raw_email заносим необработанное письмо
raw_email_string = raw_email.decode('utf-8') # Переводим текст письма в UTF-8 и сохраняем в переменную raw_email_string
# ========= Чтение заголовков ==========
# Получаем заголовки и тело письма и заносим результат в переменную email_message
email_message = email.message_from_string(raw_email_string)
message_To = email_message['To']
message_From = email.utils.parseaddr(email_message['From'])
message_Date = email_message['Date']
message_From = str(message_From) # Преобразуем tuple в str

token = mymodule.my_token
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'письмо':
        bot.send_message(message.chat.id, message_From)
        bot.send_message(message.chat.id, message_Date)
bot.polling()
