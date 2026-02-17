import re
from app.schema.coref import item

BJP_PATTERNS = [
    r"\bbjp\b", r"\bbharatiya janata party\b", r"\bnda\b", r"\bmodi\b",
    r"\bamit shah\b", r"\bjp nadda\b", r"\byogi\b", r"\bYogi Adityanath\b"
]
CONGRESS_PATTERNS = [
    r"\bcongress\b", r"\bindian national congress\b", r"\binc\b", r"\bupa\b",
    r"\brahul gandhi\b", r"\bsonia gandhi\b", r"\bmallikarjun kharge\b",
    r"\bpriyanka gandhi\b"
]

def party_relevance(text: str):
    t = text.lower()

    bjp = any(re.search(p, t) for p in BJP_PATTERNS)
    cong = any(re.search(p, t) for p in CONGRESS_PATTERNS)

    if bjp and cong:
        label = "both"
    elif bjp:
        label = "bjp"
    elif cong:
        label = "congress"
    else:
        label = "none"

    return label




def sent_tokenizer(text):
    stack = []
    sentences = []
    current_sentence = ""

    for char in text:
        current_sentence += char

        if char in ['"', '“', '”']:
            if stack:
                stack.pop()
            else:
                stack.append(char)


        elif char in ['.', '!', '?'] and not stack:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    # ✅ Important: add last sentence
    if current_sentence.strip():
        sentences.append(current_sentence.strip())

    return sentences

def Ner_function(text):
    sentences = sent_tokenizer(text)
    ner_list=[]

    for sentence in sentences:
        rel = party_relevance(sentence)
        if rel not in ["none", "both"]:
            ner_list.append(item(sent=sentence, label=rel))
        elif rel =="both":
            ner_list.append(item(sent=sentence, label="bjp"))
            ner_list.append(item(sent=sentence, label="congress"))
        else:            
            ner_list.append(item(sent=sentence, label="none"))
    return ner_list


# ner_output = Ner_function(text1)