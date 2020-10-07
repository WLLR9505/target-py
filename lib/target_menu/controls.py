class Controls:
  def __init__(self, aElect='e', aBack='q', aUp='w', aDown='s', aRight='d', aLeft='a'):
      self.elect = aElect
      self.back = aBack
      self.up = aUp
      self.down = aDown
      self.right = aRight
      self.left = aLeft

      self.pos1 = 0
      self.pos2 = 0

  def resetPos(self):
      self.pos1 = 0
      self.pos2 = 0

  def getPos1(self):
    return self.pos1
  
  def getPos2(self):
    return self.pos2

  def getUp(self):
    return self.up

  def getDown(self):
    return self.down

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getElect(self):
    return self.elect
  
  def getBack(self):
    return self.back

  def setPos1(self, p):
    self.pos1 = p
  
  def setPos2(self, p):
    self.pos2 = p