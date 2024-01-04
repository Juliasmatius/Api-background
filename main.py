import os
import platform
import requests
import json
import easygui

def set_desktop_background(image_path):
    system_platform = platform.system()

    if system_platform == 'Windows':
        try:
            import ctypes

            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, image_path, 3
            )
            if notify_success:
                message("Desktop background set successfully!","Api wallpaper")
        except Exception as e:
            message(f"Error setting desktop background: \n{e}","Api wallpaper")

    elif system_platform == 'Linux':
        try:
            desktop_environment = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()

            if 'cinnamon' in desktop_environment:
                os.system(f"gsettings set org.cinnamon.desktop.background picture-uri file://{image_path}")
            elif 'gnome' in desktop_environment:
                os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
            else:
                message("Unsupported Linux desktop environment.","Api wallpaper")
                return

            if notify_success:
                message(f"Desktop background set successfully!","Api wallpaper")
        except Exception as e:
            message(f"Error setting desktop background: {e}","Api wallpaper")
    else:
        message("Unsupported operating system.","Api wallpaper")

# Example usage:
#set_desktop_background("/home/juli/api_bg/photo.jpg")

import configparser

def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    # Create a dictionary for each section
    data = {}
    for section in config.sections():
        data[section] = dict(config.items(section))

    return data


def do_request(url):
    request = requests.get(url)
    return request.text, request.status_code

def get_img_url(data,api):
    if api=="cat" or api=="dog":
        data_json =  json.loads(data)
        data_dict = data_json[0]
        return data_dict["url"]
    elif api=="fox":   
        data_json =  json.loads(data)
        data_dict = data_json["image"]
        return data_dict
        
def message(text,title):
    easygui.msgbox(text,title)

def get_image(api):
    if api=="cat":
        url = f"https://api.thecatapi.com/v1/images/search?api_key={cat_api_key}"
    if api=="dog":
        url = f"https://api.thedogapi.com/v1/images/search?api_key={cat_api_key}"

    elif api=="fox":
        url="https://randomfox.ca/floof/"
    else:
        message("Api wallpaper experienced an error!\nNo api or an incorrect api specified in config!","An error occured!")
        quit()
    
    data, status_code = do_request(url)

    if status_code != 200:
        message(f"Api wallpaper experienced an error with the api!\nHttp error{status_code}","An error occured!")

    url = get_img_url(data,api)

    return url

def download_image(url):
    filename="image.jpg"
    request = requests.get(url)
    with open(filename,"wb") as f:
        f.write(request.content)
    return filename


if not os.path.exists("config.ini"):
        message("Configuration not found!\nPlease make a config.ini like stated on the github.","Api wallpaper")
        quit()
ini_data = read_ini_file("config.ini")

if 'config' in ini_data:
    section1_values = ini_data['config']
    api = section1_values.get('api', None)
    cat_api_key = section1_values.get('cat_api_key', None)
    notify_success = section1_values.get('notify_success', None)
    if notify_success=="True":
        notify_success=True
    else:
        notify_success=False
else:
    message("Api wallpaper experienced an error with it's config.\nConfig not found in the INI file.","An error has occured")
    exit()


img_url = get_image(api)
filename = download_image(img_url)
print(notify_success)

filepath = os.path.join(os.getcwd(),filename)

set_desktop_background(filepath)