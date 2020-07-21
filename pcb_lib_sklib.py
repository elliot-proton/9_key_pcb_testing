from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

pcb_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'resistor', 'dest':TEMPLATE, 'tool':SKIDL, 'match_pin_substring':False, 'keywords':'', 'description':'', 'F1':'resistor', 'datasheet':'', 'ref_prefix':'R', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Resistor_SMD:R_0201_0603Metric', 'pins':[
            Pin(num='1',name='RH',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='2',name='RL',func=Pin.types.BIDIR,do_erc=True)] })])