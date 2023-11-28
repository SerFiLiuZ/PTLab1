# -*- coding: utf-8 -*-
from Types import DataType


class OneHundred:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str:
        for student, subjects in self.data.items():
            all_100 = all(score == 100 for _, score in subjects)
            if all_100:
                return student
        return None
