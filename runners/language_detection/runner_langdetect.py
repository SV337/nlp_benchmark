from langdetect import detect

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "langdetect"

    def run_language_detection(self, content):
        try:
            return detect(content)
        except:
            return None
