def matrix(n=None, m=None,value=None):
    if n is None:
      s = []
      x = [0]
      s.append(x)
      return(s)
    elif n is not None and m is None:
      l = []
      y = []
      for i in range(n+1):
          if y != []:
              l.append(y)
              y = []
          for j in range(n):
              y.append(0)
      return(l)
    elif n is not None and m is not None and value is None:
      l = []
      y = []
      for i in range(n+1):
          if y != []:
              l.append(y)
              y = []
          for j in range(m):
              y.append(0)
      return(l)
    elif n is not None and m is not None and value is not None:
      l = []
      y = []
      for i in range(n+1):
          if y != []:
              l.append(y)
              y = []
          for j in range(m):
              y.append(value)
      return(l)
