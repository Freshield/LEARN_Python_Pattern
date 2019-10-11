#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_compiler.py
@Time: 2020-03-05 10:51
@Last_update: 2020-03-05 10:51
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class IOSCompiler(Compiler):
    def collectSource(self):
        print('Collecting Swift Source Code')

    def compileToObject(self):
        print('Compiling Swift code to LLVM bitcode')

    def run(self):
        print('Program runing on runtime environment')


if __name__ == '__main__':
    iOS = IOSCompiler()
    iOS.compileAndRun()