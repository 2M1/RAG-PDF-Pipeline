from docling.document_converter import DocumentConverter

source = "./db_files_pdf/E1050.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

markdown_content = result.document.export_to_markdown()

# Specify the path to save the markdown file
output_file_path = "./output_file.md"  # You can specify a path here

# Open the file in write mode and save the content
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print(f"Markdown file saved as {output_file_path}")

