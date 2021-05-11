# -*- coding: utf-8 -*-
import js2py

engTypeToKorJS='''
function javascriptCode(a,b) {
    var res = 0;
    res = a + b;
    console.log( res );
    return res;
}
'''
if __name__ == '__main__':
    engTypeToKor = js2py.eval_js(engTypeToKorJS)
    print engTypeToKor(1, 2)

# js2py.translate_file('example.js', 'example.py')
# 위에처럼 함수로 하고 write해서 연결하는걸로

