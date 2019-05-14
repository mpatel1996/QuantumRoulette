# begin with importing essential libraries for IBM Q
from qiskit import IBMQ, BasicAer, execute
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit

# set up Quantum Register and Classical Register for 3 qubits
q = QuantumRegister(2)
c = ClassicalRegister(2)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)
qc.h(q)
qc.measure(q, c)


def answer():
    myint = 0
    died = 0
    print('We are about to play 25 rounds of Russian Roulette. \nThere'
          ' are 4 players(00,01,10,11) in the game. \nYou are player 10. Will you survive?')

    while myint < 26:
        myint += 1
        job = execute(qc, backend=BasicAer.get_backend('qasm_simulator'), shots=1)
        result = job.result().get_counts(qc)
        for key in result.keys():
            state = key

        if state == '00':
            print('You survived but 00 died.\n')
        elif state == '01':
            print('You survived but 01 died.\n')
        elif state == '10':
            print('You Died. Sorry to see you go. RIP X-X\n')
            died += 1
        elif state == '11':
            print('You survived but 11 died.\n')
        else:
            print('Error 404: No players Found.')
    print("you died", died, "times in 25 rounds of RR")


answer()
