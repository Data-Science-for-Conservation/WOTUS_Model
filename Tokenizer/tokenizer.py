import spacy
import en_core_web_sm


def external_spacy_tokenizer(doc):
    """
    Applies spaCy's built-in tokenizer pipeline capabilities to
        to keep a lemmatized version of each token for alpha-
        numeric non-stop words only (excludes punctuation and whitespace)
    :param doc: string
    :return: list of lemmatized tokens found in `doc`
    """
    # lemmatizer = spacy.lang.en.English()
    # tokens = lemmatizer(doc)
    # return([token.lemma_ for token in tokens
    #         if token.lemma_.isalnum()])
    nlp = en_core_web_sm.load()
    return ([token.lemma_ for token in nlp(doc,
                                           disable=['tagger', 'parser', 'ner'])
             if (token.lemma_.isalnum() and not token.is_stop)])

# print(external_spacy_tokenizer('accomplish accomplishes accomplished'))
