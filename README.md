<!-- Sistema de Modulação Escolar — SME Planaltina-GO -->

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   >_  MODULAÇÃO SME  //  Secretaria Municipal de Educação    ║
║   ──────────────────────────────────────────────────────     ║
║   org     : Prefeitura de Planaltina-GO                      ║
║   escolas : 46 unidades escolares                            ║
║   stack   : Python · pandas · openpyxl                       ║
║   status  : ██████████████████████  PRODUÇÃO                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

![Status](https://img.shields.io/badge/status-em_produção-e53935?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-0a0a0a?style=flat-square&logo=python&logoColor=e53935)
![pandas](https://img.shields.io/badge/pandas-0a0a0a?style=flat-square&logo=pandas&logoColor=e53935)
![openpyxl](https://img.shields.io/badge/openpyxl-0a0a0a?style=flat-square&logo=python&logoColor=e53935)

</div>

---

## `$ cat problema.txt`

A Secretaria Municipal de Educação de Planaltina-GO gerencia a **modulação escolar** — o processo de alocação de professores e servidores nas 46 unidades escolares da rede municipal.

O problema: os dados chegam de fontes brutas exportadas do sistema **SCM+** (planilhas `.xls` com formatação inconsistente, células mescladas, cabeçalhos variáveis por escola). O processo de consolidação era feito **100% manualmente** por analistas, levando dias de trabalho e gerando erros frequentes de digitação e inconsistência entre arquivos.

---

## `$ cat solucao.txt`

Sistema de ETL em Python que:

1. **Extrai** os dados brutos exportados pelo SCM+ (uma planilha por escola)
2. **Limpa** inconsistências: cabeçalhos, células mescladas, tipos de dados, encoding
3. **Consolida** tudo em uma única planilha estruturada com múltiplas abas
4. **Gera** relatórios automáticos com fórmulas, validações e formatação

---

## `$ ls -la stack/`

| Componente | Tecnologia | Uso |
|------------|------------|-----|
| Linguagem | Python 3.10+ | Toda a lógica do sistema |
| Leitura/escrita Excel | openpyxl | Manipulação de .xlsx com formatação |
| Transformação de dados | pandas | Limpeza, filtragem, agrupamento |
| Paths e I/O | pathlib, os | Navegação de diretórios e arquivos |

---

## `$ cat output.txt`

O sistema gera uma planilha consolidada com as seguintes abas:

| Aba | Conteúdo |
|-----|----------|
| `Geral` | Todos os servidores consolidados, 46 escolas |
| `Por Escola` | Quantitativo de servidores por unidade escolar |
| `Por Cargo` | Distribuição de cargos (Professor, ASG, Secretário...) |
| `Por Turno` | Alocação por turno (Matutino, Vespertino, Noturno, Integral) |
| `EJA` | Servidores alocados em turmas de Educação de Jovens e Adultos |
| `Validações` | Cruzamento automático para detectar inconsistências |

Todas as abas possuem formatação automática, fórmulas de totalização e filtros aplicados.

---

## `$ cat impacto.txt`

```bash
$ diff antes.txt depois.txt

- processo: 100% manual (analistas, planilhas, copiar/colar)
- tempo: 3-5 dias de trabalho por ciclo de modulação
- erros: frequentes (digitação, merge de colunas erradas)
- cobertura: parcial (nem todas as escolas consolidadas)

+ processo: automatizado (executar script, obter resultado)
+ tempo: < 5 minutos por ciclo
+ erros: zero de digitação (validação automática)
+ cobertura: 100% das 46 escolas da rede municipal
```

---

## `$ tree projeto/`

```
modulacao-sme/
├── src/
│   ├── extrator.py          # Leitura e pré-processamento das planilhas brutas do SCM+
│   ├── consolidador.py      # Merge e consolidação dos DataFrames por escola
│   ├── gerador_relatorio.py # Criação da planilha final com formatação e fórmulas
│   └── utils.py             # Funções auxiliares: limpeza de strings, normalização de cargos
├── docs/
│   └── arquitetura.md       # Fluxo detalhado do sistema
├── .gitignore
├── requirements.txt
└── README.md
```

> **Nota:** A pasta `data/` com as planilhas brutas e o output final não está incluída neste repositório. Os dados de servidores são sigilosos e de uso interno da SME.

---

## `$ cat instalacao.txt`

```bash
# Clonar o repositório
git clone https://github.com/BJR0drigues/modulacao-sme.git
cd modulacao-sme

# Instalar dependências
pip install -r requirements.txt

# Executar o sistema
python src/extrator.py        # etapa 1: extrai dados brutos
python src/consolidador.py    # etapa 2: consolida por escola
python src/gerador_relatorio.py  # etapa 3: gera planilha final
```

---

## `$ cat aviso.txt`

```
⚠  DADOS REAIS OMITIDOS

Este repositório demonstra a arquitetura e lógica do sistema.
Os arquivos com dados reais de servidores NÃO estão incluídos
por sigilo institucional — uso interno da SME Planaltina-GO.

O código é funcional e reflete exatamente o sistema em produção.
```

---

<div align="center">

```
// sistema em produção desde 2025
// cobre 100% da rede municipal de Planaltina-GO
// 46 escolas. automatizado. sem erro manual.
```

</div>
