import datefinder

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "datefinder"

    def run_date_extraction(self, content):
        dates = datefinder.find_dates(content)
        res = []
        for date in dates:
            res.append(date.strftime("%Y-%m-%d"))
        return res
