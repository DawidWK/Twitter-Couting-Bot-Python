import tweepy
import time
import smtplib
from email.message import EmailMessage

# Twitter Api
CONSUMER_KEY =
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


# Email
USER = 
PASSWORD = 
RECIVER = 

msg = EmailMessage()
msg['From'] = USER
msg['To'] = RECIVER

count = 1
day = 1
hours_of_day = 0

while count <= 10000:
    try:
        api.update_status(f'this is my {day} day of counting, {count}/1000 \n #count #couting #pythonBot #python')
    except Exception as e:
        msg['Subject'] = 'Twitter Bot Error!'
        message = f"Couldn't count to {count} error appeared: \n{e}"
        print(f'API ERROR {count}, {day}, {hours_of_day}')
        count = count - 1
        hours_of_day = hours_of_day - 1
    # sends email
        try:
            msg.set_content(message)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(USER, PASSWORD)
                smtp.send_message(msg)
        except:
            print(f'EMAIL ERROR {count + 1}, {day}, {hours_of_day + 1}')

    # logs for linux terminal 
    print(f'At this moment: ')
    print(f'count: {count}')
    print(f'day: {day}')
    print(f'hours of day: {hours_of_day}')
    print('')

    if hours_of_day == 24:
        day = day + 1
        hours_of_day = 0

    time.sleep(3600)
    count = count + 1
    hours_of_day = hours_of_day + 1

