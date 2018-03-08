from goonj.exception import GoonjNotInitalized


def hello():
    raise GoonjNotInitalized('what the fuck is this')


hello()
