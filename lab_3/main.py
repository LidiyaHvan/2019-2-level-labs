"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if word not in self.storage and isinstance(word, str):
            self.storage[word] = hash(word)
        return hash(word)

    def get_id_of(self, word: str) -> int:
        if word in self.storage and isinstance(word, str):
            return self.storage.get(word)
        return -1


    def get_original_by(self, id: int) -> str:
        if isinstance(id, int):
            for word, value in self.storage.items():
                if value == id:
                    return word
        return 'UNK'


    def from_corpus(self, corpus: tuple):
        if not isinstance(corpus, tuple):
            return -1
        for word in corpus:
            if word not in self.storage and isinstance(word, str):
                self.storage[word] = hash(word)
        return self.storage



class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple):
            n_grams = []
            for i in range(len(sentence)):
                if len(sentence) - i > self.size:
                   n_grams.append(sentence[i: i + self.size])
                elif len(sentence) - i == self.size:
                   n_grams.append(sentence[i:])
            for n_gram in n_grams:
                if n_gram not in self.gram_frequencies.keys():
                   self.gram_frequencies[n_gram] = 1
                else:
                    self.gram_frequencies[n_gram] += 1
            return 'OK'
        else:
            return 'ERROR'

    def calculate_log_probabilities(self):
        for gram in self.gram_frequencies:
            sum_of_frequencies = 0
            for corpus_gram in self.gram_frequencies:
                if gram[:-1] == corpus_gram[:-1]:
                    sum_of_frequencies += self.gram_frequencies.get(corpus_gram)
                    probability = self.gram_frequencies[gram] / sum_of_frequencies
                    log_probability = math.log(probability)
                    self.gram_log_probabilities[gram] = log_probability

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) != self.size - 1:
            return []
        sentence = list(prefix)
        example = []
        word_1 = []
        for n_gram in self.gram_log_probabilities:
            example.append(n_gram[0: self.size - 1])
        while prefix in example:
            prob = []
            for n_gram in list(self.gram_log_probabilities.keys()):
                if n_gram[:-1] == prefix:
                    prob.append(self.gram_log_probabilities[n_gram])
            prob.sort(reverse=True)
            prob = prob[0]
            for word, probability in list(self.gram_log_probabilities.items()):
                if prob == probability:
                    word_1 = word[-1]
            sentence.append(word_1)
            pref_1 = list(prefix[1:])
            pref_1.append(word_1)
            prefix = tuple(pref_1)
        return sentence


def encode(storage_instance, corpus) -> list:
        code = []
        for sentence in corpus:
            code1 = []
            for element in sentence:
                element = storage_instance.get_id_of(element)
                code1.append(element)
            code.append(code1)
        return code


def split_by_sentence(text: str) -> list:
    if not isinstance(text, str):
        return []
    new_text = ''
    seperated_sentences = []
    text = text.replace('\n', '')
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    if '.' in text:
        for sym in text:
            if sym.isalpha() or sym == ' ' or sym == '.':
                new_text += sym.lower()
    sents = new_text.split('.')
    while '' in sents:
        sents.remove('')
    for sent in sents:
        one_sentence = sent.split()
        one_sentence.insert(0, '<s>')
        one_sentence.append('</s>')
        seperated_sentences.append(one_sentence)
    return seperated_sentences


WSt = WordStorage()
NGr = NGramTrie(5)
sentences = split_by_sentence(REFERENCE_TEXT)
for sent in sentences:
    for word_ in sent:
        WSt.put(word_)
sentences1 = encode(WSt, sentences)
for sent in sentences1:
    NGr.fill_from_sentence(tuple(sent))
NGr.calculate_log_probabilities()
prefix1 = 'Long time no see'
pref_lst = prefix1.split()
pref_num = []
for pref in pref_lst:
    pref_num.append(WSt.get_id_of(pref))
print(pref_num)
numbers_res = NGr.predict_next_sentence(tuple(pref_num))
fin = []
for number in numbers_res:
    fin.append(WSt.get_original_by(number))
print(fin)

