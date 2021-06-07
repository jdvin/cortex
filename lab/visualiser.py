import pygame, sys
from pygame.locals import *
import math as m
import colours as col
from nodes import Glia, Receptor, Neuron
from config.simulationParameters import visualisation_parameters as params

class Visualiser():
    def __init__(self, network, network_map):
        self.node_dims = params['node_dims']
        self.node_gap = params['node_gap']
        self.network_gap = params['network_gap']

        self.network_origins = []
        
        # set top left origin for network
        _x_origin = params['x_origin']
        _y_origin = params['y_origin']

        _x = _x_origin
        _y = _y_origin

        # assign each numbered point in the network map their top left origin coordinates
        # for all the layers
        for i in range(len(network)):
            # iterate through the network map from top left to bottom right
            for j in range(len(network_map)):
                for k in range(len(network_map[j])):
                    # if this location on the network map is marked for layer[i]
                    if network_map[j][k] == i + 1:
                        #append the network origins with the origin information layer[i]
                        self.network_origins.append([_x, _y])
                    _x += self.network_gap
                _x = _x_origin
                _y += self.network_gap
            _y = _y_origin

        for i in range(len(network)):
            for node in network[i].layer:
                # calcualte nodes absolute position form their relative layer position scaled by network location (origin)
                node.real_position = [self.network_origins[i][0] + node.position[0] * self.node_gap, 
                                      self.network_origins[i][1] + node.position[1] * self.node_gap]

    def draw_synapses(self, neuron, display):
        #for all d_synapses
        for d_syn in neuron.d_synapses:
            #the default colour is red
            colour = col.RED
            #if the presyanptic neuron is transmitting
            if d_syn[0].is_transmitting:
                #if the neuron is excitatory; colour is green
                if d_syn[1] == 1: colour = col.GREEN
                #if the neuron is inhibitory; colour is blue
                else: colour = col.BLUE
            #else if the presynaptic neuron is active; colour is yellow
            elif d_syn[0].is_active: colour = col.YELLOW
            #draw the synapse
            pygame.draw.line(display, colour, d_syn[0].real_position, neuron.real_position, 4)

        #for all d_synapses
        for m_syn in neuron.m_synapses:
            #the default colour is red
            colour = col.RED
            #if the presyanptic neuron is transmitting
            if m_syn[0].is_transmitting:
                #if the neuron is excitatory; colour is green
                if m_syn[1] == 1: colour = col.GREEN
                #if the neuron is inhibitory; colour is blue
                else: colour = col.BLUE
            #else if the presynaptic neuron is active; colour is yellow
            elif m_syn[0].is_active: colour = col.YELLOW
            #draw the synapse
            pygame.draw.line(display, colour, m_syn[0].real_position, neuron.real_position, 4)


    def draw_node(self, node, origin, display):
        #default colour is red
        colour = col.RED
        #if node is transmitting set colour to green
        if node.is_transmitting: colour = col.GREEN
        #else if node is active set colour to yellow
        elif node.is_active: colour = col.YELLOW

        # draw shape according to node identity
        if isinstance(node, Glia): 
            pygame.draw.circle(display, colour, node.real_position, self.node_dims, 1)
        elif isinstance(node, Neuron): 
            pygame.draw.circle(display, colour, node.real_position, self.node_dims)
        elif isinstance(node, Receptor): 
            pygame.draw.rect(display, colour, Rect(node.real_position[0]-(self.node_dims/2), _draw_position[1]-(self.node_dims/2), self.node_dims, self.node_dims))

    # draw all the layers in the network
    def draw_layers(self, layers, network_map, display):
        for i in range(len(layers)):
            for node in layers[i].layer:
                self.draw_node(node, self.network_origins[i], display)
                #self.draw_synapses(node, display)
