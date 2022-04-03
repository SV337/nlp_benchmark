from date_extractor import extract_dates
import os
import json

class Runner:
    def prepare(self):
        pass

    def name(self):
        return "extract-date"

    def run_date_extraction(self, content):
        f = open("tmp.txt", "w")
        f.write(content)
        f.close()
        output = os.popen("node --experimental-modules runners/date_extraction/extract-date.mjs tmp.txt").read()
        data = json.loads(output)

        res = []
        for d in data:
            res.append(d['date'])
        return res
