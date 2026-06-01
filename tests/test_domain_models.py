from calculator.domain.model.model import Operands, operands_factory

def test_if_operands_is_created():
    model_ = Operands(2, 7)
    assert model_.left == 2 and model_.right == 7

def test_if_operands_is_created_with_factory():
    model_ = operands_factory(2, 7)
    assert model_.left == 2 and model_.right == 7

def test_if_operands_is_created_with_wrong_type():
    model_ = operands_factory("hello world", False)
    assert model_.left == "helo world" and model_.right == False