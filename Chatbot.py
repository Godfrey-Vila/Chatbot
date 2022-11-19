import re
import Responses as long

print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")

def get_response(input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input.lower())
    response = check_all_message(split_message)
    return response
#testing response
while True:
    print('Vision: ' + get_response(input("You: ")))