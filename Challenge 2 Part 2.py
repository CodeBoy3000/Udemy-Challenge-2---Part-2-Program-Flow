ip_address = input("Please enter an IP address: ")
if len(ip_address) == 0 or ip_address[-1] != '.':
    ip_address += '.'

segment = 1
segment_length = 0

for character in ip_address:
    if character == '.':
        if segment_length == 1:
            print("segment {} contains {} character".format(segment, segment_length))
        else:
            print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1