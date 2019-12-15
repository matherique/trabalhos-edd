#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

    def __str__(self):
        return f"{self.value}"

