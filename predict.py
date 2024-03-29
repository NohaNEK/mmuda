import argparse

from MMUDA import MetaFrameWork

parser = argparse.ArgumentParser(description='TSMLDG test args parser')
parser.add_argument('--name', default='exp', help='name of the experiment')
parser.add_argument('--target', default='D',
                    help='target domain "GSMICcuv", only one target supported, images in target dataset must be same size if test_size > 1')
parser.add_argument('--target-eval', action='store_true', help='target specific eval')
parser.add_argument('--test-size', type=int, default=1, help='the batch size of target specific normalization')
parser.add_argument('--color', action='store_false', help='output the color map instead of trainId map')
parser.add_argument('--output-path', type=str, default='pre_color_ts', help='specify output path')


def predict():
    args = parser.parse_args()
    print(args)
    framework = MetaFrameWork(name=args.name, target=args.target, test_size=args.test_size)
    framework.predict_target(load_path='best_dada_seg', color=args.color,
                             train=args.target_eval, output_path=args.output_path)


if __name__ == '__main__':
    predict()
