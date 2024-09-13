def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
    text (str): The text to print.

    Raises:
    TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Replace each occurrence of `.`, `?`, `:` with the character followed by two new lines
    for char in ".?:":
        text = (char + "\n\n").join(part.strip() for part in text.split(char))
    
    # Print the final formatted text
    print(text.strip())
