# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import HpecfmAlarmsBaseAction


class loadDb(HpecfmAlarmsBaseAction):
    def run(self, events):

        mydb = self.client["app_db"]
        known = mydb["knownevents"]
        # process = mydb["processevents"]


        for event in events:
            myquery = { "u_uuid" : event['u_uuid'] }
            records = known.find(myquery).count()
            if records == 0:
                write_record = known.insert_one(event)
                # write_record = process.insert_one(event)
        return (records)


        return (self.client)
