# learn-web

> Projeto de aprendizado de desenvolvimento web full-stack (HTML, CSS, JavaScript, PHP) conduzido pelo autor através da construção de um site pessoal real, em quatro camadas progressivamente mais complexas.

---

## 1. O que este repositório é

Este repositório é o veículo pelo qual o autor aprende desenvolvimento web na prática. Em vez de seguir tutoriais lineares desconexos da realidade, cada conceito novo é introduzido no momento em que se torna necessário para a próxima entrega do site.

O resultado pretendido é duplo: (a) um site pessoal funcional, com características reais de produção; e (b) um corpo documental e de exercícios que sirva de referência consultável em projetos web futuros.

A organização segue a **taxonomia SERMI**, com cinco tipos de documento:

| Tipo | O que registra |
|---|---|
| **SPEC** | Descrições estruturais (taxonomia, fundação, contrato de responsabilidade, componentes do site). |
| **DEC** | Decisões registradas com alternativas consideradas e consequências aceitas. |
| **REP** | Relatórios de fechamento de camada. |
| **GUIDE** | Guias operacionais (uso ocasional). |
| **BRIEF** | Vitrine pública. Este arquivo. |

---

## 2. As quatro camadas

| Camada | Foco técnico | Estado |
|---|---|---|
| **C1** | HTML semântico + CSS moderno (responsivo) | Não iniciada |
| **C2** | JavaScript vanilla (interatividade, Fetch API) | Não iniciada |
| **C3** | PHP backend (páginas dinâmicas, formulários) | Não iniciada |
| **C4** | Banco de dados (persistência, CRUD) | Não iniciada |

Cada camada só é iniciada quando os critérios da camada anterior estão verificados, conforme [SPEC-002 §4](docs/SPEC/SPEC_002_Fundacao_learn_web.md).

---

## 3. Estrutura do repositório

```
learn-web/
├── README.md                       ← este arquivo (BRIEF público)
├── CLAUDE.md                       ← instruções pra IA quando atuar no repo
├── environment.txt                 ← versões locais de PHP, Node, nginx
├── bootstrap_estrutura.py          ← scaffold idempotente da estrutura
│
├── docs/
│   ├── SPEC/                       ← especificações técnicas
│   │   ├── INDEX_SPEC.md
│   │   ├── SPEC_001_Taxonomia_Documental.md
│   │   ├── SPEC_002_Fundacao_learn_web.md
│   │   └── SPEC_003_Contrato_Responsabilidade.md
│   ├── DEC/
│   │   └── INDEX_DEC.md            ← obrigatório, vazio inicialmente
│   ├── REP/                        ← relatórios de fechamento de camada
│   ├── GUIDE/                      ← guias operacionais
│   ├── BRIEF/                      ← BRIEFs numerados (raros)
│   ├── assets/                     ← imagens da documentação
│   └── logs/                       ← logs arquivados
│
└── src/                            ← código do site (organização a definir)
```

---

## 4. Como ler este repositório

**Para entender o projeto rapidamente:** este README cobre o essencial.

**Para entender em profundidade:**

1. [SPEC-001 · Taxonomia Documental](docs/SPEC/SPEC_001_Taxonomia_Documental.md) — entende como o repo se organiza e por quê.
2. [SPEC-002 · Fundação](docs/SPEC/SPEC_002_Fundacao_learn_web.md) — entende o que o projeto se compromete a entregar.
3. [SPEC-003 · Contrato de Responsabilidade](docs/SPEC/SPEC_003_Contrato_Responsabilidade.md) — entende como autor e IA dividem o trabalho.

**Para acompanhar o progresso:** ver `docs/REP/` (relatórios de fechamento de camada, à medida que forem produzidos).

**Para entender por que algo foi feito assim:** ver `docs/DEC/INDEX_DEC.md`.

---

## 5. Como rodar o site localmente

> Detalhes operacionais completos ficarão em `docs/GUIDE/GUIDE_001_Subir_site_local.md` (a produzir).

Pré-requisitos validados em 2026-05-13 (`environment.txt`):

- PHP 8.3 + php-fpm
- nginx 1.24
- Node 18 (para tooling futuro)
- Composer 2.7

O site é servido em `localhost:8080` via nginx + php-fpm, com config em `/etc/nginx/sites-available/learn-web` (a criar quando a Camada 1 começar).

---

## 6. Status

**Em fundação.** As três SPECs de fundamentação documental foram produzidas e aprovadas em 2026-05-13. A Camada 1 (HTML/CSS estático) é o próximo passo concreto.

---

## 7. Sobre o autor

Bruno Serminaro — projeto pessoal, mantido em horário próprio.

---

*Última atualização: 2026-05-13.*
