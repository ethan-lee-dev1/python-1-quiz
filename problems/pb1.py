def replace_spaces(str, punc):
    result = ""
    for char in str:
        if char == " ":
            result += punc
        else:
            result += char
    return result



# sentence = "Test  This is a test   Testing "
# sentence2 = pb1.replace_spaces(sentence, "_")
# print(sentence2) # -> Test__This_is_a_test__Testing_