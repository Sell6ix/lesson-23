import re
from typing import Iterable, TextIO, Union, Iterator


class Query:

    @staticmethod
    def filter(value: str, data: TextIO) -> Iterator[str]:
        """Фильтрация по значению"""
        return filter(lambda x: value in x, data)

    @staticmethod
    def map(value: str, data: Union[TextIO, Iterable]) -> Iterator[str]:
        """Вывод данных по номеру колонки"""
        return map(lambda x: x.split(' ')[int(value)], data)

    @staticmethod
    def unique(value: None, data: Union[TextIO, Iterable]) -> set:
        return set(data)

    @staticmethod
    def sort(value: str, data: Union[TextIO, Iterable]) -> list:
        """Сортировка"""
        reversed = value == 'asc'
        return sorted(data, reverse=reversed)

    @staticmethod
    def limit(value: str, data: Union[TextIO, Iterable]) -> list:
        return list(data)[:int(value)]

    @staticmethod
    def regex(value: str, data: Union[TextIO, Iterable]) -> list:
        """Поиск по регулярному выражению"""
        reg_exp = re.compile(r"" + value)
        result = []
        for i in list(data):
            if re.findall(reg_exp, i):
                result.append(i)
        return result

