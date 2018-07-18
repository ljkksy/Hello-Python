# -*- coding: utf-8 -*-
Height=input('请输入您的身高:')
Weight=input('请输入您的体重:')
BMI=weight/Height/Height
if BMI<18.5:
    print('您的体重过轻')
elif 18.5<=BMI<25:
    print('您的体重正常')
elif 25<=BMI<28:
    print('您的体重过重')
elif 28<=BMI<32:
    print('您的体重偏肥胖')
else:
    print('你的体重严重肥胖')