# Agent skills

[![skills.sh](https://skills.sh/b/caiofsr/skills)](https://skills.sh/caiofsr/skills)

Skills para agentes de código.

## Disponíveis

| Skill | O que faz |
| --- | --- |
| [soft-icons](./soft-icons/SKILL.md) | Cria ícones Soft Isometric 3D em SVG ou React/TypeScript, com geometria, cores e iluminação consistentes. |

## Instalação

Com Node.js e npm instalados, execute na pasta do projeto em que deseja usar a skill:

```sh
npx skills add caiofsr/skills --skill soft-icons
```

Escolha o agente no instalador. Para disponibilizar a skill em todos os seus projetos, acrescente `--global`.

Veja as opções na [documentação do instalador](https://github.com/vercel-labs/skills#readme).

## Uso

Peça ao agente algo como:

> Crie um ícone de upload em SVG no estilo Soft Isometric 3D.

A descrição permite que agentes compatíveis selecionem a skill sem invocação explícita. Ela também pode ser chamada pelo nome `soft-icons`.
