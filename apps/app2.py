import time
import random

from multiprocessing.dummy.connection import Connection
from sistema import Sistema

class Main(Sistema):
    def rand_grade(self,pipe: Connection):
        while self.running:
            rand=random.randint(0,5000) % 10
            print(rand)
            pipe.send({
                        "cmd": "send",
                        "src": "application/random1",
                        "dst": "GestorArc",
                        "msg": f"log:Nota generada {rand}"
                    })

            if  rand < 3:
                self.running = False
                pipe.send({
                    "codterm": 2,
                    "msg": "Error"
                })

            if rand > 5:
                raise Exception("Out Exception")
        
            time.sleep(5)