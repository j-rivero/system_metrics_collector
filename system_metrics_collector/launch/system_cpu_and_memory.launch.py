# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

"""Launch system CPU and system memory metrics collector nodes."""


from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Run system CPU and memory collector nodes using launch."""
    ld = LaunchDescription([
        Node(
            package='system_metrics_collector',
            node_executable='linux_cpu_collector',
            output='screen'),
        Node(
            package='system_metrics_collector',
            node_executable='linux_memory_collector',
            output='screen'
        ),
    ])
    return ld
