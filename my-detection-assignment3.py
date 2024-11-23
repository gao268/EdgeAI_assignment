import jetson.inference
import jetson.utils
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
img=jetson.utils.loadImage("/home/nvidia/jetson-inference/examples/1.jpg")
detections=net.Detect(img)
print(detections[0])
display = jetson.utils.glDisplay()
while display.IsOpen():
    display.RenderOnce(img)
    display.SetTitle("Object Detection")
