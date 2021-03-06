# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:53:59 2015

@author: croeer
"""

import unittest
import cv2
import imutils
from functions import *

class StellungenTest(unittest.TestCase):
    def test_stellung1(self):
        img_rgb = cv2.imread('samples/stellung1.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '5k2/4rpbQ/pq4p1/3p2P1/2pP1BP1/2P2PK1/P7/4R3')

    def test_stellung2(self):
        img_rgb = cv2.imread('samples/stellung2.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '7k/2q1bQ2/4npP1/1p2p3/4P1b1/2Pp4/5PP1/3R2K1')

    def test_stellung3(self):
        img_rgb = cv2.imread('samples/stellung3.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '1rb1nrk1/2q2p1p/p1p3p1/2QNP3/P7/6P1/1PP2P1P/3RR1K1')

    def test_stellung4(self):
        img_rgb = cv2.imread('samples/stellung4.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '7R/8/r6p/5Kpk/8/8/3r4/6R1')

    def test_stellung5(self):
        img_rgb = cv2.imread('samples/stellung5.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '8/8/Pk1b4/1P6/2K5/6R1/8/3r4')

    def test_stellung6_1(self):
        img_rgb = cv2.imread('samples/stellung6-1.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '7k/1p2Q1p1/4Bn2/3p2q1/P2Pp2p/2N1P3/5K1P/8')

    def test_stellung6_2(self):
        img_rgb = cv2.imread('samples/stellung6-2.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, '7k/1p2Q1p1/8/3p2q1/P2Pp1Bp/2N1P3/5K1P/8')

    def test_stellung7(self):
        img_rgb = cv2.imread('samples/stellung7.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, 'r5rk/pp2p2p/3pqnQ1/8/4P3/2N2P2/PPP3P1/2KR3R')
                        
    def test_beginn_stellung(self):
        img_rgb = cv2.imread('samples/all_pieces2.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
        img_masked,b = getBoard(img_gray)
        img_board = img_gray[ b[1]:b[1]+b[3] , b[0]:b[0]+b[2] ]

        fen, _ = setupBoard(b, img_board)

        self.assertEqual(fen, 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

if __name__ == '__main__':
    unittest.main()