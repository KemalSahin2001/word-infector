import spacy
from pattern.en import conjugate, pluralize, comparative, superlative, PRESENT, PAST, PARTICIPLE, INFINITIVE, PROGRESSIVE

# Load the large spaCy model for English
nlp = spacy.load("en_core_web_lg")

def conjugate_english_verb(verb):
    """Conjugate English verb."""
    # Simple tenses
    present_simple = conjugate(verb, tense=PRESENT)
    past_simple = conjugate(verb, tense=PAST)
    infinitive = conjugate(verb, tense=INFINITIVE)

    # Perfect tenses
    present_perfect = "have " + conjugate(verb, tense=PARTICIPLE)
    past_perfect = "had " + conjugate(verb, tense=PARTICIPLE)
    future_perfect = "will have " + conjugate(verb, tense=PARTICIPLE)

    # Progressive tenses
    present_progressive = "am " + conjugate(verb, tense=PRESENT, aspect=PROGRESSIVE)
    past_progressive = "was " + conjugate(verb, tense=PRESENT, aspect=PROGRESSIVE)
    future_progressive = "will be " + conjugate(verb, tense=PRESENT, aspect=PROGRESSIVE)

    # Future
    future_simple = "will " + infinitive

    return [infinitive, present_simple, past_simple, present_perfect, past_perfect, future_perfect, present_progressive, past_progressive, future_progressive, future_simple]

def inflect_noun(noun):
    """Inflect English noun."""
    singular = noun
    plural = pluralize(noun)
    singular_possessive = noun + "'s" if not noun.endswith('s') else noun + "'"
    plural_possessive = pluralize(noun) + "'"  # for most English nouns, plural possessive just adds an apostrophe

    return [singular, plural, singular_possessive, plural_possessive]

def inflect_adjective(adj):
    """Inflect English adjective."""
    positive = adj
    comp = comparative(adj)
    superl = superlative(adj)

    return [positive, comp, superl]

def process_word(word):
    """Process word and determine its part of speech, then inflect/conjugate accordingly."""
    doc = nlp(word)
    pos = doc[0].pos_

    if pos == "VERB":
        return conjugate_english_verb(word)
    elif pos == "NOUN":
        return inflect_noun(word)
    elif pos == "ADJ":
        return inflect_adjective(word)
    else:
        return [f"{word} is not a verb, noun, or adjective. Its detected part of speech is {pos}."]

# Example usage
word = input("Enter a word: ")
results = process_word(word)
for res in results:
    print(res)
