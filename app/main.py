#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
def main(argv, options):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.

    list = []
    list.append("(")
    for i, v in enumerate(argv):
      if v != " ":
        list.append(v)
        
      print("argv[{0}]: {1}".format(i, v))
    list.append(")")
    print list


def hoge(argv, options):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.

  list = []
  list.append("(")
  for i, v in enumerate(argv):
    if v != " ":
      list.append(v)

    print("argv[{0}]: {1}".format(i, v))
  list.append(")")
  print list

  flag1 = 0
  flag2 = 0
  graph = []
  node = []
  
  for i in range(len(list)):
  
    print i,list[i]

    if flag2 == 1:
      node.append(list[i])

    if flag1 == 1:
      if list[i] == "+":
        node.append(list[i])        
        graph.append(node)
        node = []
        node.append(list[i-1])        
        flag1-=1
        flag2+=1
      elif list[i] == "-":
        node.append(list[i])
        graph.append(node)
        node = []
        node.append(list[i-1])
        flag1-=1
        flag2+=1
      elif list[i] == "*":
        node.append(list[i])
        graph.append(node)
        node = []
        node.append(list[i-1])
        flag1-=1
        flag2+=1
      elif list[i] == "/":
        node.append(list[i])
        graph.append(node)
        node = []
        node.append(list[i-1])
        flag1-=1
        flag2+=1


    if list[i] == "(":
      flag1 +=1
  graph.append(node)

  print graph

    
main("1 + 2","1")
