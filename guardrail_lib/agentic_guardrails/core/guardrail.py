from abc import ABC, abstractmethod

# Custom exception: whenever a guardrail blocks something, this is raised
class GuardrailViolation(Exception):
    pass


# Base class: every guardrail must follow this structure
class Guardrail(ABC):

    @abstractmethod
    def validate(self, text: str, context: dict):
        """
        text: input or output text to check
        context: metadata like stage (input/output), agent name, etc.
        """
        pass
