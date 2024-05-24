from typing import List
from clip_cpp import Clip

PROD_MODEL = "models/CLIP-ViT-L-14-laion2B-s32B-b82K_ggml-model-q5_1.gguf"
DEV_MODEL = "models/clip-vit-base-patch32_ggml-model-q4_0.gguf"
model = Clip(DEV_MODEL, verbosity=0)


def create_vector_of_text(text: str) -> List[float]:
    tokens = model.tokenize(text)
    return model.encode_text(tokens)


def create_vector_of_image(fila_path: str) -> List[float]:
    return model.load_preprocess_encode_image(fila_path)


def compare(vector_a: List[float], vector_b: List[float]) -> float:
    return model.calculate_similarity(vector_b, vector_a)
