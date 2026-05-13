---
documento: SPEC-001
titulo: Taxonomia Documental do projeto learn-web
versao: v1
status: aprovado
data: 2026-05-13
autor: Bruno Serminaro
referencia: SPEC-002, SPEC-003
---

# SPEC-001 · Taxonomia Documental do projeto `learn-web`

> Define os tipos de documento produzidos no projeto, suas funções, audiências, gatilhos de produção e regras de versionamento. Estabelece a taxonomia documental como peça de arquitetura do projeto, não como ornamento administrativo. Toda a documentação produzida no escopo do projeto `learn-web` observa esta taxonomia.

---

## 1. Propósito desta especificação

### 1.1 Por que uma taxonomia documental é necessária

Um projeto técnico produz, ao longo do seu ciclo de vida, materiais que cumprem funções heterogêneas: registrar como um componente foi construído, comunicar status, ensinar conceitos a quem chega depois, justificar decisões. Essas funções, embora todas legítimas, **competem entre si quando comprimidas em um único documento**.

O sintoma típico da ausência de taxonomia é o documento que tenta ser, simultaneamente, manual de operação, registro de progresso, justificativa técnica e síntese executiva. O resultado é um artefato que não atende bem a nenhum desses propósitos e perde valor de referência rapidamente.

A solução adotada neste projeto é **separar os tipos de documento por função, audiência e momento de produção**, e tratar essa separação como restrição de projeto — não como sugestão estilística.

### 1.2 Princípio operacional fundamental

> **Cada documento tem uma função primária e uma audiência primária.**

Quando um documento começa a explicar algo, reportar progresso e ensinar um conceito ao mesmo tempo, a regra é interromper a produção e separar em documentos distintos. **Documentos curtos e focados são preferíveis a documentos longos e genéricos**, e a coexistência de múltiplos documentos curtos especializados é considerada melhor projeto que um documento único polivalente.

Esse princípio governa todas as decisões taxonômicas que se seguem.

### 1.3 Status desta SPEC no projeto

Esta é a primeira SPEC do projeto `learn-web` e a primeira peça da tríade de fundação documental (SPEC-001 Taxonomia, SPEC-002 Fundação, SPEC-003 Contrato de Responsabilidade), conforme convenção adotada pelo autor em projetos pessoais e profissionais a partir de 2026-05.

O texto aqui presente é adaptação direta da SPEC-001 v3 do projeto `baur_clientes_plan`, simplificada para o contexto de projeto pessoal de aprendizado.

---

## 2. Os cinco tipos de documento

A taxonomia adotada compreende cinco tipos, identificados pelas siglas **SPEC**, **REP**, **GUIDE**, **BRIEF** e **DEC**.

| Sigla | Nome | Função primária | Audiência primária |
|---|---|---|---|
| **SPEC** | Especificação Técnica | descrever **o que** algo é, como funciona, como está construído | autor futuro, leitor técnico |
| **REP** | Relatório | narrar **o que aconteceu** em uma fase, execução ou marco, com profundidade | autor futuro, leitor técnico |
| **GUIDE** | Guia Operacional | descrever **como operar** algo, passo a passo | quem executa o procedimento |
| **BRIEF** | Resumo Executivo | comunicar **estado e valor** em alto nível, sem jargão | leitor externo do repo (vitrine pública) |
| **DEC** | Registro de Decisão | documentar **uma decisão**, alternativas e consequências | autor futuro, com ênfase em rastreabilidade |

A divisão de responsabilidades entre os cinco tipos é exaustiva: qualquer documento legítimo do projeto cabe em um deles. Documentos que parecem caber em vários simultaneamente devem ser revisados e segmentados antes de serem aceitos no acervo.

---

## 3. SPEC — Especificação Técnica

### 3.1 Definição e função

A SPEC documenta **o que algo é e como funciona**. É o tipo de documento que permite a um leitor futuro — incluindo o próprio autor — compreender e manter aquilo que foi construído. A SPEC opera no plano da **descrição estrutural**: arquitetura, contratos, schemas, dependências, comportamento esperado.

A SPEC não substitui comentários inline no código; complementa-os no nível do sistema, descrevendo o que a leitura linha-a-linha do código não revela.

### 3.2 Quando produzir

Uma SPEC é produzida quando um componente, módulo ou conceito estrutural do projeto atinge maturidade suficiente para ser descrito como peça estável. **Especificação prematura** — antes de o componente existir ou estar estabilizado — gera desperdício, porque o documento envelhece antes de ser útil. **Especificação tardia** — meses após a construção — perde fidelidade, porque os detalhes já se diluíram.

O gatilho prático recomendado é: **logo após a primeira validação bem-sucedida do componente**.

### 3.3 Estrutura recomendada

Toda SPEC contém, no mínimo:

- **Propósito** — para que o componente existe.
- **Entrada** — o que recebe e em que formato.
- **Saída** — o que produz.
- **Lógica de processamento** — descrição em prosa do que o componente faz, em nível de sistema.
- **Tratamento de erros** — comportamento diante de entradas inválidas e falhas.
- **Dependências** — bibliotecas, módulos e schemas dos quais depende.
- **Limitações conhecidas** — o que o componente não faz.
- **Histórico de mudanças** — registro de alterações relevantes na própria SPEC.

### 3.4 Exemplos no projeto

- **SPEC-001** — esta especificação. Taxonomia documental do `learn-web`.
- **SPEC-002** — Fundação. Declara o que o projeto se compromete a entregar e em quantas camadas.
- **SPEC-003** — Contrato de Responsabilidade. Quem responde pelo quê (peculiar a projeto pessoal: cf. §3 da SPEC-003).

---

## 4. REP — Relatório

### 4.1 Definição e função

O REP narra, com profundidade técnica, **o que aconteceu** em uma fase do projeto, na execução de um exercício, na construção de uma camada. Responde à pergunta: *"o que foi feito, como foi feito, com que resultado, e o que se aprendeu?"*

O REP é o documento mais denso da taxonomia. Em um projeto de aprendizado, é também o registro do progresso intelectual do autor.

### 4.2 Quando produzir

Um REP é produzido em três circunstâncias típicas:

- **Conclusão de uma camada do projeto** — por exemplo, "conclusão da Camada 1 (HTML/CSS estático)".
- **Conclusão de um exercício relevante** — quando o autor produziu algo cuja construção e aprendizado merecem registro.
- **Investigação ou descoberta** — quando o autor enfrentou um problema cuja resolução envolveu pesquisa não-trivial.

Um REP **não** é produzido em ritmo regular. Sua produção é episódica, ditada pelo ciclo natural do projeto.

### 4.3 Estrutura recomendada

- **Contexto** — o que motivou o trabalho.
- **Escopo** — o que está coberto e o que está deliberadamente fora.
- **Trabalho realizado** — descrição cronológica ou temática.
- **Decisões tomadas** — resumo das DECs formalizadas no período.
- **Resultados** — entregáveis, validações realizadas.
- **Reflexões sobre método** — o que funcionou bem ou mal no processo.
- **Pendências e próximos passos** — o que ficou em aberto.

---

## 5. GUIDE — Guia Operacional

### 5.1 Definição e função

O GUIDE descreve **como operar algo**. O leitor não precisa entender o porquê para seguir o passo a passo e produzir o resultado esperado. A função do GUIDE é **transferir capacidade de execução**.

### 5.2 Quando produzir

Um GUIDE é produzido quando um procedimento atinge dois critérios simultaneamente:

- **Estabilidade** — o procedimento foi executado ao menos uma vez com sucesso.
- **Reuso esperado** — outras execuções estão previstas.

Procedimentos pontuais que não serão reexecutados não justificam GUIDE.

### 5.3 Estrutura recomendada

- **Objetivo** — o que o procedimento entrega ao final.
- **Pré-requisitos** — ambiente, ferramentas, estado inicial.
- **Passos** — sequência numerada, com comandos exatos.
- **Verificação** — como confirmar que cada passo correu bem.
- **Erros comuns** — antecipação dos problemas mais frequentes.

### 5.4 Exemplos previstos

- **GUIDE-001** (futuro) — Como subir o site local com nginx + php-fpm.
- **GUIDE-002** (futuro) — Como criar uma nova camada de exercício seguindo o padrão do projeto.

---

## 6. BRIEF — Resumo Executivo

### 6.1 Definição e função

O BRIEF é o documento de **comunicação externa ao trabalho técnico**. Sua função é dar visibilidade de alto nível ao estado do projeto, sem exigir do leitor familiaridade com o vocabulário técnico ou com detalhes de implementação.

No contexto deste projeto pessoal, o BRIEF principal é o **README.md do repositório** — vitrine pública pra qualquer pessoa que abra o link no GitHub.

### 6.2 Duas variantes

| Atributo | BRIEF de marco | BRIEF de período |
|---|---|---|
| Gatilho | evento ou marco (conclusão de camada, primeira entrega) | ciclo regular (raro neste projeto pessoal) |
| Nomenclatura | `BRIEF_NNN_descricao_curta.md` | `BRIEF_AAAA_MM.md` |
| Tamanho | livre, com obrigação de objetividade | indicativo de uma página |

O **README.md** é tratado como BRIEF não-numerado, com função de vitrine permanente. BRIEFs numerados são produzidos quando algum marco específico justifica documento dedicado.

### 6.3 Estrutura recomendada

- **Situação atual** — o que está pronto, em prosa direta.
- **Valor entregue** — o que o projeto faz e por quê.
- **Próximo passo** — o que vem a seguir.
- **Risco principal** (opcional) — quando relevante.

---

## 7. DEC — Registro de Decisão

### 7.1 Definição e função

O DEC documenta **uma decisão tomada no projeto**, com suas alternativas, justificativa, consequências aceitas e critérios de reavaliação. É o tipo de documento mais importante para **rastreabilidade**: explica, em qualquer momento futuro, por que o projeto é como é.

O DEC opera sob dois princípios rigorosos:

- **Atomicidade** — cada DEC trata de uma única decisão.
- **Imutabilidade após aprovação** — um DEC aprovado não é editado. Decisões que mudam dão origem a um novo DEC, que substitui (`supersedes`) o anterior. O DEC anterior tem seu status alterado para `superseded`, mas seu conteúdo permanece intacto, e seu número nunca é reutilizado.

### 7.2 Quando produzir

Um DEC é produzido sempre que uma decisão de projeto:

- afeta o comportamento ou a arquitetura do sistema,
- envolve trade-off explícito entre alternativas, ou
- estabelece um compromisso que limitará escolhas futuras.

Decisões triviais (escolhas pontuais de implementação que não restringem nada) não justificam DEC.

### 7.3 Estrutura obrigatória

- **Contexto** — o problema que motiva a decisão, em um a dois parágrafos.
- **Decisão** — em uma frase acionável, o que se decidiu.
- **Alternativas consideradas** — pelo menos duas, com descrição honesta dos motivos pelos quais foram descartadas.
- **Consequências** — positivas, negativas e o que a decisão **não** resolve. A presença de uma seção dedicada às consequências negativas é parte essencial do tipo.
- **Critérios de reavaliação** — sob quais condições a decisão deve ser revisitada.

Uma DEC sem alternativas consideradas ou sem consequências negativas é tratada como incompleta.

---

## 8. Formato e versionamento

### 8.1 Markdown como formato originário

Todos os documentos da taxonomia são **escritos originariamente em Markdown**. Justificativas:

- **Texto puro versionável**: `diff` legível por commit.
- **Independência de ferramenta**: renderizado em qualquer lugar (GitHub, editores locais).
- **Conversão sob demanda**: `.docx` ou `.pdf` são gerados quando necessário, mas são **derivados**, não fonte.

A versão canônica de cada documento é o arquivo `.md`.

### 8.2 Convenção de nomes de arquivo

| Tipo | Padrão de nome | Exemplo |
|---|---|---|
| SPEC | `SPEC_NNN_descricao_curta.md` | `SPEC_001_Taxonomia_Documental.md` |
| REP | `REP_NNN_descricao_curta.md` | `REP_001_Conclusao_Camada1_HTML_CSS.md` |
| GUIDE | `GUIDE_NNN_descricao_curta.md` | `GUIDE_001_Subir_site_local.md` |
| BRIEF de marco | `BRIEF_NNN_descricao_curta.md` | `BRIEF_001_Lancamento_site_v1.md` |
| BRIEF de período | `BRIEF_AAAA_MM.md` | `BRIEF_2026_05.md` |
| DEC | `DEC_NNN_descricao_curta.md` | `DEC_001_Sem_Frameworks_Inicialmente.md` |

O número `NNN` é sequencial dentro de cada tipo e **nunca é reutilizado**. Documentos descartados ou substituídos mantêm seu número.

### 8.3 Estrutura de pastas

```
docs/
├── SPEC/           ← especificações técnicas
├── REP/            ← relatórios
├── GUIDE/          ← guias operacionais
├── BRIEF/          ← resumos executivos
├── DEC/            ← decisões registradas
│   └── INDEX_DEC.md
├── assets/         ← imagens e mídia
│   ├── shared/
│   ├── SPEC/ DEC/ REP/ GUIDE/ BRIEF/
└── logs/           ← logs arquivados de execuções relevantes
```

### 8.4 Cabeçalho YAML obrigatório

Todo documento da taxonomia abre com frontmatter:

```yaml
---
documento: <SIGLA-NNN ou SIGLA-AAAA-MM>
titulo: <Título do documento>
versao: <v1, v2, ...>            # opcional para BRIEF; admite vX.Y para protótipo
status: <proposto | aprovado | superseded | descartado>
data: <AAAA-MM-DD>
autor: <nome>
supersede: <SIGLA-NNN ou —>      # quando aplicável
referencia: <SIGLA-NNN ou —>     # quando aplicável
audiencia: <texto livre>          # opcional, recomendado para BRIEF
---
```

### 8.5 Commits e mensagens

**Conventional Commits**, com tipo `docs` e escopo correspondente ao tipo:

| Operação | Padrão de mensagem |
|---|---|
| Adicionar SPEC | `docs(spec): adiciona SPEC-NNN ...` |
| Adicionar REP | `docs(rep): adiciona REP-NNN ...` |
| Adicionar DEC | `docs(dec): adiciona DEC-NNN ...` |
| Adicionar GUIDE | `docs(guide): adiciona GUIDE-NNN ...` |
| Adicionar BRIEF | `docs(brief): adiciona BRIEF-NNN ...` |
| Substituir | `docs(SIGLA): supersede SIGLA-XXX por SIGLA-YYY` |
| Atualizar imagem | `docs(assets): adiciona <descrição> em <local>` |

Commits de **código** seguem outros tipos: `feat`, `fix`, `refactor`, `chore`, conforme convenção padrão.

---

## 9. Imagens e demais ativos

### 9.1 Localização

Todos os ativos visuais ficam em `docs/assets/<TIPO>/<numero>/`:

```
docs/assets/
├── shared/                   ← reaproveitados entre documentos
├── SPEC/003/                 ← vinculados à SPEC-003
├── DEC/001/
└── ...
```

Estrutura criada sob demanda. Subpastas numéricas só existem quando há ativos a colocar.

### 9.2 Nomes de arquivo

- **Minúsculas com underline** (`fluxo_dados.png`, não `FluxoDados.png`).
- **Descrição substantiva**, não numeração genérica (`diagrama_camadas.png`, não `imagem_01.png`).
- **Extensão em minúsculas**.

### 9.3 Formatos preferidos

- **PNG** para diagramas, screenshots.
- **SVG** para diagramas vetoriais editáveis.
- **JPG** apenas para fotografias.

### 9.4 Referência a partir do Markdown

```markdown
![Descrição clara da figura](../assets/SPEC/003/diagrama.png)
```

Texto `alt` deve ser significativo. `![](...)` ou `![imagem](...)` são desencorajados.

---

## 10. Índices

- **`docs/DEC/INDEX_DEC.md`** — **obrigatório** desde o início. A obrigatoriedade decorre da função de rastreabilidade do tipo: sem índice, decisões importantes podem se perder.
- **`docs/SPEC/INDEX_SPEC.md`** — recomendado a partir de ~10 SPECs. **Adotado desde o início neste projeto** dada a centralidade das SPECs de fundação.
- **`docs/GUIDE/INDEX_GUIDE.md`**, **`docs/REP/INDEX_REP.md`**, **`docs/BRIEF/INDEX_BRIEF.md`** — recomendados quando o tipo passar de ~10 peças.

---

## 11. Regras checáveis pelo skill de auditoria

Esta seção declara as regras concretas que um skill de auditoria pode verificar contra o estado real do projeto. Cada regra aponta para artefato verificável e tem severidade orientativa.

| ID | Regra | Onde verificar | Severidade |
|---|---|---|---|
| **R-TAX-01** | Todo `.md` em `docs/<TIPO>/` (exceto `INDEX_<TIPO>.md`) tem frontmatter YAML com campos: `documento`, `titulo`, `status`, `data`, `autor`. SPEC/GUIDE/REP/DEC também têm `versao`. | Parse do frontmatter | Alta |
| **R-TAX-02** | Nome de arquivo obedece o padrão da §8.2 por tipo. Sufixos de versão no nome (`_v1`, `_v2`) sinalizam divergência. | Listagem + regex | Alta |
| **R-TAX-03** | Numeração sequencial dentro de cada tipo, **sem reuso**. Número repetido sinaliza violação grave. | Cruzamento nome+frontmatter+status | Crítica |
| **R-TAX-04** | `status` ∈ {`proposto`, `aprovado`, `superseded`, `descartado`}. Variações de grafia sinalizam divergência leve. | Parse do `status` | Média |
| **R-TAX-05** | Documento `superseded` é referenciado por `supersede:` em ao menos um documento ativo. | Cruzamento de `supersede:` | Alta |
| **R-TAX-06** | `INDEX_DEC.md` existe e lista todas as DECs presentes. | Cruzamento físico × INDEX | Média |
| **R-TAX-07** | Estrutura de pastas conforme §8.3 está íntegra. | Listagem de `docs/` | Baixa |
| **R-TAX-08** | DEC com status `aprovado` contém as 5 seções obrigatórias da §7.3. | Parse estrutural | Alta |
| **R-TAX-09** | Imagens referenciadas existem fisicamente; `alt` é significativo. | Parse dos links | Média |

---

## 12. Reflexões sobre o método documental

### 12.1 Documentação como projeto, não como produto

A documentação não é o que se produz **depois** do trabalho técnico para registrá-lo. Ela é parte do trabalho técnico. Uma decisão registrada em DEC ao ser tomada **economiza** retrabalho futuro; uma SPEC produzida ao final de um componente **estabiliza** o entendimento.

### 12.2 O custo da ausência é maior que o custo da presença

Toda taxonomia documental tem custo — o tempo gasto em escrever e a disciplina de manter convenções. Esse custo é visível e imediato. O custo da ausência, por outro lado, é invisível e diferido: aparece meses depois, quando uma decisão precisa ser revisitada e ninguém lembra das alternativas.

### 12.3 Honestidade como requisito documental

A presença de seções como "consequências negativas" em DECs e "limitações conhecidas" em SPECs não é ornamento. É a tradução, em forma documental, de um princípio: um sistema bem documentado é um sistema cujos limites são conhecidos.

### 12.4 Adaptação ao contexto de projeto pessoal de aprendizado

Em projeto pessoal, o autor acumula vários papéis (autor, peer-reviewer, avaliador). A taxonomia continua valendo, mas o fluxo de aprovação descrito na SPEC-003 é simplificado: aprovação ativa do autor sobre si mesmo, com a IA atuando como co-autor sob controles declarados.

A função primária da taxonomia neste projeto é **didática e mnemônica**: forçar o autor a separar "o que é" (SPEC) de "o que aconteceu" (REP) de "por que foi feito assim" (DEC) é, em si, um exercício de pensamento estruturado sobre o próprio trabalho de aprendizado.

---

## 13. Histórico

| Data | Evento |
|---|---|
| 2026-05-13 | SPEC-001 v1 produzida em status `aprovado`. Adaptada da SPEC-001 v3 do projeto `baur_clientes_plan` (Bruno Serminaro, 2026-05-12), simplificada pro contexto de projeto pessoal de aprendizado. |

---

*Fim do documento.*
