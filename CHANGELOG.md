# 2.1.0

* API: In memory inventory. Generating a inventory file is not mandatory anymore.
       On can pass the provider roles in most of the API calls.
* VMonG5K: allow to specify a working directory
* Dependencies: Upgrade Ansible to latest stable (2.7.x)

# 2.0.2

* (breaking) VMonG5K/Vagrant: Unify code. `flavour_desc` dict can be used after
  building the MachineConfiguration.

# 2.0.1

* VMonG5K: Package was missing site.yml file

# 2.0.0

Warning breaking changes:

* EnOSlib is python3.5+ compatible exclusively.

* Provider: a provider must be given a configuration object. You can build it
  from a dictionnary (this mimics EnOSlib 1.x) or build it programmaticaly. In
  pseudo code, changes are needed in your code as follow:
  ```
  from enoslib.infra.enos_g5k.configuration import Configuration
  from enoslib.infra.enos_g5k.provider import G5k
  ...
  conf = Configuration.from_dictionnary(provider_conf)
  g5k = G5k(conf)
  ...
  ```

* Provider: Configuration object
  The configuration object aim at ease the process of building configuration for
  providers. It can be validated against a jsonschema defined for each provider.
  Validation is implicit using `from_dictionnary` or explicit using the
  `finalize()` method of the configuration.

* Doc: Update docs to reflect the above

* VMonG5K: new provider that allows to start virtual machines on G5K.

# 1.12.3

* API: `utils.yml` playbook now forces fact gahering.
* Misc: initial gitlab-ci supports

# 1.12.2

* G5K: Refix an issue when number of nodes is zero

# 1.12.1

* G5K: fix an issue when number of nodes is zero

# 1.12.0

* API: `emulate|reset|validate` now accept an extra_vars dict
* G5K: `secondary_networks` are now a mandatory key
* G5K: support for zero nodes roles

# 1.11.2

* Make sure role and roles are mutually exclusive

# 1.11.1

* Fix empty `config_file` case in enostask

# 1.11.0

* G5K: add static oar job support

# 1.10.0

* G5K: align the subnet description with the other network
* API: validate_network now filters devices without ip address
* API: check_network now uses JSON serialisation to perform better

# 1.9.0

* G5K api: expose get_clusters_sites
* G5K: dhcp is blocking
* G5k: introduce drivers to interact with the platform

# 1.8.2

* Chameleon: fix flavor encoding
* Chameleon: Create one reservation per flavor
* Openstack: fix python3 compatibility

# 1.8.1

* relax openstack client constraints

# 1.8.0

* G5K api: expose exec_command_on_nodes
* Openstack: enable the use of session for blazar
* Openstack: Allow keystone v3 authentification

# 1.7.0

* G5K api: fixed get_clusters_interfaces function
* Ansible: group vars were'nt loaded
* Allow fake interfaces to be mapped to net roles

# 1.6.0

* G5K: add subnet support
* An enostask can now returns a value
* Openstack/Chameleon: support region name
* Openstack/Chameleon: support for extra prefix for the resources
* Chameleon: use config lease name

# 1.5.0

* python3 compatibility
* Confirm with predictable NIC names on g5k

# 1.4.0

* Fix the autodoc generation
* Document the cookiecutter generation
* Default to debian9 for g5k

# 1.3.0

* Change setup format
* Move chameleon dependencies to extra_require

# 1.2.1

* Drop validation of the bandwitdh
* Add missing host file

# 1.2.0

* Add reset network


# 0.0.6 

* add `min` keyword in machine descipriotn on for G5K

# 0.0.5

* reservation is supported in g5k provider
* `expand_groups` is available in the api
* `get_cluster_interfaces` is available in the g5k api.

# 0.0.4

* Exclude not involved machines from the tc.yml run
* Take force_deploy in g5k provider
* Wait ssh to be ready when `check_network=True` in `generate_inventory`
* Add start/end enostask logging

# 0.0.3

* Add static provider
* Add OpenStack provider (and chameleon derivatives)
* Add `provider_conf` validation
* Rearchitect providers
* Add dummy functionnal tests
* Add network emulation

# 0.0.2 

* Add fake interface creation option un check_network
* Encapsulate check_network in generate_inventory
* Add automatic discovery of network interfaces names/roles
* Add vagrant/g5k provider

# 0.0.1

* Initial version
