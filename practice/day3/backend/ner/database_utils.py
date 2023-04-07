from .models import Documents


def get_doc_element(doc_id: int, attribute_name: str):
    data = Documents.objects.get(doc_id=doc_id)
    element_data = getattr(data, attribute_name)
    return element_data
