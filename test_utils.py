from utils import es_primo

def test_es_primo():
    assert es_primo(2)
    assert es_primo(3)
    assert es_primo(17)
    assert not es_primo(4)
    assert not es_primo(9)
    assert es_primo(29)
    assert not es_primo(100)
