from setuptools import setup

setup(
   name='upnp_map',
   version='0.1',
   description='Minimal `upnp-map` tool. Useful to allow TCP conections on port X from the internet to this machine',
   author='bbfc',
   author_email='barrabin.fc@gmail.com',
   packages=['upnp_map'],  
   install_requires=['miniupnpc'], 
   scripts=[
       'bin/upnp-map'
   ],
   keywords=['upnp','port mapping',
             'firewall-hole','nat-hole','nat-traversal']
)
