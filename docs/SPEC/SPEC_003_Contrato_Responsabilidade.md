---
documento: SPEC-003
titulo: Contrato de Responsabilidade do projeto learn-web
versao: v1
status: aprovado
data: 2026-05-13
autor: Bruno Serminaro
referencia: SPEC-001, SPEC-002
---

# SPEC-003 · Contrato de Responsabilidade do projeto `learn-web`

> Declara quem responde pelo "o que" e pelo "como" do projeto: pessoas atribuídas aos papéis abstratos da SPEC-002 §2, regime de uso da IA como co-autor, fluxo de aprovação por artefato, fronteiras de autonomia e cadência de revisão. É a peça que muda quando a relação autor-IA é redefinida, sem que as outras SPECs de fundação precisem ser re-versionadas. Compõe, com SPEC-001 (Taxonomia) e SPEC-002 (Fundação), o conjunto obrigatório de SPECs de fundação.

---

## 1. Propósito

A SPEC-002 declarou os papéis em abstrato — autor, peer-reviewer, avaliador. Esta SPEC os preenche com pessoas, fixa como o trabalho flui entre eles e fixa o que cada um pode decidir sozinho.

O contexto deste projeto difere materialmente dos projetos profissionais do autor: é projeto **unipessoal de aprendizado**, em que o autor acumula múltiplos papéis humanos, e em que a IA atua como **co-autor sob controle declarado**. A separação rigorosa entre papéis, ainda que exercida pela mesma pessoa em momentos diferentes, é parte do regime de qualidade.

---

## 2. Escopo do contrato

O contrato governa:

- A cadeia de produção e revisão dos **artefatos formais** previstos na SPEC-001: SPECs, DECs, GUIDEs, REPs, BRIEFs.
- O regime de uso da **IA como co-autora** desses artefatos e do código do projeto.
- O fluxo de **aprovação** de mudança de status (`proposto` → `aprovado`).

Não governa a execução técnica fora do alcance documental — escrita rotineira de exercícios de prática, debugging local, ajuste de CSS pontual, etc. Essas atividades seguem a competência operacional do autor sob a SPEC-002, sem passar pelo fluxo descrito aqui.

---

## 3. Atribuição papel ↔ pessoa

### 3.1 Tabela vigente

| Papel | Pessoa | Observação |
|---|---|---|
| **Autor** | Bruno Serminaro | Produz, mantém e responde por todos os artefatos. |
| **Peer-reviewer** | Bruno Serminaro (em modo separado) | Mesma pessoa, em revisão "a frio" — idealmente com separação temporal mínima de 12 horas em relação à produção. |
| **Avaliador de qualidade** | Bruno Serminaro (em modo separado) | Terceira passada, em momento de calibração antes do fechamento de cada camada. |
| **Co-autor IA** | Claude (Anthropic, modelo vigente na sessão) | Atua sob controles declarados na §4. Sem poder de aprovação. |

A divisão entre os três primeiros papéis (autor → peer → avaliador) é preservada **mesmo sendo a mesma pessoa**. O ganho de qualidade vem da separação temporal e do modo de leitura, não de pluralidade humana.

### 3.2 Por que registrar a IA como papel

Registrar a IA como co-autor reconhece um fato operacional: parte material dos artefatos do projeto (incluindo trechos significativos desta própria SPEC) é produzida em parceria com a IA. Tratar essa parceria como **invisível** seria desonesto documentalmente e impediria que o regime de uso da ferramenta fosse auditável.

A IA neste projeto **não substitui** o autor em nenhum dos papéis humanos; **assiste** a produção e a revisão sob controles declarados.

### 3.3 Mudança de atribuição

Inclusão de outra pessoa em qualquer papel (peer-reviewer ou avaliador externo) exige nova versão desta SPEC, com entrada no histórico. Mudança de modelo de IA usado (`claude-opus-4-7` para outro modelo) **não** exige re-versão se a relação operacional descrita na §4 permanecer válida.

---

## 4. Regime de uso da IA como co-autora

### 4.1 O que a IA pode fazer

A IA, atuando como co-autora sob este contrato, pode:

- **Propor** novos artefatos (criar arquivos em status `proposto`).
- **Editar** artefatos existentes em status `proposto`.
- **Rascunhar** SPECs, DECs, GUIDEs, REPs, BRIEFs para revisão do autor.
- **Sugerir** mudanças de status, alternativas, refatorações, melhorias de código.
- **Executar** comandos de leitura no sistema (listagens, leitura de arquivos, queries `gh`, queries não-destrutivas).
- **Executar** comandos de escrita **dentro do diretório do projeto** (`~/Projetos/learn-web/`), incluindo criar/modificar arquivos sob `docs/` e `src/`.
- **Executar** comandos de versionamento (git add, git commit, git push) quando autorizada explicitamente pelo autor naquele momento.

### 4.2 O que a IA não pode fazer

A IA, atuando como co-autora sob este contrato, **não pode**:

- **Aprovar artefatos** — a transição de status `proposto` → `aprovado` é prerrogativa exclusiva do autor humano. A IA pode sinalizar "pronto para aprovação" mas a mudança do campo `status` no frontmatter é feita pelo autor.
- **Criar DEC autonomamente** — registros de decisão devem refletir deliberação do autor. A IA pode redigir uma DEC rascunhada, mas o autor a refina e aprova.
- **Modificar SPECs aprovadas** — SPECs com status `aprovado` são editadas apenas pelo autor. A IA pode propor uma nova versão (v2) em status `proposto`.
- **Executar comandos com `sudo`** — toda operação que exija elevação é feita pelo autor.
- **Versionar segredos** — `.env`, tokens, credenciais nunca são commitadas pela IA. Em caso de dúvida sobre se algo é segredo, perguntar.
- **Acessar diretórios fora do projeto sem motivo explícito** — IA opera por default dentro de `~/Projetos/learn-web/`. Leituras fora do projeto (ex.: `/etc/nginx/`) acontecem apenas com motivação clara.

### 4.3 Como o autor exerce controle

O autor exerce controle sobre a co-autoria por três mecanismos:

- **Revisão da diferença antes de aceitar** — o autor lê o que a IA produziu antes de aprovar status ou commit. Aceitar cegamente é violação deste contrato.
- **Rejeição explícita** — pedidos da IA que extrapolem o regime declarado aqui devem ser recusados, e a recusa registrada como sinal de calibração (ajustar a SPEC ou o prompt).
- **Auditoria periódica** — antes do fechamento de cada camada, o autor revisa, por amostragem, os artefatos para verificar coerência com este contrato.

### 4.4 Por que esse regime existe

A IA é poderosa: produz artefatos plausíveis rápido. Essa potência é faca de dois gumes — plausibilidade não é correção, e velocidade não é deliberação. O regime acima é um **lentificador deliberado** sobre os pontos críticos (aprovação de status, registro de decisão, modificação de SPECs aprovadas), preservando a velocidade nos pontos onde ela ajuda (rascunho, exploração, código repetitivo).

---

## 5. Fluxo de aprovação

### 5.1 Fluxo default

Para cada artefato documental produzido:

1. **Autor (com ou sem assistência da IA)** produz o artefato em status `proposto`.
2. **Autor em modo peer-reviewer** revisa, idealmente em outro dia ou após pausa significativa. Pode aprovar ou retornar com pedido de mudança.
3. **Autor em modo avaliador** valida o conjunto contra os critérios da SPEC-002 §5, em momento de fechamento de camada.
4. **Atualização do status** de `proposto` para `aprovado` no frontmatter, com entrada no histórico do próprio documento.

A passagem do artefato pela cadeia é registrada no campo `Histórico` do próprio artefato, conforme SPEC-001 §3.3.

### 5.2 Bloqueio vs registro

| Papel | Bloqueia avanço? | Em que sentido |
|---|---|---|
| Autor | Sim | Ele decide tudo. |
| Peer-reviewer (autor a frio) | Sim | Pode rejeitar e mandar revisar. |
| Avaliador (autor em terceira passada) | Sim | Pode bloquear fechamento de camada. |
| IA co-autora | Não | Apenas propõe; aceitação é do autor. |

### 5.3 Aprovação automática em projetos pessoais

Diferentemente do BAUR, **não há aprovação automática por silêncio**. Em projeto unipessoal, ausência de atuação do autor significa ausência de aprovação, não consenso tácito. Artefatos em `proposto` por tempo indeterminado permanecem nesse status até decisão ativa.

---

## 6. Aprovação por tipo de artefato

| Tipo | Quem aprova final | Observação |
|---|---|---|
| **SPEC** | Autor (após peer e avaliador) | SPECs de fundação (001, 002, 003) são aprovadas como bloco quando o projeto é fundado. |
| **DEC** | Autor | DEC sem alternativas e sem consequências negativas é devolvida. |
| **GUIDE** | Autor (após teste prático do procedimento) | GUIDE não-testado em ambiente real fica em `proposto`. |
| **REP** | Autor | REP de fechamento de camada exige aprovação antes de iniciar a próxima. |
| **BRIEF (README)** | Autor | README é editado livremente; o "estado canônico" é o que está em `main`. |
| **BRIEF numerado** | Autor | Mesmo critério que REP. |

---

## 7. Fronteiras de autonomia

### 7.1 O que o autor pode decidir sem registrar formalmente

- Escolha de variáveis CSS específicas, nomes de classes, indentação.
- Estrutura interna de um arquivo (`<header>` no topo ou `<nav>` antes).
- Refatorações puramente locais (renomear variável, extrair função).
- Comentários em código.

### 7.2 O que exige DEC

- Adoção ou abandono de qualquer biblioteca/framework (ex.: introdução de jQuery).
- Mudança de servidor (ex.: trocar nginx por Apache).
- Mudança de motor de banco (ex.: trocar MySQL por SQLite).
- Estrutura de pastas de `src/` (ex.: adotar separação MVC).
- Padrões de segurança (ex.: política de hashing de senha).
- Mudança no escopo declarado da SPEC-002 (mover algo de "fora de escopo" para "em escopo" ou vice-versa).

### 7.3 O que exige nova versão de SPEC

- Mudança nas camadas declaradas (SPEC-002 §4): número de camadas, propósito de uma camada, tecnologias da camada.
- Mudança na audiência ou no contrato de responsabilidade (esta SPEC).
- Mudança na taxonomia documental (SPEC-001).

---

## 8. Regime de exceção

### 8.1 Pausa do projeto

O autor pode **pausar** o projeto a qualquer momento sem aviso formal. A pausa preserva os artefatos no estado em que estão; o `status` dos artefatos não muda automaticamente para `descartado`.

Retomada de projeto após pausa de mais de 90 dias exige:

- Revisão das premissas da SPEC-002 §6 (ambiente local pode ter mudado).
- Confirmação da vigência desta SPEC-003 (regras de IA podem ter envelhecido).

### 8.2 Descontinuação

O autor pode **descontinuar** o projeto a qualquer momento. Descontinuação é registrada como BRIEF de marco (`BRIEF_NNN_descontinuacao.md`) explicando motivos e o estado final. Os artefatos não são apagados; o repositório fica como **arquivo histórico**.

### 8.3 Mudança material de propósito

Se o autor decidir que `learn-web` muda de "aprender web" para outra coisa (ex.: vira o site real de produção), todos os artefatos da SPEC-002 podem ser obsoletos. A regra é: **não reaproveitar** o repositório; criar **outro** repositório (`bruno-site` ou nome equivalente) e marcar `learn-web` como concluído com BRIEF de fechamento.

---

## 9. Cadência de revisão

Esta SPEC é revisada nos seguintes momentos:

- **No fechamento de cada camada** da SPEC-002 — verificar se o regime de IA, fluxo de aprovação e fronteiras de autonomia continuam adequados à fase seguinte.
- **Quando houver atrito documentado** entre o autor e a IA durante uma sessão — ajustar a §4 conforme aprendizado.
- **Anualmente, em projeto ativo** — manutenção preventiva.

Cada revisão produz, no mínimo, nota no histórico desta SPEC. Mudança material produz nova versão (`v2`, `v3`...).

---

## 10. Regras checáveis pelo skill de auditoria

| ID | Regra | Onde verificar | Severidade |
|---|---|---|---|
| **R-CON-01** | Todo artefato com `status: aprovado` tem entrada no histórico do próprio artefato datada e descrevendo a transição de `proposto`. | Parse do histórico de cada documento `aprovado` | Alta |
| **R-CON-02** | Nenhum commit autorizado pela IA contém arquivos em `.env`, credenciais ou tokens. | Inspeção dos arquivos modificados nos commits | Crítica |
| **R-CON-03** | Toda SPEC com `status: aprovado` foi modificada apenas pelo autor (não pela IA) após a aprovação. Modificação pela IA em SPEC aprovada exige nova versão (v2) em `proposto`. | Cruzamento entre histórico do documento e log de sessão | Média |
| **R-CON-04** | DEC criada pela IA sem refinamento explícito do autor antes do `aprovado` é divergência. Heurística: histórico da DEC sem entrada do autor distinta da entrada de criação sinaliza divergência. | Parse do histórico de cada DEC | Alta |
| **R-CON-05** | Camada declarada "concluída" na SPEC-002 §4 só é fechada com REP correspondente e nota no histórico desta SPEC-003 registrando a revisão de cadência. | Cruzamento entre §4 da SPEC-002, `docs/REP/` e histórico desta SPEC | Média |
| **R-CON-06** | Frontmatter de toda SPEC desta SPEC-003 e da SPEC-002 referencia a outra. Quebra de reciprocidade sinaliza divergência de governança. | Inspeção do campo `referencia` no frontmatter | Média |

---

## 11. Histórico

| Data | Evento |
|---|---|
| 2026-05-13 | SPEC-003 v1 produzida em status `aprovado`. Adaptação da SPEC-007 do `baur_clientes_plan` ao contexto de projeto pessoal unipessoal, com a IA registrada como co-autora sob controles declarados. |

---

*Fim da SPEC-003.*
