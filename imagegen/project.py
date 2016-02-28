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

import json
from .loader import create_nodes, create_output


class Project:
    def __init__(self):
        self.nodes = {}
        self.output = {}

    def load_json(self, path):
        with open(path) as f:
            data = json.load(f)
            self.nodes = create_nodes(data)
            self.output = create_output(data, self.nodes)
