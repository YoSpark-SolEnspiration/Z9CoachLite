# File: pdf_export.py — Z9CoachLite

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_lite_report(profile_data: dict, filename: str = "Z9_Insight_Report.pdf") -> bytes:
    """
    Generate a PDF report for the Lite app.
    Includes all trait visuals & summaries except Pro-level hidden logic.
    """
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, "Z9CoachLite — Insight Report")

    # Main summary
    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, f"Composite Trait Score: {profile_data['trait_score']:.2f}")
    y -= 20
    c.drawString(50, y, f"Harmony Ratio: {profile_data['harmony_ratio']:.1f}%")
    y -= 20
    c.drawString(50, y, f"Z9 Spiral Stage: {profile_data['stage']}")
    y -= 30

    # Trait summary (multi-line)
    c.drawString(50, y, "Trait Summary:")
    y -= 20
    text_object = c.beginText(50, y)
    text_object.setFont("Helvetica", 10)
    for line in profile_data["trait_summary"].split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()
