import random
import memory


def generate_reply(user_text):
    history = memory.load_memory()

    text = (user_text or '').lower()

    if 'hello' in text or 'cze' in text or 'hej' in text:
        return 'Cześć. Jak mogę pomóc?'

    if 'ai' in text or 'sztuczna' in text:
        return 'Sztuczna inteligencja to zdolność maszyn do uczenia się na danych.'

    responses = [
        'Interesujące.',
        'Opowiedz więcej.',
        'Wyjaśnij proszę swoją myśl dokładniej.',
        'To warto przeanalizować.'
    ]

    return random.choice(responses)
