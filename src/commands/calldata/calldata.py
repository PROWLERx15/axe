import typer
import src.utils.calldata_decoder as calldata_decoder
import json
from pathlib import Path

calldata_app = typer.Typer(help="Work with calldata")

@calldata_app.command("decode", help="Decode calldata using transaction, abi or address")
def decode_calldata(
        tx_hash: str = typer.Option(None, "--tx", help="Transaction hash"),
        abi_file: str = typer.Option(None, "--abi", help="Contract ABI"),
        address: str = typer.Option(None, "--address", help="Contract address"),
        calldata: str = typer.Option(None, "--calldata", help="Raw Calldata"),
        chain: str = typer.Option(..., "--chain", help="Chain name")):

    if sum([bool(tx_hash),bool(abi_file),bool(address)]) !=1:
        typer.echo("Please provide exactly one argument: --tx, --abi, or --address", err=True)                                                  
        raise typer.Exit(code=1)
    
    if tx_hash:
        try:
            func_obj, params = calldata_decoder.decode_using_transaction_hash(tx_hash, chain)
            typer.echo("\nDecoded Calldata using Transaction Hash\n")
            typer.echo(func_obj)
            typer.echo(json.dumps(params,indent=2))
            return
        except RuntimeError as e:
            typer.echo(e,err=True)
            raise typer.Exit(code=1)



    elif abi_file:
        if not calldata:
            raise typer.BadParameter("--calldata is required when using --abi")
        
        try:
            abi_file = Path(abi_file).expanduser().resolve()
            with abi_file.open("r") as f:
                abi = json.load(f)
            func_obj, params = calldata_decoder.decode_using_abi(calldata, abi, chain)
            typer.echo("\nDecoded Calldata using Contract ABI\n")
            typer.echo(func_obj)
            typer.echo(json.dumps(params,indent=2))
            return
        except  RuntimeError as e:
            typer.echo(e,err=True)
            raise typer.Exit(code=1)

    elif address:
        if not calldata:
            raise typer.BadParameter("--calldata is required when using --address")
        
        try:
            func_obj, params = calldata_decoder.decode_using_address(calldata, address, chain)
            typer.echo("\nDecoded Calldata using Contract Address\n")
            typer.echo(func_obj)
            typer.echo(json.dumps(params,indent=2))
            return
        except  RuntimeError as e:
            typer.echo(e,err=True)
            raise typer.Exit(code=1)


@calldata_app.command("encode", help="Encode calldata")
def encode(func: str = typer.Option(..., "--function", help="Function name")):
    typer.echo(f"Encoding for function {func} coming soon...")
