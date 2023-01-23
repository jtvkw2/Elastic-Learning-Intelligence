import spacy
import json
 
class EntityRecognition:
    def __init__(self) -> None:
        self.core = spacy.load("en_core_web_sm")

    def run(self, text):
        # List of all entities
        results = []
        
        # Run with general model
        doc = self.core(text)
        doc_json = doc.to_json()['ents']
        for elem in doc_json:
            elem["word"] = text[elem["start"]:elem["end"]]
            results.append(elem)
        return results
    
    def find_matches(self, input):
        result = input
        
        return result
    
    def train(self, name, data_location):
        """
        The train function is for creating a custom model for entity recognition

        Args:
            name (string): name of the model to create
            data_location (string): path to input words
        """
        pass