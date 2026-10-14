# Python OOP: Dunder (Magic) Methods

## The Core Concept
'''
 -> Dunder stands for "Double Underscore". These are built-in hooks that allow your custom classes to 
    behave like native Python objects (e.g., using `()` to call them, `[]` to index them, or `len()` to measure them). 

 -> You already know `__init__` (the setup method). For Phase 2 and Phase 3 of your 
    AI Roadmap (specifically PyTorch and Hugging Face), you must master three more.
'''

## 1. `__call__` (The PyTorch Standard)
'''
 -> Allows an object to be executed directly like a function. 
    In AI frameworks, you don't call a `.predict()` method; you just call the model object itself.

 Example:'''
class AI_Model:
    def __init__(self, name):
        self.name = name
        
    # This makes the object callable
    def __call__(self, data):
        return f"Processing {data} through {self.name}"

# Usage
my_model = AI_Model("ResNet")
result = my_model("image.png") # We trigger the object directly!


## The Core Concept
'''
 -> When you reach Phase 2 and start building Neural Networks with PyTorch, you cannot just pass raw files to a GPU. 
    You must create a custom `Dataset` class. 
    PyTorch's internal engine strictly relies on two dunder methods to understand and iterate over your data:

1. `__len__(self)`: Tells PyTorch the total size of your dataset so it can calculate training epochs and batches. 
                    Triggered automatically by `len(object)`.

2. `__getitem__(self, index)`: Tells PyTorch exactly how to fetch a single piece of data (and its label) when requested. 
                               Triggered automatically by indexing, like `object[index]`.
'''

## PyTorch Dataset Template
'''
 -> Whenever you build a custom dataset for AI, you will use this exact architectural pattern:

 Example: ''' 
class CustomVideoDataset:
    def __init__(self, video_files, labels):
        # 1. Store your raw data locations and labels
        self.video_files = video_files
        self.labels = labels

    def __len__(self):
        # 2. Return the total number of items
        return len(self.video_files)

    def __getitem__(self, index):
        # 3. Define how to fetch one single item by its index
        video = self.video_files[index]
        label = self.labels[index]
        
        # (In real PyTorch, you load the video into a Tensor here)
        return {"video": video, "label": label}

# --- How PyTorch uses it behind the scenes ---
files = ["scene1.mp4", "scene2.mp4", "scene3.mp4"]
tags = ["action", "dialogue", "action"]

# Initialize dataset
my_dataset = CustomVideoDataset(files, tags)

# PyTorch checks the size to build training batches
print(f"Total training samples: {len(my_dataset)}") 
# Output: Total training samples: 3

# PyTorch grabs specific indices to feed the GPU
print(my_dataset[1]) 
# Output: {'video': 'scene2.mp4', 'label': 'dialogue'}