
text = "Yoooooooo\nThis is some text\nHave a good one!\n"
text2 = "Have a nice day! See ya"

with open('test2.txt', 'w') as file:
    file.write(text)

with open('test2.txt','a') as file:  # appends
    file.write(text2)