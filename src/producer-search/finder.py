import wikipedia

page_content = wikipedia.page("party 4 u").content


def extract_personnel_section(page_content):
    """
    Extracts the 'Personnel' section from the Wikipedia page content.
    """
    # Split the content into sections based on the '==' delimiter
    sections = page_content.split('\n==')
    personnel_section = None

    for section in sections:
        if section.strip().lower().startswith('personnel'):
            # Remove the header and any leading/trailing whitespace
            personnel_section = section.split('==', 1)[-1].strip()
            break
    if personnel_section:
        return personnel_section
    return "Personnel section not found."


print(page_content)



