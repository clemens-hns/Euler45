	
def isPentagonal(n, t):
  for i in range (11, n):
    p = i * ( 3 * i - 1) / 2
    if (p == t): 
	  return True
  return False
  
def isHexagonal(n, t):
  for i in range (11, n):
    h = i * ( 2 * i - 1 )
    if (h == t):
      return True
  return False
  
for n in range(286, 60000):
  t = n * (n + 1) / 2
  #print "triangle: ", t
  # test to see if this is pentagonal
  if(isPentagonal(n, t)):
	print "Triangle and Pentagonal: ", t
	if(isHexagonal(n, t)):
		print "Triangle and Pentagonal and Hexagonal: ", t