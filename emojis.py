# https://pypi.org/project/emoji/

import emoji

def extract_emojis(str):
    return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)

def text_without_emojis(str):
    return ''.join(c for c in str if c not in emoji.UNICODE_EMOJI)

text_with_emoji = "Come to Jesus meeting!!!! What on earth is that supposed to be? 😔 https://t.co/a3lOpTtFig"
print(extract_emojis(text_with_emoji))
print(text_without_emojis(text_with_emoji))