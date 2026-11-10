from pathlib import Path


def ler_arquivo(caminho):
    return Path(caminho).read_text(
        encoding="utf-8"
    )

