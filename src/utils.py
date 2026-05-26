# utils.py — Funções auxiliares reutilizáveis
# Normalização de strings, cargos, nomes e datas
# usados em todo o pipeline de ETL.

import re
import unicodedata


MAPA_CARGOS = {
    "PROF": "Professor",
    "PROFESSOR": "Professor",
    "ASG": "Agente de Serviços Gerais",
    "SECRETARIO": "Secretário Escolar",
    "DIRETOR": "Diretor",
    "COORDENADOR": "Coordenador Pedagógico",
    "VIGIA": "Vigilante",
    "MERENDEIRA": "Auxiliar de Cozinha",
}


def limpar_nome(nome: str) -> str:
    """Remove espaços extras, normaliza maiúsculas e elimina caracteres especiais de nomes."""
    if not isinstance(nome, str):
        return ""
    return " ".join(nome.strip().upper().split())


def normalizar_cargo(cargo_bruto: str) -> str:
    """Mapeia variações de cargo do SCM+ para nomenclatura padronizada da SME."""
    if not isinstance(cargo_bruto, str):
        return "Não Informado"
    chave = cargo_bruto.strip().upper()
    for k, v in MAPA_CARGOS.items():
        if k in chave:
            return v
    return cargo_bruto.strip().title()


def remover_acentos(texto: str) -> str:
    """Remove acentuação para comparações e chaves de dicionário."""
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def extrair_turno(valor: str) -> str:
    """Padroniza turno: M/MAT → Matutino, V/VES → Vespertino, N/NOT → Noturno, INT → Integral."""
    if not isinstance(valor, str):
        return "Não Informado"
    v = valor.strip().upper()
    if v in ("M", "MAT", "MATUTINO"):
        return "Matutino"
    if v in ("V", "VES", "VESPERTINO"):
        return "Vespertino"
    if v in ("N", "NOT", "NOTURNO"):
        return "Noturno"
    if v in ("I", "INT", "INTEGRAL"):
        return "Integral"
    return valor.strip().title()
