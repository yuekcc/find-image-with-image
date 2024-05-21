from typing import List
from clip_cpp import Clip

model = Clip("models/clip-vit-base-patch32_ggml-model-q5_1.gguf", verbosity=2)


def embed_image(fila_path: str) -> List[float]:
    return model.load_preprocess_encode_image(fila_path)


def compare(target: List[float], pattern: List[float]) -> float:
    return model.calculate_similarity(pattern, target)


if __name__ == '__main__':
    input1 = embed_image("test_data/input-1.png")
    input2 = embed_image("test_data/input-2.png")
    input3 = embed_image("test_data/input-3.png")
    select1 = embed_image("test_data/select-1.png")
    button1 = embed_image("test_data/button-1.png")

    print("input1 vs input2", compare(input2, input1))
    print("input1 vs input2 switch", compare(input1, input2))
    print("input1 vs input3", compare(input3, input1))
    print("input1 vs select1", compare(select1, input1))
    print("input1 vs button1", compare(button1, input1))
