from __future__ import annotations

from typing import Any

from ibisml.core import Transform

import ibis.expr.types as ir


__all__ = ("FillNA",)


class FillNA(Transform):
    def __init__(self, fill_values: dict[str, Any]):
        self.fill_values = fill_values

    def transform(self, table: ir.Table) -> ir.Table:
        return table.mutate(
            [table[c].coalesce(v).name(c) for c, v in self.fill_values.items()]
        )
