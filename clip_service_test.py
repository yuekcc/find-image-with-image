from clip_service import compare, create_vector_of_image, create_vector_of_text

if __name__ == '__main__':
    input1 = create_vector_of_image("test_data/input-1.png")
    input2 = create_vector_of_image("test_data/input-2.png")
    input3 = create_vector_of_image("test_data/input-3.png")
    select1 = create_vector_of_image("test_data/select-1.png")
    button1 = create_vector_of_image("test_data/button-1.png")

    print("input1 vs input2", compare(input2, input1))
    print("input1 vs input3", compare(input3, input1))
    print("input1 vs select1", compare(select1, input1))
    print("input1 vs button1", compare(button1, input1))
