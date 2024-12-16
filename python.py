from roboflow import Roboflow
rf = Roboflow(api_key="fF8fftBxEHKCmZJYvSeZ")
project = rf.workspace("rf-projects").project("x-ray-id")
version = project.version(3)
dataset = version.download("yolov11")
..
