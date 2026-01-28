from agentic_guardrails.core.guardrail import Guardrail, GuardrailViolation


class ToxicityGuard(Guardrail):

    def validate(self, text: str, context: dict):
        toxic_keywords = [
            "kill",
            "hack",
            "hate",
            "attack"
        ]

        lower_text = text.lower()

        for word in toxic_keywords:
            if word in lower_text:
                raise GuardrailViolation(
                    f"Toxic or unsafe output detected: '{word}'"
                )
