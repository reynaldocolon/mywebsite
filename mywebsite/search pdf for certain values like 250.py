import os
import re
from tkinter import Tk, filedialog
import fitz

def highlight_optical_over_250():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    input_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not input_path:
        return

    folder = os.path.dirname(input_path)
    name, ext = os.path.splitext(os.path.basename(input_path))
    output_path = os.path.join(folder, f"{name}_optical_over_250{ext}")

    doc = fitz.open(input_path)
    total_highlights = 0
    # Matches numbers like 250.01, 1,250.00, $500.00
    amount_pattern = re.compile(r'\$?\b(\d{1,3}(?:,\d{3})*\.\d{2})\b')

    for page in doc:
        # Check each line or block of text on the page
        blocks = page.get_text("blocks")
        for b in blocks:
            text = b[4]
            if "optical" in text.lower():
                for match in amount_pattern.finditer(text):
                    raw_num = match.group(1).replace(",", "")
                    if float(raw_num) == 250.00:
                        # Highlight the matching amount on the page
                        for inst in page.search_for(match.group(0)):
                            annot = page.add_highlight_annot(inst)
                            annot.set_colors({"stroke": [1, 1, 0]})
                            annot.update()
                            total_highlights += 1

    if total_highlights > 0:
        doc.save(output_path, garbage=4, deflate=True)
        print(f"Highlighted {total_highlights} matches in: {output_path}")
    else:
        print("No matches found for 'optical' over $250.00.")

    doc.close()

if __name__ == "__main__":
    highlight_optical_over_250()
