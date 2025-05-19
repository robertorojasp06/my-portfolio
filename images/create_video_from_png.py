import cv2
import argparse
import random
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="""Create a mp4 video from a sequence of png images.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'path_to_images',
        type=str,
        help="""Path to the directory containing the png images."""
    )
    parser.add_argument(
        'path_to_output',
        type=str,
        help="""Path to the directory to save the output video."""
    )
    parser.add_argument(
        '--fps',
        type=float,
        default=0.5,
        help="Frames per second."
    )
    parser.add_argument(
        '--is_random',
        action='store_true',
        help="Add this flag to sort the images randomly."
    )
    args = parser.parse_args()
    paths_to_images = sorted(list(Path(args.path_to_images).glob('*.png')))
    if args.is_random:
        random.shuffle(paths_to_images)
    first_frame = cv2.imread(paths_to_images[0])
    out = cv2.VideoWriter(
        Path(args.path_to_output) / "output_video.mp4",
        cv2.VideoWriter_fourcc(*'avc1'),
        args.fps,
        (first_frame.shape[1], first_frame.shape[0])
    )
    for path in paths_to_images:
        frame = cv2.imread(path)
        out.write(frame)
    out.release()
    print(f"Video saved to {args.path_to_output}")


if __name__ == "__main__":
    main()
