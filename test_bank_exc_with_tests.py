import  bank_exc_with_tests
import pytest


# Test for valid choices
def test_check_choice_alpha():
    choice= "abc"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_choice(choice)
    assert str(e.value) == "you entered an alpha string, try again"

def test_check_choice_out_of_range():
    choice= "50"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_choice(choice)
    assert str(e.value) == "Invalid choice, please select a number between 1 and 4"

def test_check_choose_alpha():
    choose= "abc"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_choose(choose)
    assert str(e.value) == "you entered an alpha string, try again"

def test_check_choose_out_of_range():
    choose = "50"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_choose(choose)
    assert str(e.value) == "Invalid choice, please select a number between 1 and 10"

def test_check_acc_for_transact_fromacc():
    fromacc = "3000"
    toacc = "1002"
    amm = "1000"
    listAcc = [fromacc, toacc, amm]
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_for_transac(listAcc)
    assert str(e.value) == "'from account' not known, try again"

def test_check_acc_for_transact_toacc():
    fromacc = "1002"
    toacc = "3000"
    amm = "1000"
    listAcc = [fromacc, toacc, amm]
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_for_transac(listAcc)
    assert str(e.value) == "'to account' is not known, please try again"

def test_check_acc_for_transact_amm_alpha():
    fromacc = "1001"
    toacc = "1002"
    amm = "abc"
    listAcc = [fromacc, toacc, amm]
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_for_transac(listAcc)
    assert str(e.value) == "you entered illegal details, please try again"

def test_check_acc_for_transact_zero():
    fromacc = "1001"
    toacc = "1002"
    amm = "0"
    listAcc = [fromacc, toacc, amm]
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_for_transac(listAcc)
    assert str(e.value) == "one of the parameters is zero, try again"

def test_check_acc_number_alpha():
    accnumber = "abc"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_number(accnumber)
    assert str(e.value) == "not an integer"

def test_check_acc_number_out_of_range():
    accnumber = "5000"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_acc_number(accnumber)
    assert str(e.value) == "the account you typed does not exist, try again"

def test_check_idnumber_alpha():
    idnumber = "abc"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_idnumber(idnumber)
    assert str(e.value) == "you typed an illegal number, please try again"

def test_check_idnumber_out_of_range():
    idnumber = "111111"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_idnumber(idnumber)
    assert str(e.value) == "this id is not known, please try again"

def test_check_first_name():
    first_name = "yona"
    with pytest.raises(ValueError) as e:
        bank_exc_with_tests.check_first_name(first_name)
    assert str(e.value) == "first name not known, please try again"

def test_all_transac():
    actual = bank_exc_with_tests.all_transac()
    prob = True
    assert actual == prob

def test_transac():
    fromacc = 1001
    toacc = 1002
    amm = 1000
    actual = bank_exc_with_tests.transac(fromacc, toacc, amm)
    prob = True
    assert prob == actual






