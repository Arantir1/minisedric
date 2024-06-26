import spacy
import json 
from spacy.matcher import PhraseMatcher


trakers = ["say it clearly", "I've journeyed", "every highway"]

with open('my_way.json', 'r') as file:
    data = json.load(file)

text = data["results"]["transcripts"][0]["transcript"]

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

phrase_matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(text) for text in trakers]
for pattern in patterns:
    phrase_matcher.add(str(pattern), [pattern])
phrase_matches = phrase_matcher(doc)
insights = []

for match_id, start, end in phrase_matches:
    matched_span = doc[start:end]
    pattern_name = nlp.vocab.strings[match_id]
    insight = {
        "start_word_index": start,
        "end_word_index": end,
        "tracker_value": pattern_name,
        "transcribe_value": matched_span.text,
    }
    insights.append(insight)

print(insights)
