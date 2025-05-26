import matplotlib.pyplot as plt
import argparse
from imageio import v3 as iio
from pathlib import Path
from matplotlib_scalebar.scalebar import ScaleBar
from tqdm import tqdm


class Scaler:
    def __init__(self, pixel_size, fps, pixel_units='mm'):
        self.input_extension = '.tiff'
        self.output_extension = '.png'
        self.scalebar_fontsize = 12
        self.pixel_units = pixel_units
        self.pixel_size = pixel_size
        self.location = 'lower right'
        self.dpi = 300
        self.fps = fps
        self.add_text = True
        self.text_color = (1, 1, 1)
        self.text_position = (0.02, 0.915) # (0, 0) is bottom left, (1, 1) is top right
        self.text_fontsize = 8
        self.text_fontweight = 'bold'

    def add_scalebar(self, path_to_images, path_to_output):
        path_to_output_folder = Path(path_to_output) / Path(path_to_images).name
        path_to_output_folder.mkdir(exist_ok=True)
        paths_to_images = sorted(list(Path(path_to_images).glob(f"*{self.input_extension}")))
        for frame_idx, path_to_image in tqdm(enumerate(paths_to_images), total=len(paths_to_images)):
            image = iio.imread(path_to_image)
            scalebar = ScaleBar(
                self.pixel_size,
                units=self.pixel_units,
                fixed_value=25,
                location=self.location,
                box_alpha=1,
                box_color='black',
                font_properties={"size": self.scalebar_fontsize},
                color='white'
            )
            fig, ax = plt.subplots()
            ax.imshow(image)
            ax.add_artist(scalebar)
            ax.axis('off')
            # Add time text
            if self.add_text:
                frame_time = frame_idx / self.fps
                ax.text(
                    self.text_position[0],
                    self.text_position[1],
                    f"time: {round(frame_time * 1e3, ndigits=2)} ms",
                    color=self.text_color,
                    fontsize=self.text_fontsize,
                    fontweight=self.text_fontweight,
                    transform=ax.transAxes
                )
            fig.savefig(
                path_to_output_folder / f"{Path(path_to_image).stem}{self.output_extension}",
                transparent=True,
                dpi=self.dpi                
            )
            plt.close(fig)


def main():
    parser = argparse.ArgumentParser(
        description="Add scalebar to output frames from pymotility.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'path_to_images',
        type=str,
        help="Path to the directory containing the frame images"
    )
    parser.add_argument(
        'path_to_output',
        type=str,
        help="Path to the output directory."
    )
    parser.add_argument(
        '--pixel_size_mm',
        type=float,
        default=0.859552065,
        help="Pixel size in mm."
    )
    parser.add_argument(
        '--fps',
        type=float,
        default=200.0,
        help="Frames per second."
    )
    parser.add_argument(
        '--input_extension',
        type=str,
        default='.tiff',
        help="Image extension."
    )
    args = parser.parse_args()
    scaler = Scaler(
        pixel_size=args.pixel_size_mm,
        fps=args.fps,
        pixel_units='mm'
    )
    scaler.input_extension = args.input_extension
    scaler.add_scalebar(
        args.path_to_images,
        args.path_to_output
    )

if __name__ == "__main__":
    main()
