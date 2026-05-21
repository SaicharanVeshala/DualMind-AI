import ollama


def generate_oss_response(prompt):

    try:

        response = ollama.chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception:

        return (
            "Unable to generate response right now."
        )