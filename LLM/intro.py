from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


while True:
    prompt = input("Prompt:")

    if prompt == "exit": 
        print("Good Bye!")
        break
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    # Generate text with the model
    attention_mask = torch.ones(input_ids.shape, device=input_ids.device)

    # Generate text with attention mask and pad token ID set
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=50,
        num_return_sequences=3,
        no_repeat_ngram_size=2,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id  # Set pad_token_id to eos_token_id as a workaround
    )
    # Decode the output text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    print("Response:\n")
    for i, generated_text_enc in enumerate(output):
        generated_text = tokenizer.decode(generated_text_enc, skip_special_tokens=True)
        print(f"{generated_text}\n")
