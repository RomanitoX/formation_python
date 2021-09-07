import typer
from typing import Optional
from pathlib import Path

from typer.main import Typer

app = typer.Typer()


@app.command('run')
def main(ext: str,
         directory: Optional[Path] = typer.Argument(
             None, help="Folder to search inside"),
         delete: bool = typer.Option(False, help="Delete found files.")):
    """
    Show all the files corresponding to the given extension
    """
    if not directory:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(
            f"The folder {directory} doesn't exists.", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{ext}")

    if delete:
        typer.confirm(
            "Are you really sure you want to delete all founded files ?", abort=True)

        for file in files:
            file.unlink()
            typer.secho(f"Deleting file {file}", fg=typer.colors.RED)

    else:
        print(files)
        if files != 0:
            typer.secho(f"Founded files for extension '{ext}' in path '{directory}': ",
                        bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_WHITE)
            for file in files:
                typer.echo(file)


@app.command()
def search(ext: str):
    main(ext=ext, directory=None, delete=False)


@app.command()
def delete(ext: str):
    main(ext=ext, directory=None, delete=True)


if __name__ == "__main__":
    app()
