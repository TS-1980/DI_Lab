# v03
# 2022-02-23  ISit-18 studentai Tomas Š. ir Alvydas Ž.


from search import *

class ZirgoPuzlas(Problem):
    # Žirgo kelionės šachmatų lentoje apskaičiavimas, nurodant žirgo pradinės būsenos langelį
    # ir galutinės būsenos langelio reikšmes

    def __init__(self, initial, goal):
        # Tikslo apibūdinimas ir problemos inicijavimas
        super().__init__(initial, goal)

    def actions(self, state):
        # Pateikiamas, galimų žirgo ėjimų, sąrašas

        possible_actions = ['UPL1', 'UPL2', 'UPR1', 'UPR2', 'DWL1', 'DWL2', 'DWR1', 'DWR2']

        # Dabartinės pozicijos indeksas
        index_current_square = state

        # Apribojimų nustatymas
        if index_current_square % 8 == 0:
            if 'UPL1' in possible_actions: possible_actions.remove('UPL1')
            if 'UPL2' in possible_actions: possible_actions.remove('UPL2')
            if 'DWL1' in possible_actions: possible_actions.remove('DWL1')
            if 'DWL2' in possible_actions: possible_actions.remove('DWL2')
        if index_current_square % 8 == 7 :
            if 'UPR1' in possible_actions: possible_actions.remove('UPR1')
            if 'UPR2' in possible_actions: possible_actions.remove('UPR2')
            if 'DWR2' in possible_actions: possible_actions.remove('DWR2')
            if 'DWR1' in possible_actions: possible_actions.remove('DWR1')
        if index_current_square % 8 == 6:
            if 'UPR2' in possible_actions: possible_actions.remove('UPR2')
            if 'DWR2' in possible_actions: possible_actions.remove('DWR2')
        if index_current_square % 8 == 1:
            if 'UPL2' in possible_actions: possible_actions.remove('UPL2')
            if 'DWL2' in possible_actions: possible_actions.remove('DWL2')
        if index_current_square < 8:
            if 'UPL2' in possible_actions: possible_actions.remove('UPL2')
            if 'UPR2' in possible_actions: possible_actions.remove('UPR2')
        if index_current_square < 16:
            if 'UPL1' in possible_actions: possible_actions.remove('UPL1')
            if 'UPR1' in possible_actions: possible_actions.remove('UPR1')
        if index_current_square > 55:
            if 'DWL2' in possible_actions: possible_actions.remove('DWL2')
            if 'DWR2' in possible_actions: possible_actions.remove('DWR2')
        if index_current_square > 47:
            if 'DWL1' in possible_actions: possible_actions.remove('DWL1')
            if 'DWR1' in possible_actions: possible_actions.remove('DWR1')


        return possible_actions

    def result(self, state, action):
        # Panaudojus esamos būsenos reikšmę (langelį, kuriame yra žirgas) ir atlikus nurodytą veiksmą grąžinama
        # nauja žirgo lokacija (langelis)

        # current yra dabartinė būsena
        current = state

        delta = {'UPL1': -17, 'UPL2': -10, 'UPR1': -15, 'UPR2': -6, 'DWL1': 15, 'DWL2': 6, 'DWR1': 17, 'DWR2': 10}

        # Sukuriama nauja new_state kintamojo reikšmė
        new_state = current + delta[action]
        # Atlikus pokyčius gražinama nauja būsena
        return new_state

    def goal_test(self, state):
        # Patikrinama, ar žirgas jau pasiekė galinę būseną/tikslą
        return state == self.goal


# ______________________________________________________________________________

#
#Pradinės reikšmės (eilutės ir stulpeliai skaičiuojami pradedant nuo 0)
p_eil = 0;
p_st = 0;
#Tikslas (eilutės ir stulpeliai skaičiuojami pradedant nuo 0)
t_eil = 7;
t_st = 0;
#Pradinio lauko indekso apskaičiavimas
p_id=p_eil*8+p_st
#Tikslo lauko indekso apskaičiavimas
t_id=t_eil*8+t_st

Zirgas = ZirgoPuzlas(p_id, t_id)
solution = breadth_first_graph_search(Zirgas).solution()
# solution = depth_first_graph_search(Zirgas).solution()


print(solution)


