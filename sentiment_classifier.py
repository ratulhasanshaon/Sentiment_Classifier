punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    New_word=""  
    #print("Word is: ",word)
    for w in word:
        if w not in punctuation_chars:
            New_word=New_word+w
    #print(New_word)
    return  New_word


def get_pos(sentences):
    lower_string=sentences.lower()                    ## As the list of positive words are in lower case
    str_punc_removed=strip_punctuation(lower_string)  ##For Punctuation Removal
    #print("str_punc_removed:",str_punc_removed)
    splitted_string=str_punc_removed.split()          ## For splitting the sentence into words
    #print ("splitted_string:",splitted_string)
    
    
    pos_count=0
    for w in splitted_string:
        if w in positive_words:
            pos_count=pos_count+1
    return pos_count

def get_neg(sentences):
    lower_string=sentences.lower()                    ## As the list of negative words are in lower case
    str_punc_removed=strip_punctuation(lower_string)  ## For Punctuation Removal
    #print("str_punc_removed:",str_punc_removed)
    splitted_string=str_punc_removed.split()          ## For splitting the sentence into words
    #print ("splitted_string:",splitted_string)
    
    
    neg_count=0
    for w in splitted_string:
        if w in negative_words:
            neg_count=neg_count+1
    return neg_count




#The following code opens the twitter file
fileref=open("project_twitter_data.csv","r")
data = fileref.readlines()

#The following code writes in the csv file named resulting_data
outfile=open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")

for i in data[1:]:
    res_row=""
    splt=i.strip().split(",")           #Leading and trailing whitespaces are removed with strip
    res_row=("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write("\n")

outfile.close()
