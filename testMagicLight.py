from subprocess import call


secret_bt_handle = '0x002e'
secret_start_byte = '56'
secret_color_byte = 'F0'
secret_white_byte = '0F'
secret_end_byte = 'AA'
# basic change-color-to-purple string
#a_str = secret_start_byte + 'f00080' + '00' + secret_color_byte + secret_end_byte

a_str = '99' + 'ff0000' + 'ff00a0' + '0000ff' + 'ffffff' + '010203010203010203010203010203010203010203010203010203010203010203010203' + '013aff66'
try:
    call(['sudo', 'gatttool', '-b', '04:a3:16:a7:39:61', '--char-write-req', '-a', '0x002e', '-n', a_str])
    #call(['sudo', 'gatttool', '-b', '04:a3:16:a7:3b:4e', '--char-write', '-a', secret_bt_handle, '-n', a_str])
except:
    pass
