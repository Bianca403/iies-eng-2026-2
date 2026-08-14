# Tutorial: criar branch, trabalhar e fazer commit no vscode.dev

> Siga este tutorial na sua primeira entrega. A partir da segunda, o fluxo já vai ser natural.

---

## Passo 1 — Abrir o repositório

Acesse no navegador:

```
https://vscode.dev/github/eduardo-arcade-metrics/iies-eng-2026-2
```

Na primeira vez, clique em **Entrar com GitHub** e autorize o acesso.

> 💡 Salve esse link nos favoritos — você vai usar em toda aula.

---

## Passo 2 — Criar sua branch

No canto inferior esquerdo da tela aparece o nome **main**. Clique nele.

No menu que abre, clique em **Criar novo branch...** e digite o nome seguindo o padrão:

```
tarefa-01/seu-nome
```

Exemplo: `tarefa-01/joao-silva`

> ⚠️ Use sempre letras minúsculas e hífen. Sem espaços ou acentos.

---

## Passo 3 — Abrir e editar o notebook

No painel lateral esquerdo (Explorer), navegue até a pasta da tarefa e abra o arquivo `notebook.ipynb`.

Complete as células indicadas. O VS Code Web renderiza notebooks Jupyter nativamente, sem instalar nada.

> 💡 Para rodar o notebook com GPU, abra-o no Colab: clique em **Open in Colab** no topo do notebook.

---

## Passo 4 — Fazer o commit

Clique no ícone de **Source Control** na barra lateral (ícone de ramificação) ou pressione `Ctrl+Shift+G`.

Os arquivos modificados aparecem em **Changes**. Clique no **+** ao lado do arquivo para adicioná-lo ao stage.

Digite uma mensagem descritiva no campo de texto:

```
tarefa-01: resolução joao-silva
```

Clique em **Commit & Push**. O arquivo sobe direto para o GitHub na sua branch.

> ⚠️ Nunca commite na branch `main` — ela está protegida e o push será bloqueado.

---

## Passo 5 — Abrir o Pull Request

Após o push, acesse o repositório no GitHub:

```
https://github.com/eduardo-arcade-metrics/iies-eng-2026-2
```

Um banner amarelo aparece no topo:

> **tarefa-01/joao-silva** had recent pushes — **Compare & pull request**

Clique nele, preencha o formulário de entrega e clique em **Create pull request**.

O professor vai revisar, comentar e aprovar diretamente na PR.

> 💡 Dúvidas depois do envio? Comente na própria PR — o professor responde lá.

---

## Resumo do fluxo

```
vscode.dev → cria branch → edita notebook → commit & push → abre PR no GitHub
```

---

## Problemas comuns

| Situação | O que fazer |
|---|---|
| Não consigo fazer login | Verifique se está logado no GitHub no navegador |
| Push bloqueado | Você está na branch `main` — crie uma branch antes |
| Não aparece o banner de PR | Acesse a aba **Pull requests** no GitHub e clique em **New pull request** |
| Esqueci de criar a branch antes de editar | Crie a branch agora — as alterações não salvas acompanham |