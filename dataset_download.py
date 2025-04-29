from roboflow import Roboflow
rf = Roboflow(api_key="YOUR KEY")
project = rf.workspace("nikoosworkspace").project("potholes-japan")
version = project.version(3)
dataset = version.download("yolov7")