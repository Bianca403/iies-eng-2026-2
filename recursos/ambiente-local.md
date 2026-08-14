# Configurando o ambiente no seu computador

Este guia é opcional — todas as tarefas podem ser feitas pelo navegador usando `vscode.dev`. Mas se quiser trabalhar no seu próprio computador, siga os passos abaixo.

---

## O que instalar

### 1. Python

- Download: https://www.python.org/downloads
- Baixe a versão mais recente (3.12 ou superior)

> ⚠️ **Passo crítico no Windows:** na primeira tela do instalador, marque obrigatoriamente a opção **"Add Python to PATH"** antes de clicar em Install. Se esquecer, terá que reinstalar.

![Add Python to PATH](https://docs.python.org/3/_images/win_installer.png)

Após instalar, abra o terminal e confirme:

```bash
python --version
```

Deve aparecer algo como `Python 3.12.x`. Se aparecer erro, o PATH não foi configurado corretamente — reinstale marcando a opção.

**Instale também as bibliotecas essenciais:**

```bash
pip install notebook numpy pandas matplotlib
```

---

### 2. Git

O Git é o sistema de controle de versão que faz tudo funcionar. Instale primeiro.

- Download: https://git-scm.com/downloads
- Escolha o instalador para o seu sistema operacional
- Durante a instalação, mantenha todas as opções padrão

Após instalar, abra o terminal e configure seu nome e e-mail:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

> Use o mesmo e-mail da sua conta GitHub.

---

### 3. VS Code

Editor de código gratuito da Microsoft. Roda em Windows, Mac e Linux.

- Download: https://code.visualstudio.com
- Instale normalmente
- Na instalação no Windows, marque a opção **"Adicionar ao PATH"**

**Extensões recomendadas** (instale pelo menu Extensions no VS Code):

| Extensão | Para que serve |
|---|---|
| Python | Suporte completo à linguagem |
| Jupyter | Rodar notebooks `.ipynb` direto no VS Code |
| GitHub Pull Requests | Ver e gerenciar PRs sem sair do editor |
| Markdown Preview Enhanced | Visualizar arquivos `.md` formatados |

---

### 4. GitHub Desktop

Interface visual para Git — sem precisar usar o terminal. Ótimo para quem está começando.

- Download: https://desktop.github.com
- Faça login com sua conta GitHub após instalar

Com o GitHub Desktop você consegue:
- Clonar repositórios com um clique
- Criar e trocar de branch visualmente
- Fazer commit e push sem digitar comandos
- Ver o histórico de alterações

---

## Verificando se tudo está funcionando

Abra o terminal (Prompt de Comando no Windows ou Terminal no Mac/Linux) e rode cada comando abaixo. Todos devem retornar uma versão sem erro:

```bash
python --version
```
```bash
pip --version
```
```bash
git --version
```

Se algum retornar `comando não reconhecido` ou `not found`, o programa não está no PATH. Reinstale marcando a opção de PATH ou consulte documentaçãso oficial - IA - professor.

---

## Fluxo no computador próprio

```
GitHub Desktop → clona o repo
      ↓
cria branch no GitHub Desktop
      ↓
abre no VS Code (botão "Open in VS Code")
      ↓
edita o notebook ou arquivo
      ↓
volta ao GitHub Desktop → commit → push
      ↓
abre PR no GitHub (navegador)
```

---

## Para aprender mais

### Git e GitHub

- [Git e GitHub para iniciantes — Rafaella Ballerini](https://www.youtube.com/watch?v=DqTITcMq68k)
- [Curso de Git e GitHub — Curso em Vídeo](https://www.youtube.com/playlist?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA)
- [Documentação oficial do Git (PT-BR)](https://git-scm.com/book/pt-br/v2)

### VS Code

- [VS Code em 20 minutos](https://www.youtube.com/watch?v=uxln1hT_Ev4)
- [Documentação oficial do VS Code](https://code.visualstudio.com/docs)
- [VS Code Filipe Deschamps](https://www.youtube.com/watch?v=FCC2GbStmfc)

### GitHub Desktop

- [GitHub Desktop — documentação oficial](https://docs.github.com/pt/desktop)

### Markdown

- [Markdown Guide](https://www.markdownguide.org) — referência completa em inglês
- Consulte também: `recursos/guia-markdown.md` neste repositório