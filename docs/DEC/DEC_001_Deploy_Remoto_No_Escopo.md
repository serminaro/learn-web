---
documento: DEC-001
titulo: Inclusão de deploy em produção remota no escopo do learn-web
versao: v1
status: proposto
data: 2026-06-14
autor: Bruno Serminaro
referencia: SPEC-002
---

# DEC-001 · Inclusão de deploy em produção remota no escopo do `learn-web`

## Contexto

A SPEC-002 §3.2 declara explicitamente o **deploy em produção remota** como **fora de escopo**, prevendo que o projeto se encerra em ambiente local validado (nginx + php-fpm em `localhost:8080`) e que o deploy seria "projeto subsequente". Essa fronteira foi traçada para manter a Camada 1–4 focada em aprendizado de full-stack sem o peso operacional de infraestrutura de nuvem.

Em 2026-06-14 o autor decidiu, no entanto, que aprender a **hospedar o próprio site no Google Cloud** é parte integrante do objetivo prático do projeto (cf. SPEC-002 §1, que justifica o projeto pela necessidade real de "subir o próprio site"). O site estático da Camada 1 já existe e serve de insumo concreto para esse aprendizado. Trazer o deploy para dentro do `learn-web` — em vez de abrir um projeto separado — mantém um único vetor de aprendizado e um único acervo documental, ao custo de expandir o escopo de uma SPEC aprovada.

## Decisão

Incluir **deploy em produção remota no Google Cloud** no escopo do `learn-web`, tratando-o como capacidade transversal a ser exercitada a partir do artefato estático da Camada 1, e disparar a revisão da SPEC-002 para v2 refletindo o novo escopo.

## Alternativas consideradas

1. **Manter o deploy fora de escopo (status quo da SPEC-002 §3.2) e abrir projeto separado.**
   Descartada porque fragmentaria o aprendizado e o acervo documental em dois repositórios, contrariando o princípio de "vetor único de aprendizado" (SPEC-002 §1). O autor prefere consolidar.

2. **Trazer o deploy para o escopo sem registro formal, editando a SPEC-002 in-place.**
   Descartada por violar CLAUDE.md §4 e SPEC-001 §8 (SPEC aprovada não é editada in-place; mudança de escopo exige nova versão). Sem DEC, a rastreabilidade do "por que o escopo mudou" se perderia.

3. **Trazer o deploy para o escopo via DEC + SPEC-002 v2 (escolhida).**
   Preserva a imutabilidade da SPEC-002 v1, registra a motivação e o trade-off, e mantém auditabilidade.

## Consequências

### Positivas
- O autor aprende infraestrutura de nuvem (projeto, billing, bucket/IAM, HTTPS, DNS) usando o próprio site como objeto real.
- Um único repositório e um único acervo documental cobrem da escrita do HTML até a publicação.
- A escolha da plataforma de hospedagem (Cloud Storage vs Firebase Hosting vs, futuramente, Cloud Run/App Engine) fica registrada em DECs subsequentes.

### Negativas
- Expande o escopo de uma SPEC de fundação aprovada, aumentando a superfície do projeto e o risco de o aprendizado de DevOps competir com o foco original em full-stack.
- Introduz dependências externas não previstas (gcloud CLI, conta de billing, eventualmente domínio pago) que saem do ambiente local autocontido.
- Custos de nuvem passam a ser uma preocupação real, ainda que pequenos no plano gratuito.

### O que esta decisão NÃO resolve
- **Não** escolhe a plataforma de hospedagem nem o serviço (Cloud Storage, Firebase Hosting, Cloud Run, App Engine). Essa escolha é decisão separada, a ser registrada em **DEC-002** após avaliação prática dos caminhos.
- **Não** trata do deploy do backend PHP (Camada 3+), que exige serviço de container/dinâmico e DEC própria.
- **Não** redefine os critérios de fechamento das Camadas 1–4 da SPEC-002 §4.

## Critérios de reavaliação

Revisitar esta decisão se: (a) o custo ou a complexidade operacional do deploy passar a comprometer o foco em aprendizado full-stack; (b) o autor optar por separar infraestrutura em projeto próprio; ou (c) a SPEC-002 v2 não for aprovada, caso em que esta DEC permanece `proposto` e nenhum deploy é executado sob o guarda-chuva do `learn-web`.

---

## Histórico

| Data | Evento |
|---|---|
| 2026-06-14 | DEC-001 v1 rascunhada pela IA, aguarda revisão do autor. |
