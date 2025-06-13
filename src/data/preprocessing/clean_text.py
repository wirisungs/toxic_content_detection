import pandas as pd
import re
import emoji
from autocorrect import Speller

# Load dataset
df = pd.read_csv('../../data/raw/comments.csv')

# Giữ lại 1000 dòng đầu tiên
df = df.head(1000)

# Hàm làm sạch
spell = Speller(lang='en')

def remove_emoji(text):
    """Loại bỏ emoji khỏi văn bản."""
    try:
      text = str(text);
      return emoji.replace_emoji(text, replace='')
    except:
      return ''

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def to_lowercase(text):
    return text.lower()

def autocorrect(text):
    return spell(text)

def clean_text(text):
    text = remove_emoji(text)
    text = remove_punctuation(text)
    text = to_lowercase(text)
    text = autocorrect(text)
    return text

# Áp dụng làm sạch
df = df.head(1000).copy()
df['cleaned_comment'] = df['comment'].apply(clean_text)

df = df.drop(columns=['comment'])

# Lưu kết quả
df[['cleaned_comment']].to_csv('../../data/raw/cleaned_comments.csv', index=False)

# Xem trước
df.head()
