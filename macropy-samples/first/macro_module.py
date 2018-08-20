from macropy.core.macros import Macros

macros = Macros()

@macros.expr #pylint: disable=E1101
def expand(tree, **kw):
    return tree
