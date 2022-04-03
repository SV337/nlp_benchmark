import gcld3

class Runner:
    def prepare(self):
        self.detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=1000)

    def name(self):
        return "gcld3"

    def run_language_detection(self, content):
        lang = self.detector.FindLanguage(content)
        return lang.language
