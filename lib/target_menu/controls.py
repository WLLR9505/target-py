class Controls:
  def __init__(aElect='e', aBack='q', aUp='w', aDown='s', aRight='d', aLeft='a')
      self.elect = aElect
      self.back = aBack
      self.up = aUp
      self.down = aDown
      self.right = aRight
      self.left = aLeft

      self.pos1 = 0
      self.pos2 = 0

  def resetPos
      self.pos1 = 0
      self.pos2 = 0

  def getPos1
    return self.pos1
  
  def getPos2
    return self.pos2

  def getUp
    return self.up

  def getDown
    return self.down

  def getLeft
    return self.left

  def getRight
    return self.right

  def getElect
    return self.elect
  
  def getBack
    return self.back

  def setPos1(p)
    self.pos1 = p
  
  def setPos2(p)
    self.pos2 = p