from assistants.oss_assistant import generate_oss_response

reply = generate_oss_response(
    "Explain machine learning in simple words"
)

print(reply)