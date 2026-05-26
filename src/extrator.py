# extrator.py — Leitura e pré-processamento das planilhas brutas do SCM+
# Responsável por: ler arquivos por escola, limpar cabeçalhos,
# normalizar encoding e retornar DataFrames padronizados.

import pandas as pd
from pathlib import Path
from utils import normalizar_cargo, limpar_nome


DATA_DIR = Path("data/brutos")


def listar_arquivos_scm():
    """Retorna lista de arquivos .xlsx exportados do SCM+ na pasta de dados brutos."""
    pass


def extrair_escola(caminho_arquivo: Path) -> pd.DataFrame:
    """Lê planilha de uma escola, remove linhas de cabeçalho do SCM+ e retorna DataFrame limpo."""
    pass


def extrair_todas_escolas() -> dict[str, pd.DataFrame]:
    """Executa extração de todas as escolas e retorna dicionário {nome_escola: DataFrame}."""
    pass


if __name__ == "__main__":
    dados = extrair_todas_escolas()
    print(f"[extrator] {len(dados)} escolas extraídas.")
