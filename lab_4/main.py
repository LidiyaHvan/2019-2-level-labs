import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if not isinstance(texts, list) or not texts:
        return []
    clean_tokenize_corpus = []
    for text in texts:
        if isinstance(text, str):
            if '<br />' in text:
                text = text.replace('<br />', ' ')
            new_text = ''
            for elm in text:
                if elm.isalpha() or elm == ' ':
                    new_text += elm
            new_text = new_text.lower()
            pre_corpus = new_text.split(' ')
            corpus1 = []
            for word in pre_corpus:
                if word != '':
                    corpus1.append(word)
            clean_tokenize_corpus.append(corpus1)
    return clean_tokenize_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus:
            texts = []
            for text in self.corpus:
                if text and isinstance(text, list):
                    texts.append(text)
            for text in texts:
                tf_values = {}
                text1 = []
                for word in text:
                    if isinstance(word, str):
                        text1.append(word)
                for word in text1:
                    if word not in tf_values:
                        tf_values[word] = text1.count(word)/len(text1)
                self.tf_values.append(tf_values)
            return self.tf_values


    def calculate_idf(self):
        if self.corpus:
            texts = []
            for text in self.corpus:
                if text and isinstance(text, list):
                    texts.append(text)
            for text in texts:
                new_text = []
                for word in text:
                    if isinstance(word, str):
                        new_text.append(word)
                for word in new_text:
                    if word not in self.idf_values:
                        documents = []
                        for document in texts:
                            if word in document:
                                documents.append(document)
                        self.idf_values[word] = math.log(len(texts) / len(documents))
        return self.idf_values

    def calculate(self):
        if self.tf_values and self.idf_values:
            for text in self.tf_values:
                tf_idf_val = {}
                for word, tf_value in text.items():
                    tf_idf_val[word] = tf_value * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_val)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values:
            return ()
        if document_index >= len(self.corpus):
            return ()
        info = self.tf_idf_values[document_index]
        if word not in info:
            return ()
        rating = sorted(self.tf_idf_values[document_index], key=lambda x: self.tf_idf_values[document_index][x],
                             reverse=True)
        position = rating.index(word)
        result = (info[word], position)
        return result




if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
