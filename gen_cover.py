#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generates a Civil Action Cover Sheet PDF for King County Superior Court
with the details provided in the complaint of:
   Bo Shang v. Amazon.com, Inc.
Ensure you have the reportlab library installed:
   pip install reportlab

Usage:
   python civil_cover_sheet.py
This will produce:
   CivilActionCoverSheet.pdf
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_civil_cover_sheet(output_filename="CivilActionCoverSheet.pdf"):
    # Sample style sheet
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_heading = styles["Heading1"]
    style_subheading = styles["Heading2"]

    # Custom styles
    style_title = ParagraphStyle(
        "CoverSheetTitle",
        parent=style_heading,
        fontSize=14,
        leading=18,
        alignment=1,  # center
        spaceAfter=10,
    )

    style_section = ParagraphStyle(
        "CoverSheetSection",
        parent=style_subheading,
        fontSize=12,
        leading=14,
        spaceBefore=12,
        spaceAfter=4,
    )

    style_label = ParagraphStyle(
        "LabelStyle",
        parent=style_normal,
        fontSize=10,
        leading=12,
        textColor=colors.black,
        spaceAfter=2,
    )

    style_field = ParagraphStyle(
        "FieldStyle",
        parent=style_normal,
        fontSize=10,
        leading=12,
        textColor=colors.black,
        spaceAfter=5,
    )

    # Create the PDF document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=LETTER,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )

    content = []

    # Title
    content.append(Paragraph("Superior Court of Washington\nFor King County", style_title))

    # Subtitle
    content.append(Paragraph("Civil Case Cover Sheet", style_section))
    content.append(Spacer(1, 0.2 * inch))

    # Basic Case Information Table
    # Replace "TBD" or blank if you do not yet have a case number assigned
    case_info_data = [
        [
            Paragraph("<b>Case Number:</b>", style_label),
            Paragraph("___________ (Assigned by Clerk)", style_field),
        ],
        [
            Paragraph("<b>Case Title:</b>", style_label),
            Paragraph("Bo Shang v. Amazon.com, Inc.", style_field),
        ],
        [
            Paragraph("<b>Date of Filing:</b>", style_label),
            Paragraph("February 4, 2025", style_field),
        ],
        [
            Paragraph("<b>Judge Assigned (if known):</b>", style_label),
            Paragraph("", style_field),  # Leave blank if unknown
        ],
    ]

    case_info_table = Table(case_info_data, hAlign="LEFT", colWidths=[2 * inch, 4 * inch])
    case_info_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    content.append(case_info_table)
    content.append(Spacer(1, 0.3 * inch))

    # Plaintiff Information
    plaintiff_data = [
        [
            Paragraph("<b>Plaintiff Name(s):</b>", style_label),
            Paragraph("1)  Bo Shang", style_field),
        ],
        [
            Paragraph("<b>Plaintiff Contact Info:</b>", style_label),
            Paragraph(
                "10 McCafferty Way<br/>"
                "Phone: 781-999-4101<br/>"
                "Email: bo@shang.software",
                style_field,
            ),
        ],
    ]

    plaintiff_table = Table(plaintiff_data, hAlign="LEFT", colWidths=[2 * inch, 4 * inch])
    plaintiff_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    content.append(Paragraph("Plaintiff Information", style_section))
    content.append(plaintiff_table)
    content.append(Spacer(1, 0.3 * inch))

    # Defendant Information
    defendant_data = [
        [
            Paragraph("<b>Defendant Name(s):</b>", style_label),
            Paragraph("1)  Amazon.com, Inc.", style_field),
        ],
        [
            Paragraph("<b>Defendant Principal Address:</b>", style_label),
            Paragraph(
                "410 Terry Avenue North<br/>"
                "Seattle, WA 98109",
                style_field,
            ),
        ],
    ]

    defendant_table = Table(defendant_data, hAlign="LEFT", colWidths=[2 * inch, 4 * inch])
    defendant_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    content.append(Paragraph("Defendant Information", style_section))
    content.append(defendant_table)
    content.append(Spacer(1, 0.3 * inch))

    # Nature of the Case & Relief
    # Typically, local rules or forms may require you to check boxes or specify categories.
    # For demonstration, we use descriptive text referencing your complaint’s causes of action.
    content.append(Paragraph("Nature of the Suit / Cause of Action", style_section))

    causes_text = """
    1. Violation of the Washington Consumer Protection Act (RCW 19.86)
    2. Breach of Implied Warranty of Merchantability (RCW 62A.2-314)
    3. Negligence / Negligent Misrepresentation
    4. Damages, injunctive relief, attorneys’ fees (if allowed), and other relief
    """

    content.append(Paragraph(causes_text.strip(), style_normal))
    content.append(Spacer(1, 0.3 * inch))

    # Case Type & Assignment
    case_type_data = [
        [
            Paragraph("<b>Case Type:</b>", style_label),
            Paragraph("Civil - Consumer Protection / Contract / Negligence", style_field),
        ],
        [
            Paragraph("<b>Relief Sought:</b>", style_label),
            Paragraph(
                "Compensatory and statutory damages; injunctive relief; attorneys’ fees (if permitted); "
                "and other appropriate relief as detailed in the Complaint.",
                style_field,
            ),
        ],
    ]

    case_type_table = Table(case_type_data, hAlign="LEFT", colWidths=[2 * inch, 4 * inch])
    case_type_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    content.append(case_type_table)
    content.append(Spacer(1, 0.3 * inch))

    # Attorney or Pro Se Info
    # Plaintiff is pro se here.
    pro_se_data = [
        [
            Paragraph("<b>Filing Party:</b>", style_label),
            Paragraph("Plaintiff, Pro Se", style_field),
        ],
        [
            Paragraph("<b>Attorney/Pro Se Name:</b>", style_label),
            Paragraph("Pro Se: Bo Shang", style_field),
        ],
        [
            Paragraph("<b>Signature / Date:</b>", style_label),
            Paragraph("______________________________  Dated: February 4, 2025", style_field),
        ],
    ]

    pro_se_table = Table(pro_se_data, hAlign="LEFT", colWidths=[2 * inch, 4 * inch])
    pro_se_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, 0), 0.25, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    content.append(Paragraph("Attorney / Pro Se Information", style_section))
    content.append(pro_se_table)

    # Build the PDF
    doc.build(content)
    print(f"PDF generated successfully: {output_filename}")

if __name__ == "__main__":
    # Run the function to create the civil cover sheet PDF
    create_civil_cover_sheet("CivilActionCoverSheet.pdf")