# consolidador.py — Merge e consolidação dos DataFrames por escola
# Responsável por: receber dicionário de DataFrames, aplicar
# padronização de colunas e consolidar em um único DataFrame.

import pandas as pd
from extrator import extrair_todas_escolas


COLUNAS_PADRAO = [
    "escola", "nome_servidor", "cargo", "turno",
    "disciplina", "carga_horaria", "eja", "situacao"
]


def padronizar_colunas(df: pd.DataFrame, escola: str) -> pd.DataFrame:
    """Mapeia colunas variáveis do SCM+ para o schema padronizado do sistema."""
    pass


def consolidar(dados_escolas: dict) -> pd.DataFrame:
    """Recebe dict {escola: df} e retorna DataFrame consolidado de todas as escolas."""
    pass


def gerar_abas(df_consolidado: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Cria os DataFrames para cada aba: geral, por escola, por cargo, por turno, EJA."""
    pass


if __name__ == "__main__":
    dados = extrair_todas_escolas()
    df = consolidar(dados)
    print(f"[consolidador] {len(df)} registros consolidados.")
