#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc. All Rights Reserved.
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

"""Bugs utilities."""

__author__ = 'alexto@google.com (Alexis O. Torres)'

import logging


# Allowed bug states.
ACTIVE = 'active'
RESOLVED = 'resolved'
CLOSED = 'closed'
UNKNOWN = 'unknown'


# Bug providers.
ISSUETRACKER = 'issuetracker'


class InvalidProvider(Exception):
  """Thrown when the caller uses an invalid bug provider."""
  pass


ISSUETRACKER_STATE_STATUS_MAP = {
    'untriaged': ACTIVE,
    'assigned': ACTIVE,
    'available': ACTIVE,
    'unconfirmed': ACTIVE,
    'awaitingtranslation': ACTIVE,
    'externaldependency': ACTIVE,
    'started': ACTIVE,
    'upstream': ACTIVE,
    'resolved': RESOLVED,
    'fixed': RESOLVED,
    'wontfix': CLOSED,
    'verified': CLOSED,
    'duplicate': CLOSED,
    'confirmed': CLOSED,
    'invalid': CLOSED,
    'unknown': UNKNOWN
}


def StateFromStatus(status, provider):
  """Maps status to a state of active, resolved, closed, or unknown."""
  lowered = status.lower()
  if cmp(provider, ISSUETRACKER) == 0:
    if lowered in ISSUETRACKER_STATE_STATUS_MAP:
      return ISSUETRACKER_STATE_STATUS_MAP[lowered]
    else:
      logging.error('Unrecognized IssueTracker status: %s', lowered)
      return UNKNOWN
  else:
    raise InvalidProvider('Unrecognized provider: %s' % provider)


def GetUserLink(provider, email):
  """Retrieves a url to the profile of the specified user on the given provider.

  Args:
    provider: The name of the provider
    email: The email alias of the user.
  Returns:
    Str of the url to the profile of the user.
  """
  # Using else as a catch-all to default to issue tracker.
  user_link = 'http://code.google.com/u/' + email.split('@')[0]
  return unicode(user_link).encode('utf-8', 'ignore')