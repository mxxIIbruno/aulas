"""
    Aula sobre Threads
"""
from time import sleep
from threading import Thread


class MeuThreads(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThreads('Threads 1', 5)
t1.start()

t2 = MeuThreads('Threads 2', 5)
t2.start()

t3 = MeuThreads('Threads 3', 5)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
