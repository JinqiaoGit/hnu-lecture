from django.db import models
import json


# Create your models here.
class Documents(models.Model):
    doc_id = models.IntegerField(null=False, primary_key=True)  # max length 255
    doc_text = models.TextField(max_length=5e6)
    entities = models.TextField(max_length=2000)
    update_date = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return f"\nId: {self.doc_id}\ntext: {self.doc_text}\nentities:" \
               f" {self.entities}\nupdate date: {self.update_date}\n"

    def get_entities(self):
        return json.loads(self.entities)
