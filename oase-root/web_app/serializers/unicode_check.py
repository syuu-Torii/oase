# Copyright 2019 NEC Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys

class UnicodeCheck:

    NON_BMP_MAP = range(0x10000, sys.maxunicode + 1)

    def is_emotion(self, input_values):

        values_list = []

        for emo in input_values:
            int_emo = int(ord(emo))
            if int_emo in self.NON_BMP_MAP:
                values_list.append(emo)

        return values_list

