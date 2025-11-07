from transformers import pipeline

class SentimentModel:
    def __init__(self):
        # Load Hugging Face model for emotion detection
        self.pipe = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None,
            device=-1  # CPU
        )

    def predict_emotion(self, text):
        out = self.pipe(text)

        # Handle nested list structure
        if isinstance(out, list) and len(out) > 0 and isinstance(out[0], list):
            out = out[0]

        if isinstance(out, list):
            best = max(out, key=lambda x: x['score'])
            emotion = best['label']
            scores = {d['label']: float(d['score']) for d in out}
            return emotion, scores
        else:
            return str(out['label']), {out['label']: float(out['score'])}
