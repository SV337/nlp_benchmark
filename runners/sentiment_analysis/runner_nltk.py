from nltk.sentiment import SentimentIntensityAnalyzer

class Runner:
    def __init__(self):
        pass

    def name(self):
        return "NLTK"

    def prepare(self):
        pass

    def run_sentiment(self, content):
        sia = SentimentIntensityAnalyzer()

        sentiment = "neutral"
        sentiment_scores = sia.polarity_scores(content)
        if sentiment_scores["compound"] >= 0.05:
            sentiment = 'positive'
        elif sentiment_scores["compound"] <= -0.05:
            sentiment = 'negative'
        return sentiment
