import os   
import requests
from requests import ConnectionError
from datetime import datetime, timedelta
from random import randint

###TODO FIX ConnectionError stuff and Dirfull stuff!!!!!

def get_url(date: datetime = datetime.now()):
    """Retrieves data on NASA pic by given date. 

    Args:
      date: datetime, date to search the image from.

    Returns:
      tuple: url of image, given date 
    """
    # request information from nasa, error msg if no internet connection
    try:
        search_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=' + str(date.strftime('%Y-%m-%d'))
        data = requests.get(search_url).json()
        
        return data['url'], date

    except ConnectionError:
        print('Connection error, please check your internet connection and try again!')
        return None

def save_image(url, date):
    """
    Retrieves image with given url, saves it to local disk.
    Creates folder with given year and month if they do not exist.

    Args:
      url: string, used to get and save the image.

    Returns:
      str: Folder(s)/Filename
    """  
    # save original location to easily switch back to
    original_dir = os.getcwd()

    #check/make directories
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

    #retrieves and saves the image to current dir
    response = requests.get(url) 
    with open((str(date.strftime('%Y-%m-%d')) + '.jpg'), 'wb') as file_1:
        file_1.write(response.content)

    # change back to OG dir to avoid nested folders if user gives multiple inputs, and then return a file path for main to print out.
    os.chdir(original_dir)
    return str(date.strftime('%Y')) + '\\' + str(date.strftime('%m')) + '\\' + str(date.strftime('%Y-%m-%d')) + '.jpg'

def get_random_date():
    """Gets a random date between 16/06/1995 and Now.

    Returns:
      datetime obj: Random date 
    """
    month = randint(1,12)

    if month == 2:
        day = randint(1,28)
    elif month in [1,3,5,7,8,10,12]:
        day = randint(1,31)
    else:
        day = randint(1,30)

    return datetime(randint(1995,int(datetime.now().strftime('%Y'))), month, day)

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
            
            url_date = get_url(datetime.now())
            if url_date == None:
                continue
            file_loc = save_image(url_date[0], url_date[1])
            print(f"Todays picture saved in: {file_loc}")
            

        if user_input == '2':
           
            url_date = get_url(datetime.now() - timedelta(days=1))

            if url_date == None:
                continue

            file_loc = save_image(url_date[0], url_date[1])
            print(f"Yesterdays picture saved in: {file_loc}")
            

        if user_input == '3':
                date = get_random_date()
                url_date = get_url(date)
                if url_date == None:
                    continue
                file_loc = save_image(url_date[0], url_date[1])
                print(f"Random picture saved in: {file_loc}")
            
            
        elif user_input not in '0123':
            print("Invalid input!")
            print(help_text())


if __name__ == '__main__':
    main()

