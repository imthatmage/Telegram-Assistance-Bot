# mail_ru_llm_Nurmukhametov_Almir
# Telegram bot assistant project


## Примеры работы бота
GPT2 Answers             |  Mistral Answers | Ngram Model
:-------------------------:|:-------------------------:|:-------------------------:
![](examples/gpt2_example.png)  |  ![](examples/mistral_example.png) | ![](examples/statlm_example.png)


## Метрики на инструкционных моделях
| Model   | Training Loss | Validation Loss | Rouge1   | Rouge2   | Rougel   | Rougelsum | Bleu     |
| -----   | ------------- | --------------- | -------- | -------- | -------- | --------- | -------- |
| **GPT2**    | 1.948600      | 1.965270        | 0.171252 | 0.088855 | 0.167642 | 0.168607  | 0.480183 |
| **Mistral** | 0.931100      | 0.835708        | **0.191417** | **0.123226** | **0.190067** | **0.189545**  | **0.535177** |


## Простая модель на основе статистик встречаемости ngram
* `training_notebooks/stat_lm_training.ipynb` -- основной notebook по обучению модели.
* `Training Data`: для обучения использовался [датасет](https://huggingface.co/datasets/Den4ikAI/russian_dialogues) из диалогов собранных с Telegram чатов.

## GPT2 Model Trained Using QLoRA: LoRA (Low Rank Adaptation) and 4bit quantization
* `training_notebooks/rugptlarge_lm_qlora_training.ipynb` -- основной notebook по обучению модели
* `Training Data`: для обучения использовался из [датасет](https://huggingface.co/datasets/lksy/ru_instruct_gpt4) из инструкций, сгенерированных с помощью GPT4.

## Mistral 7b Model Trained Using QLoRA: LoRA (Low Rank Adaptation) and 4bit quantization
* `training_notebooks/mistral_7b_v0.1.ipynb` -- основной notebook по обучению модели
* `Training Data`: для обучения использовался из [датасет](https://huggingface.co/datasets/lksy/ru_instruct_gpt4) из инструкций, сгенерированных с помощью GPT4.

## Установка
### Веса моделей можно найти по [ссылке](https://drive.google.com/drive/folders/1kWuNNIbJRMgzrn3Ip_jS54pMkmEj7RVA?usp=sharing)
Для того, чтобы заработал весь функционал, архивы моделей необходимо распаковать в папку `models`.

**Для корректного функционирования бота необходимо установить все пакеты из** `requirements.txt`:

**Бота можно запустить с помощью команды**:
```
python llm_assistant_bot.py
```