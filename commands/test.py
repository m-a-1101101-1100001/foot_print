from flask import Blueprint
bp = Blueprint('test', __name__, cli_group=None)

@bp.cli.command()
def test():
    print( "ああああああああああああああ")
