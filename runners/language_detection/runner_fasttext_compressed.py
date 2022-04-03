import fasttext

# https://fasttext.cc/docs/en/python-module.html
# https://fasttext.cc/docs/en/language-identification.html
class Runner:
    def prepare(self):
        self.model = fasttext.load_model("corpus/language_detection/lid.176.ftz")

    def name(self):
        return "fasttext-compressed"

    def run_language_detection(self, content):
        #content = content.replace("\n"," ")
        lang = self.model.predict(content)
        if lang:
            return lang[0][0].replace("__label__", "")
        return None
