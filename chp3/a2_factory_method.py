# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_factory_method.py
@Time: 2019-09-18 12:28
@Last_update: 2019-09-18 12:28
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


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass
    

class PersonalSection(Section):
    def describe(self):
        print('personal section')
        
        
class AlbumSection(Section):
    def describe(self):
        print('album section')
        
        
class PatentSection(Section):
    def describe(self):
        print('patent section')
        
        
class PublicationSection(Section):
    def describe(self):
        print('publication section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(PatentSection)
        self.addSections(PublicationSection)


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(AlbumSection)


if __name__ == '__main__':
    profile_type = 'facebook'
    profile = eval(profile_type)()
    print(profile.getSections())