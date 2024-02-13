from typing import Annotated, TypeAlias

from pydantic import BaseModel, ConfigDict, Field

PositiveFloatList: TypeAlias = list[Annotated[float, Field(ge=0)]]


class OilData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    q_liq: PositiveFloatList = Field(default_factory=list)
    p_wf: PositiveFloatList = Field(default_factory=list)
