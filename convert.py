import argparse
import cv2
import pathlib

def parse_args():
    parser = argparse.ArgumentParser(description= "Extract all image frames from a video.")
    parser.add_argument('--video', help='location of a video file.', type=str, required=True)
    parser.add_argument('--export_to', default='result', help='location to export images (default: result)', type=str)
    return parser.parse_args()

def main(args):

    assert pathlib.Path(args.video).exists(), "The video file {} does not exist".format(args.video)

    cap = cv2.VideoCapture(args.video)
    export_path = get_export_path(args.export_to)

    cnt = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_path = get_image_path(export_path, cnt)
        print("writing {}".format(str(image_path)))
        cv2.imwrite(str(image_path), frame)
        cnt += 1


def get_export_path(name):
    path = pathlib.Path(name)
    path.mkdir(exist_ok = True, parents=True)

    return path

def get_image_path(export_path, id):
    return export_path.joinpath("{}.png".format(id))

if __name__ == '__main__':
    args = parse_args()
    main(args)
