# 通用异常
# try:
#     pass   //正常执行代码
# except Exception as exp:
#     pass   //报错信息和处理机制


# try:
#     with open('imgs/amd-logo.png', 'rb') as img_amd:
#         img_data = img_amd.read()
#     print('Image Opened.')
# except Exception as Exp:
#     print('Exp', Exp)


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)