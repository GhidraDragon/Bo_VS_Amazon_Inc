#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

"""
Generate a PDF of a civil action complaint using reportlab.

This script uses the ReportLab library to create a professionally 
formatted PDF document containing the provided legal text.

Dependencies:
    - Python 3.11+
    - reportlab (install via pip: pip install reportlab)

Usage:
    python generate_civil_action_pdf.py
"""

import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Indenter,
)
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER


def generate_civil_action_pdf(output_filename: str):
    """Generate a PDF for the civil action complaint text using ReportLab."""
    # Create document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=1 * inch,
        rightMargin=1 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="Civil Action Complaint",
        author="Bo Shang",
        subject="Complaint for Damages, Injunctive Relief, and Other Relief",
    )

    # Styles
    styles = getSampleStyleSheet()

    # Customize some styles
    style_title = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Title"],
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=12,
    )

    style_subtitle = ParagraphStyle(
        name="SubtitleStyle",
        parent=styles["Title"],
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    style_heading = ParagraphStyle(
        name="HeadingStyle",
        parent=styles["Heading1"],
        fontSize=12,
        leading=14,
        spaceAfter=6,
        spaceBefore=12,
    )

    style_paragraph = ParagraphStyle(
        name="ParagraphStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )

    style_paragraph_indent = ParagraphStyle(
        name="ParagraphIndentStyle",
        parent=style_paragraph,
        leftIndent=20,
    )

    style_bulleted_list = ParagraphStyle(
        name="BulletedListStyle",
        parent=style_paragraph,
        bulletIndent=20,
        leftIndent=40,
        bulletFontName="Helvetica",
        bulletFontSize=10.5,
        leading=14,
    )

    style_paragraph_centered = ParagraphStyle(
        name="CenteredParagraphStyle",
        parent=style_paragraph,
        alignment=TA_CENTER,
    )

    # Flowables container
    story = []

    # Cover / Title
    story.append(Paragraph("SUPERIOR COURT OF WASHINGTON<br/>FOR KING COUNTY", style_title))
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "BO SHANG, an individual,<br/>Plaintiff,<br/><br/>v.<br/><br/>"
            "AMAZON.COM, INC., a Delaware corporation,<br/>Defendant.<br/><br/>"
            "Case No. __________",
            style_paragraph_centered,
        )
    )
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "COMPLAINT FOR DAMAGES, INJUNCTIVE RELIEF, AND OTHER RELIEF",
            style_subtitle,
        )
    )
    story.append(Spacer(1, 24))

    # I. INTRODUCTION
    story.append(Paragraph("I. INTRODUCTION", style_heading))
    intro_text_1 = (
        "1. Plaintiff, Bo Shang (“Plaintiff”), brings this action against Amazon.com, Inc. "
        "(“Amazon” or “Defendant”), alleging that Defendant sold or facilitated the sale of "
        "a stolen Google Pixel 7A smartphone through its Prime shipping program. "
        "Plaintiff contends that after discovering the phone was stolen, Amazon:"
    )
    story.append(Paragraph(intro_text_1, style_paragraph))
    # Nested bullet points
    bullet_points_intro_1 = [
        "Required Plaintiff to drop off the return in person at an Amazon-approved location; and",
        "Imposed a 20% restocking fee due to a purported 90-day return limit — even though the device’s "
        "stolen status was unknown to Plaintiff until after that period.",
    ]
    for bp in bullet_points_intro_1:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    intro_text_2 = (
        "2. Plaintiff seeks compensatory damages, equitable relief, attorneys’ fees "
        "(if permitted by law), and any other relief deemed just and proper."
    )
    story.append(Paragraph(intro_text_2, style_paragraph))

    # II. JURISDICTION AND VENUE
    story.append(Paragraph("II. JURISDICTION AND VENUE", style_heading))
    jurisdiction_text_3 = (
        "3. Subject Matter Jurisdiction: This Court has jurisdiction over the claims asserted herein "
        "under RCW 2.08.010, which grants the Superior Court original jurisdiction in all civil actions "
        "where the value of the claim exceeds the jurisdictional limits of inferior courts."
    )
    story.append(Paragraph(jurisdiction_text_3, style_paragraph))

    jurisdiction_text_4 = (
        "4. Personal Jurisdiction: Defendant Amazon.com, Inc. is headquartered in Seattle, Washington, "
        "transacts substantial business in King County, and has purposely availed itself of the benefits "
        "and protections of Washington laws. Therefore, personal jurisdiction is proper under RCW 4.28.185 "
        "and general principles of due process."
    )
    story.append(Paragraph(jurisdiction_text_4, style_paragraph))

    jurisdiction_text_5 = (
        "5. Venue: Venue is proper in King County under RCW 4.12.025(1) because Defendant’s principal place "
        "of business is in King County, and a substantial part of the events or omissions giving rise to "
        "Plaintiff’s claims occurred in King County."
    )
    story.append(Paragraph(jurisdiction_text_5, style_paragraph))

    # III. PARTIES
    story.append(Paragraph("III. PARTIES", style_heading))
    parties_text_6 = (
        "6. Plaintiff, Bo Shang (“Plaintiff”), is an individual residing in [County/State], who purchased "
        "a Pixel 7A smartphone from Amazon’s platform under the Amazon Prime shipping program."
    )
    story.append(Paragraph(parties_text_6, style_paragraph))

    parties_text_7 = (
        "7. Defendant, Amazon.com, Inc. (“Amazon” or “Defendant”), is a Delaware corporation with its "
        "principal place of business located at 410 Terry Avenue North, Seattle, Washington 98109."
    )
    story.append(Paragraph(parties_text_7, style_paragraph))

    # IV. FACTUAL BACKGROUND
    story.append(Paragraph("IV. FACTUAL BACKGROUND", style_heading))
    factual_text_8_intro = "8. Purchase and Discovery of Stolen Status:"
    story.append(Paragraph(factual_text_8_intro, style_paragraph))

    bullet_points_8 = [
        "On or about [date of purchase], Plaintiff purchased a Google Pixel 7A smartphone from Amazon. "
        "The product was labeled “Prime,” suggesting either it was sold by Amazon or fulfilled by "
        "Amazon on behalf of a third-party seller.",
        "Plaintiff received and used the phone but subsequently discovered, through [documentation from "
        "manufacturer/mobile carrier/police report/other source], that the device had been reported "
        "stolen before Plaintiff’s purchase.",
    ]
    for bp in bullet_points_8:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    factual_text_9_intro = "9. Notification to Amazon:"
    story.append(Paragraph(factual_text_9_intro, style_paragraph))

    bullet_points_9 = [
        "Plaintiff promptly informed Amazon Customer Service of the phone’s stolen status and requested a refund.",
        "Amazon instructed Plaintiff to drop off the device at an approved Amazon or carrier location. "
        "Plaintiff was forced to personally handle and transport the stolen item at his own expense "
        "and inconvenience.",
    ]
    for bp in bullet_points_9:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    factual_text_10_intro = "10. Restocking Fee Imposed:"
    story.append(Paragraph(factual_text_10_intro, style_paragraph))

    bullet_points_10 = [
        "Amazon refused to process the return without a 20% restocking fee, asserting that the phone was "
        "outside the 90-day return window.",
        "Plaintiff contends that the stolen status was not discoverable through normal use until after "
        "this arbitrary deadline; moreover, it is unconscionable to charge any restocking fee for "
        "returning a stolen product that never should have been sold in the first place.",
    ]
    for bp in bullet_points_10:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    factual_text_11_intro = "11. Harm to Plaintiff:"
    story.append(Paragraph(factual_text_11_intro, style_paragraph))

    bullet_points_11 = [
        "Plaintiff relied on Amazon’s representations of safety, security, and product legitimacy, "
        "especially for “Prime” products.",
        "Plaintiff incurred financial, legal, and practical harm, including the inconvenience and "
        "potential liability of possessing stolen goods, time and travel costs for dropping off "
        "the return, and the 20% restocking fee demanded by Amazon.",
    ]
    for bp in bullet_points_11:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    factual_text_12_intro = "12. Amazon’s Role and Representations:"
    story.append(Paragraph(factual_text_12_intro, style_paragraph))

    bullet_points_12 = [
        "By labeling the Pixel 7A purchase with “Prime,” Amazon effectively represented to Plaintiff "
        "that the item was vetted or at least subject to certain quality and authenticity controls.",
        "Plaintiff contends Amazon either owned the device before sale (as part of its Fulfillment by "
        "Amazon stock) or acted as a primary facilitator, thus materially controlling the transaction.",
        "In numerous marketing statements, Amazon promotes its marketplace as safe and reliable, "
        "guaranteeing customers they can “buy with confidence” under programs such as “A-to-Z Guarantee.” "
        "However, these assurances proved hollow in Plaintiff’s case.",
    ]
    for bp in bullet_points_12:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    # V. CAUSES OF ACTION
    story.append(Paragraph("V. CAUSES OF ACTION", style_heading))
    causes_of_action_intro = (
        "Plaintiff realleges and incorporates by reference each of the preceding paragraphs as though "
        "fully set forth herein."
    )
    story.append(Paragraph(causes_of_action_intro, style_paragraph))

    # COUNT I – VIOLATION OF THE WASHINGTON CONSUMER PROTECTION ACT (RCW 19.86)
    story.append(
        Paragraph(
            "COUNT I – VIOLATION OF THE WASHINGTON CONSUMER PROTECTION ACT (RCW 19.86)",
            style_heading,
        )
    )
    count1_text_13 = (
        "13. The Washington Consumer Protection Act (“WCPA”), codified at RCW 19.86, "
        "prohibits unfair or deceptive acts or practices in the conduct of trade or commerce."
    )
    story.append(Paragraph(count1_text_13, style_paragraph))

    count1_text_14 = (
        "14. Defendant, by enabling the sale of stolen goods under the Amazon Prime program and by "
        "imposing an unconscionable restocking fee when the item was finally discovered to be stolen, "
        "committed one or more unfair or deceptive acts or practices likely to mislead a reasonable "
        "consumer."
    )
    story.append(Paragraph(count1_text_14, style_paragraph))

    count1_text_15 = (
        "15. Case Law Support:<br/>"
        "• <i>Hangman Ridge Training Stables, Inc. v. Safeco Title Ins. Co.</i>, 105 Wn.2d 778, "
        "784–85 (1986) (stating the elements for a private action under the WCPA, including unfair "
        "or deceptive acts, occurring in trade or commerce, that affect the public interest, and "
        "cause injury).<br/>"
        "• <i>Klem v. Washington Mut. Bank</i>, 176 Wn.2d 771, 787 (2013) (affirming that an act "
        "need only have the capacity to deceive a substantial portion of the public to violate the CPA)."
    )
    story.append(Paragraph(count1_text_15, style_paragraph))

    count1_text_16 = (
        "16. Amazon’s acts and omissions proximately caused injury to Plaintiff’s business or property, "
        "including monetary loss and other damages, thus violating RCW 19.86.020."
    )
    story.append(Paragraph(count1_text_16, style_paragraph))

    count1_text_17 = (
        "17. Pursuant to RCW 19.86.090, Plaintiff seeks actual damages, treble damages up to statutory "
        "limits, and reasonable attorneys’ fees and costs."
    )
    story.append(Paragraph(count1_text_17, style_paragraph))

    # COUNT II – BREACH OF IMPLIED WARRANTY OF MERCHANTABILITY (RCW 62A.2-314)
    story.append(
        Paragraph(
            "COUNT II – BREACH OF IMPLIED WARRANTY OF MERCHANTABILITY (RCW 62A.2-314)",
            style_heading,
        )
    )
    count2_text_18 = (
        "18. Under RCW 62A.2-314, every contract for the sale of goods includes an implied warranty "
        "of merchantability, which ensures the product is fit for the ordinary purposes for which goods "
        "of that kind are used, and that the product is lawfully sold (not stolen)."
    )
    story.append(Paragraph(count2_text_18, style_paragraph))

    count2_text_19 = (
        "19. By advertising and fulfilling the sale of a stolen Google Pixel 7A, Defendant breached "
        "the implied warranty of merchantability, as stolen merchandise cannot be lawfully resold "
        "and is inherently unfit for normal ownership and use."
    )
    story.append(Paragraph(count2_text_19, style_paragraph))

    count2_text_20 = (
        "20. Case Law Support:<br/>"
        "• <i>Baughn v. Honda Motor Co., Ltd.</i>, 107 Wn.2d 127, 151 (1986) (discussing implied warranties "
        "in the context of consumer goods).<br/>"
        "• <i>Touchet Valley Grain Growers, Inc. v. Opp &amp; Seibold Gen. Constr., Inc.</i>, 119 Wn.2d "
        "334, 341 (1992) (outlining the scope of implied warranties under Washington’s Uniform Commercial Code)."
    )
    story.append(Paragraph(count2_text_20, style_paragraph))

    count2_text_21 = (
        "21. As a direct and proximate result of Defendant’s breach, Plaintiff suffered damages in "
        "an amount to be proven at trial."
    )
    story.append(Paragraph(count2_text_21, style_paragraph))

    # COUNT III – NEGLIGENCE / NEGLIGENT MISREPRESENTATION
    story.append(
        Paragraph(
            "COUNT III – NEGLIGENCE / NEGLIGENT MISREPRESENTATION",
            style_heading,
        )
    )
    count3_text_22 = (
        "22. Defendant owed a duty of care to Plaintiff as a consumer who relied on Defendant’s "
        "platform and “Prime” services. Given Amazon’s representations of safety and security, "
        "it had a duty to prevent the sale of stolen goods or at least conduct reasonable checks."
    )
    story.append(Paragraph(count3_text_22, style_paragraph))

    count3_text_23 = (
        "23. Defendant breached this duty by failing to implement adequate inventory control, "
        "screening, or verification processes to ensure that items sold or fulfilled via Amazon "
        "Prime were not stolen property."
    )
    story.append(Paragraph(count3_text_23, style_paragraph))

    count3_text_24 = (
        "24. Case Law Support:<br/>"
        "• <i>Mbewe v. Amazon.com, Inc.</i>, No. 2:18-cv-00848-RAJ, 2019 WL 2994693 (W.D. Wash. July 9, 2019) "
        "(while not a final published opinion on negligence, referencing Amazon’s potential duty of care "
        "when fulfilling goods through its marketplace).<br/>"
        "• <i>Erie Ins. Co. v. Amazon.com, Inc.</i>, 925 F.3d 135 (4th Cir. 2019) (persuasive authority from "
        "another Circuit analyzing Amazon’s responsibilities as a seller or facilitator)."
    )
    story.append(Paragraph(count3_text_24, style_paragraph))

    count3_text_25 = (
        "25. Plaintiff relied on Amazon’s statements and “Prime” labeling, believing the product was "
        "legitimate and non-stolen. Plaintiff would not have purchased the phone had he known it was stolen."
    )
    story.append(Paragraph(count3_text_25, style_paragraph))

    count3_text_26 = (
        "26. This reliance was justifiable given Amazon’s longstanding marketing as a trusted "
        "e-commerce platform. Defendant’s negligent conduct directly and proximately caused harm "
        "to Plaintiff, including but not limited to the cost of the phone, the time and expense of "
        "the forced return, and the imposed restocking fee."
    )
    story.append(Paragraph(count3_text_26, style_paragraph))

    # VI. DAMAGES AND RELIEF SOUGHT
    story.append(Paragraph("VI. DAMAGES AND RELIEF SOUGHT", style_heading))
    damages_text = (
        "WHEREFORE, Plaintiff respectfully requests judgment in his favor as follows:"
    )
    story.append(Paragraph(damages_text, style_paragraph))

    bullet_points_damages = [
        ("1. Compensatory Damages: For all losses, including but not limited to the purchase price "
         "of the Pixel 7A, related fees, costs incurred to return the stolen device, and any other "
         "economic losses."),
        ("2. Treble Damages: As allowed under RCW 19.86.090 for violations of the Washington "
         "Consumer Protection Act, up to the statutory maximum."),
        ("3. Injunctive Relief: <br/>"
         "• Enjoining Defendant from imposing restocking fees on products that turn out to be stolen.<br/>"
         "• Requiring Defendant to improve inventory and fulfillment procedures to prevent future sales "
         "of stolen property."),
        ("4. Attorneys’ Fees and Costs: Pursuant to RCW 19.86.090 (for CPA violations) and any other "
         "applicable provision of law."),
        "5. Pre- and Post-Judgment Interest: As permitted by law.",
        "6. Such Other and Further Relief as the Court deems just, equitable, and proper.",
    ]
    for bp in bullet_points_damages:
        story.append(Paragraph(f"• {bp}", style_bulleted_list))

    # VII. JURY DEMAND
    story.append(Paragraph("VII. JURY DEMAND", style_heading))
    jury_text = (
        "Pursuant to CR 38 of the Washington Superior Court Civil Rules, Plaintiff demands "
        "trial by jury on all issues so triable."
    )
    story.append(Paragraph(jury_text, style_paragraph))

    # PRAYER FOR RELIEF
    story.append(Paragraph("PRAYER FOR RELIEF", style_heading))
    prayer_text = (
        "WHEREFORE, Plaintiff, Bo Shang, prays for judgment against Defendant, Amazon.com, Inc., "
        "in an amount to be proven at trial, including but not limited to compensatory and statutory "
        "damages, along with equitable relief, interest, costs, and attorneys’ fees (if allowed by "
        "law), and for such other relief as this Court deems just and proper."
    )
    story.append(Paragraph(prayer_text, style_paragraph))

    # Dated/Signature
    signature_block = (
        "DATED this 4 day of Feb, 2025.<br/><br/>"
        "Respectfully submitted,<br/><br/>"
        "__________________________<br/>"
        "Bo Shang (Pro Se)<br/>"
        "10 McCafferty Way<br/>"
        "781-999-4101<br/>"
        "bo@shang.software<br/>"
        "Pro Se"
    )
    story.append(Spacer(1, 12))
    story.append(Paragraph(signature_block, style_paragraph))

    # Page Break
    story.append(PageBreak())

    # Exhibits Section (placeholders for images or content)
    story.append(Paragraph("EXHIBIT 1:", style_heading))
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Placeholder for Exhibit 1 content (e.g., documentation from manufacturer, mobile carrier, "
            "police report, or other source).",
            style_paragraph,
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("EXHIBIT 2:", style_heading))
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Placeholder for Exhibit 2 content.", style_paragraph
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("EXHIBIT 3:", style_heading))
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Placeholder for Exhibit 3 content.", style_paragraph
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("EXHIBIT 4:", style_heading))
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Placeholder for Exhibit 4 content.", style_paragraph
        )
    )

    # Build the PDF
    doc.build(story)
    print(f"PDF generated successfully: {output_filename}")


def main():
    """Main entry point for the script."""
    output_file = "CivilActionComplaint.pdf"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    generate_civil_action_pdf(output_file)


if __name__ == "__main__":
    main()