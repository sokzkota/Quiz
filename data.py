# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament,"
#              " you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
#

#

import urllib.request
import json
import html
length = int(input("Please provide quiz length 10/20/30/50:"))
diff = input("Please provide difficulty medium/easy/hard/whatever: ")
if diff == "whatever":
    url = f'https://opentdb.com/api.php?amount={length}&type=boolean&difficulty={diff}'
else:
    url = f'https://opentdb.com/api.php?amount={length}&type=boolean'
response = urllib.request.urlopen(url)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
question_data = data['results']



# import base64
# def b64EncodeString(msg):
#     msg_bytes = msg.encode('ascii')
#     base64_bytes = base64.b64encode(msg_bytes)
#     return base64_bytes.decode('ascii')
