"""Easter-egg shim over :mod:`lynx_investor_core.easter`.

Binds industrials labels and fortune quotes so call sites stay
unchanged.  Also re-exports the legacy constants (LYNX_ASCII, WOLF_ASCII,
BULL_ASCII, PICKAXE_ASCII, FORTUNE_QUOTES, ROCKET_ASCII) for callers that
reference them directly (e.g. the Textual TUI).
"""

from __future__ import annotations

from lynx_investor_core import easter as _core_easter
from lynx_investor_core.easter import (  # noqa: F401
    BULL_ASCII,
    GENERIC_FORTUNES,
    ROCKET_ASCII,
    WOLF_ASCII,
)

_INDUSTRIAL_FORTUNES = (
    '"Quality is never an accident; it is always the result of intelligent effort." \u2014 John Ruskin',
    '"The greatest waste of resources is not using the ones you have." \u2014 Peter Drucker',
    '"If you can\'t describe what you are doing as a process, you don\'t know what you\'re doing." \u2014 W. Edwards Deming',
    '"In the long run, backlog is the only inventory that matters." \u2014 Industrial-sector proverb',
    '"Every operating ratio point compounds for decades." \u2014 Class I railroad proverb',
)

FORTUNE_QUOTES = tuple(GENERIC_FORTUNES) + _INDUSTRIAL_FORTUNES

_EGG = _core_easter.AgentEasterEgg(
    label="Industrials Analysis",
    sublabel="Industrials Research",
    banner_prog="lynx-industrials",
    extra_fortunes=_INDUSTRIAL_FORTUNES,
)

# Pre-rendered ASCII variants (legacy callers that import these directly).
LYNX_ASCII = _core_easter._lynx_ascii(_EGG.label)
PICKAXE_ASCII = _core_easter._pickaxe_ascii(_EGG.sublabel)


def rich_matrix(console, duration: float = 3.0) -> None:
    _core_easter.rich_matrix(console, duration=duration)


def rich_fortune(console) -> None:
    _core_easter.rich_fortune(console, _EGG)


def rich_rocket(console) -> None:
    _core_easter.rich_rocket(console)


def rich_lynx(console) -> None:
    _core_easter.rich_lynx(console, _EGG)


def tk_fireworks(root) -> None:
    _core_easter.tk_fireworks(root, _EGG)


def tk_rainbow_title(root, count: int = 20) -> None:
    _core_easter.tk_rainbow_title(root, _EGG, count=count)
