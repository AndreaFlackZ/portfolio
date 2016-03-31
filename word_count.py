
#Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
#Pairs of words overlap.
#The cat in the hat. -> The cat, cat in, in the, the hat.
#Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word. Allow the user to enter a word and get the most likely words to follow the given word.
#Input? Mr.
#The most likely pair is "Mr. Darcy".
#Advanced:
#Normalize all of the words so differences in captialization and punctuation attached to words don't affect the counts.
#Redo the pair counts: normalize the probablities in the inner dict by the count of pairs that start with the first word.
#Chain together that ability to generate random sentences, one word at a time. From a given starting word. This is a language model.


__author__ = "Andrea Flack"

def punc(word_punc):
    clean_word = word_punc.lower()
    marks = ['!',',','.',':','"','?','-',';','(',')','[',']','\\','/', '\'','\"', '\n', ' ']
    for mk in marks:
        if mk in clean_word:
            clean_word = clean_word.replace(mk,'')
    
    return clean_word

def update_counting_dic(word_to_count, clean_word):
    if clean_word in word_to_count:
        old_count = word_to_count[clean_word]
    else:
        old_count = 0
    new_count = old_count + 1
    word_to_count[clean_word] = new_count

def get_2nd_of_pair(pair):
    return pair[1]

def book():
    

    poe = {}

    with open("E_Poe.txt") as poe_book:
        book = poe_book.readlines()
        for line in book:
            words_for_line = line.split()
            for word in (words_for_line):
                clean_word = punc(word)
                update_counting_dic(poe, clean_word)


    word_cout_pairs = poe.items()
    sorted_word_count_pairs = sorted(word_cout_pairs, key=get_2nd_of_pair, reverse=True)      
    top_ten_word_count_pairs = sorted_word_count_pairs[:10] 
    for word_cout_pair in top_ten_word_count_pairs:
        #print(word_cout_pair)
        print(word_cout_pair[0], "-", word_cout_pair[1])      

   
    
book()

