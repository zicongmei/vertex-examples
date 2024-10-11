import vertexai

from vertexai.generative_models import GenerativeModel, ChatSession

PROJECT_ID = "zicong-gke-multi-cloud-dev-2"
vertexai.init(project=PROJECT_ID, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")
# model = GenerativeModel("publishers/google/models/gemma2")


chat_session = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    response = chat.send_message(prompt)
    return response.text

while True:
    # Get the input data from the user
    prompt = input("> ")
    print(get_chat_response(chat_session, prompt))
