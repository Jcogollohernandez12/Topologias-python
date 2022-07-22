from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel

class ThreeTopo(Topo):
    def build(self, h, s):
        hosts = []
        switches = []

        for pos in range(h):
            hosts.append(self.addHost('h%s'%pos))
            
        for pos in range(s):
            switches.append(self.addSwitch('sw%s'%pos))

        for pos in range(s):
            print("=====================================================")
            print('Iterando sobre el switch: %s'%pos)
            switch = switches[pos]

            # Add links of switches
            pregunta = int(input("Esta switch ya se conectado a otro switch? (1/0): "))            
            if(pregunta == 0):
                
                for pos_switch in range(s):
                    if(pos != pos_switch):
                        switch_conectar = switches[pos_switch]
                        pregunta_switch = int(input('Quiere conectar el switch ('+str(pos)+') con el switch ('+str(pos_switch)+') (1/0): '))
                        if(pregunta_switch == 1):
                            self.addLink(switch, switch_conectar)

            pregunta = int(input('Quiere conectar este switch con algun host? (1/0): '))
            if(pregunta == 1):    
                for pos_host in range(h):
                    host = hosts[pos_host]
                    pregunta_host = int(input('Quiere conectar el host ('+str(pos_host)+') con el switch ('+str(pos)+') (1/0): '))
                    if(pregunta_host == 1):
                        self.addLink(host, switch)
        

def Ejecutar():
    s = int(input("Cantidad de switches: "))
    h = int(input("Cantidad de hosts: "))    

    topo = ThreeTopo(h,s)
    controller=RemoteController('c0', ip="192.168.101.5", port=6633)
    net = Mininet(topo=topo, controller=controller)
    net.start()
    CLI(net)
    net.stop()
    
# Tell mininet to print useful information
if __name__ == "__main__":
    setLogLevel('info')
    Ejecutar()