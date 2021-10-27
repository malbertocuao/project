import pytest
import project

data = [
    {"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"},
    {"first_name":"Hassan","h_in":"76","h_meters":"1.93","last_name":"Adams"},
    {"first_name":"Arron","h_in":"77","h_meters":"1.96","last_name":"Afflalo"},
    {"first_name":"Maurice","h_in":"77","h_meters":"1.96","last_name":"Ager"},
    {"first_name":"Alexis","h_in":"84","h_meters":"2.13","last_name":"Ajinca"},
    {"first_name":"LaMarcus","h_in":"83","h_meters":"2.11","last_name":"Aldridge"}
]

sorted = [
    {"first_name":"Hassan","h_in":"76","h_meters":"1.93","last_name":"Adams"},
    {"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"},
    {"first_name":"Arron","h_in":"77","h_meters":"1.96","last_name":"Afflalo"},
    {"first_name":"Maurice","h_in":"77","h_meters":"1.96","last_name":"Ager"},
    {"first_name":"LaMarcus","h_in":"83","h_meters":"2.11","last_name":"Aldridge"},
    {"first_name":"Alexis","h_in":"84","h_meters":"2.13","last_name":"Ajinca"}
]

def sort_test():
    """ Test sort function """

    assert project.sort(data) == sorted


def test_search():
    """ Test search function """
    assert project.search(sorted, 76) == 0
    assert project.search(sorted, 1) == -1
    assert project.search(sorted, 77) >= 1 and project.search(sorted, 77) <= 3
    assert project.search(sorted, 84) == 5