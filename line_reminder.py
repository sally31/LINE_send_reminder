import datetime
import locale
import requests
import schedule
import time
from datetime import date


def LINE_Notify():
    API_url = 'https://notify-api.line.me/api/notify'
    access_token = ''#get your token from LINE
    __headers = {'Authorization': 'Bearer ' + access_token}
    message = remind_Message() 
    payload = {'message': message}
    requests.post(API_url, headers=__headers, params=payload,)



costco_datetime=date(2023,10,11)#change the date
Today = datetime.datetime.today().date() #get today's date
def remind_Message():
    #get local in japan
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    
    costco_day_count = (costco_datetime-Today).days 
    
    week_num = Today.weekday()
    week_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sut", "Sun"]
    
    if  costco_datetime > Today:
        message = "today is " + str(Today) + "\n" + week_list[week_num] + "\n" + str(costco_day_count) + "days until Costco"+str(costco_datetime)
    elif   costco_datetime == Today:  
        message = "It's Costco day" 
    elif costco_datetime < Today:
        message = "Costco day is over"
    return message


def main():
    line_notify = LINE_Notify()
    #call LINE_Notify and get a infomation
    message = remind_Message()
    # send a massege


if __name__ == '__main__':
    #get main method every day at 8AM
    schedule.every().day.at("08:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
        Today = datetime.datetime.today().date()
        
