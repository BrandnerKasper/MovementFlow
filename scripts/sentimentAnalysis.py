from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def main() -> None:
    data = [
        "This feels like shit",
        "Plays really nice but the level is to hard",
        "MORE THIS IS IT, Great Work!!",
        "I am exited to fail!",
        "It was fun, but please no more.",
        "This"
        ]
    classifier = generate_sentiment_classifier()
    classify_data(data, classifier)
    classifier2 = default()
    classify_data(data, classifier2)


def generate_sentiment_classifier():
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return classifier


def classify_data(data: list[str], classifier) -> None:
    for d in data:
        print(classifier(d))


def default():
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return classifier


main()
