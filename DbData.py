# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import cast

from dataclasses_json import dataclass_json

import adsk.core
import adsk.fusion

_app = adsk.core.Application.get()
_design: adsk.fusion.Design = cast(adsk.fusion.Design, _app.activeProduct)


@dataclass_json
@dataclass
class DbParams:
    """Dataclass - Holds add-in instance setup values"""

    toolDiaStr: str = "0.25 in"
    dbType: str = "Normal Dogbone"
    fromTop: bool = True
    toolDiaOffsetStr: str = "0 cm"

    mortiseType: bool = False
    longSide: bool = True

    minimalPercent: float = 10.0

    angleDetectionGroup: bool = False
    acuteAngle: bool = False
    obtuseAngle: bool = False
    minAngleLimit: float = 89.0
    maxAngleLimit: float = 91.0

    # parametric: bool = False
    expandModeGroup: bool = True
    expandSettingsGroup: bool = True
    logging: int = 0
    benchmark: bool = False

    @property
    def toolDia(self):
        return _design.unitsManager.evaluateExpression(self.toolDiaStr)

    @property
    def toolDiaOffset(self):
        return _design.unitsManager.evaluateExpression(self.toolDiaOffsetStr)
