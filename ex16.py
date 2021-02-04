class TriangleArea:
    def get_area(self):
        # returns -
        h = float(input("Enter height of triangle: "))      # h - height of triangle
        b = float(input("Enter base of triangle: "))        # b - base of triangle
        print("Area of triangle having height={height} and base={base} is: {area}".format(height=h, base=b, area=((h*b)/2)))


ta = TriangleArea()
ta.get_area()
