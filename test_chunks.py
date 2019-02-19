from .main import arrayChunk


def test_chunk_three():
    base = [1, 2, 3, 4, 5, 6]
    assert arrayChunk(base, 3) == [[1, 2, 3], [4, 5, 6]]


def test_chunk_four():
    base = [1, 2, 3, 4, 5, 6]
    assert arrayChunk(base, 4) == [[1, 2, 3, 4], [5, 6]]


def test_chunk_zero():
    base = [1, 2, 3, 4, 5, 6]
    assert arrayChunk(base, 0) == []


def test_chunk_seven():
    base = [1, 2, 3, 4, 5, 6]
    assert arrayChunk(base, 7) == [[1, 2, 3, 4, 5, 6]]
