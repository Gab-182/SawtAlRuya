import openai
import os 
# Set your API key
api_key = os.environ.get('GPT')

# Initialize the OpenAI client
openai.api_key = api_key

# Example prompt for text generation
prompt = """I will give you YOLO object detection logs and you explain it to blind person as if he is seeing the image, [W NNPACK.cpp:64] Could not initialize NNPACK! Reason: Unsupported hardware.
0: 384x640 (no detections), 225.2ms
0: 384x640 1 person, 172.3ms

0: 384x640 1 person, 1 cell phone, 160.0ms
0: 384x640 1 person, 1 remote, 160.4ms
0: 384x640 1 person, 1 remote, 162.0ms
0: 384x640 1 person, 1 cell phone, 172.0ms"""

# Generate text using the API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50  # Adjust the number of tokens as needed
)

# Print the generated text
print(response.choices[0].text)
# print(openai.Model.list())

chat_gpt_like_bit = """import openai

# Initialize the chat messages history
messages = [{"role": "assistant", "content": "How can I help?"}]

# Function to display the chat history
def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

# Function to get the assistant's response
def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

# Main chat loop
while True:
    # Display chat history
    display_chat_history(messages)

    # Get user input
    prompt = input("User: ")
    messages.append({"role": "user", "content": prompt})

    # Get assistant response
    response = get_assistant_response(messages)
    messages.append({"role": "assistant", "content": response})"""

blog_outline_generator = """import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Please generate a blog outline on how a beginner can break into the field of data science."

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
"""