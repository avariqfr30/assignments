## No. 4##
import re
words = ["Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."]

split_words = []

for element in words:
    split_words += re.split("(?<![A-Z][a-z]\.)(?<=\.|\?)\s+", element)

print(*split_words, sep='\n')
####
