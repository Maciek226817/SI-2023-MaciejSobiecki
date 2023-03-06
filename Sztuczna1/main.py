# import numpy as np
# import pandas as pd
# from scipy.stats import mode
#
# aus = np.loadtxt("australian.txt")
# atrybut_type = np.genfromtxt('australian-type.txt', dtype='str')
# #
# # # zadanie3a
# # # wydzielenie etykiet klas decyzyjnych
# # labels = aus[:, -1]
# #
# # # wyświetlenie unikalnych klas decyzyjnych
# # print(np.unique(labels))
# #
# # # Zadanie3b
# # # wielkości klas decyzyjnych (liczby obiektów w klasach)
# # print("size: ", len(aus))
# #
# # # zadanie3c
# # # minimalne i maksymalne wartości poszczególnych atrybutów (dotyczy atrybutów numerycznych)
# # # pobranie indeksów atrybutów numerycznych
# #
# # numeryczny = np.where(atrybut_type == 'n')[0]
# # # min_values = np.min(aus[:, numeryczny].astype(np.double), axis=0)
# # # max_values = np.max(aus[:, numeryczny].astype(np.double), axis=0)
# # # for i in range(len(numeryczny)):
# # #     print('Minimalna wartość dla atrybutu', numeryczny[i], ':', min_values[i])
# # #     print('Maksymalna wartość dla atrybutu', numeryczny[i], ':', max_values[i])
# #
# # n = [2,3,7,10,13,14]
# # for i in n:
# #     print("max a",i," = ", np.max(aus[:, i]))
# #     print("min a", i, " = ", np.min(aus[:, i]))
# #
# # # zadanie3d
# # #  dla każdego atrybutu wypisujemy liczbę różnych dostępnych wartości (for each
# # # attribute detect the number of different available values)
# # for i in range (0,14):
# #     print("number a",i," : ", len(np.unique(aus[:,i])))
# #
# # # zadanie3e
# # #  dla każdego atrybutu wypisujemy listę wszystkich różnych dostępnych wartości
# # # (for each attribute list the set of different, available values)
# # for i in range (0,14):
# #     print("all a",i," : ", np.unique(aus[:,i]))
# #
# # # zadanie3f
# # # odchylenie standardowe dla poszczególnych atrybutów w całym systemie i w klasach decyzyjnych (dotyczy atrybutów numerycznych) (compute standard deviation
# # # for each attribute in the whole system and separately for each decision class).
# #
# # for i in n:
# #     print("stadardowe",i," :", np.std(aus[:,i], 0))
# #
# # aus_numeric = aus[:, numeryczny].astype(np.double)
# # for x in np.unique(aus[:, -1]):
# #     data_numeric_class = aus_numeric[aus[:, -1] == x]
# #     std_devs_class = np.std(data_numeric_class, axis=0)
# #     print('Odchylenie standardowe dla poszczególnych atrybutów w klasie', x, ':', std_devs_class)
# #
#
#
#
# # Zadanie4a
# # with open("australian.txt", "r") as f:
# #     data = pd.read_table(f, sep="\t")
# #
# # # liczność zbioru danych
# # n = len(data)
# #
# # # wygenerowanie 10% brakujących wartości
# # missing_values = np.random.choice(data.index, size=int(n*0.1), replace=False)
# # for col in data.columns:
# #     data.loc[missing_values, col] = "?"
# #
# # # naprawa brakujących wartości
# # for col in data.columns:
# #     if data[col].dtype == "object":
# #         # metoda najczęstszej wartości dla atrybutów nominalnych
# #         most_frequent_value = data[col].mode()[0]
# #         data[col] = data[col].replace("?", most_frequent_value)
# #     else:
# #         # metoda średniej wartości dla atrybutów numerycznych
# #         mean_value = data[col].mean()
# #         data[col] = pd.to_numeric(data[col], errors="coerce")
# #         data[col] = data[col].fillna(mean_value)
#
# # print(data.head())
#
# # # zadanie4b
# # with open("australian.txt", "r") as f:
# #     data = pd.read_table(f, sep="\t")
# #
# # # normalizacja atrybutów numerycznych na przedział <-1,1>
# # for col in data.columns:
# #     if data[col].dtype != "object":
# #         # tu wstawiam przedzialy: <0,1>,<-10,10>
# #         a = -1
# #         b = 1
# #         data[col] = ((data[col] - np.min(data)) * (b - a)) / (np.max(data) - np.min(data)) + a
# #
# # print(data.head())
# # zadanie4c
#
# def standarization_calc(mean, variance, aiobj):
#     x = (float(aiobj) - mean) / variance
#     return str(x)
#
# x1, y1 = np.where(atrybut_type == "n")
#
# for i in x1:
#     meanai = np.mean(np.array(aus[:, i], dtype='float'))
#     varianceai = np.var(np.array(aus[:, i], dtype='float'))
#     for j in range(len(aus)):
#         aus[j, i] = standarization_calc(meanai, varianceai, aus[j, i])
#
# # zadanie4d
# data = np.loadtxt("Churn_Modelling.csv", delimiter=",", dtype="str")
# data1 = np.delete(data, 0, axis=0)
#
# # wybranie kolumny geography i unikatowych elementow
# geography = data1[:, 4]
# unique_attributes = np.unique(geography)
# dummy_variables = []
#
# # stworzenie dummy variables
# for i, j in enumerate(unique_attributes):
#     dummy_variables.append(np.where(geography == j, "1", "0").tolist())
# dummy_variables = np.asarray(dummy_variables)
#
# # dodanie kolumn w miejsce kolumny geography
# temp_data = data1[:, 0:4]
# temp_data = np.insert(temp_data, 4, dummy_variables[1], axis=1)
# temp_data = np.insert(temp_data, 5, dummy_variables[2], axis=1)
# temp_data = np.append(temp_data, data1[:, 5:], axis=1)
#
# # uzupelnienie rzedu z nazwami o dummy variables
# name_row = data[0, :4]
# name_row = np.insert(name_row, 4, ["Geography.symbol2", "Geography.symbol3"], axis=0)
# name_row = np.append(name_row, data[0, 5:], axis=0)
#
# # dodanie rzedu z nazwami do tabeli
# temp_data = np.insert(temp_data, 0, name_row, axis=0)
