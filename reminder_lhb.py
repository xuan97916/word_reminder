import os
import time
import threading
import pygame
import concurrent.futures


# load word book
book_name = '01_自然地理.txt'
book_path = os.path.join('./vocabulary_lhb','word_part',book_name)

# load word audio
audio_dict = {}
for file_name in os.listdir('./vocabulary_lhb/audio/'+book_name.split('.')[0]):
    if file_name.endswith('.mp3'):
        audio_dict[file_name.split('.')[0]] = os.path.join('./vocabulary_lhb/audio/'+book_name.split('.')[0],file_name)

line_list = []
with open(book_path, 'r',encoding='UTF-8') as f:
    for line in f:
        if line.strip() != '':
            line_list.append(line.strip())
        
def init_pygame():
    pygame.init()
    pygame.mixer.init()
    
def play_audio(audio_path,stop_signal):
    if not os.path.exists(audio_path):
        pass
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if stop_signal.is_set():
            pygame.mixer.music.stop()
            break
        time.sleep(0.1)
        
# def play_sound(audio_path):
#     playsound(audio_path)

def word_input_and_check(word_list, english, stop_signal):
    answer = input('Your answer: ')
    if answer == english:
        print('correct! You have ' + str(len(word_list) - 1) + ' words left.')
        word_list.pop(0)
    else:
        print('Wrong! The correct answer is ' + english + '. You have ' + str(len(word_list)) + ' words left.')
        wrong_word = word_list.pop(0)
        word_list.append(wrong_word)
    stop_signal.set()
    return word_list

stop_signal = threading.Event()
init_pygame()
        
while len(line_list) > 0:
    english = line_list[0].split('|')[0].strip()
    if '/' in english:
        english = english.split('/')[0]
    
    english_audio = audio_dict[english]
    if len(line_list[0].split('|')) >2:
        chinese = line_list[0].split('|')[2].strip()
        print(chinese)
    else:
        print("no chinese avaliable")
    # concurrent play audio
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_sound = executor.submit(play_audio,english_audio,stop_signal)
        future_word_input = executor.submit(word_input_and_check, line_list, english, stop_signal)
    stop_signal.clear()
    line_list = future_word_input.result()
    print(len(line_list))
    
    
    
    