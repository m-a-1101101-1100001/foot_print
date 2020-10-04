
from flask import Blueprint
from usecase.PairsUsecase import PairsUsecase

bp = Blueprint('pairs', __name__, cli_group=None)


@bp.cli.command()
def pairs():
    """
    ペアーズの自動足跡コマンド
    """
    pairs_usecase = PairsUsecase()
    pairs_usecase.invoke()
