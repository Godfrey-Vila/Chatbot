import re
import long_responses as long

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
    response('I\'m Vision, your personal chat bot, and you?', ['what', 'is', 'your', 'name','who', 'are', 'you'],
             required_words=['what', 'who'])
    response('I\'m Great!!, How about you?',['how', 'are', 'you'], required_words=['how'])
    response('Thank You Very much', ['i', 'love', 'you', 'vision'], required_words=['love', 'vision'])
    response(long.R_EATING, ['do', 'you', 'want', 'to', 'eat'], required_words=['you', 'eat'])

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