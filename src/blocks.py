from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n")
    stripped_list = []
    for entry in list_of_blocks:
        stripped_entry = entry.strip()
        if stripped_entry:
            stripped_list.append(stripped_entry)
    print(stripped_list)
    return stripped_list