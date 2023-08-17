from transformers import pipeline

class Ellie():
    """
    This is a dqn agent. This will handle most of the needed action portion of the network.
    """

    def __init__(self) -> None:
        self.pipe = pipeline("conversational", model="PygmalionAI/pygmalion-6b")

    def get_response(self, prompt):
        response = self.pipe(prompt)
        return response
    
    def ingest(self):
        pass
    