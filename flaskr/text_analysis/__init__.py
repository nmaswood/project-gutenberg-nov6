import os
from groq import Groq


def get_plot_summary_analysis(text):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following plot: {text[:30000]}",
            }
        ],
        model="llama3-8b-8192"
        # Groq has 30000 token limit
    )
    return chat.choices[0].message.content
