import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

PROMPTS = {
    "Brief (2-3 sentences)":  "Summarize the following text in 2-3 clear, concise sentences.",
    "Bullet points":          "Summarize the following text as exactly 5 bullet points. Each bullet should be one sentence.",
    "ELI5 (Simple English)":  "Explain the following text like I am 5 years old. Use very simple words and short sentences.",
    "Key takeaways":          "Extract the 3 most important takeaways from the following text. Number each one.",
}


def get_styles() -> list:
    """Return available summary styles."""
    return list(PROMPTS.keys())


def summarize(text: str, style: str) -> str:
    """
    Send text to Claude Haiku and return a summary.

    Args:
        text:  The input text to summarize.
        style: One of the keys in PROMPTS.

    Returns:
        The summary string from Claude.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = PROMPTS.get(style, PROMPTS["Brief (2-3 sentences)"])

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n---\n\n{text}"
            }
        ]
    )
    return message.content[0].text
