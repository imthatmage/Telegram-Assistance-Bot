# mail_ru_llm_Nurmukhametov_Almir
# Telegram bot assistant project

## Веса моделей можно найти по [ссылке](https://drive.google.com/drive/folders/1kWuNNIbJRMgzrn3Ip_jS54pMkmEj7RVA?usp=sharing)
Для того, чтобы заработал весь функционал архивы моделей необходимо распаковать в папку `models`.

## Простая модель на основе статистик встречаемости ngram
* `training_notebooks/stat_lm_training.ipynb` -- основной notebook по обучению модели.
* `Training Data`: для обучения использовался [датасет](https://huggingface.co/datasets/IlyaGusev/gazeta) из новостных текстов на русском языке.

## GPT2 Model Trained Using QLoRA: LoRA (Low Rank Adaptation) and 4bit quantization
* `training_notebooks/rugptlarge_lm_qlora_training.ipynb` -- основной notebook по обучению модели
* `Training Data`: для обучения использовался из [датасет](https://huggingface.co/datasets/lksy/ru_instruct_gpt4) из инструкций, сгенерированных с помощью GPT4.