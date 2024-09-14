import gradio as gr
import PIL.Image as Image

from ultralytics import ASSETS, YOLO

model = YOLO("/home/vasu/Documents/chessMooveTrack/model/yolo8/runs_yolo8/detect/train4/weights/best.pt")


def predict_image(img, conf_threshold, iou_threshold):
    """Predicts objects in an image using a YOLOv8 model with adjustable confidence and IOU thresholds."""
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=418,
    )

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im


iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Yolo8 Chess Piece Detection",
    description="Upload images for inference. The Ultralytics YOLOv8m model is used by default.",
    examples=[
        [ASSETS / "/home/vasu/Documents/chessMooveTrack/black.jpg", 0.7, 0.5],
        [ASSETS / "/home/vasu/Documents/chessMooveTrack/lessmultichess.jpg", 0.7, 0.5],
    ],
)

if __name__ == "__main__":
    iface.launch()