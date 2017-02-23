#Python script to create a normal turing machine (that can also work as a binary turing machine)

#Some simple variables we should declare
tapeSize = 1000;



#Setup the tape
tape = [0] * tapeSize

#Los estados estaran declarados en el siguiente orden:
#[estado actual],[simbolo leido],[simbolo escribir],[direccion movimiento], [siguiente estado]
states = [['q1'],[0],[1],['r'],['q2']]
