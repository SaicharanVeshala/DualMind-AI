from google import genai


# ---------------- CREATE CLIENT ---------------- #

client = genai.Client(
    api_key="AIzaSyBBxFNKrEBhBc048YRujfUwXdR2BcfSk38"
)


# ---------------- FRONTIER RESPONSE ---------------- #

def generate_frontier_response(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        error_message = str(e)

        # Quota exceeded
        if "429" in error_message:

            return (
                "Frontier model quota exceeded. "
                "Please try again later."
            )

        return (
            "Unable to generate response right now."
        )