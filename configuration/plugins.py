# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }

#PLUGINS = ["netbox_secrets"]

# PLUGINS_CONFIG = {
#   "netbox_secretstore": {
#     ADD YOUR SETTINGS HERE
#   }
# }

# In your configuration.py
PLUGINS = ["netbox_topology_views"]
