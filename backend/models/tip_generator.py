from transformers import pipeline

class TipGenerator:
    def __init__(self):
        self.pipe = pipeline(
            "text2text-generation",
            model="declare-lab/flan-alpaca-base",
            device=-1
        )

    def generate_tip(self, emotion, excerpt):
        prompt = (
            f"The user feels {emotion}. "
            f"Give one short, empathetic advice and one simple actionable step "
            f"to improve their mood. Be warm and concise. "
            f"Context: {excerpt}"
        )

        out = self.pipe(
            prompt,
            max_new_tokens=60,
            temperature=0.8,
            top_p=0.9,
            repetition_penalty=1.5,
            do_sample=True
        )

        text = out[0].get("generated_text", "").strip()

        if not text:
            text = "Take a deep breath and appreciate the moment. You’re doing great."

        return text


# Test
tg = TipGenerator()
print(tg.generate_tip("sadness", "I feel low and tired. Nothing seems to motivate me today."))
