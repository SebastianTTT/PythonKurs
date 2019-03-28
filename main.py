# -*- coding: utf-8 -*-
# untitled01/main.py

class Ramka:
    def __init__(self, znak):
        """
        Konstruktor
        :param znak: znak ktorym bedzie rysowana ramka
        """
        self.znak = znak;

    def __str__(self):
        return "Ramka " + self.znak

    def linia(self,ile):
        """
        Rusuje linie o podanej dlugosci
        :param ile:
        :return:
        """
        for _ in range(ile+2):
            print(self.znak)
        print()

    def rysuj(self, zawartosc):
        """
        Wyswietla podany tekst w ramce narysowanym znakiem
        podanym w konstruktorze
        :param zawartosc: co wyswietlic
        :return:
        """
        dlugosc = len(str(zawartosc))
        self.linia(dlugosc)
        print("{0}{1}{0}".format(self.znak, zawartosc))
        self.linia(dlugosc)


