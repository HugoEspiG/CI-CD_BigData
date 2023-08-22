from utils import es_primo

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(17) == True
    assert es_primo(4) == False
    assert es_primo(9) == False
    assert es_primo(29) == True
    assert es_primo(100) == False
