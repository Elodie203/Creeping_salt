# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:25:32 2025

@author: eharle
"""
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd


def ouvrir_tracer(file_path, titre, time_shift=0, m_shift=0): 

    # Lire et traiter les données
    data = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    for line in lines[1:]:  # Ignorer la première ligne (en-tête)
        parts = line.strip().split("\t")
        try:
            time = float(parts[0])   
            force = float(parts[2])
            position = float(parts[1])   
            data.append([time/60/60, position, force])
        except ValueError:
                continue  # Ignorer les lignes qui ne contiennent pas de valeurs numériques

    # Convertir en DataFrame
    df = pd.DataFrame(data, columns=["Temps (s)", "Position (mm)", "Force (g)"])


    # Numpy tableau 
    time_data = df["Temps (s)"].values
    force_data = df["Force (g)"].values
    position_data = df["Position (mm)"].values

    #plot
    #plt.figure()
    plt.scatter(time_data+time_shift,force_data-force_data[0]+m_shift, s=2)
    plt.title(titre)
    plt.xlabel('Time [h]', fontsize=16)
    plt.ylabel('Masse [g]', fontsize=16)
    plt.yscale('log')
    #plt.xscale('log')

plt.figure()
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/github/mass_measurement/masse_sel_3_02.dat", 'masse sel, exp du 3/02 (tournoi)')


plt.figure()
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/cristallisation_sel_2025-06-06.dat", 'Deuxieme exp sel 06/06, RH <20%, barreau verre + sel pur + parafilm sur les bords')

plt.figure()
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/cristallisation_sel_2025-06-13.dat", 'Troisieme exp sel 13/06 (encore en cours), RH~30%, barreau verre + gros sel + couvercle parafilm')
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/cristallisation_sel_2025-18-06.dat", 'Troisieme exp sel 18/06 (suite du 13/06), RH~30%, barreau verre + gros sel + couvercle parafilm', time_shift=186810.077/3600, m_shift= 6.423+5.860)

plt.figure()
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/cristallisation_sel_2025-20-06bis.dat", 'Quatrieme exp sel 20/06, RH~30%, barreau verre petit (février) + gros sel + parafilm sur les bords')



plt.figure()
ouvrir_tracer("C:/Users/elodi/Desktop/Projet_Sel/sel_11_07/cristallisation_sel_2025-11-07.dat", '5e exp sel 11/07, RH~35%, cristallisoir à bords bas + gros sel + parafilm couvercle et bords')






plt.show()


