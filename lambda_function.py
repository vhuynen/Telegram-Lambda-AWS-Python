import json
import os
import requests

TELEGRAM_TOKEN =os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")

def lambda_handler(event, context):
    bot_request = 'https://api.telegram.org/' + TELEGRAM_TOKEN + '/sendMessage?chat_id=' + TELEGRAM_CHAT_ID + '&text=' + event['Records'][0]['Sns']['Message']  
    print(event)
    print(bot_request)
    response = requests.get(bot_request) 
    return {
        'statusCode': response.status_code,
      'msg': json.dumps('Message send with successed !'),
       'body': json.dumps(response.json())
  }