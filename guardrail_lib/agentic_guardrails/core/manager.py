from agentic_guardrails.core.guardrail import GuardrailViolation


class GuardrailManager:
    def __init__(self, input_guards: list, output_guards: list):
        self.input_guards = input_guards
        self.output_guards = output_guards

    def validate_input(self, prompt: str, context: dict = None):
        if context is None:
            context = {"stage": "input"}

        for guard in self.input_guards:
            guard.validate(prompt, context)

    def validate_output(self, response: str, context: dict = None):
        if context is None:
            context = {"stage": "output"}

        for guard in self.output_guards:
            guard.validate(response, context)
