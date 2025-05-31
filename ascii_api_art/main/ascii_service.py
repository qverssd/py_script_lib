import pyfiglet

def generate_ascii_art(text: str, font: str, str = "slant") -> str:
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        return f"[ERROR] {str(e)}"