from instabot import Bot
import glob, os 
from login import myusername, mypassword #requires separate python file
# need to create multiple functions now for album and single photo

"""
#### remove json file 
try:
    os.remove('config')
except:
    pass

bot = Bot()

bot.login(username = myusername, password = mypassword)
os.chdir("images")
for file in glob.glob("*.jpg"):
    name = os.path.splitext(os.path.basename(file))[0]
    with open(f'{name}.txt') as text:
        contents = text.read()
    bot.upload_photo(file, caption = contents)

"""


#### remove json file 
try:
    os.remove('config')
except:
    pass

bot = Bot()

bot.login(username = myusername, password = mypassword)
os.chdir("images")

image_list = []
for file in glob.glob("*.jpg"):
    image_list.append(os.path.basename(file))
#name = os.path.splitext(os.path.basename(image_list[-1]))[0]
for text in glob.glob("*.txt"):
        contents = text.read()
bot.upload_album(image_list, caption = contents)