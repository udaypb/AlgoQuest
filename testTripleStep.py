import TripleStep as ts
def testTripleStep():
    assert ts.possibleWays(3) == 4
    assert ts.possibleWays(4) == 7
    assert ts.possibleWays(5) == 13


if __name__ == '__main__':
    testTripleStep()
    print('All tests passed')