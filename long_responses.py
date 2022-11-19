import  random
import datetime


R_EATING = "I cannot eat sorry beacuse I am a software only, sorry"
R_PLACE = "I develop in a place of  Kasiglahan Village San Jose Rodriguez Rizal, but to be specific I live inside your machine"
R_CHEERUP = "Aww don't be sad, I know you can do it! I'm here to help you and cheer you up!!!   You can do it! We love you!!!"
R_IMPRESSION = " My first impression about you is, you are attractive, diligent and enjoyable to communicate"
R_SPORTS = "My favorite sports is playing video games such as Mobile legends and Call of Duty"
now = datetime.datetime.now()
R_DATETIME = "The current date and time is: " + now.strftime("\nDate: %m-%d-%y    Time:  %H:%M")
def unknown():
    response = [' Sorry!, I cannot understand that',
                'Can you please repeat it'
                ' What is it?'
                '...... no response, sorry!'][random.randrange(4)]
    return response
