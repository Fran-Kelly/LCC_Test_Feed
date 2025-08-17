import os

def summarise_report(title, url, content):
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Summarise in ≤50 words: {title} {content}"}]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[AI summary failed, fallback used] {content[:150]}"
    return f"[Local summary] {content[:150]}"
