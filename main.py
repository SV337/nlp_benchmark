import os
import glob
import time
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import importlib
import pandas as pd

import corpus

class Result:
    def __init__(self, criteria):
        self.criteria = criteria
        self.total = 0
        self.runners_classification = {}

    def create_entry(self, name):
        self.runners_classification.update({
            name: {
                "count": 0,
                "valid": 0,
                "valid_class": 0,
                "avg_time": 0,
                "sum_time": 0,
            }
        })

    def update(self, name, valid, elapsed):
        if not name in self.runners_classification:
            self.create_entry(name)

        self.runners_classification[name]["count"] += 1
        count = self.runners_classification[name]["count"]
        if valid:
            self.runners_classification[name]["valid"] += 1
        self.runners_classification[name]["valid_class"] = self.runners_classification[name]["valid"] / count

        avg_time = self.runners_classification[name]["avg_time"]
        self.runners_classification[name]["avg_time"] = (avg_time + elapsed) / count
        self.runners_classification[name]["sum_time"] += elapsed

    def read_from_file(self, filename):
        data = pd.read_csv(filename, names = ["name", "valid_class", "avg_time"], header = None)
        for i, d in data.iterrows():
            self.runners_classification.update({ d["name"]: {
                "valid_class": d["valid_class"], 
                "avg_time": d["avg_time"], 
            }})

    def save_to_file(self, name, filename):
        file = open(filename, "a")
        res = self.runners_classification[name]
        valid_class = res["valid"] / res["count"]
        avg_time = res["avg_time"]
        file.write(f"{name},{valid_class},{avg_time}\n")
        file.close()

    def addlabels(self, ax, x, y, y_text):
        for i in range(len(x)):
            ax.text(i, y[i], y_text[i], ha = 'center')

    def plot_stats(self):
        x_axis = self.runners_classification.keys()
        valid_class_bar = []
        avg_time_bar = []

        for _, res in self.runners_classification.items():
            valid_class = res["valid_class"]
            avg_time = res["avg_time"] * 1e3
            valid_class_bar.append(valid_class)
            avg_time_bar.append(avg_time)
        
        _, (ax1, ax2) = plt.subplots(2)
        ax1.bar(x_axis, valid_class_bar)
        ax2.bar(x_axis, avg_time_bar)

        self.addlabels(ax1, x_axis, valid_class_bar, [f'{i:.3f}' for i in valid_class_bar])
        self.addlabels(ax2, x_axis, avg_time_bar, [f'{i:.3f}' for i in avg_time_bar])

        ax1.set_xlabel("Libraries")
        ax1.set_ylabel("Precision")
        ax2.set_xlabel("Libraries")
        ax2.set_ylabel("Mean execution time (milliseconds)")

        plt.legend(loc='best')
        plt.show()

class Evaluator:
    def __init__(self):
        self.criterias = ["sentiment", "language_detection", "date_extraction"]
        self.init_datasets()
        self.runners_class = {criteria: [] for criteria in self.criterias}
        self.init_runners_class()
        self.init_results()

    def init_runners_class(self):
        folder = "runners"
        runner_classname = "Runner"

        for file in glob.iglob(folder + '/**/*.py', recursive=True):
            file = file[:-3]
            mod_path = file.replace("/", ".")
            mod = importlib.import_module(mod_path)

            if runner_classname in dir(mod):
                runner_class = getattr(mod, runner_classname)
                for method in dir(runner_class):
                    for criteria in self.criterias:
                        if f"run_{criteria}" == method:
                            self.runners_class[criteria].append(runner_class)

    def init_datasets(self):
        self.datasets = {
            "sentiment": corpus.SentimentCorpus(),
            "language_detection": corpus.LanguageCorpus4(),
            "date_extraction": corpus.DateExtractionCorpus(),
        }

    def init_results(self):
        self.results = { criteria: Result(criteria) for criteria in self.criterias }

    def print_datasets_stats(self):
        for _, dataset in self.datasets.items():
            dataset.print_stats()
        print("\n\n")

    def run_all(self):
        for criteria, dataset in self.datasets.items():
            for runner_class in self.runners_class[criteria]:
                runner = runner_class()
                name = runner.name()

                runner.prepare()
                fn = getattr(runner, f"run_{criteria}")
                print(f"\n[*] Running {name} ...")


                for i in tqdm(range(len(dataset))):
                    content = dataset[i]

                    start_t = time.perf_counter()
                    res = fn(content)
                    elapsed = time.perf_counter() - start_t

                    self.results[criteria].update(
                            name,
                            dataset.valid_classification(name, i, res),
                            elapsed
                    )

                # save stats
                self.results[criteria].save_to_file(name, f"stats_{criteria}.csv")

            self.results[criteria].plot_stats()

def start_evaluation():
    evaluator = Evaluator()
    evaluator.print_datasets_stats()
    evaluator.run_all()

def print_stats():
    criteria = "date_extraction"
    res = Result(criteria)
    res.read_from_file(f"stats_{criteria}.csv")
    res.plot_stats()

if __name__ == "__main__":
    #print_stats()
    start_evaluation()
