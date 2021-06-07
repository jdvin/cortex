from layer import Layer
import numpy as np
import random as rand

class Factory():

    def __init__(self):
        self.layers = []

    def create_layer(self, dimensions, node_params, layer_params):
        """create a new layer and return it

        Keyword arguments
        dimensions -- [0] width, [1] height
        node_params -- config file for nodes
        """
        self.layers.append(Layer(dimensions, node_params, layer_params))
        return self.layers[-1]

    def stimulate_layer(self, stim_pattern, layer):
        """Bring a given subset of a layer to threshold

        Keyword arguments
        stim_pattern -- array of bools which display which nodes to stimulate
        layer -- the layer to stimulate
        """
        for i in range(len(stim_pattern)):
            if stim_pattern[i] == 1:
                layer[i].sum = layer[i].threshold

    def network_active_nodes(self):
        _network_active_nodes = []

        for l in self.layers:
            _network_active_nodes += l.layer_active_nodes()
        
        return _network_active_nodes

    def update(self):
        # update calculate neuron sums
        [n.update_t1() for l in self.layers for n in l.layer]
        # activate above threshold neurons
        [n.update_t2() for l in self.layers for n in l.layer]
        # update distal synaptic weights
        [l.update_distal_synapses() for l in self.layers]
        
    def train_network(self, layer, data):
        pass

    def generate_distal_synapses(self, layer_1, layer_2, is_bidirectional, proportion, valence, p_mean, p_sd):
        """creates synapses between layer_1 and layer_2
        
        Keyword arguments
        is_bidirectional -- False : synapses travel from layer_1 to layer_2, True : synapses are generated in both directions
        proportion -- cell from layer_1 connects to <proportion> of cells from layer_2
        valence -- 1: excitatory, -1: inhibitory
        p_mean -- permanence mean
        p_sd -- permanence sd for synapses
        """

        for post_node in layer_2:            
            # generate list of nodes in layer 1 to form synapses from
            _pool_size = int(len(layer_1) * proportion)
            _pool = rand.sample(range(len(layer_1)), _pool_size)
            
            # populate node in layer 2 (and layer 1 if bidirectional) with synapses using the pool
            for i in _pool:
                _permance = np.random.normal(p_mean, p_sd)
                post_node.d_synapses.append([layer_1[i], valence, _permance])
                if is_bidirectional:
                    layer_1[i].d_synapses.append([post_node, valence, _permance])
                
    def generate_proximal_synapses(self, pre_layer, post_layer, perm):
        
        for i in range(len(post_layer)):
            post_layer[i].d_synapses.append([pre_layer[i], 1, perm])



