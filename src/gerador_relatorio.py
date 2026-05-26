# gerador_relatorio.py — Criação da planilha final com formatação e fórmulas
# Responsável por: receber abas consolidadas, aplicar formatação
# com openpyxl, inserir fórmulas de totalização e salvar o arquivo.

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows
from pathlib import Path
import pandas as pd
from consolidador import consolidar, gerar_abas
from extrator import extrair_todas_escolas


OUTPUT_DIR = Path("output")


def criar_pasta_output():
    """Cria a pasta de saída se não existir."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def formatar_cabecalho(ws, linha: int = 1):
    """Aplica formatação de cabeçalho: negrito, cor de fundo, bordas."""
    pass


def inserir_aba(wb: openpyxl.Workbook, nome_aba: str, df: pd.DataFrame):
    """Insere DataFrame em aba do workbook com formatação e auto-filtro."""
    pass


def gerar_relatorio_final(abas: dict[str, pd.DataFrame]):
    """Cria o workbook final com todas as abas, formatação e salva em output/."""
    pass


if __name__ == "__main__":
    criar_pasta_output()
    dados = extrair_todas_escolas()
    from consolidador import consolidar, gerar_abas
    df = consolidar(dados)
    abas = gerar_abas(df)
    gerar_relatorio_final(abas)
    print("[gerador] Relatório gerado em output/.")
