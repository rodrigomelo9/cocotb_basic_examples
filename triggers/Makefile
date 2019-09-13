export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES = triggers.v
TOPLEVEL        = triggers
MODULE          = triggers

include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

clean::
	@rm -fr *.pyc *.xml

view: all
	gtkwave $(SIM_BUILD)/waveforms.vcd
