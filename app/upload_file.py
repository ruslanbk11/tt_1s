#! /usr/bin/env python3

import sys
import base64

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} filename".format(sys.argv[0]))
        sys.exit(1)
    filename = sys.argv[1]
    service = ServiceProxy('')
    with open( filename, 'rb') as input_file::
        content = input_file.read()
        b64_content = base64.b64encode(conten).decode('utf-8')
        print(type(b64_content))

        response = service.api.upload_file(b64_content)
        print("Responce: {}".format(response))
