class VolumeOfSphere:
    def calculate(self):
        # returns volume of a sphere
        radius = float(input("Enter radius: "))     # radius - radius of a sphere
        volume = (4/3)*(22/7)*radius*radius*radius      # volume - volume of a sphere
        return volume


vol = VolumeOfSphere()
print("Volume of sphere: {volume:.2f}".format(volume=vol.calculate()))  # .2f is used for 2 decimal points
