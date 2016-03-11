# clarifai_test.py
#
# some Python scripts to play around with the Clarifai API
# some of this code is from the example documentation given at
# https://github.com/clarifai/clarifai-python

import json
import random
from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi() #assumes environemnt variables are set

image_selection_list = ['me.png', 'Scan 1.png', 'Scan 2.png', 'Scan 3.png', 'Scan 4.png', 'Scan 5.png']
index = random.randint(0, len(image_selection_list)-1)
print "selected image: %s" % (image_selection_list[index])
try:
    result = clarifai_api.tag_images(open(image_selection_list[index], 'rb'))
    # print json.dumps(result, indent=2)
    for tag,prob in result['results']['result']['tag']['classes'],result['results']['result']['tag']['probs']:
        print "tagged: %s with probability: %s" % (tag,prob)
except Exception as e:
    raise e
    print "Encountered an error: %s" % (e)
