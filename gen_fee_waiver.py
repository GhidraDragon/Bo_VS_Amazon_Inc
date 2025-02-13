#!/usr/bin/env python3
"""
Generate a Fee Waiver Request (PDF) for:
 - Case Number: FW25-000155 SEA
 - Case Title: SHANG VS AMAZON INC
 - Court: King County Superior Court
 - Applicant: Bo Shang (receives MA Medicaid)

This script uses ReportLab to create a PDF document with the necessary
information filled out, including a signature line on behalf of Bo Shang.
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit

def generate_fee_waiver_request(output_path: str):
    """
    Generates a Fee Waiver Request PDF for:
      - Case Number: FW25-000155 SEA
      - Case Title: SHANG VS AMAZON INC
      - Court: King County Superior Court
      - Applicant: Bo Shang (receives MA Medicaid)
    and saves it to the specified output path.
    """
    # Create a canvas for the PDF
    pdf = canvas.Canvas(output_path, pagesize=LETTER)
    width, height = LETTER
    
    # Set title
    pdf.setTitle("Fee Waiver Request - Bo Shang")
    
    # Define initial positions and styling
    x_left = inch
    y_top = height - inch
    line_spacing = 14
    pdf.setFont("Times-Roman", 12)
    
    # Helper function to draw multi-line text
    def draw_multiline_text(c, text, x, y, max_width=500):
        """
        Draw multiline text, automatically wrapping as needed,
        from the given (x, y) position, moving upwards.
        """
        lines = simpleSplit(text, "Times-Roman", 12, max_width)
        for line in lines:
            c.drawString(x, y, line)
            y -= line_spacing
        return y

    # Heading
    pdf.setFont("Times-Bold", 14)
    pdf.drawString(x_left, y_top, "Fee Waiver Request")
    pdf.setFont("Times-Roman", 12)
    y_top -= 2 * line_spacing

    # Court Information
    text_court = (
        "Superior Court of Washington\n"
        "County of King\n"
        "Case Number: FW25-000155 SEA\n"
        "Case Title: SHANG VS AMAZON INC\n"
    )
    y_top = draw_multiline_text(pdf, text_court, x_left, y_top)

    # Section Break
    y_top -= line_spacing

    # Applicant Statement
    text_statement = (
        "I, the undersigned, hereby request a waiver of fees for the above-referenced case. "
        "I am currently receiving MA Medicaid benefits and am unable to pay the court fees "
        "without substantial hardship to myself and/or my dependents.\n\n"
        
        "I declare that the following information is true and complete to the best of my knowledge:\n\n"
        
        "1. Full Name of Applicant: Bo Shang\n"
        "2. Address: 10 McCafferty Way, Burlington MA 01803\n"
        "3. Phone Number: 781-999-4101\n"
        "4. Date of Birth: 06/06/1988\n"
        "5. Government Assistance Received: MA Medicaid (Active)\n\n"
        
        "I understand that by requesting this fee waiver, the Court may require additional documentation "
        "in support of my financial situation and my receipt of government benefits. "
        "I agree to provide such documentation if requested.\n\n"
        
        "Under penalty of perjury under the laws of the State of Washington, I certify that "
        "the information provided in this request is true and correct."
    )
    y_top = draw_multiline_text(pdf, text_statement, x_left, y_top)

    # Signature
    y_top -= 2 * line_spacing
    pdf.drawString(x_left, y_top, "Signature (on behalf of Applicant): _______Bo Shang______   Date: ___2/13/2025__")

    y_top -= line_spacing
    pdf.drawString(x_left, y_top, "Signed By: /s/ Bo Shang")

    # Finalize and save PDF
    pdf.showPage()
    pdf.save()

def main():
    """
    Main function to demonstrate the generation of the Fee Waiver Request PDF.
    You can specify a different output file as needed.
    """
    output_pdf = "Fee_Waiver_Request_Bo_Shang.pdf"
    generate_fee_waiver_request(output_pdf)
    print(f"PDF generated and saved as: {os.path.abspath(output_pdf)}")

if __name__ == "__main__":
    main()