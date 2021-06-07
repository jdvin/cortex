# import pygame, sys
# from pygame.locals import *
# import math as m
# import colours as col
# from nodes import glia, receptor, neuron
# import typist as t

# class Interface():

#     # TODO: nodes can be emphasised by left click
#     # TODO: emphasised nodes have thier values and synapses displayed in a menue on the right of the screeen
#     # TODO: emphasised nodes can be cycled via a button in the menue
#     # TODO: you can edit the synapses of the emphasised nodes by clicking them in the menue then entering new values in the console

#     def __init__(self):
#         self.d_neuron_values = "1;1;5;0"
#         self.t_pre = None
#         self.t_post = None
#         self.receptor_keys = [
#                                 pygame.K_0,
#                                 pygame.K_1,
#                                 pygame.K_2,
#                                 pygame.K_3,
#                                 pygame.K_4,
#                                 pygame.K_5,
#                                 pygame.K_6,
#                                 pygame.K_7,
#                                 pygame.K_8,
#                                 pygame.K_9
#                               ]

#     def generate_neuron(self,node):
#         print("press 'd' to use default neuron values else press 'a' to use alternate values")
#         print("d = 1;1;5;0 ELSE: enter <base_thresh;leak;refrac;duty_period>")
#         ip = None
#         while ip == None:
#             pygame.event.pump()
#             keys_down = pygame.key.get_pressed()
#             if keys_down[pygame.K_d]:
#                 ip = 'd'
#             elif keys_down[pygame.K_a]:
#                 ip = input('-->')
#         if ip == 'd': ip = self.d_neuron_values
#         ip = ip.split(';')
#         i_vals = [int(i) for i in ip]
#         return neuron(node.position, [], [], i_vals[0], i_vals[1], i_vals[2], i_vals[3])

#     def generate_receptor(self,node):
#             print("press key for receptor")
#             print("Keys 0 - 9")
#             key = None
#             while key == None:
#                 pygame.event.pump()
#                 keys_down = pygame.key.get_pressed()
#                 for k in self.receptor_keys:
#                     if keys_down[k]: return receptor(node.position, k)

#     def cycle_node(self, node):
#         if isinstance(node, glia): return self.generate_neuron(node)
#         if isinstance(node, neuron): return self.generate_receptor(node)
#         if isinstance(node, receptor): return glia(node.position)

#     def node_interaction(self,cortex,node_dims):
#         #loop through cortex
#         for i in range(len(cortex)):
#             #make a shape out of the node position and dimensions
#             node_collider = Rect(cortex[i].position[0]-(_node_dims/2),cortex[i].position[1]-(_node_dims/2),node_dims,node_dims)
#             #if the aforementioned shape collides with the mouse
#             if node_collider.collidepoint(pygame.mouse.get_pos()):
#                 #return the index of the node represented by the shape and as well as the node it is to be replced by
#                 return [i, self.cycle_node(_cortex[i])]

#     def synapse_generation(self,cortex,node_dims):
#         if self.t_pre == None:
#             #loop through the cortex
#             for i in range (len(_cortex)):
#                 #create a shape out of the node position and dimensions
#                 node_collider = Rect(_cortex[i].position[0]-(_node_dims/2),cortex[i].position[1]-(_node_dims/2),node_dims,node_dims)
#                 #if the aforemtioned shape collides with the mouse
#                 if node_collider.collidepoint(pygame.mouse.get_pos()):
#                     #set the presynaptic temp to the index of that node
#                     self.t_pre = i
#                     print("right click postsynaptic neuron")
#         else:
#             #loop through the cortex
#             for j in range(len(_cortex)):
#                 #create a shape out of the nodes position and dimensions
#                 # TODO: maybe turn this very popular line of code into a function
#                 node_collider = Rect(_cortex[j].position[0]-(_node_dims/2),cortex[j].position[1]-(_node_dims/2),node_dims,node_dims)
#                 #if the aforementioned shape collides with the mouse and j is not equal to pre
#                 if node_collider.collidepoint(pygame.mouse.get_pos()) and j != self.t_pre:
#                     self.t_post = j
#                     #break
#                     print("enter synapse values: <type of synapse(d||m);action type(-1||+1);permanance>")
#                     ip = input('-->')
#                     ip = ip.split(';')
#                     ip_vals = [self.t_post, self.t_pre]
#                     [ip_vals.append(i) for i in ip]
#                     self.t_pre = None
#                     self.t_post = None
#                     return ip_vals
    
