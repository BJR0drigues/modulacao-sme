# Arquitetura do Sistema de Modulação SME

## Visão Geral

O sistema segue um pipeline ETL clássico (Extract → Transform → Load) adaptado para o contexto da Secretaria Municipal de Educação de Planaltina-GO.

## Fluxo do Sistema

```
[SCM+]
   │
   │  exportação manual (.xlsx por escola)
   ▼
[data/brutos/]
   │
   │  extrator.py
   │  - lê cada arquivo
   │  - remove cabeçalhos variáveis do SCM+
   │  - normaliza encoding (latin-1 → utf-8)
   │  - retorna DataFrame por escola
   ▼
[dict {escola: DataFrame}]
   │
   │  consolidador.py
   │  - padroniza colunas para schema único
   │  - aplica normalização de cargos e turnos (via utils.py)
   │  - merge de todas as escolas
   │  - gera abas: Geral, Por Escola, Por Cargo, Por Turno, EJA
   ▼
[dict {aba: DataFrame}]
   │
   │  gerador_relatorio.py
   │  - cria workbook openpyxl
   │  - insere cada DataFrame em aba própria
   │  - aplica formatação: cabeçalho, cores, bordas, auto-filtro
   │  - insere fórmulas SOMA nas linhas de totais
   │  - salva em output/modulacao_YYYY-MM-DD.xlsx
   ▼
[output/modulacao_YYYY-MM-DD.xlsx]
```

## Schema Padronizado

Após a extração, todos os DataFrames seguem este schema:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `escola` | str | Nome da unidade escolar |
| `nome_servidor` | str | Nome completo do servidor (maiúsculas) |
| `cargo` | str | Cargo normalizado (via MAPA_CARGOS) |
| `turno` | str | Matutino / Vespertino / Noturno / Integral |
| `disciplina` | str | Disciplina (professores) ou N/A |
| `carga_horaria` | int | Horas semanais |
| `eja` | bool | True se alocado em turma EJA |
| `situacao` | str | Ativo / Afastado / Cedido |

## Tratamento de Inconsistências

O SCM+ exporta planilhas com variações frequentes:

- **Cabeçalhos na linha 3 ou 4** (varia por escola): `extrator.py` detecta a linha de cabeçalho pelo conteúdo
- **Células mescladas**: pandas trata como NaN — `extrator.py` faz forward-fill
- **Cargos com abreviações**: `utils.normalizar_cargo()` mapeia para nomenclatura padrão
- **Encoding inconsistente**: openpyxl lida nativamente; fallback para latin-1
- **Linhas de totais dentro da planilha**: filtradas por regex antes do parse

## Volumes

- 46 escolas processadas por ciclo
- ~1.800 a 2.200 registros por ciclo de modulação
- Tempo de execução: < 5 minutos em hardware padrão
- Frequência: executado a cada ciclo de modulação (início de semestre)
