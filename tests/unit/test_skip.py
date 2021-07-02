import pytest

try:
    import mylib
except ImportError:
    mylib = None

@pytest.mark.skip("Этот процесс не запущен")
def test_fail():
    assert False

@pytest.mark.skipif(mylib is None, reason="mylib не существует")
def test_mylib():
    assert mylib.foobar() == 42

def test_skip_at_runtime():
    if True:
        pytest.skip('Конец! Я не хочу запускать этоpy')