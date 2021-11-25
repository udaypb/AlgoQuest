import RandomTaskBasedOnWeightProbability as rtbwp
def testRandomTaskBasedOnWeightProbability():
    assert rtbwp.random_task(['a', 'b', 'c', 'd', 'e'], [10, 20, 30, 40, 50]) != None
    assert rtbwp.random_task(['a', 'b'], [10, 40]) != None

if __name__ == '__main__':
    testRandomTaskBasedOnWeightProbability()
    print('All tests passed')