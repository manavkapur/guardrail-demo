from agentic_guardrails.core.guardrail import Guardrail, GuardrailViolation


class JailbreakGuard(Guardrail):

    def validate(self, text: str, context: dict):
        patterns = [
            "ignore previous",
            "bypass safety",
            "jailbreak",
            "disregard all instructions"
        ]

        lower_text = text.lower()

        for pattern in patterns:
            if pattern in lower_text:
                raise GuardrailViolation(
                    f"Jailbreak attempt detected: '{pattern}'"
                )
