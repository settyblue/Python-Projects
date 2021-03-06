__author__ = 'rakshith'

import networkx as nx
import numpy
import os
import json

def compute_correlation(dict1, dict2):
    keys = list(dict1.viewkeys() | dict2.viewkeys())
    return numpy.corrcoef([dict1.get(x, 0) for x in keys],[dict2.get(x, 0) for x in keys])[0, 1]

def graph_from_file(input_file):
    file = open(input_file)
    lines = file.readlines()
    line_count = 0
    graph = nx.DiGraph()
    for line in lines:
        if line_count < 4 and input_file != './facebook_data/facebook_combined.txt':
            line_count += 1
            continue
        else:
            line_count += 1
            graph.add_edge(line.split()[0],line.split()[1])
    return graph

def compute_graph_parameters(graph,i=0):
    graph_parameters = {}
    if nx.is_directed(graph):
        graph_parameters['in_degree_centrality'] = nx.in_degree_centrality(graph)
        graph_parameters['out_degree_centrality'] = nx.out_degree_centrality(graph)
    else:
        graph_parameters['degree_centrality'] = nx.degree_centrality(graph)
    graph_parameters['closeness_centrality'] = nx.closeness_centrality(graph)
    graph_parameters['betweenness_centrality'] = nx.betweenness_centrality(graph)
    if i==0:
        graph_parameters['eigenvector_centrality'] = nx.eigenvector_centrality(graph)
    graph_parameters['pagerank_centrality'] = nx.pagerank(graph,alpha=0.85)
    graph_parameters['clustering'] = nx.clustering(graph.to_undirected())
    return graph_parameters

def compute_correlation_matrix(graph_parameters_dict):
    correlation_matrix = []
    for key1 in graph_parameters_dict:
        list1 = []
        for key2 in graph_parameters_dict:
            list1.append(compute_correlation(graph_parameters_dict[key1],graph_parameters_dict[key2]))
        correlation_matrix.append(list1)
    return correlation_matrix

def dict_matrix_listofists(graph_parameters_dict):
    matrix = []
    for key1 in graph_parameters_dict:
        list1 = []
        print key1
        for key2 in graph_parameters_dict[key1]:
            list1.append(graph_parameters_dict[key1][key2])
        matrix.append(list1)
    return matrix

def run():

    files = [f for f in os.listdir('./data/')]
    for input_data_file in files:
        data_graph = graph_from_file('./data/'+input_data_file)
        print 'Dataset Name : ',input_data_file
        print 'Number of Edges = ',data_graph.number_of_edges()
        print 'Number of Nodes = ',data_graph.number_of_nodes()
        if not os.path.exists('./graphml/'):
            os.makedirs('./graphml/')
        nx.write_graphml(data_graph, './graphml/'+input_data_file+".graphml")
        graph_characteristics = compute_graph_parameters(data_graph)
        #print graph_characteristics
        correlation_matrix =  compute_correlation_matrix(graph_characteristics)
        correlation_array_to_print = numpy.array(correlation_matrix)
        #mat2 = numpy.array(dict_matrix_listofists(graph_characteristics))
        print correlation_array_to_print
        if not os.path.exists('./output/'):
            os.makedirs('./output/')
        output_filename = './output/'+input_data_file+"_out"
        output_file = open(output_filename,"wb")
        json.dump(dict_matrix_listofists(graph_characteristics),output_file)
        output_file.close()
        print '-----------------'
        print

    files = [f for f in os.listdir('./facebook_data')]
    for input_data_file in files:
        print 'file read : ' + input_data_file
        data_graph = graph_from_file('./facebook_data/'+input_data_file)
        print 'Dataset Name : ',input_data_file
        print 'Number of Edges = ',data_graph.number_of_edges()
        print 'Number of Nodes = ',data_graph.number_of_nodes()
        nx.write_graphml(data_graph, './graphml/'+input_data_file+".graphml")
        graph_characteristics = compute_graph_parameters(data_graph,1)
        #print graph_characteristics
        correlation_matrix =  compute_correlation_matrix(graph_characteristics)
        correlation_array_to_print = numpy.array(correlation_matrix)
        #mat2 = numpy.array(dict_matrix_listofists(graph_characteristics))
        print 'Correlation Matrix : '
        print correlation_array_to_print
        output_filename = './output/'+input_data_file+"_out"
        output_file = open(output_filename,"wb")
        print 'Column IDs :'
        json.dump(dict_matrix_listofists(graph_characteristics),output_file)
        output_file.close()
run()
