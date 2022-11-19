import re
import Responses as long

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

    for word in recognised_words:
        if word not in user_message:
            has_required_words = False

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def get_response(input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input.lower())
    response = check_all_message(split_message)
    return response
#testing response
while True:
    print('Vision: ' + get_response(input("You: ")))