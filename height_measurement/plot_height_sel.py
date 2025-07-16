# -*- coding: utf-8 -*-
"""
@author: eharle
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.cm import get_cmap


# Fonction pour afficher les points pour chaque frame avec une légende progressive et un décalage temporel
# Utilise un temps donné (t_2301) pour le décalage dans la deuxième série
def plot_points_by_frame_with_time_shift(x, y, frames, nframes, time_shifts=None, title="Points par frame", colormap="viridis"):
    fig, ax = plt.subplots(figsize=(10, 6))
    #cmap = get_cmap(colormap)  # Colormap personnalisable
    cmap = get_cmap("plasma")  # Colormap pour les couleurs progressives


    for frame in range(1, nframes + 1):
        indices = np.where(frames == frame)[0]
        if len(indices) > 0:
            color = cmap(frame / nframes)  # Couleur en fonction de la frame
            if time_shifts is not None:
                x_shifted = x[indices] + time_shifts[indices]  # Décalage basé sur les temps donnés
            else:
                x_shifted = x[indices]  # Pas de décalage
            ax.scatter(x_shifted, y[0]-y[indices], alpha=0.5, s=10, color=color, label=f"Frame {frame}")

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=1, vmax=nframes))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("Frames")

    ax.set_title(title)
    ax.set_xlabel("Time (s)", fontsize=16)
    ax.set_ylabel("Maximum height (mm)", fontsize=16)
    plt.tight_layout()
    plt.show()


# Fonction pour afficher les points pour chaque frame avec une légende progressive
def plot_points_by_frame(x, y, frames, nframes, title="Points par frame"):
    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = get_cmap("plasma")  # Colormap pour les couleurs progressives

    for frame in range(1, nframes + 1):
        indices = np.where(frames == frame)[0]
        if len(indices) > 0:
            color = cmap(frame / nframes)  # Couleur en fonction de la frame
            ax.scatter(x[indices], y[0]-y[indices], alpha=0.5, s=12, color=color, label=f"Frame {frame}")

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=1, vmax=nframes))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("progression in time")

    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.tight_layout()
    plt.show()

def plot_max_height_per_frame(y, frames, nframes, t_frame, title="Hauteur maximale par frame"):
    max_heights = []

    for frame in range(1, nframes + 1):
        indices = np.where(frames == frame)[0]
        if len(indices) > 0:
            max_y = np.min(y[indices])
        else:
            max_y = np.nan  # Aucun point pour cette frame
        max_heights.append(max_y)
    t = np.arange(1, nframes + 1) *t_frame/60  # Temps en heures    plt.figure(figsize=(10, 5))
    plt.scatter(t, max_heights[0]-max_heights , marker='o', s=12)
    plt.title(title)
    plt.xlabel("Time (h)", fontsize=16)
    plt.ylabel("Hauteur maximale (cm)", fontsize=16)
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.show()


#%% 21/01 et 23/01 pdt tournoi
# Charger les données
file_path = " " #a changer

try:
    datas = pd.read_excel(file_path, engine='odf')
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    exit()

# Nombre total de frames
nframes_2101 = 42
nframes_2301 = 121

# Extraction des colonnes pertinentes
x_sel = datas.iloc[:, 12].dropna().tolist()
y_sel = np.array(datas.iloc[:, 13].dropna().tolist())-60
frame_sel = np.array(datas.iloc[:, 14].dropna().tolist())
t_2101 = np.array(datas.iloc[:, 15].dropna().tolist())


x_sel_2301 = datas.iloc[:, 23].dropna().tolist() #valeurs en mm
y_sel_2301 = np.array(datas.iloc[:, 24].dropna().tolist()) #valeurs en mm
frame_sel_2301 = np.array(datas.iloc[:, 21].dropna().tolist())
t_2301 = np.array(datas.iloc[:, 22].dropna().tolist())


# Affichage des points pour les frames d'une deuxième sélection avec décalage temporel basé sur t_2301
plot_points_by_frame_with_time_shift(
    np.array(x_sel_2301), y_sel_2301, frame_sel_2301, nframes_2301, time_shifts=t_2301, title="experiment ICS 23/01")


plot_points_by_frame(np.array(x_sel_2301), y_sel_2301, frame_sel_2301, nframes_2301, title="experiment ICS 23/01", temps=t_2301)

plot_points_by_frame(np.array(x_sel), -y_sel, frame_sel, nframes_2101, title="experiment ICS 21/01", temps=t_2101)



#%%05/06
# Charger les données
file_path = "C:/Users/elodi/Desktop/Projet_Sel/sel_05_06_datas.ods"

try:
    datas = pd.read_excel(file_path, engine='odf')
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    exit()


# Nombre total de frames
nframes_0506 = 237

# Extraction des colonnes pertinentes
x_sel_0506 = datas.iloc[:, 6].dropna().tolist()
y_sel_0506 = np.array(datas.iloc[:, 7].dropna().tolist())
frame_sel_0506 = np.array(datas.iloc[:, 4].dropna().tolist())
t_0506 = np.array(datas.iloc[:, 5].dropna().tolist())



# Affichage des points pour les frames d'une première sélection
plot_points_by_frame(np.array(x_sel_0506), y_sel_0506, frame_sel_0506, nframes_0506, title="1st experiment ICS 05/06, pure NaCl, Al rod")


# Affichage des points pour les frames d'une première sélection (sans décalage supplémentaire)
plot_points_by_frame_with_time_shift(np.array(x_sel_0506), y_sel_0506, frame_sel_0506, nframes_0506, title="1st experiment ICS 05/06, pure NaCl, Al rod", time_shifts=t_0506)

plot_max_height_per_frame(y_sel_0506, frame_sel_0506, nframes_0506, t_frame=9,  title="Hauteur maximale par frame,1st experiment ICS 05/06, pure NaCl, Al rod")



#%% 11/06

# Charger les données
file_path = "C:/Users/elodi/Desktop/Projet_Sel/sel_11_06_datas.ods"

try:
    datas = pd.read_excel(file_path, engine='odf')
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    exit()
    
        

# Nombre total de frames
nframes_1106 = 237

# Extraction des colonnes pertinentes
x_sel_1106 = datas.iloc[:, 6].dropna().tolist()
y_sel_1106 = np.array(datas.iloc[:, 7].dropna().tolist())
frame_sel_1106 = np.array(datas.iloc[:, 4].dropna().tolist())
t_1106 = np.array(datas.iloc[:, 5].dropna().tolist())

plot_points_by_frame_with_time_shift(np.array(x_sel_1106), y_sel_1106, frame_sel_1106, nframes_1106, title="2nd experiment ICS 11/06, pure NaCl, glass rod", time_shifts=t_1106)
plot_points_by_frame(np.array(x_sel_1106), y_sel_1106, frame_sel_1106, nframes_1106, title="2nd experiment ICS 11/06, pure NaCl, glass rod")
plt.show()





plot_max_height_per_frame(y_sel_1106, frame_sel_1106, nframes_1106, t_frame=12, title="Hauteur maximale par frame, exp 11/06")


plt.show()

#%% 20/06
# Charger les données
file_path = "C:/Users/elodi/Desktop/Projet_Sel/sel_20_06_datas.ods"

try:
    datas = pd.read_excel(file_path, engine='odf')
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    exit()



# Nombre total de frames
nframes_2006 = 135

# Extraction des colonnes pertinentes
x_sel_2006 = datas.iloc[:, 6].dropna().tolist()
y_sel_2006 = np.array(datas.iloc[:, 7].dropna().tolist())
frame_sel_2006 = np.array(datas.iloc[:, 4].dropna().tolist())
t_2006 = np.array(datas.iloc[:, 5].dropna().tolist())

plot_points_by_frame_with_time_shift(np.array(x_sel_2006), y_sel_2006, frame_sel_2006, nframes_2006, title="4th experiment ICS 20/06, pure NaCl, glass rod", time_shifts=t_2006)
plot_points_by_frame(np.array(x_sel_2006), y_sel_2006, frame_sel_2006, nframes_2006, title="4th experiment ICS 20/06, pure NaCl, glass rod")
plt.show()


plot_max_height_per_frame(y_sel_2006, frame_sel_2006, nframes_2006, t_frame=24, title="Hauteur maximale par frame, exp 20/06")


plt.show()


#%%11/07, cristallisoir à bords bas 

file_path = "C:/Users/elodi/Desktop/Projet_Sel/sel_11_07_datas.ods"

try:
    datas = pd.read_excel(file_path, engine='odf')
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    exit()



# Nombre total de frames
nframes_11_07 = 275

# Extraction des colonnes pertinentes
x_sel_11_07 = datas.iloc[:, 6].dropna().tolist()
y_sel_11_07 = np.array(datas.iloc[:, 7].dropna().tolist())
frame_sel_11_07 = np.array(datas.iloc[:, 4].dropna().tolist())
t_11_07 = np.array(datas.iloc[:, 5].dropna().tolist())

plot_points_by_frame_with_time_shift(np.array(x_sel_11_07), y_sel_11_07, frame_sel_11_07, nframes_11_07, title="5e exp, cristallisoir à bords bas, gros sel, RH~35%", time_shifts=t_11_07)
plot_points_by_frame(np.array(x_sel_11_07), y_sel_11_07, frame_sel_11_07, nframes_11_07, title="5e exp, cristallisoir à bords bas, gros sel, RH~35%")
plt.show()

plot_max_height_per_frame(y_sel_11_07, frame_sel_11_07, nframes_11_07, t_frame=21, title="Hauteur maximale par frame, exp 11/07")


plt.show()




"""
w= np.where(frame_sel==4)
ygoods=np.zeros(len(w[0]))
for i in range(0, len(w)): 
    ygoods[i]= y_sel[w[0][i]]
print(ygoods)
plt.figure()
plt.scatter(x_sel, y_sel, alpha=0.3, s=3) 

for i in range(0,len(y_sel)): 
    w= np.where(int(frame_sel[i])==1)
    #print(w)
    #print(w, x_sel[w])
    #y_goods=y_sel[w]
    print(i)
    
  

for i in range(len(y_sel_0506)): 
    for k in range(0, nframes_0506):
        w=np.zeros((nframes_0506, len(y_sel_0506)))
        w[k]= np.where(frame_sel_0506==k+1)
    print(w, x_sel_0506[w])
    y_goods_0506=y_sel_0506[w]
"""

