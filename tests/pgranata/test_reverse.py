import sys 
sys.path.append("packages/pgranata/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({"input":"testo"})
    assert res["output"] == "testo"[::-1]
