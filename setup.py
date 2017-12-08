from setuptools import setup

setup(
   name='upnp_map',
   version='0.1.1',
   description='Minimal `upnp-map` tool. Useful to allow TCP conections on port X from the internet to this machine',
   author='bbfc',
   author_email='rainbrowcorals@gmail.com',
   url='https://github.com/barrabinfc/upnp-map',
# download_url = 'https://github.com/barrabinfc/upnp-map/archive/0.1.tar.gz', # I'll explain this in a second
   packages=['upnp_map'],  
   install_requires=['miniupnpc'], 
   scripts=[
       'bin/upnp-map'
   ],
   keywords=['upnp','port mapping','firewall-hole','nat-hole','nat-traversal']
)
