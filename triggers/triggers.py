import cocotb
from cocotb.clock import Clock

#
# Simulator Signals Triggers
#

from cocotb.triggers import Edge, RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
def simulator_signal_triggers(dut):
    """Playing with the Simulator Signals Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    for i in range(4):
        yield RisingEdge(dut.clk_i)
        print_fired(dut,"RisingEdge")
    for i in range(4):
        yield FallingEdge(dut.clk_i)
        print_fired(dut,"FallingEdge")
    for i in range(4):
        yield Edge(dut.clk_i)
        print_fired(dut,"Edge")
    for i in range(4):
        yield ClockCycles(dut.clk_i, 3)
        print_fired(dut,"ClockCycle")

#
# Simulator Timing Triggers
#

from cocotb.triggers import Timer, ReadOnly, ReadWrite, NextTimeStep

@cocotb.test()
def simulator_timing_triggers(dut):
    """Playing with the Simulator Timing Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    yield Timer(2) # Fires after the specified simulation time period has elapsed
    print_fired(dut,"Timer")
    yield Timer(2, "ns")
    print_fired(dut,"Timer")
    yield Timer(2000, "ps")
    print_fired(dut,"Timer")
    yield Timer(0.002, "us")
    print_fired(dut,"Timer")
    #
    yield NextTimeStep() # Fires when the next time step is started
    print_fired(dut,"NextTimeStep")
    yield ReadWrite() # Fires when the readwrite portion of the sim cycles is reached
    print_fired(dut,"ReadWrite")
    yield ReadOnly() # Fires when the current simulation timestep moves to the readonly phase
    print_fired(dut,"ReadOnly")

#
# Python Triggers
#

from cocotb.triggers import Combine, First, Join

@cocotb.test()
def python_triggers(dut):
    """Playing with the Python Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    t1 = Timer(1)
    t2 = Timer(2)
    yield Combine(t1,t2) # Fires when all of the triggers have fired
    print_fired(dut,"Combine")
    yield First(t1,t2) # Fires when the first trigger fires
    print_fired(dut,"First")
    yield Join(cocotb.fork(reset(dut))) # Fires when the forked coroutine has completed
    print_fired(dut,"Join")

from cocotb.triggers import Event, Lock

#
# Synchronization Triggers
#

@cocotb.test()
def synchronization_triggers(dut):
    """Playing with the Synchronization Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    dut._log.warn("Not yet implemented")

#
# Auxiliary functions and coroutines
#

@cocotb.coroutine
def reset(dut):
    dut.rst_i <= 1
    yield RisingEdge(dut.clk_i)
    dut.rst_i <= 0
    dut._log.info("Reset complete")

def print_fired(dut, trigger):
    dut._log.info("* %s trigger fired" % trigger)
