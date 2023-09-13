# CIN Preparation

![example](example.jpg)

**A python-based algorithm for CIN**, specially optimized for CIN rectification. Given an input image which contains a CIN, the algorithm detects the card contour and performs perspective transformation in order to obatin the rectified CIN as output. 


## Usage
### Install
`$ pip install -r requirements.txt`


### Run
1. Go to `Prepration_CIN/`

2. Single-image processing：`$ python rectify.py [input_path] [output_path]`
    - `input_path`: the path of input image
    - `output_path`: the path of output result
    - e.g. `$ python rectify.py example/3.jpg result/3_res.png`

3. Mutiple-image processing：`$ python rectify.py [input_dir] [output_dir]`
    - `input_dir`: the directory of inputs
    - `output_dir`: the directory of ouputs
    - e.g. `$ python rectify.py example/ result/`

    > the default save format is '.png'.


## Unsolved situation
- The CIN is incomplete or is occuluded by other objects.
- If the CIN is upside down, the output will not adjust the rotation.



