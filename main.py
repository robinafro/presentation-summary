from get_text import get_text
from scrape import summarize as summarize_f

import re
import sys

def summarize(file_path, bullet_points=True):
    text_arr, text = get_text(file_path)

    summarized = summarize_f(text)['summary']

    if bullet_points:
        arr = re.split(r"\. ", summarized)
        new_arr = []

        for i, text in enumerate(arr):
            if re.match(r"(\w| )+[a-z] ?", text):
                new_arr.append(text)
            else:
                if i == 0:
                    new_arr.append(text)
                else:
                    new_arr[i - 1] = new_arr[i - 1] + ". " + text

        for i, text in enumerate(new_arr):
            new_arr[i] = "- " + text + ". "

        summarized = "\n".join(new_arr)

    return summarized

if __name__ == "__main__":
    # Read the command arguments
    if len(sys.argv) > 1:
        print(summarize(sys.argv[1], bullet_points=(sys.argv[2] == "true" if len(sys.argv) > 2 else True)))
    else:
        print(summarize(input("Enter the file path: "), bullet_points=(input("Bullet points? (true/false): ").lower() == "true")))