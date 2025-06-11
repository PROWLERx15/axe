import typer
from src.commands.calldata.calldata import calldata_app

app = typer.Typer(
    help="Axe is a python based EVM CLI Tool for working with blockchain")

app.add_typer(calldata_app, name="calldata")
