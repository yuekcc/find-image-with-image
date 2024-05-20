from clip_cpp import Clip

model = Clip("models/clip-vit-large-patch14_ggml-model-q8_0.gguf", 2)


def make_image_embed(fila_path):
    return model.load_preprocess_encode_image(fila_path)

def make_pattern_score(target, pattern):
    return model.calculate_similarity(pattern, target)


input1 = make_image_embed("test_data/input-1.png")
input2 = make_image_embed("test_data/input-2.png")
input3 = make_image_embed("test_data/input-3.png")
select1 = make_image_embed("test_data/select-1.png")
button1 = make_image_embed("test_data/button-1.png")

print("input1 vs input2", make_pattern_score(input2, input1))
print("input1 vs input2 switch", make_pattern_score(input1, input2))
print("input1 vs input3", make_pattern_score(input3, input1))
print("input1 vs select1", make_pattern_score(select1, input1))
print("input1 vs button1", make_pattern_score(button1, input1))
