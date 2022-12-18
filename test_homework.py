import pytest
from homework import take_from_list


@pytest.fixture
def list():
    return [1,2,3,4]

def test_index_error(list,tmp_path):
    with pytest.raises(IndexError):
        index = [5,3,6,1]
        take_from_list(list,index)

def test_value_error_string(list,tmp_path):
    with pytest.raises(ValueError):
        index = ["kot",1,4,3,"5"]
        take_from_list(list,index)

def test_value_error_float(list,tmp_path):
    with pytest.raises(ValueError):
        index = [3,5,9,0.6]
        take_from_list(list,index)





