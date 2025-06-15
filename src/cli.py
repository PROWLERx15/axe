import typer
from src.commands.calldata.calldata import calldata_app
from src.commands.constants.constants_command import constants_app

app = typer.Typer(
    help="Axe is a python based EVM CLI Tool for working with blockchain")

app.add_typer(calldata_app, name="calldata")
app.add_typer(constants_app,name="constants")