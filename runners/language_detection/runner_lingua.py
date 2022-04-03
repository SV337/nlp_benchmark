from lingua import Language, LanguageDetectorBuilder

class Runner:
    def prepare(self):
        self.detector = LanguageDetectorBuilder.from_all_languages().build()

    def name(self):
        return "lingua"

    def run_language_detection(self, content):
        lang = self.detector.detect_language_of(content)
        if lang:
            return lang.iso_code_639_1.name.lower()
        return None
