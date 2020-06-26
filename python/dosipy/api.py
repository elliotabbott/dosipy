import argparse

from scipy.ndimage.measurements import label
from scipy.ndimage.morphology import generate_binary_structure
from numpy import array

from dosipy.voxel_utils.parser import VoxelParserContextManager


def get_records(filepath):
    with VoxelParserContextManager(filepath) as parser:
        records = set(parser.read_records())
    return records


if __name__ == '__main__':
    args = argparse.ArgumentParser(description='A tool to help my lift')
    args.add_argument('--tumour', dest='tumour_filepath', required=True)
    args.add_argument('--liver', dest='liver_filepath', required=True)
    args.add_argument('--whole', dest='whole_filepath', required=True)

    options = args.parse_args()

    tumour_records = get_records(options.tumour_filepath)
    liver_records = get_records(options.liver_filepath)
    whole_records = get_records(options.whole_filepath)

    missing_tumour_records = tumour_records - whole_records
    missing_liver_records = liver_records - whole_records
    if len(missing_liver_records) > 0 or len(missing_tumour_records) > 0:
        raise Exception("All records are required to be in Whole Body file.")

    for rec in whole_records:
        if rec in tumour_records:
            rec.is_tumour = True
        if rec in liver_records:
            rec.is_liver = True



            # a = array([[0, 0, 1, 1, 0, 0],
            #            [0, 0, 0, 1, 0, 0],
            #            [1, 1, 0, 0, 1, 0],
            #            [0, 0, 0, 1, 0, 0]])
            # b = generate_binary_structure(3, 2)
            # labeled_array, num_features = label(a)
            # print(labeled_array, '\n', b)