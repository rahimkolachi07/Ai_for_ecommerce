def remove_special_character(sentence):
    words = sentence.split()
    cleaned_words = [word.replace("¿", "") for word in words[:5]] + words[5:]
    cleaned_sentence = " ".join(cleaned_words)
    return cleaned_sentence
