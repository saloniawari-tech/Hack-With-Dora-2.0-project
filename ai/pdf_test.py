from utils.pdf_loader import extract_pdf_text


pdf_path = "ai/sample_data/lease.pdf"


text = extract_pdf_text(pdf_path)


print("====================")
print("PDF TEXT")
print("====================")

print(text)