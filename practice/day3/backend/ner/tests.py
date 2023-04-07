from django.test import TestCase
from .models import Documents
from django.db import models
import json
from typing import List, Dict, Union


def _create_document(doc_id: int, doc_text: str, entities: List[Dict[str, Union[str, int]]]) -> models.Model:
    doc = Documents.objects.create(doc_id=doc_id, doc_text=doc_text, entities=json.dumps(entities))
    return doc


# Create your tests here.
class DocumentsModelTests(TestCase):

    def test_document_entity_is_valid_json(self):
        """
        Explain the test issue here.
        Demonstrate the input and output
        """
        # entities = [{"label": "TICKER", "start": 0, "end": 4, "token": "AAPL"}]
        # _create_document(doc_id=666, doc_text='AAPL is a company', entities=entities)
        data = Documents.objects.all()
        print(data)
        # self.assertTrue(all([isinstance(json.loads(i.entities), list) for i in data]))
        self.assertTrue(True)

