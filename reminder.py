

word_dict = {}

word_list = []

def make_word_dict(word_path, word_dict, word_list):
    with open(word_path, 'r',encoding='UTF-8') as f:
        for line in f:
            english = line.split(',')[0].strip()
            chinese = line.split(',')[1].strip()
            word_dict[english] = chinese
            word_list.append(english)


make_word_dict('./word_book/test_word_3-8', word_dict, word_list)

while len(word_list) > 0:
    print(word_dict[word_list[0]])
    answer = input('your answer: ')
    if answer == word_list[0]:
        print('correct! You have ' + str(len(word_list) - 1) + ' words left.')
        word_list.pop(0)
    else:
        print('Wrong! The correct answer is ' + word_list[0] + '. You have ' + str(len(word_list)) + ' words left.')
        wrong_word = word_list.pop(0)
        word_list.append(wrong_word)




