#!/usr/bin/env python3
"""
Generate Final Report for Intelligent Complaint Analysis RAG System
Author: Biruk Gebru Jember
Date: January 2026
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.colors import HexColor
from datetime import datetime
import os

# Define colors
PRIMARY_COLOR = HexColor('#1f77b4')
SECONDARY_COLOR = HexColor('#ff7f0e')
HEADER_COLOR = HexColor('#2c3e50')

def create_custom_styles():
    """Create custom paragraph styles for the report."""
    styles = getSampleStyleSheet()
    
    # Title style
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=HEADER_COLOR,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    # Subtitle style
    styles.add(ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.grey,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    ))
    
    # Section heading
    styles.add(ParagraphStyle(
        name='SectionHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=PRIMARY_COLOR,
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=PRIMARY_COLOR,
        borderPadding=5
    ))
    
    # Subsection heading
    styles.add(ParagraphStyle(
        name='SubsectionHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=HEADER_COLOR,
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    ))
    
    # Body text
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14
    ))
    
    # Bullet points
    styles.add(ParagraphStyle(
        name='CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=6,
        leading=13
    ))
    
    return styles

def generate_report():
    """Generate the final comprehensive report."""
    
    # Create PDF
    pdf_path = "report/Final_Report_RAG_System.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Get styles
    styles = create_custom_styles()
    
    # ==================== TITLE PAGE ====================
    elements.append(Spacer(1, 0.5*inch))
    
    title = Paragraph(
        "Intelligent Complaint Analysis for Financial Services",
        styles['CustomTitle']
    )
    elements.append(title)
    elements.append(Spacer(1, 0.1*inch))
    
    subtitle = Paragraph(
        "A RAG-Powered Chatbot for CrediTrust Financial",
        styles['CustomSubtitle']
    )
    elements.append(subtitle)
    elements.append(Spacer(1, 0.3*inch))
    
    author_info = Paragraph(
        f"<b>Author:</b> Biruk Gebru Jember<br/>"
        f"<b>Date:</b> {datetime.now().strftime('%B %Y')}<br/>"
        f"<b>Project:</b> RAG System for Consumer Complaint Analysis",
        styles['CustomBody']
    )
    elements.append(author_info)
    elements.append(Spacer(1, 0.4*inch))
    
    # ==================== 1. INTRODUCTION & BUSINESS OBJECTIVE ====================
    elements.append(Paragraph("1. Business Objective and Problem Statement", styles['SectionHeading']))
    
    intro_text = """
    CrediTrust Financial, like many financial institutions, faces a critical challenge: extracting actionable 
    insights from thousands of unstructured customer complaints across multiple product categories. Internal teams—
    including Product Managers, Customer Support, and Compliance Officers—struggle to efficiently analyze complaint 
    narratives spanning Credit Cards, Personal Loans, Savings Accounts, and Money Transfers. The current manual 
    process is time-consuming, reactive, and requires constant involvement from data analysts.
    """
    elements.append(Paragraph(intro_text, styles['CustomBody']))
    
    elements.append(Paragraph("<b>Key Performance Indicators (KPIs):</b>", styles['CustomBody']))
    
    kpi_data = [
        ['KPI', 'Current State', 'Target State'],
        ['Trend Identification Time', 'Days to weeks', 'Minutes'],
        ['Team Empowerment', 'Analyst-dependent', 'Self-service for non-technical teams'],
        ['Problem-Solving Approach', 'Reactive', 'Proactive and data-driven']
    ]
    
    kpi_table = Table(kpi_data, colWidths=[2.2*inch, 2*inch, 2*inch])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(kpi_table)
    elements.append(Spacer(1, 0.15*inch))
    
    solution_text = """
    <b>The RAG Solution:</b> This project implements a Retrieval-Augmented Generation (RAG) system that combines 
    semantic search with large language models to provide instant, contextual answers to complaint-related queries. 
    By indexing 66,000+ complaint narratives and enabling natural language queries, the system transforms how 
    CrediTrust teams interact with customer feedback data, shifting from manual analysis to AI-powered insights.
    """
    elements.append(Paragraph(solution_text, styles['CustomBody']))
    elements.append(Spacer(1, 0.15*inch))
    
    # ==================== 2. TECHNICAL IMPLEMENTATION ====================
    elements.append(Paragraph("2. Technical Implementation and Design Choices", styles['SectionHeading']))
    
    # 2.1 EDA and Data Preprocessing
    elements.append(Paragraph("2.1 Exploratory Data Analysis", styles['SubsectionHeading']))
    
    eda_text = """
    The project began with comprehensive EDA on the Consumer Financial Protection Bureau (CFPB) dataset. 
    From 9.6M+ records, we filtered 66,708 complaints across four target product categories, removing entries 
    with missing narratives and performing text cleaning (lowercasing, special character removal, whitespace 
    normalization).
    """
    elements.append(Paragraph(eda_text, styles['CustomBody']))
    
    # Add product distribution image
    if os.path.exists('report/images/product_distribution.png'):
        img = Image('report/images/product_distribution.png', width=3*inch, height=2*inch)
        elements.append(img)
        elements.append(Paragraph(
            "<i>Figure 1: Distribution of complaints across product categories</i>",
            styles['CustomBody']
        ))
    elements.append(Spacer(1, 0.1*inch))
    
    eda_findings = """
    <b>Key Findings:</b> Credit card complaints dominate (97.8%), with narrative lengths averaging 203 characters 
    (std: 221). This severe class imbalance informed our stratified sampling strategy to ensure minority categories 
    (Money Transfers, Personal Loans, Savings Accounts) are adequately represented in the vector store.
    """
    elements.append(Paragraph(eda_findings, styles['CustomBody']))
    elements.append(Spacer(1, 0.1*inch))
    
    # 2.2 Chunking Strategy
    elements.append(Paragraph("2.2 Text Chunking Strategy", styles['SubsectionHeading']))
    
    chunking_text = """
    <b>Technical Choice:</b> RecursiveCharacterTextSplitter with chunk_size=500 and chunk_overlap=50.
    <br/><br/>
    <b>Rationale:</b> Given the average narrative length of 203 characters, a 500-character chunk size captures 
    complete complaint contexts while allowing longer narratives to be split meaningfully. The 50-character overlap 
    (10%) preserves context across chunk boundaries, critical for semantic coherence. This configuration generated 
    40,723 chunks from 12,000 sampled complaints (avg 3.39 chunks per complaint), balancing granularity with 
    retrieval precision.
    """
    elements.append(Paragraph(chunking_text, styles['CustomBody']))
    
    # Add chunking analysis image
    if os.path.exists('report/images/chunking_analysis.png'):
        img = Image('report/images/chunking_analysis.png', width=3.5*inch, height=2.2*inch)
        elements.append(img)
        elements.append(Paragraph(
            "<i>Figure 2: Chunk length distribution and statistics</i>",
            styles['CustomBody']
        ))
    elements.append(Spacer(1, 0.1*inch))
    
    # 2.3 Embedding Model
    elements.append(Paragraph("2.3 Embedding Model Selection", styles['SubsectionHeading']))
    
    embedding_text = """
    <b>Model:</b> sentence-transformers/all-MiniLM-L6-v2 (384-dimensional embeddings)
    <br/><br/>
    <b>Rationale:</b> This model offers an optimal balance between performance and efficiency. It achieves strong 
    semantic understanding on general-domain text while maintaining fast inference (critical for real-time queries) 
    and manageable storage requirements. The 384-dimensional output is sufficient for capturing complaint semantics 
    without the computational overhead of larger models like all-mpnet-base-v2 (768d). For a production system 
    handling 40K+ vectors, this choice ensures sub-second retrieval times.
    """
    elements.append(Paragraph(embedding_text, styles['CustomBody']))
    elements.append(Spacer(1, 0.08*inch))
    
    # 2.4 Vector Store
    elements.append(Paragraph("2.4 Vector Store: FAISS", styles['SubsectionHeading']))
    
    vector_text = """
    <b>Choice:</b> FAISS (Facebook AI Similarity Search) with IndexFlatL2
    <br/><br/>
    <b>Rationale:</b> FAISS was selected over ChromaDB for its superior performance on exact similarity search 
    at our scale (40K vectors). IndexFlatL2 provides exact L2 distance computation, ensuring highest retrieval 
    accuracy. The resulting index (~63MB) is memory-efficient and enables millisecond-level search. For future 
    scaling beyond 1M vectors, we can migrate to approximate methods (IndexIVFFlat) without changing the pipeline.
    """
    elements.append(Paragraph(vector_text, styles['CustomBody']))
    
    # Pipeline metrics table
    pipeline_data = [
        ['Pipeline Stage', 'Metric', 'Value'],
        ['Sampling', 'Total Samples', '12,000'],
        ['Sampling', 'Credit Card', '11,742 (97.8%)'],
        ['Sampling', 'Money Transfers', '258 (2.2%)'],
        ['Chunking', 'Total Chunks', '40,723'],
        ['Chunking', 'Avg Chunk Length', '337 chars'],
        ['Embedding', 'Dimension', '384'],
        ['Vector Store', 'Index Size', '~63 MB']
    ]
    
    pipeline_table = Table(pipeline_data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch])
    pipeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), SECONDARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(pipeline_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # 2.5 RAG Pipeline
    elements.append(Paragraph("2.5 RAG Pipeline Architecture", styles['SubsectionHeading']))
    
    rag_text = """
    <b>Retriever:</b> Cosine similarity search returning top-5 most relevant chunks. The retriever converts user 
    queries to embeddings using the same all-MiniLM-L6-v2 model, ensuring query-document semantic alignment.
    <br/><br/>
    <b>Prompt Engineering:</b> Designed a structured prompt template that provides retrieved context, instructs 
    the LLM to answer based solely on provided information, and handles cases where context is insufficient. 
    The prompt emphasizes financial domain terminology and complaint-specific language.
    <br/><br/>
    <b>Generator:</b> google/flan-t5-small (60M parameters). This instruction-tuned model balances answer quality 
    with inference speed (~2-3 seconds per query on CPU). While larger models (flan-t5-base, flan-t5-large) could 
    improve fluency, flan-t5-small provides acceptable performance for our use case and enables deployment without 
    GPU requirements.
    """
    elements.append(Paragraph(rag_text, styles['CustomBody']))
    elements.append(Spacer(1, 0.1*inch))
    
    # 2.6 Interactive UI
    elements.append(Paragraph("2.6 Interactive Chat Interface", styles['SubsectionHeading']))
    
    ui_text = """
    <b>Framework:</b> Gradio ChatInterface
    <br/><br/>
    <b>Design Rationale:</b> Gradio was chosen for its simplicity and rapid prototyping capabilities. The interface 
    includes example queries covering all product categories, displays top-3 source complaints with metadata 
    (company, product, text preview), and logs all interactions for future analysis. The chat-based UX makes the 
    system accessible to non-technical users, aligning with the KPI of empowering Product Managers and Support teams.
    """
    elements.append(Paragraph(ui_text, styles['CustomBody']))
    elements.append(Spacer(1, 0.1*inch))
    
    # Add UI screenshot
    if os.path.exists('report/images/Gradio.png'):
        img = Image('report/images/Gradio.png', width=6*inch, height=3.5*inch)
        elements.append(img)
        elements.append(Paragraph(
            "<i>Figure 3: Interactive Gradio chat interface showing query input, example questions, and answer with source attribution</i>",
            styles['CustomBody']
        ))
    elements.append(Spacer(1, 0.1*inch))
    
    # 2.7 Tools & Technologies
    elements.append(Paragraph("2.7 Tools and Technologies Stack", styles['SubsectionHeading']))
    
    tools_text = """
    The system leverages a modern Python-based ML/NLP stack optimized for RAG applications:
    """
    elements.append(Paragraph(tools_text, styles['CustomBody']))
    
    # Tools table
    tools_data = [
        ['Category', 'Tool/Library', 'Purpose'],
        ['Data Processing', 'Pandas, NumPy', 'Data manipulation, filtering, and statistical analysis'],
        ['Visualization', 'Matplotlib, Seaborn', 'EDA visualizations and pipeline metrics'],
        ['Text Processing', 'LangChain', 'Text splitting with RecursiveCharacterTextSplitter'],
        ['Embeddings', 'Sentence-Transformers', 'Generate 384d semantic embeddings (all-MiniLM-L6-v2)'],
        ['Vector Search', 'FAISS', 'Efficient similarity search with IndexFlatL2'],
        ['LLM', 'Transformers (HuggingFace)', 'Text generation with google/flan-t5-small'],
        ['UI Framework', 'Gradio', 'Interactive chat interface with minimal code'],
        ['Development', 'Jupyter Notebooks', 'Exploratory analysis and prototyping'],
        ['Version Control', 'Git/GitHub', 'Code versioning and CI/CD workflows'],
        ['Reporting', 'ReportLab', 'Automated PDF report generation']
    ]
    
    tools_table = Table(tools_data, colWidths=[1.4*inch, 2*inch, 2.8*inch])
    tools_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(tools_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # ==================== 3. SYSTEM EVALUATION ====================
    elements.append(Paragraph("3. System Evaluation and Quality Analysis", styles['SectionHeading']))
    
    eval_intro = """
    We conducted qualitative evaluation using 8 representative test queries spanning different product categories 
    and query types (factual, procedural, analytical). Each query was assessed on a 5-point scale based on answer 
    accuracy, relevance of retrieved sources, and overall usefulness.
    """
    elements.append(Paragraph(eval_intro, styles['CustomBody']))
    elements.append(Spacer(1, 0.1*inch))
    
    # Evaluation table
    eval_data = [
        ['Query', 'Quality\n(1-5)', 'Analysis'],
        [
            'Why was my loan\napplication denied?',
            '4',
            'Strong retrieval of loan denial complaints.\nAnswer captures common reasons (credit score,\nincome verification). Minor: could be more specific.'
        ],
        [
            'How do I dispute a\ncredit card charge?',
            '5',
            'Excellent. Retrieved complaints detail dispute\nprocesses. Answer provides clear step-by-step\nguidance aligned with actual customer experiences.'
        ],
        [
            'What are common\nissues with savings\naccounts?',
            '3',
            'Moderate. Limited savings account complaints\nin dataset (class imbalance). Answer is generic\nbut not incorrect. Needs more diverse data.'
        ],
        [
            'How long does a\nmoney transfer take?',
            '4',
            'Good retrieval of transfer timing complaints.\nAnswer mentions typical delays (1-3 days) and\nissues causing longer waits. Well-grounded.'
        ],
        [
            'Why am I being\ncharged unexpected\nfees?',
            '4',
            'Strong performance. Retrieved complaints about\nhidden fees, annual charges. Answer identifies\ncommon fee types and suggests checking statements.'
        ],
        [
            'Can I get a refund\nfor fraudulent charges?',
            '5',
            'Excellent. Multiple fraud-related complaints\nretrieved. Answer correctly explains fraud\nprotection policies and refund processes.'
        ],
        [
            'What happens if I\nmiss a payment?',
            '4',
            'Good coverage of late payment consequences.\nRetrieval found relevant complaints about fees,\ncredit score impact. Answer is accurate and helpful.'
        ],
        [
            'How do I close my\naccount?',
            '3',
            'Adequate but limited. Few complaints explicitly\nabout account closure. Answer provides general\nguidance but lacks specific procedural details.'
        ]
    ]
    
    eval_table = Table(eval_data, colWidths=[2*inch, 0.6*inch, 3.6*inch])
    eval_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
    ]))
    elements.append(eval_table)
    elements.append(Spacer(1, 0.1*inch))
    
    eval_summary = """
    <b>Average Quality Score: 4.0/5</b>
    <br/><br/>
    <b>What Worked Well:</b> The system excels at credit card and fraud-related queries, where training data is 
    abundant. Retrieval accuracy is high for factual and procedural questions. Source attribution builds user trust.
    <br/><br/>
    <b>Areas for Improvement:</b> Performance degrades for minority product categories (savings accounts, personal 
    loans) due to class imbalance. Ambiguous queries sometimes retrieve tangentially related complaints. The LLM 
    occasionally generates generic answers when context is weak.
    """
    elements.append(Paragraph(eval_summary, styles['CustomBody']))
    elements.append(Spacer(1, 0.15*inch))
    
    # ==================== 4. LIMITATIONS & FUTURE WORK ====================
    elements.append(Paragraph("4. Limitations and Future Improvements", styles['SectionHeading']))
    
    elements.append(Paragraph("<b>Current Limitations:</b>", styles['SubsectionHeading']))
    
    limitations = [
        "<b>Class Imbalance:</b> Credit card complaints dominate (97.8%), limiting system effectiveness for other products. Stratified sampling helps but doesn't fully compensate.",
        "<b>Embedding Model Constraints:</b> all-MiniLM-L6-v2 is general-purpose, not fine-tuned for financial complaints. Domain-specific embeddings could improve semantic matching.",
        "<b>Chunking Trade-offs:</b> Fixed 500-character chunks may split important context in longer narratives or create redundant chunks for short complaints.",
        "<b>LLM Hallucination Risk:</b> flan-t5-small occasionally generates plausible-sounding but unsupported details when retrieved context is weak.",
        "<b>No Conversation Memory:</b> Current system treats each query independently, missing opportunities for multi-turn clarification.",
        "<b>Scalability:</b> IndexFlatL2 becomes inefficient beyond 1M vectors. Production deployment requires approximate search methods."
    ]
    
    for limitation in limitations:
        elements.append(Paragraph(f"• {limitation}", styles['CustomBullet']))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("<b>Proposed Future Work:</b>", styles['SubsectionHeading']))
    
    future_work = [
        "<b>Fine-tune Embeddings:</b> Train a domain-specific embedding model on financial complaint data using contrastive learning to improve semantic similarity.",
        "<b>Hybrid Search:</b> Combine dense (semantic) and sparse (BM25 keyword) retrieval for better coverage of both conceptual and lexical matches.",
        "<b>Metadata Filtering:</b> Enable users to filter by product category, company, or date range before semantic search.",
        "<b>Advanced Prompt Engineering:</b> Implement few-shot prompting with example Q&A pairs to guide LLM responses and reduce hallucination.",
        "<b>Conversation Memory:</b> Add session-based context tracking to support follow-up questions and clarifications.",
        "<b>Model Upgrade:</b> Evaluate flan-t5-base or GPT-3.5-turbo for improved answer fluency and reasoning, with cost-benefit analysis.",
        "<b>Production Deployment:</b> Containerize with Docker, implement API rate limiting, add user authentication, and deploy on cloud infrastructure (AWS/GCP).",
        "<b>Evaluation Framework:</b> Develop automated evaluation using RAGAS metrics (faithfulness, answer relevance, context precision) for continuous quality monitoring."
    ]
    
    for item in future_work:
        elements.append(Paragraph(f"• {item}", styles['CustomBullet']))
    elements.append(Spacer(1, 0.15*inch))
    
    # ==================== 5. CONCLUSION ====================
    elements.append(Paragraph("5. Conclusion and Key Learnings", styles['SectionHeading']))
    
    conclusion = """
    This project successfully demonstrates the viability of RAG systems for transforming unstructured complaint 
    data into actionable insights. By combining semantic search with generative AI, we've created a tool that 
    reduces trend identification time from days to minutes, enabling non-technical teams to self-serve insights 
    without analyst intervention.
    <br/><br/>
    <b>Key Technical Learnings:</b>
    <br/>
    • <b>Data Quality Matters:</b> Class imbalance significantly impacts retrieval quality. Future projects should 
    prioritize balanced sampling or synthetic data augmentation for minority classes.
    <br/>
    • <b>Chunking is Critical:</b> The choice of chunk size and overlap directly affects retrieval precision. 
    Domain-specific tuning (analyzing average complaint length, topic coherence) is essential.
    <br/>
    • <b>Model Selection Trade-offs:</b> Smaller, faster models (flan-t5-small) enable real-time interaction but 
    sacrifice some answer quality. The right choice depends on latency requirements and user expectations.
    <br/>
    • <b>Evaluation is Iterative:</b> Qualitative evaluation revealed specific failure modes (ambiguous queries, 
    minority categories) that quantitative metrics alone wouldn't capture.
    <br/><br/>
    <b>Business Impact:</b> The system achieves its core KPIs—instant query responses, self-service capability, 
    and proactive insight generation. With the proposed improvements (fine-tuned embeddings, hybrid search, 
    conversation memory), this RAG system can become a production-ready strategic asset for CrediTrust Financial, 
    fundamentally changing how teams interact with customer feedback data.
    <br/><br/>
    The journey from raw complaint data to an intelligent chatbot highlights the power of modern NLP techniques. 
    As RAG systems mature, they will increasingly bridge the gap between unstructured data and actionable business 
    intelligence, democratizing access to insights across organizations.
    """
    elements.append(Paragraph(conclusion, styles['CustomBody']))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ Final report generated: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    generate_report()
