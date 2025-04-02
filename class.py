def getKey(KeyName):
    ans = False

    for event in pygame.event.get():pass
    keyinput=pygame.key.get_pressed()

    myKey=getattr(pygame,'K{}'.format(KeyName))
    if keyinput[myKey]:
        ans=True
    pygame.display.update()
    return ans