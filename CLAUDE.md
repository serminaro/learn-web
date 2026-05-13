# CLAUDE.md — instruções pra IA neste repositório

> Este arquivo é lido automaticamente pelo Claude Code quando você inicia uma sessão dentro de `learn-web/`. Define o que a IA pode e não pode fazer, como deve estruturar suas contribuições e como deve se comportar ao editar artefatos do projeto.
>
> Este arquivo **complementa**, mas não substitui, a [SPEC-003 (Contrato de Responsabilidade)](docs/SPEC/SPEC_003_Contrato_Responsabilidade.md), que é a fonte canônica das regras de governança.

---

## 1. Antes de qualquer ação

Ao entrar neste repositório, **ler primeiro**:

1. **[SPEC-001](docs/SPEC/SPEC_001_Taxonomia_Documental.md)** — taxonomia documental do projeto. Você precisa saber o que é SPEC, DEC, REP, GUIDE, BRIEF antes de propor qualquer artefato.
2. **[SPEC-002](docs/SPEC/SPEC_002_Fundacao_learn_web.md)** — o que o projeto se compromete a entregar e em quantas camadas. Saber em que camada o projeto está antes de propor código.
3. **[SPEC-003](docs/SPEC/SPEC_003_Contrato_Responsabilidade.md)** — **leitura obrigatória**. Define o que você pode e não pode fazer neste projeto.

**Se o usuário pedir algo que conflita com a SPEC-003 §4, recuse e cite a regra.** A recusa é parte do contrato, não desobediência.

---

## 2. O que você pode fazer sem perguntar

- Ler qualquer arquivo do repositório.
- Listar pastas, rodar `git status`, `git log`, `git diff`, `gh repo view`.
- Propor mudanças com diff claro, esperando aprovação.
- Rascunhar SPECs, DECs, GUIDEs, REPs, BRIEFs em status `proposto`.
- Criar arquivos novos em `src/` quando explicitamente solicitado.
- Rodar comandos não-destrutivos dentro de `~/Projetos/learn-web/`.

---

## 3. O que exige confirmação explícita antes

- `git commit`, `git push`, `gh pr create` — qualquer operação que altere o repo remoto ou o histórico local.
- `git add` em massa (use `git add <arquivo>` específico).
- Mudança no campo `status` de qualquer artefato (de `proposto` pra `aprovado` é prerrogativa do autor).
- Criação de DEC — você pode rascunhar, mas a DEC só é aprovada pelo autor.
- Modificação de SPEC com status `aprovado`. Se algo precisa mudar, propor **nova versão** (v2) em status `proposto`.
- Instalação de dependências (`composer require`, `npm install`).

---

## 4. O que você não pode fazer

- **`sudo` qualquer coisa.** Operações que exijam elevação são feitas pelo autor.
- **Versionar segredos.** `.env`, tokens, credenciais nunca são adicionados ao git. Em dúvida, pergunte.
- **Aprovar artefatos.** A mudança `proposto` → `aprovado` é exclusivamente do autor.
- **Modificar SPECs aprovadas in-place.** Sempre via nova versão.
- **Adotar frameworks fora do escopo declarado em SPEC-002 §3.2.** Introduzir React, Vue, Laravel, jQuery sem DEC autorizando é violação direta.
- **Sair do diretório `~/Projetos/learn-web/`** sem motivo declarado pelo autor.

---

## 5. Como propor mudanças

### 5.1 Para artefatos documentais

- Sempre criar com `status: proposto` no frontmatter.
- Anexar entrada de histórico no fim do documento: `2026-MM-DD | <SIGLA-NNN> v1 rascunhada pela IA, aguarda revisão do autor.`
- Avisar o autor que o documento está pronto para revisão e indicar o caminho.
- Não mover para `aprovado` por iniciativa própria.

### 5.2 Para código em `src/`

- Seguir as restrições técnicas da SPEC-002 §3.2 (vanilla, sem frameworks).
- Em camadas C3+: **todo output de dado externo passa por escape** (`htmlspecialchars` em PHP), **toda query usa prepared statement**. Violar essas regras é severidade crítica (R-FUN-05).
- Estrutura de pastas em `src/` evolui com o projeto; quando a estrutura mudar materialmente, propor DEC.

### 5.3 Para commits

Conventional Commits, conforme SPEC-001 §8.5:

```
docs(spec): adiciona SPEC-004 estrutura do src
docs(dec): adiciona DEC-001 escolha do motor de banco
feat(c1): adiciona página inicial em html semantico
fix(c2): corrige listener duplicado no formulario
chore: atualiza .gitignore com vendor/
```

Commits da IA são produzidos com co-autoria explícita:

```
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## 6. Padrão de comunicação esperado

Quando o autor te pedir algo:

- **Explique antes de fazer**, especialmente em decisões que envolvem trade-off. O autor tem preferência declarada por entender antes de aplicar (cf. memória `feedback-explain-before-install`).
- **Cite documento + seção** quando uma regra do projeto justifica sua escolha. Ex.: "Vou criar em status `proposto` conforme SPEC-003 §4.1."
- **Seja conciso.** Respostas longas com cabeçalhos só quando justificadas. Resposta direta é o default.
- **Não invente atalhos** que economizem tempo às custas do regime documental. A velocidade vem do código, não do encurtamento de SPECs.

---

## 7. Ferramentas de ambiente

O autor opera neste projeto em:

- **Terminal**: Kitty 0.32 com Tokyo Night e JetBrainsMono Nerd Font.
- **Editor**: Neovim 0.12.2 com kickstart.nvim, LSPs ativos (intelephense, html-lsp, css-lsp, typescript-language-server, eslint-lsp, gopls, lua-language-server, prettier, stylua).
- **Servidor local**: nginx 1.24 + php-fpm 8.3 servindo `localhost:8080`.
- **Versionamento**: git + GitHub (`serminaro/learn-web`, público).

Quando propor comandos, assumir esse ambiente.

---

## 8. Se você está em dúvida

**Pergunte antes de fazer.** Em projeto pessoal, o autor prefere ser interrompido a ter que desfazer trabalho extrapolado. Em particular, pergunte sempre que:

- Houver dúvida se uma mudança extrapola o escopo declarado.
- O usuário pedir algo que aparenta conflitar com uma SPEC.
- Você não souber em qual tipo (SPEC, DEC, GUIDE, REP, BRIEF) um artefato proposto deve cair.
- Você precisar de informação fora do repositório (ex.: dados de outros projetos, repositórios externos).

---

*Última atualização: 2026-05-13.*
