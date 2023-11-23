import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:
    @pytest.fixture()
    def xml_content_and_data(self) -> tuple[str, DataType]:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
    <Иванов_Иван_Иванович>
        <математика>90</математика>
        <литература>90</литература>
        <философия>90</философия>
    </Иванов_Иван_Иванович>
    <Петров_Иван_Иванович>
        <математика>61</математика>
        <литература>61</литература>
        <философия>61</философия>
    </Петров_Иван_Иванович>
</root>
"""

        data = {
            "Иванов_Иван_Иванович":
                [
                    ("математика", 90),
                    ("литература", 90),
                    ("философия", 90)
                ],
            "Петров_Иван_Иванович":
                [
                    ("математика", 61),
                    ("литература", 61),
                    ("философия", 61)
                ]
        }
        return xml_content, data

    @pytest.fixture()
    def xml_filepath_and_data(
        self, xml_content_and_data: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        xml_content, data = xml_content_and_data
        xml_filepath = tmpdir.join("my_data.xml")
        with open(str(xml_filepath), "w", encoding="utf-8") as file:
            file.write(xml_content)
        return str(xml_filepath), data

    def test_read(self, xml_filepath_and_data: tuple[str, DataType]) -> None:
        xml_filepath, expected_data = xml_filepath_and_data
        reader = XMLDataReader()
        result_data = reader.read(xml_filepath)
        assert result_data == expected_data
