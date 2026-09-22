import requests
from bs4 import BeautifulSoup
import re
import wikipedia

USER_AGENT = "MyWikiBot/1.0 (https://example.com/; myemail@example.com)"

def get_one_paragraph_wikipedia(min_words=75, max_words=100, max_tries=8):
    tries = 0
    headers = {"User-Agent": USER_AGENT}
    while tries < max_tries:
        tries += 1
        try:
            title = wikipedia.random()
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != 200:
                continue

            soup = BeautifulSoup(r.text, "html.parser")
            content = soup.select_one("div.mw-parser-output")
            if not content:
                continue

            paras = content.find_all("p")
            good_paras = []
            for p in paras:
                text = p.get_text().strip()
                if not text:
                    continue
                if len(text.split()) < 20:
                    continue
                good_paras.append(text)

            if not good_paras:
                continue

            # Combine into one block of text
            combined = " ".join(
                re.sub(r"\s+", " ", re.sub(r"\[.*?\]", "", p)).strip()
                for p in good_paras if p.strip()
            )

            # Split into sentences
            sentences = re.split(r'(?<=[.!?])\s+', combined)
            sentences = [s.strip() for s in sentences if s.strip()]

            # Build paragraph sentence by sentence until word count in range
            final_sentences = []
            word_count = 0
            for s in sentences:
                s_words = len(s.split())
                if word_count + s_words > max_words:
                    break
                final_sentences.append(s)
                word_count += s_words
                if word_count >= min_words:
                    break

            if min_words <= word_count <= max_words:
                return " ".join(final_sentences)

        except Exception:
            pass

# Example usage
if __name__ == "__main__":
    paragraph = get_one_paragraph_wikipedia()
    print(paragraph)
    print("\nWord Count:", len(paragraph.split()))
