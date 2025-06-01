from pydantic import validate_call, Field
from typing import Annotated


@validate_call
def thoughtful_package_sort(
    width: Annotated[float, Field(gt=0)],
    height: Annotated[float, Field(gt=0)],
    length: Annotated[float, Field(gt=0)],
    mass: Annotated[float, Field(gt=0)],
):
    """
    Sort packages into STANDARD, SPECIAL, or REJECTED.
    Criteria:
    - A bulky package either:
        - volume (Width x Height x Length) is greater than or equal to 1,000,000 cm3
        - or, when one of its dimensions is greater or equal to 150 cm.
    - A heavy package mass is greater or equal to 20 kg.

    Args:
        width: float in cm
        height: float in cm
        length: float in cm
        mass: float in kg

    Returns on of the following strings:
    - STANDARD: not bulky or heavy packages.
    - SPECIAL: either heavy or bulky packages.
    - REJECTED: heavy and bulky packages.
    """

    bulky = False
    heavy = False

    if any(
        [width * height * length >= 1000000, width >= 150, height >= 150, length >= 150]
    ):
        bulky = True
    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
