import os   
import requests
import urllib.request
from datetime import datetime, timedelta
from random import randint

###TODO FIX ConnectionError stuff and Dirfull stuff!

def get_url(date: datetime = datetime.now()):
    """Retrieves data on NASA pic by given date. 

    Args:
      date: datetime, date to search the image from.

    Returns:
      tuple: url of image, given date 
    """
    search_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=' + str(date.strftime('%Y-%m-%d'))
    data = requests.get(search_url).json()
    
    return data['url'], date

def save_image(url, date):
    """
    Retrieves image with given url, saves it to local disk.
    Creates folder with given year and month if they do not exist.

    Args:
      url: string, used to get and save the image.

    Returns:
      str: Folder(s)/Filename
    """  
    try:
        os.chdir('Nasa_pictures\\')
    except FileNotFoundError:
        os.mkdir('Nasa_pictures')
        os.chdir('Nasa_pictures\\')
    try:
        os.chdir(str(date.strftime('%Y')))
    except FileNotFoundError:
        os.mkdir(str(date.strftime('%Y')))
        os.chdir(str(date.strftime('%Y')))
    try:
        os.chdir(str(date.strftime('%m')))
    except FileNotFoundError:
        os.mkdir(str(date.strftime('%m')))
        os.chdir(str(date.strftime('%m')))

    urllib.request.urlretrieve(url, (str(date.strftime('%Y-%m-%d')) + '.jpg'))

    return str(date.strftime('%Y')) + '\\' + str(date.strftime('%m')) + '\\' + str(date.strftime('%Y-%m-%d')) + '.jpg'

def get_random_date():
    """Gets a random date between 16/06/1995 and Now.

    Returns:
      datetime obj: Random date 
    """
    return datetime(randint(1995,int(datetime.now().strftime('%Y'))), randint(1,12), randint(1,30))

def help_text():
    text = """
User commands:
    0 = Exit
    1 = Load picture of current day
    2 = Load picture of yesterday
    3 = Load a random picture from June 1995 to current day
"""
    return text


def main():
    """Main function, loop menu, take user input and respond accordingly.
    
    User commands(int):
      1 = Load picture of current day
      2 = Load picture of yesterday
      3 = Load a random picture from June 1995 to current day.

    """

    print(help_text())

    while True:

        user_input = input("Choose command (1,2,3): ")

        if user_input == '0':
            print("Thanks for using my app!")
            break

        if user_input == '1':
            try:
                url_date = get_url(datetime.now())
                file_loc = save_image(url_date[0], url_date[1])
                print(f"Todays picture saved in: Nasa_pictures\\{file_loc}")
            except ConnectionError:
                print("No internet connection!")

        if user_input == '2':
            try:
                url_date = get_url(datetime.now() - timedelta(days=1))
                file_loc = save_image(url_date[0], url_date[1])
                print(f"Yesterdays picture saved in:  Nasa_pictures\\{file_loc}")
            except ConnectionError:
                print("No internet connection!")

        if user_input == '3':
            try:
                date = get_random_date()
                url_date = get_url(date)
                file_loc = save_image(url_date[0], url_date[1])
                print(f"Random picture saved in: Nasa_pictures\\{file_loc}")
            except ConnectionError:
                print("No internet connection!")
            
        elif user_input not in '0123':
            print("Invalid input!")
            print(help_text())
main()

