import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Edge, RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
def simulator_triggers(dut):
    """Check the waveforms"""
    cocotb.fork(Clock(dut.clk_i, 2).start())
    yield reset(dut)
    #
    yield RisingEdge(dut.clk_i)
    dut.RisingEdge_i <= 1
    yield RisingEdge(dut.clk_i)
    dut.RisingEdge_i <= 0
    yield RisingEdge(dut.clk_i)
    dut.RisingEdge_i <= 1
    yield RisingEdge(dut.clk_i)
    dut.RisingEdge_i <= 0
    #
    yield FallingEdge(dut.clk_i)
    dut.FallingEdge_i <= 1
    yield FallingEdge(dut.clk_i)
    dut.FallingEdge_i <= 0
    yield FallingEdge(dut.clk_i)
    dut.FallingEdge_i <= 1
    yield FallingEdge(dut.clk_i)
    dut.FallingEdge_i <= 0
    #
    yield Edge(dut.clk_i)
    dut.Edge_i <= 1
    yield Edge(dut.clk_i)
    dut.Edge_i <= 0
    yield Edge(dut.clk_i)
    dut.Edge_i <= 1
    yield Edge(dut.clk_i)
    dut.Edge_i <= 0
    #
    yield ClockCycles(dut.clk_i, 3)
    dut.ClockCycles_i <= 1
    yield ClockCycles(dut.clk_i, 3)
    dut.ClockCycles_i <= 0
    yield ClockCycles(dut.clk_i, 3)
    dut.ClockCycles_i <= 1
    yield ClockCycles(dut.clk_i, 3)
    dut.ClockCycles_i <= 0
    #
    yield Edge(dut.clk_i)

@cocotb.coroutine
def reset(dut):
    dut.rst_i         <= 1
    dut.RisingEdge_i  <= 0
    dut.FallingEdge_i <= 0
    dut.Edge_i        <= 0
    dut.ClockCycles_i <= 0
    yield ClockCycles(dut.clk_i, 3)
    dut.rst_i <= 0
    yield RisingEdge(dut.clk_i)
    dut._log.info("Reset complete")
