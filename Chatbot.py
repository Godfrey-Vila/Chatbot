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

def get_response(input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input.lower())
    response = check_all_message(split_message)
    return response
#testing response
while True:
    print('Vision: ' + get_response(input("You: ")))