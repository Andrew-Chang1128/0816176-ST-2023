import angr
import sys
import claripy
import logging
logging.getLogger('angr.sim_manager').setLevel(logging.DEBUG)
# proj = angr.Project('./src/prog', load_options={'auto_load_libs': True})
# TODO


# find_addr = 0x401363
# avoid_addr = 0x40134d

def handle_fgets_real_input(raw_input):
    idx = 0
    for c in raw_input:
        if c == ord('\n') or c == ord('\0'):
            break
        idx += 1
    return raw_input[:idx]

class MyHook(angr.SimProcedure):
    def run(self, fmt, n):
        simfd = self.state.posix.get_fd(sys.stdin.fileno())
        data, ret_size = simfd.read_data(4)
        self.state.memory.store(n, data)
        return 1

# class ReplacementScanf(angr.SimProcedure):
#     def run(self, format_string, param0):
#         scanf0 = claripy.BVS('scanf0', 4)
#         # scanf1 = claripy.BVS('scanf1', 32)

#         scanf0_address = param0
#         self.state.memory.store(scanf0_address, scanf0, endness=project.arch.memory_endness)
#         # scanf1_address = param1
#         # self.state.memory.store(scanf1_address, scanf1, endness=project.arch.memory_endness)
        
#         self.state.globals['solutions'] = scanf0
proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
# initial_state = project.factory.entry_state()
# scanf_symbol = '__isoc99_scanf'
# proj.hook_symbol(scanf_symbol, ReplacementScanf(), replace=True)
proj.hook_symbol('__isoc99_scanf', MyHook(), replace=True)

# state = proj.factory.blank_state(addr=main_addr)
def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    if b'AC!' in stdout_output:
        return True  
    else :
        return False

def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    if b'WA!' in  stdout_output:
        return True  
    else :
        return False

state  = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=is_successful, avoid=should_abort)
# simgr.explore(find=is_successful, avoid=avoid_addr)
if simgr.found:
    print(simgr.found[0].posix.dumps(sys.stdin.fileno()))

    # input1 = simgr.found[0].posix.dumps(sys.stdin.fileno())[:0x20]
    # input1 = handle_fgets_real_input(input1)

    # input2 = simgr.found[0].posix.dumps(sys.stdin.fileno())[0x20:]
    # input2 = handle_fgets_real_input(input2)
    s = simgr.found[0].posix.dumps(sys.stdin.fileno())
    out = simgr.found[0].posix.dumps(sys.stdout.fileno())
    print(out)
    d = []
    f = open("solve_input", "w")
    f.truncate(0)
    
    for i in range(0, 15):
        d.append(int.from_bytes(s[i * 4 : i * 4 + 4], byteorder='little', signed=True))
        f = open("solve_input", "a")
        f.write(str(int.from_bytes(s[i * 4 : i * 4 + 4], byteorder='little', signed=True)) + str('\n'))
        f.close()

    print(d)

    # input1 = simgr.found[0].posix.dumps(sys.stdin.fileno())[0:0x20].decode()
    # print(type(input1))
    # print((input1))
    # int_val = int.from_bytes(input1, "little")
    # print(int_val)
    # input2 = simgr.found[0].posix.dumps(sys.stdin.fileno())[0x20:0x40]

    # print('x1: ' + input1.decode())
    # print('x2: ' + input2.decode())
    # for i in simgr.found:
    #     solution_state = i
    #     stored_solutions = solution_state.globals['solutions']
    #     scanf0_solution = solution_state.solver.eval(stored_solutions)
    #     print("[+] Success! Solution is: {0}".format(scanf0_solution))
        #print(scanf0_solution, scanf1_solution)

else:
    print('Failed')
