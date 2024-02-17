"""
    QSS - Estilos do QT for Python
    https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
    Dark Theme
    https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
"""
import qdarktheme
from variables import (PRIMARY_COLOR, PRIMARY_COLOR_DARKEST,
                       PRIMERY_COLOR_DARKER)

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {PRIMERY_COLOR_DARKER};
    }}
    PushButto[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {PRIMARY_COLOR_DARKEST};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}"
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            }
        },
        additional_qss=qss
    )
