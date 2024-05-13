# ARCHIVED AND UNMAINTAINED
This project will no longer be getting updates. The spagetti code is just too low quality and using this on a linux is a mess. Feel free to fork.

# Api-background
Set your wallpaper based on a random image from an api.
Prebuilt binaries are available for Windows and Linux [here](https://github.com/Juliasmatius/Api-background/releases). Sorry mac users, i dont have a mac to test/build this.(Please do tell me how it worked though)
## This will not work with wallpaper engine or any similar application. Please disable those.

# Usage
Configure settings and run the executable.

# Configuration
```
[config]
api=fox
; The above can be cat, dog or fox.
cat_api_key= live_xxxxxxxxxxxxxx
; Get your api key from https://thecatapi.com/signup, only needed for cat and dog modes.
notify_success = False
; Notify about successfully setting the background.
```
Above you can see example configurations.
`api` can be cat, dog or fox. This will set which api the code uses to get the images. \ 
`cat_api_key` is the api key used by the cat and dog api's. You can get yours at [thecatapi.com](https://thecatapi.com/signup) PS. Its free \
`notify_success` chooses weather the code will make a popup after successfully changing the wallpaper. \


# Building
It is always advicable to build yourself, but prebuild binaries are available for Windows and Linux [here](https://github.com/Juliasmatius/Api-background/releases). Here are the instuctions to build this project. \
0. Install python from [their website](https://www.python.org/)
1. Intall PyInstaller using `pip3 install pyinstaller`
2. Install dependencies using `pip3 install requests easygui`
3. Download main.py and config.ini
4. Run `python3 -m PyInstaller -F -w main.py`
5. Wait
6. Go into the "dist" folder. You should see main.exe there.
Now you're done. Keep in mind config.ini needs to *always* be precent for the program to run.


# Image sources
Cat images are from [the cat api](thecatapi.com)
Dog images are from [the dog api](thedogapi.com)
Fox images are from [randomfox](https://randomfox.ca/)(might update to [foxes.cat](https://foxes.cat/)

