#!/usr/bin/env python
import binascii
import pprint
import sys

def app_info(help_flag):
    """ Display information """

    VER = "0.0.2"
    USAGE = f"Usage: python {sys.argv[0]} [-h | -v] | file_name]"
    CONTACT = "questions/feedback -> ognyan@endurosat.com"
    HELP = """
    =============================
    Parse PHOENIX Mode UHF Beacon
    =============================
    Parses PHOENIX Mode [RAW HEX] AX25 packets. 

        -h      Help, shows this text
        -v      Version, shows the version

        file_name   The .bin/.txt file name of beacon data in the same dir.

        {}
        
    NOTE: Output is a dict.
        
    -----------------------------
    {}

    """.format(USAGE, CONTACT)

    if help_flag == True:
        return HELP
    else:
        return VER

def format_temp(temp_val):
    """ Format temperature values depending on sign. """
    if temp_val < 32768:
        formatted_temp_val = temp_val * 0.00390625
    else:
        formatted_temp_val = (((temp_val >> 4) - 1) ^ 0xFFF) * (-0.0625)

    return formatted_temp_val

def impl_struct(frame):
    """ Implement beacon structure"""

    payload = frame[2]
    head            = [int((payload[2] + payload[1]), 16)]
    v_batt          = [int((payload[4] + payload[3]), 16)]
    i_batt          = [int((payload[6] + payload[5]), 16)]
    v_bcr           = [int((payload[8] + payload[7]), 16)]
    i_bcr           = [int((payload[10] + payload[9]), 16)]
    v_x             = [int((payload[12] + payload[11]), 16)]
    i_xm            = [int((payload[14] + payload[13]), 16)]
    i_xp            = [int((payload[16] + payload[15]), 16)]
    v_y             = [int((payload[18] + payload[17]), 16)]
    i_ym            = [int((payload[20] + payload[19]), 16)]
    i_yp            = [int((payload[22] + payload[21]), 16)]
    v_z             = [int((payload[24] + payload[23]), 16)]
    i_zm            = [int((payload[26] + payload[25]), 16)]
    i_zp            = [int((payload[28] + payload[27]), 16)]
    i_3V3           = [int((payload[30] + payload[29]), 16)]
    i_5V            = [int((payload[32] + payload[31]), 16)]
    t_mcu           = [int((payload[34] + payload[33]), 16)]  
    t_batt1         = [int((payload[36] + payload[35]), 16)]
    t_batt2         = [int((payload[38] + payload[37]), 16)]
    t_batt3         = [int((payload[40] + payload[39]), 16)]
    t_batt4         = [int((payload[42] + payload[41]), 16)]
    cnd_input       = [int((payload[44] + payload[43]), 16)] 
    cnd_output1     = [int((payload[46] + payload[45]), 16)]
    cnd_output2     = [int((payload[48] + payload[47]), 16)]
    por_cycles      = [int((payload[52] + payload[51]), 16)] 
    v_under         = [int((payload[54] + payload[53]), 16)]
    v_short         = [int((payload[56] + payload[55]), 16)]
    v_overtemp      = [int((payload[58] + payload[57]), 16)]
    t_max1          = [int((payload[60] + payload[59]), 16)]
    t_min1          = [int((payload[62] + payload[61]), 16)]
    def1            = [int((payload[64] + payload[63]), 16)]
    r_batt          = [int((payload[66] + payload[65]), 16)]
    v_ideal_batt    = [int((payload[68] + payload[67]), 16)]
    UHFAnt          = [(payload[72] + payload[71] + payload[70] + payload[69])]
    scw             = [int((payload[74] + payload[73]), 16)]
    def2            = [int(payload[65],16)]

    # Identifiers
    CONOPS_MODE_PHOENIX = int("0xa1c9", 16)     # CONOPS
    CONOPS_MODE_OTHER   = int("0xe7a9", 16)     # CONOPS
    ANTENNA_REGISTERS_OFF   = "deafbeef"        # ANTENNA

    # Units
    units = {
        "miliV"         : "[mV]",
        "volt"          : "[V]",
        "amp"           : "[A]",
        "miliamp"       : "[mA]",
        "centigrade"    : "[°C]",
        "ohm"           : "[Ω]",
    }

    frame_struct = {
        "ConOps magic num ID             :   "   :   ["OP MODE: {PHOENIX}" if head[0] == CONOPS_MODE_PHOENIX else "Other"],
        "EPS I Battery Voltage           :   "   :   [float(v_batt[0] * 0.0023394775), units["volt"]],
        "EPS I Battery Current           :   "   :   [float(i_batt[0] * 3.0517578), units["miliamp"]],
        "BCR Voltage                     :   "   :   [float(v_bcr[0] * 0.0023394775), units["volt"]],
        "BCR Current                     :   "   :   [float(i_bcr[0] * 1.5258789), units["miliamp"]],
        "SOL PAN X V                     :   "   :   [float(v_x[0] * 0.0024414063), units["volt"]],
        "SOL PAN X- Current              :   "   :   [float(i_xm[0] * 0.6103516), units["miliamp"]],
        "SOL PAN X+ Current              :   "   :   [float(i_xp[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Y V                     :   "   :   [float(v_y[0] * 0.0024414063), units["volt"]],
        "SOL PAN Y- Current              :   "   :   [float(i_ym[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Y+ Current              :   "   :   [float(i_yp[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Z V                     :   "   :   [float(v_z[0] * 0.0024414063), units["volt"]],
        "SOL PAN Z- Current              :   "   :   [float(i_zm[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Z+ Current              :   "   :   [float(i_zp[0] * 0.6103516), units["miliamp"]],
        "3.3V Bus Current                :   "   :   [float(i_3V3[0] * 2.0345052), units["miliamp"]],
        "5V   Bus Current                :   "   :   [float(i_5V[0] * 2.0345052), units["miliamp"]],
        "MCU Temperature                 :   "   :   [float(((t_mcu[0] * 0.0006103516) - 0.986 ) / 0.00355), units["centigrade"]],
        "Battery Cell 1 Temp             :   "   :   [float(format_temp(t_batt1[0])), units["centigrade"]],
        "Battery Cell 2 Temp             :   "   :   [float(format_temp(t_batt2[0])), units["centigrade"]],
        "Input Condition                 :   "   :   [hex(cnd_input[0])],
        "Output Conditions 1             :   "   :   [hex(cnd_output1[0])],
        "Output Conditions 2             :   "   :   [hex(cnd_output2[0])],
        "Power ON Cycle Counter          :   "   :   [por_cycles[0]],
        "Under Voltage Cond Counter      :   "   :   [hex(v_under[0])],
        "Short Circuit Cond Counter      :   "   :   [hex(v_short[0])],
        "Over Temp Cond Counter          :   "   :   [hex(v_overtemp[0])],
        "Battpack1 temp sensor 1 max temp:   "   :   [float(format_temp(t_max1[0])), units["centigrade"]],
        "Battpack1 temp sensor 1 min temp:   "   :   [float(format_temp(t_min1[0])), units["centigrade"]],
        "Default Vals LUPs & fastcharge  :   "   :   [hex(def1[0])],
        "Default Vals OUTs 1:6           :   "   :   [hex(def2[0])],
        "Battery Internal Resistance     :   "   :   [float(r_batt[0] * 1.4972656), units["ohm"]],
        "Battery Ideal Voltage           :   "   :   [float(v_ideal_batt[0] * 0.0023394775), units["volt"]],
        "UHF Antenna Registers           :   "   :   [("ANTENNA - 0x{}".format(str(UHFAnt[0]).upper())) if UHFAnt[0] == ANTENNA_REGISTERS_OFF else ("ANTENNA: {CONNECTED - DEPLOYED} - 0x" + str(UHFAnt[0]))],
        "UHF Status Control Word         :   "   :   [hex(scw[0])],
    }

    print("\n")
    try:
        pprint.pprint(frame_struct, sort_dicts=False)
    except KeyboardInterrupt:
        pass
    return 0

def format_frame(input_file):
    """ Preliminary formatting of beacon frame """

    with open(input_file, 'rb') as f:

        # Store Frame
        frame = f.read()
        frame_stripped = frame.strip()

        separate_chunks = [num for num in frame_stripped]
        frame_string = binascii.hexlify(data = frame_stripped).decode('ascii')
        
        frame_array   = []
        header_bytes  = []
        size_bytes    = []
        payload_bytes = []
        
        for i,j in zip(frame_string[::2], frame_string[1::2]):
            frame_array.append(i + j)

        # Header Bytes
        header_bytes = frame_array[0]

        # Size Bytes
        size_bytes = frame_array[1]

        # Payload Bytes
        payload_bytes = frame_array[1:len(frame_array)]
        payload_bytes_visual = payload_bytes.copy()

        # Print additional frame information
        #print("\nEntire frame: {}".format(frame_array))
        #print("\nHeader bytes: {}".format(header_bytes))
        #print("\nSize Bytes: {}(hex) | {}(int)".format(hex(int(size_bytes,16)), int(size_bytes, 16)))
        #print("\nPayload Bytes: {}".format(payload_bytes_visual))

        frame_parts = [header_bytes, size_bytes, payload_bytes]
        return frame_parts

def main():

    opts = [opt for opt in sys.argv[0:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[0:] if not arg.startswith("-")]

    if '-h' in opts:
        help_flag = True
        print(app_info(help_flag))
    elif '' in args:
        help_flag = True
        print(app_info(help_flag))
    elif '-v' in opts:
        help_flag = False
        VER = app_info(help_flag)
        print("Version: ", VER)
    else:
        if len(args) == 1:
            help_flag = True
            print(app_info(help_flag))
            #continue;
        elif ".txt" in args[1] or ".bin" in args[1]:
            frame = format_frame(args[1])
            impl_struct(frame)

if __name__ == '__main__':
    main()
