from .builder import to_build_keyboard


def get_request_contact_keyboard():
    return to_build_keyboard({'text': 'Share the contact', 'request_contact': True}, resize_keyboard=True)