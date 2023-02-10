# For the sake of keeping this short, I have chosen these 7 words to be the slurs
# Also, I have created a dummy text file which contains few sentences.
# I have assumed that sentences are separated by newline characters
# Also this code will only detect slurs that are present as individual words in the sentence,
# It won't detect the slurs that are substrings of someother word, example -: theSlurA

slurs = ['SlurA','SlurB','SlurC','SlurD','SlurE','SlurF','SlurG']

# Extracting the data from the file, line by line
file_content = []
with open('input.txt','r') as f:
    for line in f.readlines():
        file_content.append(line.strip())


punctuations = ['?',';','.',',']

# Splitting the sentences into words
words_in_sentence = [i.split(" ") for i in file_content]


#Removing punctuations and whitespaces
only_words_in_sentence = []
for sentence in words_in_sentence:
    temp = []
    for word in sentence:
        if len(word) == 0:
            continue
        elif word[-1] in punctuations:
            temp.append(word[:-1])
        else:
            temp.append(word)
    only_words_in_sentence.append(temp)


# Try an empty sentence

absolute_slur_count = []
percentage_slur_count = []

# Now I will be counting the number of slurs in each sentence, and then ranking
# the sentences based on absolute slur count and percentage slur count
# If the given word is a slur, I will increase the profanity count by 1
# And after iterating through the entire sentence, I will append the profanity_count and the percentage profanity count
# to the respective lists

for i in range(len(only_words_in_sentence)):
    length = len(only_words_in_sentence[i])
    profanity_count = 0
    if length == 0:
        absolute_slur_count.append([profanity_count,i])
        percentage_slur_count.append([profanity_count,i])
        continue
    for word in only_words_in_sentence[i]:
        if word in slurs:
            profanity_count+=1
    absolute_slur_count.append([profanity_count,i])
    percentage_slur_count.append([(profanity_count/length)*100,i])

absolute_slur_count.sort(reverse=True)
percentage_slur_count.sort(reverse=True)

# Now I will print the sentences along with their profanity_count/percecntage_profanity count

print("The most profane sentences based on the absolute count of slurs present are-: ")
print()

for profanity_count,sentence_index in absolute_slur_count:
    print(file_content[sentence_index] + ' : ' + f'Profanity count is {profanity_count}')
    print()

print("The most profane sentences based on the percentage count of slurs present are-: ")
print()

for percentage_profanity_count,sentence_index in percentage_slur_count:
    print(file_content[sentence_index] + ' : ' + f'Percentage profanity count is {percentage_profanity_count}%')
    print()





