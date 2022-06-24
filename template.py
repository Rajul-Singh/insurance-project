import os


dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "src",
    "models",
    os.path.join("webapp", "templates"),
    os.path.join("webapp", "static"),
    "reports",
    "logs",
    "docs",
    "tests",
    "data_given"
    
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir, ".gitkeep"), "w") as f:
        pass

file_ = [
    "dvc.yaml",
    "params.yaml",
    os.path.join("src","__init__.py"),
    os.path.join("tests","__init__.py")
    
]

for file in file_:
    with open(file, "w") as f:
        pass