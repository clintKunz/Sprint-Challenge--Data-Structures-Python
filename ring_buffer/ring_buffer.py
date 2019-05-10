class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < len(self.storage):
      self.storage[self.current] = item
      self.current += 1
      return self.storage
    else: 
      self.current = 0
      return self.append(item)

  def get(self):
    pass

buffer = RingBuffer(3)
print(buffer.append(2))
print(buffer.append(3))
print(buffer.append(4))
print(buffer.append(5))