# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""`gcloud iot devices create` command."""

from __future__ import absolute_import
from __future__ import unicode_literals

from googlecloudsdk.api_lib.cloudiot import devices
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iot import flags
from googlecloudsdk.command_lib.iot import resource_args
from googlecloudsdk.command_lib.iot import util
from googlecloudsdk.core import log


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.GA)
class Create(base.CreateCommand):
  """Create a new device."""

  @staticmethod
  def Args(parser):
    resource_args.AddDeviceResourceArg(parser, 'to create')
    flags.AddDeviceFlagsToParser(parser)
    flags.AddDeviceCredentialFlagsToParser(parser)

  def Run(self, args):
    client = devices.DevicesClient()

    device_ref = args.CONCEPTS.device.Parse()
    registry_ref = device_ref.Parent()

    credentials = util.ParseCredentials(args.public_keys,
                                        messages=client.messages)
    metadata = util.ParseMetadata(args.metadata, args.metadata_from_file,
                                  client.messages)

    response = client.Create(
        registry_ref, device_ref.devicesId,
        blocked=args.blocked,
        credentials=credentials,
        metadata=metadata
    )
    log.CreatedResource(device_ref.devicesId, 'device')
    return response
