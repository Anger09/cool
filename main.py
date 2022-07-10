import telebot

bot = telebot.TeleBot('5464661782:AAGV1JM0cHSaGv2rWw9_fys7SeHxEIzZTWU')
@bot.message_handler(content_types='/start')
def send_everything(message):
    bot.send_message(message.chat.id, 'Привет')
# Русский язык
    if message.text == 'Привет':
        bot.send_message(message.chat.id,'Как дела?')
        bot.send_message(message.chat.id,'Что-то хотел?')
    elif message.text == 'Норм':
        bot.send_message(message.chat.id,'У меня тоже) жду пока меня программист до пишет')
    elif message.text == 'Жди':
        bot.send_message(message.chat.id,'Слушаюсь Босс')
    elif message.text == 'А возможно добавить дело':
        bot.send_message(message.chat.id, 'На данный момент нельзя ждите обновления')
    elif message.text == 'А когда выходят обновления':
        bot.send_message(message.chat.id, 'Каждую суботту, так что ждите')
    elif message.text == 'Хорошо спасибо за информацию':
        bot.send_message(message.chat.id, 'Не за что обращайтесь')
    elif message.text == 'Ауу':
        bot.send_message(message.chat.id, 'Извините произошёл сбой серверов')
    elif message.text == '/stop':
        bot.send_message(message.chat.id, 'Хорошо, до свидание')
    elif message.text == 'Здарова':
        bot.send_message(message.chat.id, 'Как дела?')
    elif message.text == 'Нормально':
        bot.send_message(message.chat.id, 'У меня тоже) жду пока меня программист до пишет')
    elif message.text == 'Пр':
        bot.send_message(message.chat.id, 'Как дела?')
    elif message.text == 'Где твой хозяин?':
        bot.send_message(message.chat.id, 'В Москве')
    elif message.text == 'Хорошо':
        bot.send_message(message.chat.id, 'У меня тоже) жду пока меня программист до пишет')
    elif message.text == 'Как у тебя дела?':
        bot.send_message(message.chat.id, 'Нормально')
    elif message.text == 'Я тоже буду ждать':
        bot.send_message(message.chat.id, 'Хорошо это скоро произайдёт')
    elif message.text == 'Я тоже жду':
        bot.send_message(message.chat.id, 'Хорошо это скоро произайдёт')
    elif message.text == 'Нравится ли вам тот человек которым вы стали?':
        bot.send_message(message.chat.id, 'Да')
    elif message.text == 'О чём вы будете сожелеть,что не сделали в своей жизни':
        bot.send_message(message.chat.id, 'Что я не извенял друзей')
    elif message.text == 'Хай':
        bot.send_message(message.chat.id, 'Как дела?')
    elif message.text == 'Ой':
        bot.send_message(message.chat.id, 'Да нечего страшного')
    elif message.text == 'Что ты можешь':
        bot.send_message(message.chat.id, 'Я могу полностью заменить человека в опщении,могу потсказать какой нибуть мультфиль или фильм')
    elif message.text == 'На сколько скоро?':
        bot.send_message(message.chat.id,'От года до трёх')
    elif message.text == 'Хорошо буду ждать':
        bot.send_message(message.chat.id, 'Жди')
    elif message.text == 'Да хотел':
        bot.send_message(message.chat.id, 'Что именно?')
    elif message.text == 'Я бы хотел узнать об обновлениях':
        bot.send_message(message.chat.id, 'Обновления проходят примерно в 16:00 до 18:00')
    elif message.text == 'Спасибо':
        bot.send_message(message.chat.id, 'Не за что')
    elif message.text == 'Нормально, да':
        bot.send_message(message.chat.id, 'Что именно?')
    elif message.text == 'Переведите меня на разработчика':
        bot.send_message(message.chat.id, 'Извените в данный момент он занет')
    elif message.text == '/Разработчик':
        bot.send_message(message.chat.id, '@Ang1r')
    elif message.text == 'Расскажи интересный факт':
        bot.send_message(message.chat.id,' В 1889 году королева Италии Маргарита Савойская заказала первую доставку пиццы')
    elif message.text == 'А когда он освободиться?':
        bot.send_message(message.chat.id, 'Этого мне не извесно')
    elif message.text == 'А когда он освободиться?#Друг':
        bot.send_message(message.chat.id, '*Он свободен по всем дням кромя субботы)')
    elif message.text == '#Друг':
        bot.send_message(message.chat.id, 'Ты что-то хотел?')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, 'Что именно?')
    elif message.text == 'Ты освободился?':
        bot.send_message(message.chat.id, 'Я свободен по всем дням кормя субботы')
    elif message.text == 'Хорошо пока/stop':
        bot.send_message(message.chat.id, 'Пока')
#Разработчик
    elif message.text == '/Инфо':
        bot.send_message(message.chat.id, 'Приветствую вас разработчик что вы желаете?')
    elif message.text == '/Настройки':
        bot.send_message(message.chat.id, 'Хорошо вам перевести на русский или оставить так как он есть')
    elif message.text == '/Оставить как он есть':
        bot.send_message(message.chat.id, 'Edit Bots/setname - change a bot s name/setdescription - change bot description/setabouttext - change bot about info/setuserpic - change bot profile photo/setcommands - change the list of commands/deletebot - delete a bot')
    elif message.text == '/Переведи на русский':
        bot.send_message(message.chat.id, 'Редактор бота /setname - изменить имя бота,/setdescription - изменить описание бота,/setabouttext - изменить информацию о боте,/setuserpic - изменить фотографию профиля бота,/setcommands - изменить список команд,/deletebot - удалить бота.')
    elif message.text == '/Настройки разработчика':
        bot.send_message(message.chat.id, 'Хорошо вам перевести на русский или оставить так как он есть')
#Девушка,подруга:
    #elif message.text == '#Подруга':
        #bot.send_message(message.chat.id, 'Да,что-то хотела?')
    #elif message.text == 'Да':
        #bot.send_message(message.chat.id, 'Что именно?')
    #elif message.text == 'Ты свободен ':
        #bot.send_message(message.chat.id, 'Я свободен по всем дням кормя субботы')
    #elif message.text == 'Хорошо гулять будешь':
        #bot.send_message(message.chat.id, 'Нет')
    #elif message.text == 'Из-за чего':
        #bot.send_message(message.chat.id, 'Я тренируюсь во Free Fire')
    #elif message.text == '#Девушка':
        #bot.send_message(message.chat.id, 'Да,что-то хотела зай?')
    #elif message.text == 'Да':
        #bot.send_message(message.chat.id, 'Что именно?')
    #elif message.text == 'Ты свободен ':
        #bot.send_message(message.chat.id, 'Для тебя я всегда свободен ;)')
    #elif message.text == 'Хорошо гулять будешь':
        #bot.send_message(message.chat.id, 'Да только немного потренируюсь')
    #elif message.text == 'Хорошо как потринируешься напиши':
        #bot.send_message(message.chat.id, 'Хорошо')
#Матершиники
    #elif message.text == 'Блять':
        #bot.send_message(message.chat.id, 'Не материтесь')
    #elif message.text == 'И начё что':
        #bot.send_message(message.chat.id, 'Иначе вы получите бан навсегда')
    #elif message.text == 'Эй ты еблан':
        #bot.send_message(message.chat.id, 'Нам не особо хочется знать о вас')
    #elif message.text == 'Ты чё ахуел':
        #bot.send_message(message.chat.id, 'Также как и вы')
    #elif message.text == 'Хуй с тобой':
        #bot.send_message(message.chat.id, 'Чё хотел?')












#Англиский язык
    elif message.text == 'Hello,do you know English':
        bot.send_message(message.chat.id, 'Yes,sure')
    elif message.text == 'Wow super':
        bot.send_message(message.chat.id, 'Yes,of course,my creator has provided for everything')
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'Hello')
        bot.send_message(message.chat.id, 'How are you')
    elif message.text == 'Norm':
        bot.send_message(message.chat.id, 'Me too')
    elif message.text == 'Fine':
        bot.send_message(message.chat.id, 'Me too')
    elif message.text == 'What else cen you do':
        bot.send_message(message.chat.id, 'I can replace a person in coommunication by half,i can recommend a cartoon,a film')
    elif message.text == 'Well recommend me a movie':
        bot.send_message(message.chat.id,'Well what genre: Horror, fantasy,mysticism,adventure')
    elif message.text == 'Horror':
        bot.send_message(message.chat.id,'Pine Street house,Cursed House,Devil"sHand,Sand,Sinister,MadisonCounty')
    elif message.text == 'Are you here':
        bot.send_message(message.chat.id, 'Sorry there was an error')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hello')
        bot.send_message(message.chat.id, 'How are you')


bot.polling(non_stop=True)