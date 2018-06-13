# Copyright 2016 Google Inc. All Rights Reserved.
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

"""Helper methods for configuring deployment manager command flags."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib.deployment_manager import dm_api_util
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.command_lib.util.apis import arg_utils


RESOURCES_AND_OUTPUTS_FORMAT = """
    table(
      resources:format='table(
        name,
        type:wrap,
        update.state.yesno(no="COMPLETED"),
        update.error.errors.group(code),
        update.intent)',
      outputs:format='table(
        name:label=OUTPUTS,
        finalValue:label=VALUE)'
    )
"""

OPERATION_FORMAT = """
    table(
      name,
      operationType:label=TYPE,
      status,
      targetLink.basename():label=TARGET,
      error.errors.group(code),
      warnings.group(code)
    )
"""

DEPLOYMENT_FORMAT = """
    default(
      name, id, description, fingerprint,insertTime, manifest.basename(),
      labels, operation.operationType, operation.progress,
      operation.status, operation.user, operation.endTime, operation.startTime,
      operation.error, operation.warnings, update)
"""

_DELETE_FLAG_KWARGS = {
    'help_str': ('Delete policy for resources that will change as part of '
                 'an update or delete. `delete` deletes the resource while '
                 '`abandon` just removes the resource reference from the '
                 'deployment.'),
    'default': 'delete',
    'name': '--delete-policy'
}


def GetDeleteFlagEnumMap(policy_enum):
  return arg_utils.ChoiceEnumMapper(
      _DELETE_FLAG_KWARGS['name'],
      policy_enum,
      help_str=_DELETE_FLAG_KWARGS['help_str'],
      default=_DELETE_FLAG_KWARGS['default'])


def AddDeploymentNameFlag(parser):
  """Add properties flag."""
  parser.add_argument('deployment_name', help='Deployment name.')


def AddConfigFlags(parser):
  """Add flags for different types of configs."""
  parser.add_argument(
      '--config',
      help='Filename of a top-level yaml config that specifies '
      'resources to deploy.')

  parser.add_argument(
      '--template',
      help='Filename of a top-level jinja or python config template.')

  parser.add_argument(
      '--composite-type',
      help='Name of a composite type to deploy.')


def AddPropertiesFlag(parser):
  """Add properties flag."""

  parser.add_argument(
      '--properties',
      help='A comma separated, key:value, map '
      'to be used when deploying a template file or composite type directly.',
      type=arg_parsers.ArgDict(operators=dm_api_util.NewParserDict()),
      dest='properties')


def AddAsyncFlag(parser):
  """Add the async argument."""
  parser.add_argument(
      '--async',
      help='Return immediately and print information about the Operation in '
      'progress rather than waiting for the Operation to complete. '
      '(default=False)',
      dest='async',
      default=False,
      action='store_true')


def AddFingerprintFlag(parser):
  """Add the fingerprint argument."""
  parser.add_argument(
      '--fingerprint',
      help=('The fingerprint to use in requests to modify a deployment. If not '
            'specified, a get deployment request will be made to fetch the '
            'latest fingerprint. A fingerprint is a randomly generated value '
            'that is part of the update, stop, and cancel-preview request to '
            'perform optimistic locking. It is initially generated by '
            'Deployment Manager and changes after every request to modify '
            'data. The latest fingerprint is printed when deployment data is '
            'modified.'),
      dest='fingerprint')
