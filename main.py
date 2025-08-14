import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("   ")

@bot.message_handler(commands=['start'])
def start_message(message):
   bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе принять лекарства!')
   reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
   reminder_thread.start()


@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = [
        "**Приём строго по инструкции**: Важно соблюдать дозировку и частоту приёма, указанные врачом или производителем препарата. Это обеспечит максимальную эффективность лечения и минимизирует риск побочных эффектов.",
        "**Совместимость с пищей**: Некоторые лекарства лучше усваиваются на голодный желудок, другие — вместе с едой. Обязательно проверяйте рекомендации производителя относительно приема пищи перед употреблением таблеток.",
        "**Запивать водой**: Лекарства рекомендуется запивать чистой водой комнатной температуры. Другие напитки (чай, кофе, соки) могут снижать эффективность препарата или вызывать нежелательные реакции организма.",
        "**Соблюдение режима**: Если лекарство назначено регулярно, старайтесь принимать его примерно в одно и то же время суток. Это помогает поддерживать стабильную концентрацию активного вещества в крови.",
        "**Контроль побочных эффектов**: Обратите внимание на возможные побочные эффекты и немедленно сообщайте врачу, если заметили необычную реакцию организма на препарат."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о приеме лекарств {random_fact}')


def send_reminders(chat_id):
    first_rem = "08:00"
    second_rem = "13:00"
    end_rem = "18:11"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - прими лекарства")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)