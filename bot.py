from instabot import Bot
import glob, os 
from login import myusername, mypassword #requires separate python file

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