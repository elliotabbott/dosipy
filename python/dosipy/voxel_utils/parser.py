import csv

from dosipy.voxel_utils.record import Coordinate, Record

X_COORD_NAME = 'x (mm)'
Y_COORD_NAME = 'y (mm)'
Z_COORD_NAME = 'z (mm)'
PIXEL_KEY = 'pixel ( )'


def parse_line(values):
    coordinate = Coordinate(
        float(values[X_COORD_NAME]),
        float(values[Y_COORD_NAME]),
        float(values[Z_COORD_NAME]),
    )
    pixel_value = float(values[PIXEL_KEY])
    return Record(coordinate, pixel_value)


class Parser(object):
    def __init__(self, stream):
        self.__name = None
        self.__stream = stream

    @property
    def name(self):
        return self.__name

    def read_records(self):
        self.__name = next(self.__stream)
        reader = csv.DictReader(self.__stream, dialect='excel-tab')
        assert(
            sorted(reader.fieldnames) == sorted([X_COORD_NAME, Y_COORD_NAME, Z_COORD_NAME, PIXEL_KEY])
        )
        for line in reader:
            yield parse_line(line)


class VoxelParserContextManager(object):
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__fp = None

    def __enter__(self):
        self.__fp = open(self.__filepath)
        return Parser(self.__fp)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()
