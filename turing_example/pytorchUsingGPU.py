import torch
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

if torch.cuda.is_available():
    print('CUDA available')
    print('devices')
    for i in range(torch.cuda.device_count()):
        print('device', i)
        print(torch.cuda.get_device_name(i))
        mem = torch.cuda.mem_get_info(i) 
        print(f'free memory {convert_size(mem[0])}')
        print(f'total memory {convert_size(mem[1])}')
else:
    print('CUDA *not* available')
