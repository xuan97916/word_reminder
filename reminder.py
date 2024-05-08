import os

word_dict = {}

word_list = []

def make_word_dict(word_path, word_dict, word_list):
    with open(word_path, 'r',encoding='UTF-8') as f:
        for line in f:
            english = line.split(',')[0].strip()
            chinese = line.split(',')[1].strip()
            word_dict[english] = chinese
            word_list.append(english)

def make_word_dict_all(word_dir, word_dict, word_list):
    file_list = [os.path.join(word_dir,x) for x in os.listdir(word_dir)]
    for file_name in file_list: 
        with open(file_name, 'r',encoding='UTF-8') as f:
            for line in f:
                english = line.split(',')[0].strip()
                chinese = line.split(',')[1].strip()
                word_dict[english] = chinese
                word_list.append(english)

# make_word_dict('./word_book/test_word_3-7', word_dict, word_list)
make_word_dict_all('./word_book', word_dict, word_list)

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




