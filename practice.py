


with open(vocabulary.txt, 'a') as f:
   
    file = open("vocabulary.txt", "w")
    writing = True

    while writing:
        eng_word =  f.write(input("영어 단어를 입력하세요:"))
        kor_word = input("한국어 뜻을 입력하세요:")
        if eng_word or kor_word == "q":
            writing = False
            print("Check out the vocabulary.txt")
        