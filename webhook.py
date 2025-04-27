import json
import telebot

TOKEN = '7992505133:AAHavMiq_2BU1qCr2Qyk5AMf61p15V9_2xg'
bot = telebot.TeleBot(TOKEN)

def handler(event, context):
    if event['httpMethod'] == 'POST':
        json_data = json.loads(event['body'])
        update = telebot.types.Update.de_json(json_data)
        
        chat_id = update.message.chat.id
        
        if update.message.text == '/start':
            bot.send_message(chat_id, "Salom! Xush kelibsiz!")
        else:
            bot.send_message(chat_id, "Salom!")

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Xabar yuborildi'})
        }
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Faqat POST request qabul qilinadi'})
        }