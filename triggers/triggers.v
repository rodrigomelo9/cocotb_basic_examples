`timescale 1ns/1ps

module triggers (
    input        clk_i,
    input        rst_i,
    // Simulator Triggers
    input        RisingEdge_i,
    input        FallingEdge_i,
    input        Edge_i,
    input        ClockCycles_i
);

   initial begin
      $dumpfile("./sim_build/waveforms.vcd");
      $dumpvars (0,triggers);
  end

endmodule
