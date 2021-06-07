import pygame, sys
from pygame.locals import *

class Glia():
    def __init__ (self,position):
        self.position =position
        self.is_transmitting = False
        self.is_active = False

class Receptor():
    def __init__ (self,position,bound_key):
        self.position =position
        self.bound_key =bound_key
        self.is_transmitting = False
        self.is_active = False

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.bound_key]:
            self.is_transmitting = True
        else:
            self.is_transmitting = False


class Neuron():
    #neurons recieve streaming input from ddirect synapses which can be either
    #excitatory (positive) or inhibitory (negative)
    #each time step this input is summed
    #if the sum is greater than the threshold the neuron is activated
    #if the neuron is active it transiently;
    #stops taking input, sends an outward signal, reactivates(after refractory), counts if it is reactivated shortly after the last
    #if the neuron is continuously reactivted it gradually increases its threshold
    #if a neuron is unactivated for long periods of time it will lower its threshold
    #neurons also have modulatory synapses which can effect the threshold of the synapse
    #these operate similarly in that all modulatory synapses on a neuron are summed and then change the threshold respectively
    #at the end of each timestep a neuron will leak some of its accumulated charge and its threshold will move towards baseline
    def __init__(self, position, real_position, d_synapses, m_syanpses, base_threshold, leak, refractory, duty_period):
        #location of the neuron in layer space
        self.position =position
        #location of the neuron in network space
        self.real_position = real_position
        #direct_synapses [<0>presynaptic neuron object, <1>type of action (-1 or +1), <2>permance of synapse]
        self.d_synapses =d_synapses
        #modulatory_synapses [<0>presynaptic neuron object, <1>type of action (-1 or +1), <2>permanace of synapse]
        self.m_synapses =m_syanpses
        #sum of direct synaptic inputs
        self.sum = 0
        #threshold the neuron will tend to if left alone
        self.base_threshold = base_threshold
        #the current action potential threshold of the neuron
        self.threshold = self.base_threshold
        #rate in which sum is pushed towards 0
        self.leak = leak
        #the refractory period of the neuron
        self.refractory = refractory
        #the time left in the current refractory period
        self.t_refractory = 0
        #is the neuron active?
        self.is_active = False
        # was the neuron active last time step?
        self.was_active = False
        #is this neuron transmitting?
        self.is_transmitting = False
        #preiod of time during which successive activations of the neuron will add to its active duty
        self.duty_period = duty_period
        #time left in the current duty period
        self.t_duty_period = 0
        #amount of times the neuron has been successively activate within its duty period
        self.active_duty = 0
        #note most learning for organisms is on a negatively accelerating learning curve
        #what will the learning model for this neuron be? all or none? above a threshold?

    def homeostasis(self):
        #increment charge towards 0
        if self.sum < 0: self.sum += self.leak
        if self.sum > 0: self.sum -= self.leak
        #habituation and adaption here (i think)

    def receive_input(self):
        #loop through all direct synapses
        # TODO: condense into list comprehension once working
        for d_syn in self.d_synapses:
            #if the signal from the neuron syanpsed by d_syn is active then add its (sign*permanence) to sum
            if d_syn[0].is_active:
                self.sum += (d_syn[1]*d_syn[2])

        #loop through all modulatory synapses
        # TODO: condense into list comprehension once working
        for m_syn in self.m_synapses:
            #if the signal from the neuron syanpsed by m_syn is active then add its (sign*permanance) to threshold
            if m_syn[0].is_active: 
                self.threshold += (m_syn[1]*m_syn[2])

    def activation_logic(self):
        #activate neuron
        self.is_active = True
        #begin refractory period
        self.t_refractory = self.refractory
        #transmit signal
        self.is_transmitting = True
        #if the last duty period is not over
        if self.t_duty_period > 0:
            #increment active duty
            self.active_duty += 1
        #if the last duty period finsihed
        else:
            #either decrement active duty or wipe it; which of these is better?
            if self.active_duty > 0: self.active_duty -= 1
            #self.active_duty = 0

    #_signals is an array of booleans for every neuron in thenetwork corresponding to their binary activation
    #receives inputs, control duty period, control refractory
    def update_t1(self):
        #if not active
        if not self.is_active:
            self.was_active = False
            #receive input
            self.receive_input()
            #decrement time until end of duty period
            if self.t_duty_period > 0: self.t_duty_period -= 1
        #if active
        else:
            #decrement remaining time in current refractory period
            self.t_refractory -= 1

    #control activity
    def update_t2(self):
        #if active
        if self.is_active:
            #stop transmitting
            self.is_transmitting = False
            #if current refractory period is over
            if self.t_refractory == 0:
                #deactivate neuron
                self.is_active = False
                # flag that the neuron was active last timestep
                self.was_active = True
                #begin duty period countdown
                self.t_duty_period = self.duty_period
        #if not active
        else:
            #if sum is greater than or equal to threshold
            if self.sum >= self.threshold:
                self.activation_logic()

        self.homeostasis()


    def get_synapse(self, pre_node, valence):
        for d_syn in self.d_synapses:
            if d_syn[0] == pre_node and d_syn[1] == valence:
                return d_syn
