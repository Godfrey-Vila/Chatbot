import  random
import datetime

R_EATING = "I cannot eat sorry beacuse I am a software only, sorry"
R_PLACE = "I develop in a place of  Kasiglahan Village San Jose Rodriguez Rizal, but to be specific I live inside your machine"

now = datetime.datetime.now()
R_DATETIME = "The current date and time is: " + now.strftime("\nDate: %m-%d-%y    Time:  %H:%M")
def unknown():
    response = [' Sorry!, I cannot understand that',
                'Can you please repeat it'
                ' What is it?'
                '...... no response, sorry!'][random.randrange(4)]
    return response