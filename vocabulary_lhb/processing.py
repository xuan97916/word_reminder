import re

vocabulary_txt_path = "/export2/code/word_reminder/vocabulary_lhb/vocabulary.txt"

cnt = 1


with open(vocabulary_txt_path, "r") as f:
    charpter_path = ""
    charpter_name = []
    lines = f.readlines()
    for idx in range(len(lines)):
        if lines[idx].strip() == "+++":
            charpter_path = "./word_part/"+ str(cnt).zfill(2) + "_" + lines[idx - 1].strip() + ".txt"
            print(charpter_path)
            charpter_name.append(lines[idx - 1])
            cnt += 1
        # if the line is start with alphabet
        elif (
            bool(re.search(r'[a-zA-Z]', lines[idx][0]))
            and lines[idx][0] != "-"
        ):
            with open(charpter_path, "a") as f:
                f.write(lines[idx])
