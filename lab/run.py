import pygame, sys
from pygame.locals import *
import math as m
from config import neuronParameters
from config import layerParameters
from nodes import Glia, Receptor, Neuron
from visualiser import Visualiser
#from interface import interface
from factory import Factory
from data.dataGenerator import *

# initialize engine
pygame.init()
# set screen width/height and caption
size = [1200, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cortex')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

#interface = interface()

layer_factory = Factory()

layer_dimensions = [5,5]
layer_size = layer_dimensions[0] * layer_dimensions[1]


input_layer = layer_factory.create_layer(layer_dimensions, neuronParameters.params, layerParameters.params)
inter_layer = layer_factory.create_layer(layer_dimensions, neuronParameters.params, layerParameters.params)
repre_layer = layer_factory.create_layer(layer_dimensions, neuronParameters.params, layerParameters.params)

syn_sparcity = 1

syn_scale = 5

layer_factory.generate_distal_synapses(input_layer.layer, inter_layer.layer, False, syn_sparcity, 1, 1/syn_scale, 0.25/syn_scale)
layer_factory.generate_distal_synapses(input_layer.layer, inter_layer.layer, False, syn_sparcity, -1, 0, 0)

#layer_factory.generate_proximal_synapses(inter_layer.layer, repre_layer.layer, 1)

#two dimensional array denoting 2d position of each layer
#indexes of network begin at 1, 0's denote no network at a location
network_map = [[1,2,3]]

stim_patterns = [random_stimulation(layer_size, 0.2) for i in range(3)]

vis = Visualiser(layer_factory.layers, network_map)

i = -1
flag = False

##:MAIN:##
# Loop until the user clicks close button
done = False
#initialise_cortex()
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # write sim logic here
    if flag:
        i += 1
        if i == len(stim_patterns):
            i = 0
    
        _input = stim_patterns[i]
        layer_factory.stimulate_layer(_input, input_layer.layer)
        flag = False
    else:
        flag = True

    layer_factory.update()

    # clear the screen before drawing
    screen.fill((50, 50, 50))

    # write draw code here
    vis.draw_layers(layer_factory.layers, network_map, screen)

    # display what’s drawn. this might change.
    pygame.display.update()

    # run at X fps
    clock.tick(1)

# close the window and quit
pygame.quit()
