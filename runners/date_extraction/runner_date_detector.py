from date_detector import Parser

class Runner:
    def prepare(self):
        self.parser = Parser()

    def name(self):
        return "date_detector"

    def run_date_extraction(self, content):
        matches = self.parser.parse(content)
        if matches is None:
            return None

        res = []
        for match in matches:
            date = match.date
            res.append(date.strftime("%Y-%m-%d"))
        return res
