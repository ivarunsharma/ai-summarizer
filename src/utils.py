import newspaper


def fetch_url_text(url: str) -> str:
    """Fetch and extract article text from a URL."""
    article = newspaper.Article(url)
    article.download()
    article.parse()
    if not article.text:
        raise ValueError("Could not extract text from this URL. Try a different article.")
    return article.text


def get_stats(text: str) -> dict:
    """Return word, sentence and character counts for a piece of text."""
    words     = len(text.split())
    sentences = len([s for s in text.split(".") if s.strip()])
    chars     = len(text)
    return {"words": words, "sentences": sentences, "chars": chars}


def compression_ratio(original: str, summary: str) -> int:
    """Return how much smaller the summary is vs original, as a percentage."""
    orig_words = len(original.split())
    summ_words = len(summary.split())
    if orig_words == 0:
        return 0
    return round((1 - summ_words / orig_words) * 100)
