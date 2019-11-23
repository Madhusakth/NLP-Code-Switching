import csv
import json
import re
import os
import string
from nltk.corpus import words
from googletrans import Translator


def cleanText(line):
	result = " ".join(filter(lambda x:x[0]!='#', line.split()))
	result = " ".join(filter(lambda x:x[0]!='@', result.split()))
	result = re.sub(r'(?i)\b((?:https?://|.com\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', result)
	result = re.sub('\s+',' ', result) #remove enter and tab space
	result = re.sub(r'\.+', " ", result)
	# to_delete = set(string.punctuation) - {'.', ',', '!', '?'} # remove special characters
	result = re.sub('[^.,!?\"\'a-zA-Z0-9 \n\.]', '', result)
	# result = " ".join(result)
	return result
	# ^a-zA-Z0-0.,!?

output_file= open("dev_emoji.txt","w+")


translated = []
path = '/home/neeha/UT/Sem3/NLP/FP/NLP-Code-Switching/emoji_data/'
# path = '/home/neeha/UT/Sem3/NLP/FP/USER_TWEETS_SPANISH_ENGLISH/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            filename = os.path.join(r, file)
            # print('filename')
            with open('/home/neeha/UT/Sem3/NLP/FP/NLP-Code-Switching/emoji_data/positive_emoji_spanglish.json','r') as json_file:
            	data = json.load(json_file)
            	for line in data:
            		translator = Translator()
            		# print("line['text']", line['text'])
            		line = cleanText(line['text'])
            		if any((word in words.words() and len(word)>1 and len(line.split()) > 5) for word in line.split()):
            			print(line)
            			str1='ho'
            			translator = translator.translate('a')
            			if translator.text not in translated:
	            			print("Line:",translator.text)
	            			output_file.write('1\t')
	            			output_file.write(translator.text)
	            			output_file.write("\n")
	            			translated.append(translator.text)
            		# else:
            		# 	print('Tweet contains no english words')
output_file.close()

#with open('output.csv','wb') as result_file:
#    wr = csv.writer(result_file, dialect='excel')
#    wr.write(translated)
