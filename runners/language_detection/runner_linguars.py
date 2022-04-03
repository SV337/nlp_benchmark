import linguars

class Runner:
    def prepare(self):
        self.detector = linguars.LanguageDetector()

    def name(self):
        return "linguars"

    def run_language_detection(self, content):
        lang = self.detector.detect(content)
        if lang:
            return lang.iso_code_639_1.lower()
        return None
