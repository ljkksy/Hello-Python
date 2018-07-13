#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1=input('请输入你上学期的成绩:')
s2=input('请输入你这学期的成绩:')
r=(s2-s1)/s1*100
if r>=0:
    print("你成绩提高的百分点:'%.1f%%'" % r)
else:
    print("你成绩降低的百分点:'-%.1f%%'" % r)