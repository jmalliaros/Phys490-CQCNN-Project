import csv
import os
from generate_graphs import *
from classical_walk import random_walk
from qwalk import qwalk_me
import numpy as np
from tqdm import tqdm
import argparse

# number of nodes in graph
nodes = [8]
# number of graphs
# size = 4000
# shots = 10


def write_csv(graph_data, n, size, shots):
    folder_path = os.path.abspath(os.path.join(__file__, "../.."))
    file_path = os.path.join(folder_path, 'data/graphs_{}.csv'.format(n))
    # Loading bar
    pbar = tqdm(total=size*shots, ascii=True)
    with open(file_path, "w", newline='') as f:
        graph_writer = csv.writer(f, delimiter = ' ',)

        for graph in graph_data:
            q_count_list = []
            c_count_list = []

            for i in range(shots):
                classical_count = random_walk(*graph)
                quantum_count, quantum_probs = qwalk_me(*graph)
                c_count_list.append(classical_count)
                q_count_list.append(quantum_count)
                pbar.update(1)

            avg_classical_count = np.average(c_count_list)
            avg_quantum_count = np.average(q_count_list)

            row = graph[0].reshape(-1).tolist() + [graph[1], graph[2], avg_classical_count, avg_quantum_count]
            graph_writer.writerow(row)

            # if (avg_classical_count > avg_quantum_count):
            #     print(row)

        pbar.close()


if __name__ == '__main__':
    # Command line arguments
    parser = argparse.ArgumentParser(description='Generate n node graph data saved at data/graphs_n.csv')
    parser.add_argument('-n', default=10, type=int,
                        help='number of nodes for the graph')
    parser.add_argument('-size', default=1000, type=int,
                        help='size of the dataset to generate (default=1000)')
    parser.add_argument('-shots', default=10, type=int,
                        help='number of times where quantum and classical walks are repeated for a graph (default=10)')
    args = parser.parse_args()

    graph_dataset = generate_graph_data(args.n, args.size)
    write_csv(graph_dataset, args.n, args.size, args.shots)
