import cocotb
from cocotb.clock import Clock

from cocotb.triggers import Edge, RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
def simulator_signal_triggers(dut):
    """Playing with the Simulator Signals Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    for i in range(4):
        yield RisingEdge(dut.clk_i)
        dut._log.info("* %s trigger fired" % "RisingEdge")
    for i in range(4):
        yield FallingEdge(dut.clk_i)
        dut._log.info("* %s trigger fired" % "FallingEdge")
    for i in range(4):
        yield Edge(dut.clk_i)
        dut._log.info("* %s trigger fired" % "Edge")
    for i in range(4):
        yield ClockCycles(dut.clk_i, 3)
        dut._log.info("* %s trigger fired" % "ClockCycle")

from cocotb.triggers import Timer, ReadOnly, ReadWrite, NextTimeStep

@cocotb.test()
def simulator_timing_triggers(dut):
    """Playing with the Simulator Timing Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    yield Timer(2)
    dut._log.info("* %s trigger fired" % "Timer")
    yield Timer(2, "ns")
    dut._log.info("* %s trigger fired" % "Timer")
    yield Timer(2000, "ps")
    dut._log.info("* %s trigger fired" % "Timer")
    yield Timer(0.002, "us")
    dut._log.info("* %s trigger fired" % "Timer")
    #
    yield NextTimeStep()
    dut._log.info("* %s trigger fired" % "NextTimeStep")
    yield ReadWrite()
    dut._log.info("* %s trigger fired" % "ReadWrite")
    yield ReadOnly()
    dut._log.info("* %s trigger fired" % "ReadOnly")

from cocotb.triggers import Combine, First, Join

@cocotb.test()
def python_triggers(dut):
    """Playing with the Python Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    t1 = Timer(1)
    t2 = Timer(2)
    yield Combine(t1,t2)
    dut._log.info("* %s trigger fired" % "Combine")
    yield First(t1,t2)
    dut._log.info("* %s trigger fired" % "First")
    yield Join(cocotb.fork(reset(dut)))
    dut._log.info("* %s trigger fired" % "Join")

from cocotb.triggers import Event, Lock

@cocotb.test()
def synchronization_triggers(dut):
    """Playing with the Synchronization Triggers"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    dut._log.warn("Not yet implemented")

@cocotb.coroutine
def reset(dut):
    dut.rst_i <= 1
    yield RisingEdge(dut.clk_i)
    dut.rst_i <= 0
    dut._log.info("Reset complete")
