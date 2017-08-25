import sys
import os
if sys.version_info < (3,0):
    raise Exception('Please use Python version 3 or greater.')

sys.path.append(os.path.join(os.path.dirname(__file__), './'))
from qiskit import QuantumProgram,QuantumCircuit
from Qconfig import *

def QISKit_AND_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='AND_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 3)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])

    qCircuit.ccx(qRegister[0],qRegister[1],qRegister[2])
    qCircuit.measure(qRegister[2], cRegister[0])
    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_OR_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='OR_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 3)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])
    qCircuit.cx(qRegister[0], qRegister[2])
    qCircuit.ccx(qRegister[0],qRegister[1],qRegister[2])
    qCircuit.cx(qRegister[1], qRegister[2])
    qCircuit.measure(qRegister[2], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_NOT_Gate(x):
    backend ='local_qasm_simulator'
    Circuit='NOT_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 1)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    qCircuit.x(qRegister[0])
    qCircuit.measure(qRegister[0], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_NAND_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='NAND_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 3)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])

    qCircuit.ccx(qRegister[0],qRegister[1],qRegister[2])
    qCircuit.x(qRegister[2])
    qCircuit.measure(qRegister[2], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_NOR_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='NOR_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 3)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])
    qCircuit.cx(qRegister[0], qRegister[2])
    qCircuit.ccx(qRegister[0],qRegister[1],qRegister[2])
    qCircuit.cx(qRegister[1], qRegister[2])
    qCircuit.x(qRegister[2])
    qCircuit.measure(qRegister[2], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_EXOR_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='EXOR_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 2)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])
    qCircuit.cx(qRegister[0], qRegister[1])
    qCircuit.measure(qRegister[1], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result = result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKit_EXNOR_Gate(x,y):
    backend ='local_qasm_simulator'
    Circuit='EXNOR_GATE'
    qProgram = QuantumProgram()
    qRegister = qProgram.create_quantum_register('q1', 2)
    cRegister = qProgram.create_classical_register('c1', 1)
    qCircuit = qProgram.create_circuit(Circuit, [qRegister], [cRegister])

    if (x == 1):
        qCircuit.x(qRegister[0])
    if (y == 1):
        qCircuit.y(qRegister[1])
    qCircuit.cx(qRegister[0], qRegister[1])
    qCircuit.x(qRegister[1])
    qCircuit.measure(qRegister[1], cRegister[0])

    qobj = qProgram.compile([Circuit], backend=backend)
    result = qProgram.run(qobj, wait=2, timeout=240)
    dic_result=result.get_counts(Circuit)
    max_prob_key = max(dic_result, key=dic_result.get)
    return int(max_prob_key)

def QISKIT_Half_Adder_Circuit(A,B):
    S=QISKit_EXOR_Gate(A,B)
    C=QISKit_AND_Gate(A,B)
    return S,C

def QISKIT_Full_Adder_Circuit(A,B,Cin):
    AB_S,AB_C=QISKIT_Half_Adder_Circuit(A, B)
    Sum,ABC_C=QISKIT_Half_Adder_Circuit(Cin,AB_S)
    Cout = QISKit_OR_Gate(ABC_C,AB_C)
    return Sum, Cout

def QISKIT_Half_Sub_Circuit(A,B):
    D = QISKit_EXOR_Gate(A, B)
    notA=QISKit_NOT_Gate(A)
    Br=QISKit_AND_Gate(notA,B)
    return D,Br

def QISKIT_Full_Sub_Circuit(A,B,Bin):
    AB_D,AB_Br=QISKIT_Half_Sub_Circuit(A, B)
    Diff,ABC_Br=QISKIT_Half_Sub_Circuit(AB_D,Bin)
    Bout = QISKit_OR_Gate(ABC_Br,AB_Br)
    return Diff,Bout

def QISKIT_Add(A_num,B_num):
    Cin=0
    A_bin=bin(A_num)[2:]
    B_bin=bin(B_num)[2:]
    if len(A_bin)>len(B_bin):
        cipher = len(A_bin)
    else:
        cipher = len(B_bin)
    A_bin = A_bin.zfill(cipher)
    B_bin = B_bin.zfill(cipher)
    ret=''
    for i in range(cipher-1,-1,-1):
        Sum, Cin = QISKIT_Full_Adder_Circuit(int(A_bin[i]),int(B_bin[i]),Cin)
        ret= str(Sum) + ret
    ret=int(str(Cin) + ret,2)
    return ret

print('AND_Gate(0,0) : %s'%(QISKit_AND_Gate(0,0)))
print('AND_Gate(0,0) : %s'%(QISKit_AND_Gate(0,1)))
print('AND_Gate(0,0) : %s'%(QISKit_AND_Gate(1,0)))
print('AND_Gate(0,0) : %s'%(QISKit_AND_Gate(1,1)))

print('Or_Gate(0,0) : %s'%(QISKit_OR_Gate(0,0)))
print('Or_Gate(0,0) : %s'%(QISKit_OR_Gate(0,1)))
print('Or_Gate(0,0) : %s'%(QISKit_OR_Gate(1,0)))
print('Or_Gate(0,0) : %s'%(QISKit_OR_Gate(1,1)))

print('NOT_Gate(0) : %s'%(QISKit_NOT_Gate(0)))
print('NOT_Gate(1) : %s'%(QISKit_NOT_Gate(1)))

print('NAND_Gate(0,0) : %s'%(QISKit_NAND_Gate(0,0)))
print('NAND_Gate(0,0) : %s'%(QISKit_NAND_Gate(0,1)))
print('NAND_Gate(0,0) : %s'%(QISKit_NAND_Gate(1,0)))
print('NAND_Gate(0,0) : %s'%(QISKit_NAND_Gate(1,1)))

print('NOR_Gate(0,0) : %s'%(QISKit_NOR_Gate(0,0)))
print('NOR_Gate(0,0) : %s'%(QISKit_NOR_Gate(0,1)))
print('NOR_Gate(0,0) : %s'%(QISKit_NOR_Gate(1,0)))
print('NOR_Gate(0,0) : %s'%(QISKit_NOR_Gate(1,1)))

print('EXOR_Gate(0,0) : %s'%(QISKit_EXOR_Gate(0,0)))
print('EXOR_Gate(0,0) : %s'%(QISKit_EXOR_Gate(0,1)))
print('EXOR_Gate(0,0) : %s'%(QISKit_EXOR_Gate(1,0)))
print('EXOR_Gate(0,0) : %s'%(QISKit_EXOR_Gate(1,1)))

print('EXNOR_Gate(0,0) : %s'%(QISKit_EXNOR_Gate(0,0)))
print('EXNOR_Gate(0,0) : %s'%(QISKit_EXNOR_Gate(0,1)))
print('EXNOR_Gate(0,0) : %s'%(QISKit_EXNOR_Gate(1,0)))
print('EXNOR_Gate(0,0) : %s'%(QISKit_EXNOR_Gate(1,1)))

print('Half_Adder_Gate(0,0) : %s,%s'%(QISKIT_Half_Adder_Circuit(0,0)))
print('Half_Adder_Gate(0,0) : %s,%s'%(QISKIT_Half_Adder_Circuit(0,1)))
print('Half_Adder_Gate(0,0) : %s,%s'%(QISKIT_Half_Adder_Circuit(1,0)))
print('Half_Adder_Gate(0,0) : %s,%s'%(QISKIT_Half_Adder_Circuit(1,1)))

print('Full_Adder_Gate(0,0,0) : %s,%s'%(QISKIT_Full_Adder_Circuit(0,0,0)))
print('Full_Adder_Gate(0,0,1) : %s,%s'%(QISKIT_Full_Adder_Circuit(0,0,1)))
print('Full_Adder_Gate(0,1,0) : %s,%s'%(QISKIT_Full_Adder_Circuit(0,1,0)))
print('Full_Adder_Gate(0,1,1) : %s,%s'%(QISKIT_Full_Adder_Circuit(0,1,1)))
print('Full_Adder_Gate(1,0,0) : %s,%s'%(QISKIT_Full_Adder_Circuit(1,0,0)))
print('Full_Adder_Gate(1,0,1) : %s,%s'%(QISKIT_Full_Adder_Circuit(1,0,1)))
print('Full_Adder_Gate(1,1,0) : %s,%s'%(QISKIT_Full_Adder_Circuit(1,1,0)))
print('Full_Adder_Gate(1,1,1) : %s,%s'%(QISKIT_Full_Adder_Circuit(1,1,1)))

print('Half_Sub_Gate(0,0) : %s,%s'%(QISKIT_Half_Sub_Circuit(0,0)))
print('Half_Sub_Gate(0,0) : %s,%s'%(QISKIT_Half_Sub_Circuit(0,1)))
print('Half_Sub_Gate(0,0) : %s,%s'%(QISKIT_Half_Sub_Circuit(1,0)))
print('Half_Sub_Gate(0,0) : %s,%s'%(QISKIT_Half_Sub_Circuit(1,1)))

print('Full_Sub_Gate(0,0,0) : %s,%s'%(QISKIT_Full_Sub_Circuit(0,0,0)))
print('Full_Sub_Gate(0,0,1) : %s,%s'%(QISKIT_Full_Sub_Circuit(0,0,1)))
print('Full_Sub_Gate(0,1,0) : %s,%s'%(QISKIT_Full_Sub_Circuit(0,1,0)))
print('Full_Sub_Gate(0,1,1) : %s,%s'%(QISKIT_Full_Sub_Circuit(0,1,1)))
print('Full_Sub_Gate(1,0,0) : %s,%s'%(QISKIT_Full_Sub_Circuit(1,0,0)))
print('Full_Sub_Gate(1,0,1) : %s,%s'%(QISKIT_Full_Sub_Circuit(1,0,1)))
print('Full_Sub_Gate(1,1,0) : %s,%s'%(QISKIT_Full_Sub_Circuit(1,1,0)))
print('Full_Sub_Gate(1,1,1) : %s,%s'%(QISKIT_Full_Sub_Circuit(1,1,1)))

print('10 + 30 = %s'%(QISKIT_Add(10,30)))