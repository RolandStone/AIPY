import transformers
import torch

# Load the pre-trained model
model = transformers.AutoModelForCausalLM.from_pretrained("distilgpt2")
tokenizer = transformers.AutoTokenizer.from_pretrained("distilgpt2")

conversations = []

def chatbot():
    user_input = input("You: ")
    conversations.append(["User: ", user_input])
    if "hi" in user_input.lower():
        bot_response = "Hello!"
    elif "bye" in user_input.lower():
        bot_response = "Goodbye!"
    else:
        # Encode the user's input and generate a response
        input_ids = tokenizer.encode(user_input, return_tensors='pt', add_special_tokens=True)
        if input_ids.shape[1] == 0:
            bot_response = "I couldn't understand your input. Could you please rephrase it?"
        else:
            attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
            response = model.generate(input_ids, attention_mask=attention_mask, max_length=100, top_k=50, top_p=0.9, eos_token_id=50256, pad_token_id=50256)
            bot_response = tokenizer.decode(response[0], skip_special_tokens=True)
    print("Bot: " + bot_response)
    conversations.append(["Bot: ", bot_response])

while True:
    chatbot()

