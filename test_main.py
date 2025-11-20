import pytest
import main

# Тесты для get_first_and_last_element()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], [1, 4]),
    (["a", "b", "c"], ["a", "c"]),
    ([1], [1, 1]),
    ([], []),
])
def test_get_first_and_last_element(input_list, expected):
    assert main.get_first_and_last_element(input_list) == expected

# Тесты для get_middle_elements()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4, 5], [2, 3, 4]),
    (["a", "b", "c"], ["b"]),
    ([1, 2], []),
    ([1], []),
    ([], []),
])
def test_get_middle_elements(input_list, expected):
    assert main.get_middle_elements(input_list) == expected

# Тесты для get_elements_from_second_to_fourth()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4, 5, 6], [2, 3, 4]),
    (["a", "b", "c", "d"], ["b", "c", "d"]),
    ([1, 2, 3], [2, 3]),
    ([1, 2], [2]),
    ([1], []),
])
def test_get_elements_from_second_to_fourth(input_list, expected):
    assert main.get_elements_from_second_to_fourth(input_list) == expected

# Тесты для add_element_to_start_and_end()
@pytest.mark.parametrize("input_list, element, expected", [
    ([1, 2, 3], 0, [0, 1, 2, 3, 0]),
    ([], "a", ["a", "a"]),
    (["b"], "c", ["c", "b", "c"]),
])
def test_add_element_to_start_and_end(input_list, element, expected):
    # Создаем копию, чтобы исходный список не менялся между тестами
    list_copy = input_list[:]
    assert main.add_element_to_start_and_end(list_copy, element) == expected

# Тесты для remove_second_element()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], [1, 3, 4]),
    (["a", "b", "c"], ["a", "c"]),
    ([1, 2], [1]),
])
def test_remove_second_element(input_list, expected):
    list_copy = input_list[:]
    assert main.remove_second_element(list_copy) == expected

@pytest.mark.parametrize("input_list", [
    ([1]),
    ([]),
])
def test_remove_second_element_edge_cases(input_list):
    """Тест для случаев, когда удаление невозможно без ошибки."""
    list_copy = input_list[:]
    # В таких случаях функция может либо вернуть список без изменений,
    # либо вызвать ошибку. Проверим первый вариант.
    assert main.remove_second_element(list_copy) == list_copy
