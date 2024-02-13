from typing import Annotated, Self, TypeAlias

from pydantic import BaseModel, ConfigDict, Field

PositiveFloat: TypeAlias = Annotated[float, Field(ge=0)]


class Point(BaseModel):
    q_liq: PositiveFloat
    p_wf: PositiveFloat

    model_config = ConfigDict(frozen=True)

    def __eq__(self, other: Self) -> bool:
        result = False
        if self.q_liq == other.q_liq and self.p_wf == other.p_wf:
            result = True
        return result
