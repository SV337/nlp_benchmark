from htmldate import find_date

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "htmldate"

    def run_date_extraction(self, content):
        date = find_date(content)
        return [date]
