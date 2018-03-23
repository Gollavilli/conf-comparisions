with open("hello.txt", "r") as text, open("hello2.txt", "r") as txt:
    text2 = [line.strip('\n') for line in txt]
    text2 = [x for x in text2 if x != '']
    print text2
    count = 0
    for line in text:
        if not any (txt in line for txt in text2):
            #print line
            count +=1
    print count