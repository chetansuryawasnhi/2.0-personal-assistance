import openai
import time

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Define a prompt
prompt = "Once upon a time"

# Set the number of requests you want to make (reduced to 3 in this example)
num_requests = 3

for _ in range(num_requests):
    # Generate text using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # You can adjust the number of tokens as needed
    )

    # Print the generated text
    print(response.choices[0].text)

    # Add a delay before making the next request (2 seconds in this example)
    time.sleep(2)
