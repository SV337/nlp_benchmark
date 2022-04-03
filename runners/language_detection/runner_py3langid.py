import py3langid as langid

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "py3langid"

    def run_language_detection(self, content):
        lang, _ = langid.classify(content)
        return lang
