from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = 7
AVAIABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    print(model_class.objects.all())

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code

def check_long_url_present(model_instance):
    model_class = model_instance.__class__
    return model_class.objects.get(long_url=model_instance.long_url)
