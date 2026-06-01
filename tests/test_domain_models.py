from calculator.domain.model.model import Operands, operands_factory

def test_if_operands_is_created():
    model_ = Operands(2, 7)
    assert model_.left == 2 and model_.right == 7

def test_if_operands_is_created_with_factory():
    model_ = operands_factory(2, 7)
    assert model_.left == 2 and model_.right == 7

def test_if_operands_is_created_with_wrong_type():
    model_ = operands_factory("boom", 5.5)
    assert model_.left == "boom" and model_.right == 5.5