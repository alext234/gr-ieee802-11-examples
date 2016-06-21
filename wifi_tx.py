#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Tx
# Generated: Tue Feb  2 15:42:16 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from wifi_phy_hier import wifi_phy_hier  # grc-generated hier_block
import foo
import ieee802_11
import pmt
import time
import wx


class wifi_tx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Wifi Tx")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 50
        self.samp_rate = samp_rate = 10e6
        self.period = period = 100
        self.pdu_length = pdu_length = 100
        self.out_buf_size = out_buf_size = 96000
        self.mult = mult = .4
        self.lo_offset = lo_offset = 11e6
        self.freq = freq = 2.422e9
        self.encoding = encoding = 0

        ##################################################
        # Blocks
        ##################################################
        _tx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	label='tx_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tx_gain_sizer)
        self._samp_rate_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label="Sample Rate",
        	choices=[10e6, 20e6],
        	labels=["10 Mhz", "20 Mhz"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._samp_rate_chooser)
        _period_sizer = wx.BoxSizer(wx.VERTICAL)
        self._period_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_period_sizer,
        	value=self.period,
        	callback=self.set_period,
        	label='period',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._period_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_period_sizer,
        	value=self.period,
        	callback=self.set_period,
        	minimum=1,
        	maximum=10000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_period_sizer)
        _pdu_length_sizer = wx.BoxSizer(wx.VERTICAL)
        self._pdu_length_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_pdu_length_sizer,
        	value=self.pdu_length,
        	callback=self.set_pdu_length,
        	label='pdu_length',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._pdu_length_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_pdu_length_sizer,
        	value=self.pdu_length,
        	callback=self.set_pdu_length,
        	minimum=0,
        	maximum=1500,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_pdu_length_sizer)
        _mult_sizer = wx.BoxSizer(wx.VERTICAL)
        self._mult_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_mult_sizer,
        	value=self.mult,
        	callback=self.set_mult,
        	label='mult',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._mult_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_mult_sizer,
        	value=self.mult,
        	callback=self.set_mult,
        	minimum=0,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_mult_sizer)
        self._lo_offset_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.lo_offset,
        	callback=self.set_lo_offset,
        	label="LO Offset",
        	choices=[0, 6e6, 11e6],
        	labels=['0 MHz', '6 MHz', '11 MHz'],
        )
        self.Add(self._lo_offset_chooser)
        self._freq_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Channel",
        	choices=[2412000000.0, 2417000000.0, 2422000000.0, 2427000000.0, 2432000000.0, 2437000000.0, 2442000000.0, 2447000000.0, 2452000000.0, 2457000000.0, 2462000000.0, 2467000000.0, 2472000000.0, 2484000000.0, 5170000000.0, 5180000000.0, 5190000000.0, 5200000000.0, 5210000000.0, 5220000000.0, 5230000000.0, 5240000000.0, 5260000000.0, 5280000000.0, 5300000000.0, 5320000000.0, 5500000000.0, 5520000000.0, 5540000000.0, 5560000000.0, 5580000000.0, 5600000000.0, 5620000000.0, 5640000000.0, 5660000000.0, 5680000000.0, 5700000000.0, 5745000000.0, 5765000000.0, 5785000000.0, 5805000000.0, 5825000000.0, 5860000000.0, 5870000000.0, 5880000000.0, 5890000000.0, 5900000000.0, 5910000000.0, 5920000000.0],
        	labels=['  1 | 2412.0 | 11g', '  2 | 2417.0 | 11g', '  3 | 2422.0 | 11g', '  4 | 2427.0 | 11g', '  5 | 2432.0 | 11g', '  6 | 2437.0 | 11g', '  7 | 2442.0 | 11g', '  8 | 2447.0 | 11g', '  9 | 2452.0 | 11g', ' 10 | 2457.0 | 11g', ' 11 | 2462.0 | 11g', ' 12 | 2467.0 | 11g', ' 13 | 2472.0 | 11g', ' 14 | 2484.0 | 11g', ' 34 | 5170.0 | 11a', ' 36 | 5180.0 | 11a', ' 38 | 5190.0 | 11a', ' 40 | 5200.0 | 11a', ' 42 | 5210.0 | 11a', ' 44 | 5220.0 | 11a', ' 46 | 5230.0 | 11a', ' 48 | 5240.0 | 11a', ' 52 | 5260.0 | 11a', ' 56 | 5280.0 | 11a', ' 58 | 5300.0 | 11a', ' 60 | 5320.0 | 11a', '100 | 5500.0 | 11a', '104 | 5520.0 | 11a', '108 | 5540.0 | 11a', '112 | 5560.0 | 11a', '116 | 5580.0 | 11a', '120 | 5600.0 | 11a', '124 | 5620.0 | 11a', '128 | 5640.0 | 11a', '132 | 5660.0 | 11a', '136 | 5680.0 | 11a', '140 | 5700.0 | 11a', '149 | 5745.0 | 11a', '153 | 5765.0 | 11a', '157 | 5785.0 | 11a', '161 | 5805.0 | 11a', '165 | 5825.0 | 11a', '172 | 5860.0 | 11p', '174 | 5870.0 | 11p', '176 | 5880.0 | 11p', '178 | 5890.0 | 11p', '180 | 5900.0 | 11p', '182 | 5910.0 | 11p', '184 | 5920.0 | 11p'],
        )
        self.Add(self._freq_chooser)
        self._encoding_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.encoding,
        	callback=self.set_encoding,
        	label="Encoding",
        	choices=[0,1,2,3,4,5,6,7],
        	labels=["BPSK 1/2", "BPSK 3/4", "QPSK 1/2", "QPSK 3/4", "16QAM 1/2", "16QAM 3/4", "64QAM 2/3", "64QAM 3/4"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._encoding_chooser)
        self.wifi_phy_hier_0 = wifi_phy_hier(
            chan_est=0,
            encoding=encoding,
            sensitivity=0.56,
        )
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"packet_len",
        )
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(freq, rf_freq = freq - lo_offset, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0x02, 0x11, 0x87, 0xBA, 0x68, 0x3B]))
        self.foo_packet_pad2_0 = foo.packet_pad2(False, False, 0.01, 100, 1000)
        (self.foo_packet_pad2_0).set_min_output_buffer(96000)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", "", "52001", 10000, False)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((mult, ))
        (self.blocks_multiply_const_vxx_0).set_min_output_buffer(100000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("".join("x" for i in range(pdu_length))), period)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.wifi_phy_hier_0, 'mac_in'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_ofdm_mac_0, 'phy in'))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.foo_packet_pad2_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.wifi_phy_hier_0, 0))    
        self.connect((self.foo_packet_pad2_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.wifi_phy_hier_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.wifi_phy_hier_0, 1), (self.blocks_null_sink_0, 0))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self._tx_gain_slider.set_value(self.tx_gain)
        self._tx_gain_text_box.set_value(self.tx_gain)
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_chooser.set_value(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
        self._period_slider.set_value(self.period)
        self._period_text_box.set_value(self.period)
        self.blocks_message_strobe_0_0.set_period(self.period)

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length
        self._pdu_length_slider.set_value(self.pdu_length)
        self._pdu_length_text_box.set_value(self.pdu_length)
        self.blocks_message_strobe_0_0.set_msg(pmt.intern("".join("x" for i in range(self.pdu_length))))

    def get_out_buf_size(self):
        return self.out_buf_size

    def set_out_buf_size(self, out_buf_size):
        self.out_buf_size = out_buf_size

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult
        self._mult_slider.set_value(self.mult)
        self._mult_text_box.set_value(self.mult)
        self.blocks_multiply_const_vxx_0.set_k((self.mult, ))

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset
        self._lo_offset_chooser.set_value(self.lo_offset)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.freq, rf_freq = self.freq - self.lo_offset, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_chooser.set_value(self.freq)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.freq, rf_freq = self.freq - self.lo_offset, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self._encoding_chooser.set_value(self.encoding)
        self.wifi_phy_hier_0.set_encoding(self.encoding)


def main(top_block_cls=wifi_tx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
