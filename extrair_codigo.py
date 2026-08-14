import json
import sys
from pathlib import Path


def extrair_codigo(tarefa: str):
    """
    Extrai o código Python de todos os notebooks de entrega de uma tarefa
    e salva como codigo_extraido.py em cada pasta de aluno.

    Uso:
        python extrair_codigo.py 02-variaveis-e-prints
    """
    entregas_path = Path("tarefas") / tarefa / "entregas"

    if not entregas_path.exists():
        print(f"Pasta de entregas não encontrada: {entregas_path}")
        return

    notebooks = list(entregas_path.rglob("notebook.ipynb"))

    if not notebooks:
        print(f"Nenhum notebook encontrado em {entregas_path}")
        return

    for nb_path in notebooks:
        try:
            cells = json.loads(nb_path.read_text(encoding="utf-8"))["cells"]
            codigo = "\n\n".join(
                "".join(c["source"])
                for c in cells
                if c["cell_type"] == "code" and "".join(c["source"]).strip()
            )

            if not codigo.strip():
                print(f"  sem código: {nb_path}")
                continue

            saida = nb_path.parent / "codigo_extraido.py"
            saida.write_text(codigo, encoding="utf-8")
            print(f"  extraído: {saida}")

        except Exception as e:
            print(f"  erro em {nb_path}: {e}")

    print(f"\nExtração concluída. Agora rode:")
    print(f"  dolos run -l python tarefas/{tarefa}/entregas/*/codigo_extraido.py")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python extrair_codigo.py <nome-da-tarefa>")
        print("Exemplo: python extrair_codigo.py 02-variaveis-e-prints")
        sys.exit(1)

    extrair_codigo(sys.argv[1])
