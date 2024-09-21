def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    firstGreater = 'red' if redShirtHeights[0] > blueShirtHeights[0] else 'blue'
    print(firstGreater)
    for i in range(len(redShirtHeights)):
        if firstGreater == 'blue' and blueShirtHeights[i] <= redShirtHeights[i]:
            return False
        if firstGreater == 'red' and redShirtHeights[i] <= blueShirtHeights[i]:
            return False

    return True