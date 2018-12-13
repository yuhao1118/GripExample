import cv2
# from "PIPELINE_FILE_NAME" import "CLASS_NAME"
from grip import GripPipeline
from time import sleep


def extra_process(pipeline):
    """
    Performs extra processing on the pipeline's outputs and print data on screen.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []
    # Find the bounding boxes of the contours to get x, y, width, and height
    # X and Y are coordinates of the top-left corner of the bounding box
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x - 320 / 2)
        center_y_positions.append(y - 240 / 2)
        widths.append(w)
        heights.append(y)
    print("centerX: " + str(center_x_positions))
    print("centerY: " + str(center_y_positions))
    print("width: " + str(widths))
    print("height: " + str(heights))
    print("\n")


def main():
    # For usb/built-in camera
    camera = cv2.VideoCapture(1)
    # For ip camera (MJPEG Stream)
    # camera = cv2.VideoCapture("/url-to-your-stream/video.mjpg")
    mypipeline = GripPipeline()

    while camera.isOpened():
        have_frame, frame = camera.read()
        if have_frame is not None:
            mypipeline.process(frame)
            extra_process(mypipeline)
            sleep(0.5)

    print("Capture closed")


if __name__ == "__main__":
    main()
