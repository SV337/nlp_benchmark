import datefinder
from date_detector import Parser
from date_extractor import extract_dates

class Runner:
    def prepare(self):
        self.parser = Parser()

    def name(self):
        return "merge_all"

    def run_datefinder(self, content):
        dates = datefinder.find_dates(content)
        res = set()
        for date in dates:
            res.add(date.strftime("%Y-%m-%d"))
        return res

    def run_date_extractor(self, content):
        try:
            dates = extract_dates(content)
        except:
            return None
        if dates is None:
            return None

        res = set()
        for date in dates:
            if date is not None:
                res.add(date.strftime("%Y-%m-%d"))
        return res

    def run_date_detector(self, content):
        matches = self.parser.parse(content)
        if matches is None:
            return None

        res = set()
        for match in matches:
            date = match.date
            res.add(date.strftime("%Y-%m-%d"))
        return res

    def add_result(self, results, result):
        if result is not None and len(result) > 0:
            results.update(result)

    def run_date_extraction(self, content):
        results = set()
        self.add_result(results, self.run_datefinder(content))
        self.add_result(results, self.run_date_extractor(content))
        self.add_result(results, self.run_date_detector(content))

        return results
