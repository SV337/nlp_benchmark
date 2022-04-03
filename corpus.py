import os
import pandas as pd
from tika import parser
from langcodes import Language
from dateutil.parser import parse

import json

def read_file_content(file):
    parsed = parser.from_file(file)
    return parsed["content"]

def read_raw_file(file):
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
        return content
    except UnicodeDecodeError:
        f = open(file, "rb")
        bin_content = f.read()
        content = bin_content.decode("ISO-8859-1")
        return content


def get_all_folder_files(path):
    all_files = []
    for subdir, _, files in os.walk(path):
        rel_dir = os.path.relpath(subdir, ".")
        for file in files:
            all_files.append(rel_dir + "/" + file)
    return all_files

class Corpus:
    def __init__(self):
        pass

    def __len__(self):
        raise Exception("TODO")

    def __getitem__(self,index):
        raise Exception("TODO")

    def valid_classification(self, name, idx, value):
        raise Exception("TODO")

    def print_stats(self):
        raise Exception("TODO")

class SentimentCorpus(Corpus):
    def __init__(self):
        self.path = "corpus/sentiment_analysis/txt_sentoken"
        self.files = get_all_folder_files(self.path)

    def __len__(self):
        return len(self.files)

    def __getitem__(self,index):
        return read_file_content(self.files[index])

    def valid_classification(self, name, idx, value):
        return value in self.files[idx]

    def print_stats(self):
        pass

class LanguageCorpus1(Corpus):
    def __init__(self):
        self.path = "corpus/language_detection/language_detection.csv"
        self.data = pd.read_csv(self.path)
        self.mappings = {
            "English": "en",
            "Malayalam": "ml",
            "Tamil": "ta",
            "Spanish": "es",
            "Dutch": "nl",
            "French": "fr",
            "Portugeese": "pt",
            "Italian": "it",
            "Russian": "ru",
            "Sweedish": "sv",
            "Arabic": "ar",
            "Turkish": "tr",
            "German": "de",
            "Danish": "da",
            "Kannada": "kn",
            "Greek": "el",
            "Hindi": "hi",
        }

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        return self.data["Text"][index]

    def valid_classification(self, name, idx, value):
        lang = self.data["Language"][idx]
        code = self.mappings[lang]
        return code == value

    def print_stats(self):
        pass

class LanguageCorpus2(Corpus):
    def __init__(self):
        self.path = "corpus/language_detection/dataset.csv"
        self.data = pd.read_csv(self.path)
        self.idx = 0
        self.errors = {}
        self.mappings = {
            "English": "en",
            "Malayalam": "ml",
            "Tamil": "ta",
            "Spanish": "es",
            "Dutch": "nl",
            "French": "fr",
            "Portugese": "pt",
            "Italian": "it",
            "Russian": "ru",
            "Swedish": "sv",
            "Arabic": "ar",
            "Turkish": "tr",
            "German": "de",
            "Danish": "da",
            "Kannada": "kn",
            "Greek": "el",
            "Hindi": "hi",
            "Urdu": "ur",
            "Persian": "fa",
            "Pushto": "ps",
            "Korean": "ko",
            "Estonian": "et",
            "Romanian": "ro",
            "Chinese": "zh",
            "Latin": "lt",
            "Indonesian": "id",
            "Japanese": "ja",
            "Thai": "th",
        }

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        return self.data["Text"][index]

    def valid_classification(self, name, idx, value):
        lang = self.data["language"][idx]
        code = self.mappings[lang]
        return code == value

    def print_stats(self):
        sum_len = 0
        sum_word = 0

        for content in self.data["Text"]:
            sum_len += len(content)
            sum_word += len(content.split(" "))

        print("[*] Number of languages: \t\t", len(self.mappings))
        print("[*] Average length of sentence: \t", sum_len / len(self.data))
        print("[*] Average number of words: \t\t", sum_word / len(self.data))

class LanguageCorpus3(Corpus):
    def __init__(self):
        self.path = "corpus/language_detection/train.csv"
        self.data = pd.read_csv(self.path)
        self.errors = {}

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        return self.data["text"][index]

    def valid_classification(self, name, idx, value):
        if value is None:
            return False
        value = Language.get(value).to_alpha3()
        lang = self.data["labels"][idx]
        code = Language.get(lang).to_alpha3()
        return code == value

    def print_stats(self):
        sum_len = 0
        sum_word = 0

        for content in self.data["text"]:
            sum_len += len(content)
            sum_word += len(content.split(" "))

        print("[*] Number of languages: \t\t", 20)
        print("[*] Number of sentences: \t\t", len(self.data))
        print("[*] Average length of sentence: \t", sum_len / len(self.data))
        print("[*] Average number of words: \t\t", sum_word / len(self.data))

class LanguageCorpus4(Corpus):
    def __init__(self):
        self.path = "corpus/language_detection/tatoeba/top48_sentences.csv"
        self.data = pd.read_csv(self.path)
        self.errors = {}

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        return self.data["text"][index]

    def valid_classification(self, name, idx, value):
        if value is None:
            return False
        value = Language.get(value).to_alpha3()
        lang = self.data["labels"][idx]
        code = Language.get(lang).to_alpha3()
        return code == value

    def print_stats(self):
        sum_len = 0
        sum_word = 0

        for content in self.data["text"]:
            sum_len += len(content)
            sum_word += len(content.split(" "))

        print("[*] Number of languages: \t\t", 48)
        print("[*] Number of sentences: \t\t", len(self.data))
        print("[*] Average length of sentence: \t", sum_len / len(self.data))
        print("[*] Average number of words: \t\t", sum_word / len(self.data))

class DateExtractionCorpus(Corpus):
    def __init__(self):
        self.path = "corpus/date_extraction/htmldate"
        self.files = get_all_folder_files(self.path)
        sol1 = open("corpus/date_extraction/eval_default.json", "r")
        sol2 = open("corpus/date_extraction/eval_mediacloud_2020.json", "r")

        self.res = {}
        tmp = {}
        tmp.update(json.load(sol1))
        tmp.update(json.load(sol2))
        for val in tmp.values():
            self.res.update({ val["file"]: val["date"] })

    def __len__(self):
        return len(self.files)

    def __getitem__(self,index):
        content = read_raw_file(self.files[index])
        return content

    def valid_classification(self, name, idx, value):
        if value is None:
            return False
        valid_date = self.res[os.path.basename(self.files[idx])]

        for val in value:
            try:
                date = parse(val).strftime("%Y-%m-%d")
            except:
                date = value
            if date == valid_date:
                return True
        return False

    def print_stats(self):
        pass
