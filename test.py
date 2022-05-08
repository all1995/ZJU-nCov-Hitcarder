import requests
import ddddocr

main_url = 'https://healthreport.zju.edu.cn/ncov/wap/default/index'
captcha_url = 'https://healthreport.zju.edu.cn/ncov/wap/default/code'
ocr = ddddocr.DdddOcr()

sess = requests.session()

cookie_dict = {'eai-sess': 'q7t9nc9lb4fjtc1pb3n5b61cu4'}
sess.cookies = requests.cookies.cookiejar_from_dict(cookie_dict)

resp = sess.get(captcha_url)
captcha = ocr.classification(resp.content)
print(captcha)
