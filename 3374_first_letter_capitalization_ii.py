import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def cap_word(word):
        parts = word.split('-')

        if len(parts) == 2 and parts[0] and parts[1]:
            return '-'.join(
                p[:1].upper() + p[1:].lower()
                for p in parts
            )

        w = word.lower()
        return w[0].upper() + w[1:] if w and w[0].isalpha() else w

    user_content['original_text'] = user_content['content_text']

    user_content['converted_text'] = user_content['content_text'].apply(
        lambda text: ' '.join(cap_word(word) for word in text.split(' '))
    )

    return user_content[['content_id', 'original_text', 'converted_text']]