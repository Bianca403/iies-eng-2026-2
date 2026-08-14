# Guia rápido de Markdown

Markdown é uma forma simples de formatar texto usando símbolos comuns. Você escreve texto puro e ele é renderizado como um documento organizado — com títulos, listas, tabelas e destaques.

É o formato padrão de documentação no GitHub, no VS Code e nos principais ambientes de desenvolvimento.

> **Por que agentes de IA adoram Markdown?**
> Ferramentas como ChatGPT, Claude e Copilot respondem naturalmente em Markdown. Isso porque a estrutura clara — títulos, listas, blocos de código — ajuda o modelo a organizar o raciocínio e facilita a leitura humana ao mesmo tempo. Saber Markdown é saber falar a língua dessas ferramentas.

---

## Títulos

Use `#` para criar títulos. Quanto mais `#`, menor o título.

```markdown
# Título principal
## Seção
### Subseção
```

---

## Ênfase

```markdown
**negrito**
*itálico*
~~tachado~~
```

Resultado: **negrito**, *itálico*, ~~tachado~~

---

## Listas

**Lista simples:**
```markdown
- Maçã
- Banana
- Laranja
```

**Lista numerada:**
```markdown
1. Primeiro passo
2. Segundo passo
3. Terceiro passo
```

---

## Links e imagens

```markdown
[texto do link](https://github.com)

![texto alternativo](https://url-da-imagem.png)
```

---

## Citação

```markdown
> "Uma citação importante."
```

Resultado:

> "Uma citação importante."

---

## Código

Código inline: use acento grave `` ` ``

```markdown
Use a função `print()` para exibir valores.
```

Bloco de código: use três acentos graves e o nome da linguagem

````markdown
```python
nome = "João"
print(f"Olá, {nome}!")
```
````

---

## Tabela

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|---|---|---|
| dado A | dado B | dado C |
| dado D | dado E | dado F |
```

Resultado:

| Coluna 1 | Coluna 2 | Coluna 3 |
|---|---|---|
| dado A | dado B | dado C |
| dado D | dado E | dado F |

---

## Linha divisória

```markdown
---
```

---

## Resumo

| Elemento | Sintaxe |
|---|---|
| Título | `# Texto` |
| Negrito | `**texto**` |
| Itálico | `*texto*` |
| Lista | `- item` |
| Link | `[label](url)` |
| Citação | `> texto` |
| Código inline | `` `codigo` `` |
| Tabela | `\| col \| col \|` |
| Divisória | `---` |

---

> Dica: no vscode.dev, clique com o botão direito no arquivo `.md` e selecione **Open Preview** para ver o resultado formatado em tempo real.