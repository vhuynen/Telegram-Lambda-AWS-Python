# Send Telegram Message via Python Lambda AWS 

This Lambda function allow to send an message through Telegram Bot API when it is triggered by Amazon SNS (Simple Notification Service).

# Deprecated version

This function use the vendored version of **requests** library from **Botocore** and Python 3.7 runtime.  

```python
import json
import os
from botocore.vendored import requests

TELEGRAM_TOKEN =os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")

def lambda_handler(event, context):
    bot_request = 'https://api.telegram.org/' + TELEGRAM_TOKEN + '/sendMessage?chat_id=' + TELEGRAM_CHAT_ID + '&text=' + event['Records'][0]['Sns']['Message'] 
    print(event)
    print(bot_request)
    response = requests.get(bot_request) 
    return {
       'statusCode': response.status_code,
       'msg': json.dumps('Message send with succ essed !'),
       'body': json.dumps(response.json())
   }
```

When you execute this function you have an warning log that the HTTP Client from **Botocore** is deprecated and that it will be removed from lambda after **2021/03/31**.

```
/var/runtime/botocore/vendored/requests/api.py:72: DeprecationWarning: You are using the get() function from 'botocore.vendored.requests'.  This dependency was removed from Botocore and will be removed from Lambda after 2021/03/31. https://aws.amazon.com/blogs/developer/removing-the-vendored-version-of-requests-from-botocore/. Install the requests package, 'import requests' directly, and use the requests.get() function instead
DeprecationWarning
```

For more information, you can read this paper about this topic : https://aws.amazon.com/fr/blogs/developer/removing-the-vendored-version-of-requests-from-botocore/

# Stable version

This lambda function use the strong **requests** library **urllib3**

```python
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
```

To execute this function you must import yourself the requests library into your package and then use the console to upload and deploy the package.

- Import the library **requests** into a work directory on your file system :
  - `sudo pip install requests -t .`

- Create `lambda_function.py`  into your work directory

- Copy the content of `lambda_function.py` from lambda console

- Paste it in your `lambda_function.py` from your work directory

- Zip the content of your work directory, which is your deployment package (Zip the directory content, not the directory)
- Go to the Lambda console, select upload zip file and upload your deployment package
- Deploy your code and execute the function

Now, your lambda function should work without warning.

# Structure SNS Message

```json
{
   "Records":[
      {
         "EventSource":"aws:sns",
         "EventVersion":"1.0",
         "EventSubscriptionArn":"arn:aws:sns:us-west-2:307004840:IoTMailboxPLPSNSTopic:8c9b83d1-120e-4eaf-b125-825ed7f0e657",
         "Sns":{
            "Type":"Notification",
            "MessageId":"ea18fd6d-33f1-553f-85f0-a5ac8a3d78f0",
            "TopicArn":"arn:aws:sns:us-west-2:307004840:IoTMailboxPLPSNSTopic",
            "Subject":"None",
            "Message":"HelloWorld! Have de Nice Day!",
            "Timestamp":"2021-03-09T17:59:40.790Z",
            "SignatureVersion":"1",
            "Signature":"",
            "SigningCertUrl":"",
            "UnsubscribeUrl":"",
            "MessageAttributes":{
               
            }
         }
      } 
```

