# import modules
import re
import string

# make empty list for counting letters/word and words/sentence
lw2 = []
lw_count = []
ws = []
ws2_count = []

# read text file
t_file = open("hemingway.txt", "r")
contents = t_file.read()	

# split string into words 
words = re.split(" ", contents)

# count words
word_count = len(words)

# remove punctuation from words list
lw = [c for c in words if c not in ",.?!;:"]

# separate words into individual lists
lw2 = [list(l) for l in lw]

# loop though list for letter counts
for x in range(len(lw2)):
	lw_count.append(len(lw2[x]))

# calculate average letters per word from lw count
avg_lpw = sum(lw_count)/float(len(lw_count))

# split string into sentences
sent = contents.split(".")

# count sentences and account for blank object after last period
sent_count = len(sent)-1

# seperate sentences into individual lists
for x in range(len(sent)-1):
    ws.append(sent[x])

    # remove punctuation
    ws = str(ws).join(c for c in ws if c not in ",.?!;:")

    # split by indivitual word to new list, count it, and append 
    	# ws2 count list for later use
    ws2 = re.split(" ", ws)
    ws2_count.append(len(ws2))

    # reset ws count before next loop
    ws = []

# calculate average words per sentence using ws2 count
avg_wps = sum(ws2_count)/float(len(ws2_count))

# print text analysis to terminal 
print("Paragraph Analysis - Hemingway.txt")
print("-------------------------------------")
print("Approx. Word Count: " + str(word_count))
print("Approx. Sentence Count: " + str(sent_count))
print("Avg. Letters per Word: " + str(avg_lpw))
print("Avg. Words per Sentence: " + str(avg_wps))

# create and write text files
f = open("Paragraph_Analysis_Hemingway.txt", "w")

f.writelines("Paragraph Analysis - Hemingway.txt" + "\n")
f.writelines("-------------------------------------" + "\n")
f.writelines("Approx. Word Count: " + str(word_count) + "\n")
f.writelines("Approx. Sentence Count: " + str(sent_count) + "\n")
f.writelines("Avg. Letters per Word: " + str(avg_lpw) + "\n")
f.writelines("Avg. Words per Sentence: " + str(avg_wps) + "\n")
f.close()

# all PyParagraph assignment conditions met --------------------------