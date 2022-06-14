
def gerade():
      x1 = int(input("x of first point:"))
      y1 = int(input("y of first point:"))
      x2 = int(input("x of second point:"))
      y2 = int(input("y of second point:"))

      P1 = "P1(" + str(x1) + "," + str(y1) + ")"
      P2 = "P2(" + str(x2) + "," + str(y2) + ")"

      m = round((y2 - y1) / (x2 - x1), 2)
      b = round(y1 - (m * x1), 2)

      print("The equation of the straight line passing through " + P1 + " and " + P2 + " is...")
      print("y = " + str(m) + "x " + "+ " + str(b))
gerade()