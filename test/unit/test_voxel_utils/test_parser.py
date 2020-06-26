from unittest import TestCase

from dosipy.voxel_utils.parser import Parser
from dosipy.voxel_utils.record import Record, Coordinate


class TestParser(TestCase):
    def test_should_parse_header_only(self):
        mock_file = [
            'SIRT BAH 2',
            '\t'.join(('x (mm)', 'y (mm)', 'z (mm)', 'pixel ( )')),
        ]
        parser = Parser(iter(mock_file))
        records = list(parser.read_records())
        self.assertEqual('SIRT BAH 2', parser.name)
        self.assertEqual(len(records), 0)


    def test_should_parse_voxel_record(self):
        mock_file = [
            'SIRT Tumour 2',
            '\t'.join(('x (mm)', 'y (mm)', 'z (mm)', 'pixel ( )')),
            '\t'.join(('1', '2', '3', '5')),
        ]
        parser = Parser(iter(mock_file))
        records = list(parser.read_records())
        self.assertEqual(len(records), 1)
        self.assertEqual(
            records, [Record(Coordinate(1.0, 2.0, 3.0), 5.0)]
        )

    def test_should_parse_many_records(self):
        mock_file = [
            'SIRT Tumour 2',
            '\t'.join(('x (mm)', 'y (mm)', 'z (mm)', 'pixel ( )')),
            '\t'.join(('1', '2', '3', '5')),
            '\t'.join(('1', '7', '3', '5')),
            '\t'.join(('1', '7', '3', '6')),
        ]
        parser = Parser(iter(mock_file))
        records = list(parser.read_records())

        self.assertEqual(len(records), 3)

        expected_records = [
            Record(Coordinate(1.0, 2.0, 3.0), 5.0),
            Record(Coordinate(1.0, 7.0, 3.0), 5.0),
            Record(Coordinate(1.0, 7.0, 3.0), 6.0),
        ]
        self.assertEqual(records, expected_records)
