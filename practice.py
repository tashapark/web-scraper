

with open("vocabulary.txt", 'r') as f:   
    vocabulary = [line.strip().split(": ") for line in f]
writing = True 
while writing:
    for eng_word, kor_word in vocabulary:
        answer = input(f"{kor_word}: ")
        if eng_word == answer:
            print("맞았습니다!") 
        else: 
            print(f"아쉽습니다. 정답은 {eng_word}입니다.")
    writing = False
