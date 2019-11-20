import csv
from googletrans import Translator

#load json data

translated = []
for line in json_file:
    translator = Translator()
    translator.translate(line['text'])
    translated.append(translator.text)

with open('output.csv','wb') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerow(translated)
