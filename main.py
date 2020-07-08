import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    # notification.notify(
    #     title = title,
    #     message = message,
    #     app_icon = None,
    #     timeout = 1
    # )
    Notify.init("Test Notifier")
    n = Notify.Notification.new(title, message)
    n.show()
def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    myHtmlData = getData("https://www.mohfw.gov.in/")
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    myDataStr = ""
    # print(soup.prettify())
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")

    states = ['Gujarat', 'Uttar Pradesh']

    for item in itemList[0:35]:
        dataList = item.split('\n')
        if(dataList[1] in states):
            print(dataList)
            nTitle = "Cases of Covid-19"
            nText = f"{dataList[1]}\nActive Cases: {dataList[2]}\nCured: {dataList[3]}\nDeaths: {dataList[4]}\nTotal Confirmed Cases: {dataList[5]}"
            print(nText)
            notifyMe(nTitle, nText)