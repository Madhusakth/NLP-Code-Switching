import csv
import json
import re
import os
import string
from nltk.corpus import words
from googletrans import Translator
translate_urls = ["translate.google.co.kr",
                       "translate.google.at", "translate.google.de",
                       "translate.google.ru", "translate.google.ch",
                       "translate.google.fr", "translate.google.es"]
tr = Translator(service_urls=translate_urls)

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

spanish_tweets = open("spanish_tweets_dev.txt","w+")
output_file= open("dev_emoji.txt","w+")


translated = []
path = '/work/05942/neeha/maverick2/NLP/NLP-Code-Switching/emoji_data/'
# path = '/home/neeha/UT/Sem3/NLP/FP/USER_TWEETS_SPANISH_ENGLISH/'

files = []
# r=root, d=directories, f = files
for r,d,f in os.walk(path):
	for file in f:
		if '.json' in file:
			filename = os.path.join(r,file)
			if('positive_emoji' in filename):
				label=1
			else:
				label=0
			with open(filename,'r') as json_file:
				data = json.load(json_file)
				for line in data:
					translator = Translator(service_urls=translate_urls)
					line = cleanText(line['text'])
					if (any((word in words.words() and len(word)>1 and len(line.split()) > 5) for word in line.split())):
						spanish_tweets.write(str(label))
						spanish_tweets.write('\t')
						spanish_tweets.write(line)
						spanish_tweets.write('\n')
						translator = translator.translate(line)
						if(translator.text not in translated):
							print(translator.text)
							output_file.write(str(label))
							output_file.write('\t')
							output_file.write(translator.text)
							output_file.write("\n")
							translated.append(translator.text)
						else:
							print('Tweet contains no english words')
output_file.close()

#with open('output.csv','wb') as result_file:
#    wr = csv.writer(result_file, dialect='excel')
#    wr.write(translated)
