from dateparser.search import search_dates

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "dateparser"

    def run_date_extraction(self, content):
        try:
            dates = search_dates(content)
        except:
            return None

        if dates is None:
            return None

        res = []
        for date in dates:
            res.append(date[1].strftime("%Y-%m-%d"))
        return res
