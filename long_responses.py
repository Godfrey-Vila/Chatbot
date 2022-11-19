import  random

R_EATING = "I cannot eat sorry beacuse I am a software only, sorry"
def unknown():
    response = [' Sorry!, I cannot understand that',
                'Can you please repeat it'
                ' What is it?'
                '...... no response, sorry!'][random.randrange(4)]
    return response