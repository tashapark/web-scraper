
   

writing = True 
while writing: 
    with open("vocabulary.txt", 'r') as f:   
        for line in f:
            data = line.strip().split(": ") 
            if len(data) < 2:
                continue  # 올바른 형식의 단어 쌍이 아닌 경우 건너뜀..
            # 파일에는 제대로 저장되었지만, 입력중에 띄어쓰기가 된 것들에서 에러가 나는 것으로 여겨짐. 
            # 결국 모든 data에서 넘김 없이 출력했지만, 추가해서 단어 쌍으로 2개가 아닌 줄은 넘기도록 짜는게 추후에도 좋을 듯. 
            eng_word, kor_word = data[0], data[1]
            answer = input(f"{kor_word}: ")
            if eng_word == answer:
                print("맞았습니다!") 
            else: 
                print(f"아쉽습니다. 정답은 {eng_word}입니다.")
    writing = False
