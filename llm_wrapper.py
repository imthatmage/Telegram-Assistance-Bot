from typing import Literal
import os

import torch
from peft import (
    PeftConfig,
    PeftModel,
)
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)


class LLMWrapper:

    def __init__(self, model_name):
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            load_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        PEFT_MODEL = f"models/{model_name}"

        config = PeftConfig.from_pretrained(PEFT_MODEL)
        self.model = AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path,
            return_dict=True,
            quantization_config=bnb_config,
            device_map="auto",
        )

        self.tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
        self.model = PeftModel.from_pretrained(self.model, PEFT_MODEL)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate(self, input_text, **generation_params):
        input_text = f'### Задание: {input_text}\n\n### Ответ:'
        self.device = "cuda:0"
        encoding = self.tokenizer(input_text, return_tensors="pt").to(self.device)
        with torch.inference_mode():
            outputs = self.model.generate(
                input_ids = encoding.input_ids,
                attention_mask = encoding.attention_mask,
                **generation_params,
        )
        pred_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        sequence_start = pred_text.find("## Ответ:") + 9

        pred_text = pred_text[sequence_start:]
        return pred_text
        

def construct_model(model_name: Literal["gpt2", "mistral_7b"]):
    model = LLMWrapper(model_name)
    generation_params = {
        "max_new_tokens": 300,
        "num_beams": 3,
        "early_stopping": True,
        "no_repeat_ngram_size": 2,
        "eos_token_id": model.tokenizer.eos_token_id,
        "pad_token_id": model.tokenizer.eos_token_id,
    }
    return model, generation_params
