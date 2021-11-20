from __future__ import print_function
import numpy as np
import time
import pandas as pd
import math
from histogram import *
import matplotlib.pyplot as plt

data_dir = './data/'
save_dir = '/home/SharedData/priyadarshini/olfactory/'

mol_descriptor = []
ingred_molecule = []

def main():

    # mol_descp = np.load(data_dir+'pubchemId_descriptor_pairs.npy',allow_pickle=True)
    ingredient_molecule = np.load(data_dir+'molecule_entityId.npy',allow_pickle=True)
    print(ingredient_molecule, len(ingredient_molecule))
    flash()
    mol_descp = np.array(mol_descp)
    ingredient_molecule = np.array(ingredient_molecule)

    molecule_entityId = []
    for k in range(len(mol_descp)):
        pubchem = mol_descp[k, 0]
        temp = []
        for l in range(len(ingredient_molecule)):
            count = ingredient_molecule[l,1].count(pubchem)
            if count>0:
                temp.append(ingredient_molecule[l,0])
        
        molecule_entityId.append([pubchem, temp])

    print(molecule_entityId, len(molecule_entityId))
    np.save(data_dir+'molecule_entityId.npy', molecule_entityId)

    pubchem_ingredient = np.load(data_dir+'molecule_entityId.npy',allow_pickle=True)
    pubchem_ingredient = np.array(pubchem_ingredient)
    ingredient_len = [len(pubchem_ingredient[k,1]) for k in range(len(pubchem_ingredient))]
    print(ingredient_len, len(ingredient_len), np.max(ingredient_len), np.min(ingredient_len))
    plt.hist(ingredient_len, bins=range(np.min(ingredient_len), np.max(ingredient_len)),edgecolor="black")
    plt.ylabel('No of molecules')
    plt.xlabel('No of ingredients')
    plt.show()


    # mol_descp = np.array(mol_descp)
    # descriptor_len = [len(mol_descp[k,1]) for k in range(len(mol_descp))]
    # # print(descriptor_len, len(descriptor_len), np.max(descriptor_len), np.min(descriptor_len))
    # plt.hist(descriptor_len, bins=range(np.min(descriptor_len), np.max(descriptor_len)),edgecolor="black")
    # plt.ylabel('No of molecules')
    # plt.xlabel('No of descriptors')
    # plt.show()



if __name__ == '__main__':
    main()