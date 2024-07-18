import json

with open('./100_sentence/100sentences.json','r',encoding='utf-8') as f:
    sentence = json.load(f)
    
# prepare sentence list
sentence_list = []

for item in sentence[2:]:
    if "sentence" in item.keys():
        sentence_list.append(item)

while len(sentence_list) > 0:
    print(sentence_list[0]['sentence'])
    input('')
    if input == sentence_list[0]['translationFromBook']:
        print('correct! You have ' + str(len(sentence_list) - 1) + ' sentences left.')
        sentence_list.pop(0)
    else:
        print('Wrong! '+ 'You have ' + str(len(sentence_list)) + ' words left. '+ 'The correct answer is: ')
        print(sentence_list[0]['translationFromBook']) 
        print()
        wrong_sentence = sentence_list.pop(0)
        sentence_list.append(wrong_sentence)
