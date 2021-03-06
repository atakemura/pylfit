#-------------------------------------------------------------------------------
# @author: Tony Ribeiro
# @created: 2019/05/06
# @updated: 2019/05/06
#
# @desc: example of the use of GULA algorithm
#-------------------------------------------------------------------------------

import sys
sys.path.insert(0, 'src/')
sys.path.insert(0, 'src/algorithms')
sys.path.insert(0, 'src/objects')

from utils import eprint
from logicProgram import LogicProgram
from gula import GULA

# 1: Main
#------------
if __name__ == '__main__':

    # 0) Example from text file representing a logic program
    #--------------------------------------------------------
    eprint("Example using logic program definition file:")
    eprint("----------------------------------------------")

    benchmark = LogicProgram.load_from_file("benchmarks/logic_programs/repressilator.lp")

    eprint("Original logic program: \n", benchmark.logic_form())

    eprint("Generating transitions...")

    input = benchmark.generate_all_transitions()

    eprint("GULA input: \n", input)

    model = GULA.fit(benchmark.get_variables(), benchmark.get_values(), input)

    eprint("GULA output: \n", model.logic_form())

    expected = benchmark.generate_all_transitions()
    predicted = model.generate_all_transitions()

    precision = LogicProgram.precision(expected, predicted) * 100

    eprint("Model accuracy: ", precision, "%")

    state = [1,1,1]
    next = model.next(state)

    eprint("Next state of ", state, " is ", next, " according to learned model")

    eprint("----------------------------------------------")

    # 1) Example from csv file encoding transitions
    #--------------------------------------------------------
    eprint()
    eprint("Example using transition from csv file:")
    eprint("----------------------------------------------")

    input = GULA.load_input_from_csv("benchmarks/transitions/repressilator.csv")

    eprint("GULA input: \n", input)

    variables = ["p", "q", "r"]
    values = [[0,1],[0,1],[0,1]]

    model = GULA.fit(variables, values, input)

    eprint("GULA output: \n", model.logic_form())

    expected = input
    predicted = model.generate_all_transitions()

    print(predicted)

    precision = LogicProgram.precision(expected, predicted) * 100

    eprint("Model accuracy: ", precision, "%")

    state = [1,1,1]
    next = model.next(state)

    eprint("Next state of ", state, " is ", next, " according to learned model")

    eprint("----------------------------------------------")

    # 1) Example from csv file encoding transitions
    #--------------------------------------------------------
    eprint()
    eprint("Example using transition from csv file:")
    eprint("----------------------------------------------")

    input = GULA.load_input_from_csv("benchmarks/transitions/multi_valued_loop_up_down.csv")

    eprint("GULA input: \n", input)

    variables = ["a", "b"]
    values = [[0,1,2],[0,1,2]]

    model = GULA.fit(variables, values, input)

    eprint("GULA output: \n", model.logic_form())

    expected = input
    predicted = model.generate_all_transitions()

    print(predicted)

    precision = LogicProgram.precision(expected, predicted) * 100

    eprint("Model accuracy: ", precision, "%")

    state = [1,1,1]
    next = model.next(state)

    eprint("Next state of ", state, " is ", next, " according to learned model")

    eprint("----------------------------------------------")
