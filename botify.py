import tweepy
import pyttsx3
import re
import time
import subprocess
import pyautogui
import pydirectinput
import os

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

auth = tweepy.OAuthHandler('efKHM0WwikpMh3znBMhwRaG1m', 'mfIjvFeFfnaIyDXo9eHyKVMbYcTk7Umty6ZNsVvKFRgJNHaUjL')
auth.set_access_token('1398882389267423232-ZSUiPD4R3LeJYKbnwQ8kR4c0YHPb0n', 'auuxAPbsI5mNhqrtSpF3Hu6mnJdiZExIG73Kw51ZKoUCP')


api = tweepy.API(auth)

# public_tweets = api.home_timeline() # it gives out all the tweets which are on my start screen (tweets we see after opening twitter)
# for tweet in public_tweets:
#     print(tweet.text)

# Since, over time, the names of various Twitter concepts have evolved, some old names are still used in Tweepy. So keep in mind that, in the context of this article, these equivalences hold:

# A status is a tweet .
# A friendship is a follow-follower relationship.
# A favorite is a like.

user = api.me()
# print(user.name) #it shows my name
# print(user.screen_name) #it shows the name of my handle which is shown when someone mention us
# print(user.friends_count) # it shows whom i am following
# #user['verified'] = True #not working
# print(user) # can find out from here what to display

#for friends in (tweepy.Cursor(api.friends)).items():
    # print('done')

user1 = api.get_user('naval')

print(user1.name)
print(user.followers())

# for likes in tweepy.Cursor(api.favorites).items(): #just keep in mind that [C]ursor starts with capital 'C'
#     print(likes.user.name)
#     print(likes.text)

# working
# api.update_status("just for fun") will not run as it runs only once in a row

# working
# for tweets in api.home_timeline() :
#     (tweets.user).follow()
#     api.create_friendship(tweets.user.screen_name)
# create_friendship and follow do the same thing but in create_friendship we have to give user's screen name while in follow() there is no need

# working
# for tweet in tweepy.Cursor(api.search,'startup').items(5): #since, its in cursor(pagination), it is not written in the brackets and written with a comma
#     tweet.favorite()
#     print('done!')

# for SMS or voice calling, we can use twilo api

tweets_aw = []
for i in tweepy.Cursor(api.user_timeline,screen_name=user1.screen_name,include_rts = False,exclude_replies=True,tweet_mode = 'extended').items():
    jkl= (i.full_text).replace("\n","")
    tweets_aw.append(jkl)

twe = [a for a in tweets_aw if not re.search('https?://[^\s<>"]+|www\.[^\s<>"]+', a)]
print(twe)


a = '...........................  HERE COMES THE NEXT TWEET  ......................................'
tew = a.join(twe)

engine = pyttsx3.init('sapi5')
engine. setProperty("rate", 165)
#engine.say(tew)
engine.save_to_file(tew,'AUDIO.mp3')
engine.runAndWait()

os.system('ffmpeg  -stream_loop -1 -i tf.mp4 -i AUDIO.mp3 -shortest -map 0:v:0 -map 1:a:0 -y VIDEO.mp4')

time.sleep(300)

print('done')

time.sleep(5)
subprocess.call(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe","/max"])
sb = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\searchbar.png")
pyautogui.moveTo(sb)
pyautogui.write('https://discord.com/channels/893928616201682964/893928616201682967')
pyautogui.press('enter')

time.sleep(10)

vc = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\vc.png")
pyautogui.moveTo(vc)
pyautogui.click() 
time.sleep(5)

# subprocess.call("C:\\Windows\\System32\\control.exe")
# time.sleep(5)

# pyautogui.click("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\sound.png")
# time.sleep(1)

# # x = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\-.png")
# # pyautogui.click(x)

# pyautogui.moveTo("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\pb-vc.png")
# pyautogui.click(button='right')
# time.sleep(1)

# pyautogui.click("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\sad.png")
# time.sleep(2)


# pyautogui.click("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\recording.png")
# time.sleep(1)

# pyautogui.moveTo("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\r-vc.png")
# pyautogui.click(button='right')
# time.sleep(1)


# pyautogui.click("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\photos\\sad.png")
# time.sleep(2)




