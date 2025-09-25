from fpdf import FPDF

def gerar_pdf(dados: dict, titulo: str = "Formulário") -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, titulo, ln=True, align="C")
    pdf.ln(10)

    for chave, valor in dados.items():
        pdf.multi_cell(0, 10, f"{chave}: {valor}")

    # Retorna diretamente como bytes
    pdf_bytes = pdf.output(dest="S").encode("latin1") if isinstance(pdf.output(dest="S"), str) else bytes(pdf.output(dest="S"))
    return pdf_bytes
