# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student_elem in root:
            student_name = student_elem.tag.strip()
            self.students[student_name] = []

            for subject_elem in student_elem:
                subject_name = subject_elem.tag.strip()
                subject_score = int(subject_elem.text.strip())
                self.students[student_name].append((
                    subject_name,
                    subject_score)
                )

        return self.students
