import csv
import json
from googletrans import Translator


translated = []
#load json data
with open('/scratch/cluster/msakthi/Desktop/maddy/cs388/NLP-finalproject/NLP-Code-Switching/data/tweets_ur3sti_1.json') as json_file:
    data = json.load(json_file)
    for line in data:
        translator = Translator()
        print("line:", line)
        print("line['text']", line['text'])
        translator = translator.translate(line['text'])
        print("translator.text", translator.text)
        translated.append(translator.text)

#with open('output.csv','wb') as result_file:
#    wr = csv.writer(result_file, dialect='excel')
#    wr.write(translated)
