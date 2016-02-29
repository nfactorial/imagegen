"""
Copyright 2016 nfactorial

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import time
import os.path
import argparse

from .nodes import *

from .project import Project
from .node_registry import NODE_REGISTRY

"""
Run unit tests with....
python -m unittest discover tests
"""

parser = argparse.ArgumentParser(description='Imaggen - by nfactorial',
                                 prog='imagegen')
parser.add_argument('-f',
                    dest='filename',
                    required=False,
                    help='The filename of the JSON definition file containing the image to be generated.')
parser.add_argument('--nodes',
                    action='store_true',
                    help='List all the nodes available within the imagegen distribution.')
parser.add_argument('-job',
                    type=int,
                    help='The number of pixels to processed by each job.')
args = parser.parse_args()

DEFAULT_JOB_SIZE = 32

# List all nodes if the user requested it within the command line.
if args.nodes:
    print('Available nodes: ')
    for key, value in NODE_REGISTRY.items():
        if value.description:
            print('\t%s - %s' % (key, value.description))
        else:
            print('\t%s - <no description>' % key)

JOB_SIZE = DEFAULT_JOB_SIZE if args.job is None else args.job
if JOB_SIZE <= 0:
    raise ValueError('Job size must be greater than zero (found %d).' % JOB_SIZE)

if args.filename:
    # Make sure the JSON file exists before we try to load it.
    if not os.path.exists(args.filename):
        print('Imagegen - ERROR - Could not locate file \'%s\'.' % args.filename)
        exit()

    project = Project()
    project.load_json(args.filename)

    start_time = time.time()

    for _, output in project.output.items():
        image = output.generate_image(JOB_SIZE)
        if image is not None:
            image.save(output.filename)
            # image.show()

    print('Imagegen took %s seconds to generate.' % (time.time() - start_time))
