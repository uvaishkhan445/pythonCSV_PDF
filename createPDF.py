from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create a PDF file
pdf_file_name = "table_example.pdf"
pdf = SimpleDocTemplate(pdf_file_name, pagesize=letter)

# Sample data for the table
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
    ["David", 28, "Houston"],
]

# Create a Table object
table = Table(data)

# Add style to the table
style = TableStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header background
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center alignment for all cells
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Bold header font
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),  # Padding for header
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Background color for data
        ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Grid lines
    ]
)

table.setStyle(style)

# Build the PDF with the table
pdf.build([table])

print(f"PDF file '{pdf_file_name}' created successfully!")
