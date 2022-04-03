from pyfranc import franc

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "pyfranc"

    def run_language_detection(self, content):
        try:
            lang = franc.lang_detect(content)
        except:
            return None
        code = lang[0][0]
        return code
