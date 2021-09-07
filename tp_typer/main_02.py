import typer
import time

app = typer.Typer()


def main(
        delete: bool = typer.Option(False, help="Mes couillmes"),
        ext: str = typer.Argument("txt", help="Extension à chercher")):

    ext = typer.prompt("Quelle extension souhaitez-vous chercher ?")

    styled_ext = typer.style(ext, bold=True, fg=typer.colors.RED)

    typer.echo(
        f"Recherche des fichiers avec l'extension {styled_ext} [txt] by default")

    if delete:
        typer.confirm(
            "Souhaitez vous vraiment supprimer les fichiers ?", abort=True)

    typer.secho("Suppresion des fichiers...", fg='red')

    data = range(100)
    with typer.progressbar(data) as progress:
        for data in progress:
            time.sleep(0.05)


@app.command("search")
def search_py():
    main(delete=False, ext="py")


@app.command("delete")
def delete_py():
    main(delete=True, ext="py")


if __name__ == "__main__":
    app()
