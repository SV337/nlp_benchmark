from date_extractor import extract_dates

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "date-extractor"

    def run_date_extraction(self, content):
        try:
            dates = extract_dates(content)
        except:
            return None
        if dates is None:
            return None

        res = []
        for date in dates:
            if date is not None:
                res.append(date.strftime("%Y-%m-%d"))
        return res
