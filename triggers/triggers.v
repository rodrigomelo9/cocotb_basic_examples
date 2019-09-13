`timescale 1ns/1ns

module triggers (
    input clk_i,
    input rst_i
);

   initial begin
      $dumpfile("./sim_build/waveforms.vcd");
      $dumpvars (0,triggers);
  end

endmodule
