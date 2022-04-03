from transformers import pipeline

class Runner:
    def prepare(self):
        self.pipe = pipeline(
            "text-classification",
            model="papluca/xlm-roberta-base-language-detection"
        )

    def name(self):
        return "xlm_roberta"

    def run_language_detection(self, content):
        try:
            preds = self.pipe(content)
        except:
            return None
        pred = preds[0]
        return pred["label"]
