   


with open("vocabulary.txt", 'a') as f:   
    writing = True 
    while writing:
        eng_word =  input("영어 단어를 입력하세요:")
        kor_word =  input("한국어 뜻을 입력하세요:")

        if eng_word == "q" or kor_word == "q":
            writing = False
            print("Check out the 'vocabulary.txt'")
        else:
            f.write(f"{eng_word}: {kor_word}\n")
    