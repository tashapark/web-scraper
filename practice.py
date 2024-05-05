   
import random

voca_dicts ={}

writing = True 
while writing: 
    with open("vocabulary.txt", 'r') as f:   
        for line in f:
            data = line.strip().split(": ")
            if len(data) < 2:
                continue
            eng_word, kor_word = data[0], data[1]
            voca_dicts[eng_word] = kor_word

            # 섞을 수 있게 리스트로 
            voca_keys = list(voca_dicts.keys())
            random.shuffle(voca_keys)
           
            for eng_word in voca_keys:
                kor_word = voca_dicts[eng_word]
                answer = input(f"{kor_word}: ")
                if eng_word == answer:
                    print("맞았습니다!") 
                else: 
                    print(f"아쉽습니다. 정답은 {eng_word}입니다.")
    
            if answer == "q":
                writing = False
                break
