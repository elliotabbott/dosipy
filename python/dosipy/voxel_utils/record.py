class Coordinate(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "Coordinate<x={!r},y={!r},z={!r}".format(
            self.x, self.y, self.z
        )


class Record(object):
    def __init__(self, coordinate, photon_count):
        self.coordinate = coordinate
        self.photon_count = photon_count
        self.is_tumour = False
        self.is_liver = False

    def __hash__(self):
        return hash(self.coordinate)

    def __eq__(self, other):
        return self.coordinate == other.coordinate and self.photon_count == other.photon_count

    def __repr__(self):
        return "VoxelRecord<coordinate={!r},photon_count={!r},is_tumour={!r},is_liver={!r}".format(
            self.coordinate, self.photon_count, self.is_tumour, self.is_liver
        )
