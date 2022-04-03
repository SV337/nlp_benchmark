from textblob import TextBlob

class Runner():
    def __init__(self):
        pass

    def name(self):
        return "TextGlob"

    def prepare(self):
        pass

    def run_sentiment(self, content):
        blob = TextBlob(content)
        if blob.sentiment.polarity > 0:
            return "positive"
        elif blob.sentiment.polarity < 0:
            return "negative"
        return "neutral"
