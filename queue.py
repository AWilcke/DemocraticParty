class Queue (): 
	def __init__(self):
		self.songs = []

	def isEmpty(self):
		return self.songs == []

	def enqueue(self, song):
		if self.isEmpty(): 
			self.songs.append((0, song, []))
		else:
			if (self.search(song) == -1):
				self.songs.append((0, song, []))
				self.sort()

	def next(self):
		song = self.songs[0][1]
		self.songs.pop(0)
		return song

	def dequeue(self):
		return self.songs.pop()

	def size(self):
		return len(self.songs) 

	def sort(self): 
		self.songs.sort(reverse=True)

	def search(self, song):
		for i in range(1, self.size(), 1):
			if (self.songs[i][1] == song):
				return i
		return -1

	def vote(self, song, userid, num): 
		index = [b for (a, b, c) in self.songs].index(song)
		if (not userid in self.songs[index][2]):
			self.songs[index][2].append(userid)
			self.songs[index] = (self.songs[index][0] + num, self.songs[index][1], self.songs[index][2])


'''q = Queue()
q.enqueue('Hello')
q.enqueue('7 Years')
q.enqueue('Stressed Out')
q.enqueue('I Was Wrong')
print q.songs
q.vote('7 Years', 'user1', 1)
q.vote('7 Years', 'user2', 1)
q.vote('Hello', 'user1', 1)
q.vote('Stressed Out', 'user2', -1)
q.enqueue('Sorry')
q.vote('7 Years', 'user3', 1)
q.vote('Hello', 'user3', 1)
q.vote('Sorry', 'user3', 1)
q.vote('Sorry', 'user4', 1)
q.sort()
print q.songs
q.dequeue()
print q.songs
print q.size()
print q.next()
print q.songs'''