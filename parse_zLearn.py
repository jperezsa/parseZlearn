#!/usr/bin/python3

nick = []
word = []
desc = []


with open("zLearn.txt", encoding="utf8", errors='ignore') as file:
   

    for line in file:
        if line[0] == 'a':
            clean_nick = line[1:] 
            clean_nick = clean_nick.strip('\n')
            clean_nick = clean_nick.split('!')
            nick.append(clean_nick[0])

        if line[0] == 'k':
            clean_word = line[1:]
            clean_word = clean_word.strip('\n')
            word.append(clean_word)

        if line[0] == 'd':
            clean_desc = line[1:]
            desc.append(clean_desc)
        
    
print(desc)
