from get_text import get_text
from scrape import summarize as summarize_f

def summarize(file_path, bullet_points=True):
    text_arr, text = get_text(file_path)

    summarized = summarize_f(text).summary

    if bullet_points:
        arr = summarized.split(". ")

        for i, text in enumerate(arr):
            arr[i] = "- " + text + ". "

        summarized = "\n".join(arr)

    return summarized

if __name__ == "__main__":
    print(summarize(input("Enter the file path: ")))