from goose3 import Goose

class Runner:
    def prepare(self):
        self.g = Goose()

    def name(self):
        return "goose3"

    def run_date_extraction(self, content):
        article = self.g.extract(raw_html=content)
        date = article.publish_date
        return [date]
