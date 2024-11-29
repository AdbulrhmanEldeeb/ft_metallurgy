from unsloth import FastLanguageModel
from prompts import metallurgy_prompt
import torch 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model():
    max_seq_length = 2048
    dtype = None
    load_in_4bit = True

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="Abdulrhman37/lora_model",
        max_seq_length=max_seq_length,
        dtype=dtype,
        load_in_4bit=load_in_4bit,
    )
    FastLanguageModel.for_inference(model)
    return model, tokenizer

def answer(model, tokenizer, query: str) -> str:
    inputs = tokenizer(
        [metallurgy_prompt.format(query, "", "")], 
        return_tensors="pt"
    ).to(device)

    outputs = model.generate(**inputs, use_cache=True)
    result = tokenizer.batch_decode(outputs)
    split_content = result[0].split("### Response:")
    return split_content[1].strip().replace("<|end_of_text|>", "")
