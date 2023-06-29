import numpy as np
from typing import Optional


class Data:
    def __init__(self, x: np.ndarray, y: np.ndarray, label: Optional[str] = None):
        self.x = x
        self.y = y
        self.label = label

    x: np.ndarray
    y: np.ndarray
    label: Optional[str]


class Data3D:
    def __init__(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,  label: Optional[str] = None):
        self.x = x
        self.y = y
        self.z = z
        self.label = label

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    label: Optional[str]
