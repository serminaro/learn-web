#!/usr/bin/env python3
"""
================================================================================
bootstrap_estrutura.py
================================================================================
Cria a estrutura de pastas do repositório `learn-web`, conforme a taxonomia
SERMI definida pelo autor (SPEC-001).

Princípios:
    - Idempotente: rodar várias vezes não quebra.
    - Não-destrutivo: arquivos existentes nunca são sobrescritos.
    - Sem dependências externas: só biblioteca-padrão do Python.
    - Verboso: imprime o que está fazendo, com marcadores claros.

Uso:
    # Da raiz do repositório (mesma pasta deste script):
    python bootstrap_estrutura.py

    # Ver o que seria criado, sem criar:
    python bootstrap_estrutura.py --dry-run

    # Criar em outro caminho (útil para teste):
    python bootstrap_estrutura.py --raiz /tmp/teste

Requisitos:
    Python >= 3.8 (biblioteca-padrão apenas)
================================================================================
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime


# ==============================================================================
# CONFIGURAÇÃO — pastas previstas pela SPEC-001 §8.3
# ==============================================================================

PASTAS = [
    "docs/SPEC",
    "docs/DEC",
    "docs/GUIDE",
    "docs/REP",
    "docs/BRIEF",
    "docs/assets/shared",
    "docs/assets/SPEC",
    "docs/assets/DEC",
    "docs/assets/GUIDE",
    "docs/assets/REP",
    "docs/assets/BRIEF",
    "docs/logs",
    "src",
]

GITKEEP_EM = [
    "docs/DEC",
    "docs/GUIDE",
    "docs/REP",
    "docs/BRIEF",
    "docs/assets/shared",
    "docs/assets/SPEC",
    "docs/assets/DEC",
    "docs/assets/GUIDE",
    "docs/assets/REP",
    "docs/assets/BRIEF",
    "docs/logs",
    "src",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold idempotente da estrutura learn-web.")
    parser.add_argument("--dry-run", action="store_true", help="Não cria nada; só imprime o que faria.")
    parser.add_argument("--raiz", default=".", help="Diretório-raiz onde criar a estrutura (default: cwd).")
    args = parser.parse_args()

    raiz = Path(args.raiz).resolve()
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{agora}] bootstrap_estrutura — raiz: {raiz}")
    print(f"[{agora}] dry-run: {args.dry_run}")
    print()

    criados = 0
    pulados = 0

    for rel in PASTAS:
        alvo = raiz / rel
        if alvo.exists():
            print(f"  • já existe   : {rel}")
            pulados += 1
        else:
            print(f"  + criar pasta : {rel}")
            if not args.dry_run:
                alvo.mkdir(parents=True, exist_ok=True)
            criados += 1

    print()
    for rel in GITKEEP_EM:
        gk = raiz / rel / ".gitkeep"
        if gk.exists():
            print(f"  • já existe   : {rel}/.gitkeep")
            pulados += 1
        else:
            print(f"  + criar .gitkeep: {rel}/.gitkeep")
            if not args.dry_run:
                gk.touch()
            criados += 1

    print()
    print(f"Resumo: {criados} criado(s), {pulados} pulado(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
