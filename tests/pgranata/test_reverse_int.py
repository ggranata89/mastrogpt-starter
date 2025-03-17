import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/pgranata/reverse"
    res = req.get(url,{"input":"esrever"}).json()
    assert res.get("output") == "reverse"
