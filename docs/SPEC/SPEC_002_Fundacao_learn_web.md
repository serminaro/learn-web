---
documento: SPEC-002
titulo: Fundação do projeto learn-web
versao: v1
status: aprovado
data: 2026-05-13
autor: Bruno Serminaro
referencia: SPEC-001, SPEC-003
---

# SPEC-002 · Fundação do projeto `learn-web`

> Declara o que o projeto `learn-web` se compromete a realizar: propósito, audiência, escopo, fora de escopo, decomposição em camadas, critérios de sucesso e regras auditáveis. É a peça contra a qual se afere se o projeto entregou ou não o que prometeu, e é a segunda das três SPECs de fundação obrigatórias, ao lado da SPEC-001 (Taxonomia) e da SPEC-003 (Contrato de Responsabilidade).

---

## 1. Propósito

O projeto `learn-web` é o veículo pelo qual o autor aprende **desenvolvimento web full-stack** — HTML, CSS, JavaScript e PHP — construindo um site pessoal real, em camadas progressivamente mais complexas.

A motivação é prática. O autor tem necessidade explícita de subir o próprio site (mencionada no histórico de planejamento do ambiente, em 2026-05-12). Em vez de seguir tutorial linear desconexo da prática, este projeto faz da construção do site o **vetor único de aprendizado**: cada conceito novo é introduzido no momento em que se torna necessário para a próxima entrega.

O resultado pretendido é duplo: (a) um site pessoal funcional, hospedado, com características reais de produção; e (b) um corpo de conhecimento técnico e documental que sirva de referência consultável para o próprio autor em projetos web futuros.

---

## 2. Audiência

Os papéis abstratos abaixo são preenchidos por pessoas físicas na SPEC-003. Nas circunstâncias deste projeto pessoal, o autor acumula a maior parte deles.

| Papel | Função frente a esta SPEC |
|---|---|
| **Autor** | Produz a SPEC, mantém-na em dia e responde por sua aplicação no projeto. |
| **Peer-reviewer** | Revisa tecnicamente os artefatos frente ao que esta SPEC declara. |
| **Avaliador de qualidade** | Valida o conjunto da produção frente aos critérios da §5. |

A divisão entre os três níveis é deliberada e preserva-se mesmo em projeto unipessoal: cada nível corresponde a um modo de leitura diferente do artefato, e a passagem por todos eles continua sendo regime de produção exigido, conforme detalhado na SPEC-003.

---

## 3. Escopo

### 3.1 O que o projeto entrega

O projeto entrega, ao longo das suas quatro camadas:

1. **Um site pessoal hospedável**, construído incrementalmente de HTML estático até backend dinâmico com persistência. O site deve ser **real**: navegável, com conteúdo próprio do autor, com features que justifiquem cada camada técnica.
2. **Um corpo documental** sob a taxonomia SERMI (SPEC-001), cobrindo: especificações por camada, decisões registradas, guias operacionais e relatórios de fechamento.
3. **Um conjunto de exercícios numerados** em `src/`, cada um isolando um conceito técnico (ex.: `src/01-html-semantico/`, `src/02-css-grid/`, etc.), que sirvam de referência consultável para o autor.

A entrega é cumulativa: cada camada produz artefatos que servem de insumo direto para a próxima.

### 3.2 Fora de escopo

O projeto **não** se compromete a:

- **Adotar frameworks front-end** (React, Vue, Svelte) na vigência desta versão da SPEC. A camada de aprendizado é deliberadamente vanilla.
- **Adotar frameworks PHP** (Laravel, Symfony, Slim). PHP procedural e organizado é suficiente para os critérios da Camada 3.
- **Usar TypeScript.** JavaScript ES6+ vanilla é o alvo. Mudança exige DEC.
- **Cobrir mobile nativo** (iOS/Android). Web responsiva é o escopo; aplicação nativa fica fora.
- **Implementar testes automatizados em escala.** Testes manuais e validações ad-hoc são suficientes para o critério de "site funcionando". A introdução de testes pode acontecer numa fase futura, registrada em DEC.
- **Deploy em produção remota.** Este projeto encerra-se em ambiente local validado (nginx + php-fpm em `localhost:8080`). O deploy é projeto subsequente, fora do escopo desta SPEC.
- **DevOps avançado** (Docker, Kubernetes, CI/CD). Ambiente local nativo é suficiente.

---

## 4. Decomposição em camadas

A solução decompõe-se em quatro camadas. Cada camada tem propósito próprio, artefatos próprios e critério de fechamento próprio. A passagem para a camada seguinte só ocorre quando os critérios da camada atual estão verificados.

| Camada | Propósito | Tecnologias | Estado em 2026-05-13 |
|---|---|---|---|
| **C1 — Estrutura e estilo estáticos** | Aprender HTML semântico e CSS moderno construindo páginas estáticas do site. | HTML5, CSS3 (Flexbox, Grid, custom properties), responsividade | Não iniciada |
| **C2 — Interatividade client-side** | Adicionar interatividade ao site usando JavaScript vanilla. | JavaScript ES6+, DOM API, Fetch API, módulos | Não iniciada |
| **C3 — Backend dinâmico** | Gerar HTML dinâmico, processar formulários, lidar com sessão. | PHP 8.3, templating manual, validação de input, headers HTTP | Não iniciada |
| **C4 — Persistência** | Persistir dados entre requisições com banco de dados relacional. | MySQL ou SQLite (a definir em DEC), prepared statements | Não iniciada |

A separação em camadas reflete escalonamento de **complexidade conceitual e de risco**:

- A Camada 1 trabalha com o cliente apenas como **renderizador** de markup.
- A Camada 2 introduz **lógica no cliente** sem mudar o modelo de servidor.
- A Camada 3 introduz **lógica no servidor** sem mudar o modelo de dados.
- A Camada 4 introduz **estado persistente**.

Cada camada paga seu custo de erro com a anterior estável. Pular ou misturar camadas durante o aprendizado dilui o ganho didático e dificulta diagnóstico quando algo quebra.

---

## 5. Critérios de sucesso

Os critérios abaixo são auditáveis: cada um aponta para artefato concreto contra o qual a verificação pode ser feita.

### 5.1 Camada 1 — Estrutura e estilo estáticos

- **C1.1** — O site tem ao menos 3 páginas estáticas com conteúdo próprio do autor (ex.: home, sobre, contato), cada uma como arquivo `.html` em `src/` ou subpasta.
- **C1.2** — As páginas usam HTML **semântico**: `<header>`, `<main>`, `<nav>`, `<section>`, `<article>`, `<footer>` empregados conforme função, não como divs decoradas.
- **C1.3** — O CSS está em arquivo externo (`.css`), não inline nem em tag `<style>`. Variáveis CSS (`--cor-primaria`, etc.) são usadas para temas e cores.
- **C1.4** — O design é responsivo: o site se mantém legível e navegável em viewport de 320px de largura (mobile) e 1920px (desktop). Verificável com DevTools do navegador.
- **C1.5** — O site é servido localmente por nginx em `localhost:8080`, e há REP-001 documentando o fechamento da camada.

### 5.2 Camada 2 — Interatividade client-side

- **C2.1** — O site tem ao menos 3 features interativas implementadas em JavaScript vanilla, cada uma documentada como exercício isolado em `src/`.
- **C2.2** — Pelo menos uma das features usa **Fetch API** para consumir dado externo (API pública gratuita, ex.: lista de países, cotação, clima).
- **C2.3** — O código JavaScript é organizado em **módulos ES6** (`import`/`export`), não em scripts globais.
- **C2.4** — Nenhuma biblioteca JS externa (jQuery, lodash, etc.) é usada. Se a necessidade aparecer, é justificada em DEC.
- **C2.5** — REP-002 documenta o fechamento da camada.

### 5.3 Camada 3 — Backend dinâmico

- **C3.1** — Pelo menos uma página é **gerada dinamicamente** pelo PHP (não apenas servida estaticamente). Conteúdo deve depender de algo: query string, sessão, hora atual, formulário.
- **C3.2** — Pelo menos um **formulário HTML** é processado pelo PHP: dados recebidos, validados, e o resultado da validação reapresentado ao usuário.
- **C3.3** — Toda saída HTML que inclui dado de origem externa (formulário, query string) passa por **escape contra XSS** (`htmlspecialchars` ou equivalente). Output não-escapado é divergência.
- **C3.4** — O código PHP segue **organização clara**: arquivos por responsabilidade (rotas, lógica, templating), sem misturar muita coisa em um único `.php`. O padrão exato será documentado em SPEC dedicada.
- **C3.5** — REP-003 documenta o fechamento da camada.

### 5.4 Camada 4 — Persistência

Critérios desta camada são **provisórios** e devem ser calibrados em SPEC dedicada quando a implementação iniciar.

- **C4.1** — Existe schema documentado do banco de dados (`schema.sql` ou equivalente) versionado no repo.
- **C4.2** — Pelo menos uma feature do site usa **CRUD completo** (Create, Read, Update, Delete) sobre uma entidade do schema.
- **C4.3** — Todas as queries usam **prepared statements** (PDO ou mysqli com bind). Concatenação de string em SQL é divergência grave.
- **C4.4** — Senhas, se houver autenticação, são armazenadas com `password_hash()` — nunca em texto claro nem com hash simples (MD5, SHA1).
- **C4.5** — REP-004 documenta o fechamento da camada.

---

## 6. Premissas e dependências

O projeto assume, como condição para suas entregas:

- **Ambiente local validado** em 2026-05-12: nginx 1.24 + PHP 8.3-fpm + Composer + Node 18 (cf. `environment.txt`).
- **Site teste anterior** (`~/Projetos/site-teste`) preservado como referência de "primeira página funcionando", não absorvido pelo `learn-web`.
- **Permissão `751` em `/home/bruno`** preservada (necessária pro `www-data` do nginx atravessar). Reversão pra 750 derruba o site local.
- **Editor configurado** (Neovim 0.12 + kickstart + LSPs PHP/HTML/CSS/JS) operacional pra produtividade na escrita do código.
- **IA (Claude) disponível como co-autor** sob os controles da SPEC-003 §4 (a definir).

Mudança em qualquer destas premissas dispara reavaliação desta SPEC.

---

## 7. Não-objetivos

Não-objetivos são critérios contra os quais o projeto **se recusa a otimizar**. Distinguem-se do "fora de escopo" (§3.2): aqui não se trata de o que o projeto não faz, mas de o que **não é função-objetivo**.

- **Performance não é critério de sucesso.** Páginas que carregam em 2 segundos são aceitáveis. Otimização (lazy loading, code splitting, minificação) é exercício posterior, não obrigatório.
- **Estética sofisticada não é critério.** Design utilitário e legível basta. Não há concurso de beleza visual.
- **Cobertura exaustiva da linguagem não é objetivo.** O autor aprende o subconjunto necessário para entregar cada camada. Recursos avançados (PHP traits, JS Proxy, CSS subgrid) só entram se a entrega pedir.
- **Cobertura de browsers legados não é objetivo.** Suporte a navegadores modernos (Chrome/Firefox/Edge recentes) é suficiente. IE não é alvo.

---

## 8. Regras checáveis pelo skill de auditoria

Esta seção declara as regras concretas que um skill de auditoria pode verificar contra o estado real do projeto.

| ID | Regra | Onde verificar | Severidade |
|---|---|---|---|
| **R-FUN-01** | Para cada camada concluída, existe REP correspondente em `docs/REP/` (REP-001 para C1, REP-002 para C2, etc.). Camada declarada "concluída" sem REP é divergência. | Cruzamento entre §4 (estado) e `docs/REP/` | Alta |
| **R-FUN-02** | Esta SPEC e a SPEC-003 (Contrato) se referenciam mutuamente. SPEC-001 é referenciada por ambas. | Inspeção dos campos `referencia` nos cabeçalhos | Média |
| **R-FUN-03** | Nenhum arquivo em `src/` usa biblioteca/framework fora do escopo declarado em §3.2 sem DEC autorizando. Exemplo de violação: `import React from 'react'` sem DEC. | Grep no `src/` por imports/requires conhecidos de frameworks | Alta |
| **R-FUN-04** | Para cada critério C1–C4 declarado na §5, existe artefato concreto que permita sua verificação (página, arquivo, query, REP). Critério sem artefato é critério ornamental. | Inspeção da §5 cruzada com a estrutura real do projeto | Média |
| **R-FUN-05** | Nenhum dado de origem externa (query string, formulário) é incluído em HTML sem escape (C3.3) ou em SQL sem prepared statement (C4.3). Violações são severidade crítica em camadas C3+ ativas. | Grep estático em `src/*.php` | Crítica |
| **R-FUN-06** | Toda decisão arquitetural materialmente relevante referida em código ou em SPEC tem DEC formalizada. Constatação de "decisão implícita" sem DEC sinaliza dívida documental. | Inspeção de SPECs e código por menções a decisão sem `DEC-NNN` | Média |

---

## 9. Histórico

| Data | Evento |
|---|---|
| 2026-05-13 | SPEC-002 v1 produzida em status `aprovado`. Primeira versão; entra em vigor imediatamente como peça de fundação do `learn-web`. |

---

*Fim da SPEC-002.*
