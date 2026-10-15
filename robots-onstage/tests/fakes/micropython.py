"""Falso de `micropython`: const y decoradores que en el PC no hacen nada."""


def const(valor):
    return valor


def native(funcion):
    return funcion


def viper(funcion):
    return funcion
