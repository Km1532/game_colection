import os
import re
import string
from typing import List
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords

def check_folder_exist(folder: str):
    """Check if folder exists."""
    if not os.path.exists(folder):
        raise FileNotFoundError(f'Folder {folder} does not exist')

def get_filenames_from_folder(folder: str) -> List[str]:
    """Get list of filenames in folder."""
    return os.listdir(folder)

def filter_filenames(filenames: List[str]) -> List[str]:
    """Filter filenames to match the pattern 1900_BoysNames.txt."""
    match_filename = re.compile(r'^[1-2][09][0-9][0-9]_(BoysNames|GirlsNames)\.txt$')
    return [filename for filename in filenames if match_filename.search(filename)]

def remove_chars_from_text(text: str, chars: str) -> str:
    """Remove specified characters from text."""
    return "".join([ch for ch in text if ch not in chars])

def run(folder: str):
    """Main controller."""
    try:
        check_folder_exist(folder)
    except FileNotFoundError as error:
        return error

    filenames = get_filenames_from_folder(folder)
    filtered_filenames = filter_filenames(filenames)

    if 'new_file.txt' not in filtered_filenames:
        print('OK')
    else:
        print('Wrong')

if __name__ == '__main__':
    path_to_folder = 'baby_names'
    print(run(path_to_folder))
