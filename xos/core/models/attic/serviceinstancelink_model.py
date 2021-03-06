
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def __xos_save_base(self, *args, **kwargs):
    subCount = sum([1 for e in [self.subscriber_service, self.subscriber_service_instance, self.subscriber_network] if e is not None])
    if (subCount > 1):
        raise XOSConflictingField(
            "Only one of subscriber_service, subscriber_service_instance, subscriber_network should be set")


def delete(self, *args, **kwargs):
    provider_service_instance = self.provider_service_instance
    super(ServiceInstanceLink, self).delete(*args, **kwargs)

    # This should be handled by a model_policy, but we don't currently have a
    # model policy for core objects, so handle it during the save method.
    if provider_service_instance and (not provider_service_instance.deleted):
        provider_service_instance.link_deleted_count += 1
        provider_service_instance.save(always_update_timestamp=True, update_fields=["updated", "link_deleted_count"])
