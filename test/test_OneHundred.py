from src.OneHundred import OneHundred
from src.Types import DataType
import pytest

class TestOneHundred:

    @pytest.fixture()
    def input_data(self) -> DataType:
        data: DataType = {
            "Студент1": [
                ("предмет1", 100),
                ("предмет2", 100),
            ],
            "Студент2": [
                ("предмет1", 95),
                ("предмет2", 100),
            ],
            "Студент3": [
                ("предмет1", 100),
                ("предмет2", 100),
            ],
        }
        return data

    def test_find_one_hundred(self, input_data: DataType) -> None:
        finder = OneHundred(input_data)
        result = finder.find()
        assert result == "Студент1"  # Ожидаем, что найдется первый студент, у которого все оценки 100

    def test_find_no_one_hundred(self, input_data: DataType) -> None:
        # Создаем данные, в которых нет студента с оценками 100
        data_without_one_hundred: DataType = {
            "Студент1": [
                ("предмет1", 90),
                ("предмет2", 90),
            ],
            "Студент2": [
                ("предмет1", 95),
                ("предмет2", 98),
            ],
        }

        finder = OneHundred(data_without_one_hundred)
        result = finder.find()
        assert result is None  # Ожидаем, что не найдется студентов со всеми оценками 100
