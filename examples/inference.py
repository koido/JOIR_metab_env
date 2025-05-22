from transformers import pipeline


def main():
    """事前学習済みの感情分析モデルで簡単な推論を行います。"""
    classifier = pipeline("sentiment-analysis", framework="tf")
    text = "I love using pre-trained models!"
    result = classifier(text)[0]
    print(f"ラベル: {result['label']}, スコア: {result['score']:.4f}")


if __name__ == "__main__":
    main()
