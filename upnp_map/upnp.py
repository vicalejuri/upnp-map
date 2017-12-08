try:
    import miniupnpc
    has_upnp = True
except ImportError:
    has_upnp = False

import threading
import time

class UPNPThread(threading.Thread):
    TIMEOUT = 60 * 60 * 3   # 3 hour refresh

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.internal_port = None
        self.external_port = None

        if has_upnp:
            self.upnp = UPNP(self.app)
        self._running = False

    def stop(self):
        if self.upnp is not None:
            try:
                self.upnp.removePortForward(self.external_port)
            except Exception as e:
                pass
        
        self._running = False

    def run(self, internal_port, external_port):
        self._running = True

        self.internal_port = internal_port
        self.external_port = external_port

        while self._running:
            if self.internal_port is not None and self.external_port is not None and self.upnp is not None:
                try:
                    self.upnp.addPortForward(self.internal_port, self.external_port)
                except Exception as e:
                    pass

            time.sleep(self.TIMEOUT)


class UPNP():
    def __init__(self, app):
        self.app = app
        if has_upnp:
            self.upnp = miniupnpc.UPnP()
            self.upnp.discoverdelay = 10

    def addPortForward(self, internal_port, external_port):
        try:
            if has_upnp:
                discover = self.upnp.discover()
                igd = self.upnp.selectigd()
                port_result = self.upnp.addportmapping(external_port, 'TCP', self.upnp.lanaddr, internal_port, 'www.me', '')

                pp_url = lambda ip,port: 'http://%s:%s' % (ip, port)

                addresses = {'local': pp_url(self.upnp.lanaddr, internal_port),
                             'external': pp_url( self.upnp.externalipaddress(), external_port) }                

                self.app.logger.info("Port Forward Attempt: Mapping {1} --> {0} ... {2}".format( 
                    addresses['local'], addresses['external'], (port_result and 'OK' or 'FAILED')))
            else:
                raise ValueError('Missing library: miniupnpc - install using pip')

        except Exception as e:
            raise

    def removePortForward(self, external_port):
        try:
            if has_upnp:
                discover = self.upnp.discover()
                igd = self.upnp.selectigd()
                port_result = self.upnp.deleteportmapping(external_port, 'TCP')

                self.app.logger.info("Port Delete Attempt: ~{0} ... {1}".format( external_port, port_result and 'OK' or 'FAILED'))
            else:
                raise ValueError('Missing library: miniupnpc - install using pip')

        except Exception as e:
            raise