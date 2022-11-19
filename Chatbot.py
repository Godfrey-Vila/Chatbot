import re
import long_responses as long

#https://www.youtube.com/watch?v=Ea9jgBjQxEs&ab_channel=Indently
print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calculate the percentage of the recognized words in user.
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_message(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, sigle_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, sigle_response, required_words)
    #responses of chat bot (Vison)
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'tol', 'par'], sigle_response=True)
    response('I\'m Vision, your personal chat bot', ['what', 'is', 'your', 'name'],
             required_words=['what', 'your', 'name'])
    response('I\'m Vision, your personal chat bot', ['who', 'are', 'you'],
           required_words=['who', 'you'])
    response('As for today, I am 1 day old', ['how', 'old'])
    response('I\'m Great!!, Thanks for asking',['how', 'are', 'you'], required_words=['how'])
    response('Thank You Very much', ['i', 'love', 'you', 'vision'], required_words=['love', 'vision'])
    response(long.R_EATING, ['do', 'you', 'want', 'to', 'eat'], required_words=['you', 'eat'])
    response(long.R_PLACE, ['where', 'do', 'you', 'live'], required_words=['where', 'live'])
    response(long.R_DATETIME, ['what','is','the', 'date', 'and', 'time', 'today'], required_words=['date', 'time'])
    response(long.R_CHEERUP, ['I am', 'sad', 'and',  'down',],required_words=['sad', 'down'])
    response(long.R_IMPRESSION, ['impression', 'About', 'Me'], required_words=['impression', 'me'])
    response(long.R_SPORTS, ['what', 'is', 'your', 'favorite', 'sport'], required_words=['favorite', 'sport'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

   # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response
#testing response
while True:
    print('Vision: ' + get_response(input("You: ")))


