from typing import Any
from unittest.mock import mock_open, patch

from src.files import FileWork, JSONSaver


def test_file_work() -> None:
    class Test(FileWork):
        def get_data(self) -> Any:
            str(1)

        def write_data(self, dict_data: list) -> Any:
            str(1)

        def delete_data(self, vacancy: dict) -> Any:
            str(1)

    test = Test()
    FileWork.get_data(test)
    FileWork.write_data(test, [])
    FileWork.delete_data(test, {})


def test_json_saver_get_data() -> None:
    js = JSONSaver()

    with patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]'):
        data = js.get_data()
        assert data == [{"key": "value"}]


def test_json_saver_write_data() -> None:
    js = JSONSaver()

    with patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]'):
        js.write_data([{"url": "value"}])


def test_json_saver_delete_data() -> None:
    js = JSONSaver()

    with patch("builtins.open", new_callable=mock_open, read_data='[{"url": "value"}]'):
        js.delete_data({"url": "value"})
