from coco_assistant import COCO_Assistant
import argparse
import os

parser = argparse.ArgumentParser(description='merge, train-test split or do both')
parser.add_argument('-m', '--mode', default='m+s',
                    help='whether "m" for merge, "s" for split or "m+s" for merge then split')
parser.add_argument('-id', '--img_dir',
                    help='if mode include merge, specify path to image directory')
parser.add_argument('-ad', '--ann_dir',
                    help='if mode include merge, specify path to annotation directory')
parser.add_argument('-a', '--annotations', metavar='coco_annotations', type=str,
                    help='specify only if mode = "s"; path to COCO annotations file.')
parser.add_argument('-tr', '--train', type=str,
                    help='specify only if mode = "s" or "m+s"; training annotations name')
parser.add_argument('-te', '--test', type=str, 
                    help='specify only if mode = "s" or "m+s"; testing annotations name')
parser.add_argument('-s', dest='split', type=float, required=True,
                    help="A percentage of a split; a number in (0, 1)")              

args = parser.parse_args()

def main(args):
    img_dir = args.img_dir
    ann_dir = args.ann_dir
    cas = COCO_Assistant(img_dir, ann_dir)
    if args.mode == "m+s" or args.mode == "m":
        img_dir = args.img_dir
        ann_dir = args.ann_dir
        cas.merge()
        if args.mode == "m+s":
            cas.splitter(cas.dst_ann, args.split, os.path.join(cas.res_dir, args.train), os.path.join(cas.res_dir, args.test))
    elif args.mode == "s":
        cas.splitter(args.annotations, args.split, args.train, args.test)
    else:
        print('wrong mode')

if __name__ == "__main__":
    main(args)