import random
L1 = ['penalty 1 T1:', 'penalty 2 T1:', 'penalty 3 T1:', 'penalty 4 T1:', 'penalty 5 T1:', 'penalty 6 T1:', 'penalty 7 T1:', 'penalty 8 T1:', 'penalty 9 T1:', 'penalty 10 T1:', 'penalty 11 T1:', 'penalty 12 T1:', 'penalty 13 T1:', 'penalty 14 T1:', 'penalty 15 T1:', 'penalty 16 T1:', 'penalty 17 T1:', 'penalty 18 T1:', 'penalty 19 T1:', 'penalty 20 T1:', 'penaltys T1:']
L2 = ['penalty 1 T2:', 'penalty 2 T2:', 'penalty 3 T2:', 'penalty 4 T2:', 'penalty 5 T2:', 'penalty 6 T2:', 'penalty 7 T2:', 'penalty 8 T2:', 'penalty 9 T2:', 'penalty 10 T2:', 'penalty 11 T2:', 'penalty 12 T2:', 'penalty 13 T2:', 'penalty 14 T2:', 'penalty 15 T2:', 'penalty 16 T2:', 'penalty 17 T2:', 'penalty 18 T2:', 'penalty 19 T2:', 'penalty 20 T2:', 'penaltys T2:']
L3 = ['penalty 1 T3:', 'penalty 2 T3:', 'penalty 3 T3:', 'penalty 4 T3:', 'penalty 5 T3:', 'penalty 6 T3:', 'penalty 7 T3:', 'penalty 8 T3:', 'penalty 9 T3:', 'penalty 10 T3:', 'penalty 11 T3:', 'penalty 12 T3:', 'penalty 13 T3:', 'penalty 14 T3:', 'penalty 15 T3:', 'penalty 16 T3:', 'penalty 17 T3:', 'penalty 18 T3:', 'penalty 19 T3:', 'penalty 20 T3:', 'penaltys T3:']
L4 = ['penalty 1 T4:', 'penalty 2 T4:', 'penalty 3 T4:', 'penalty 4 T4:', 'penalty 5 T4:', 'penalty 6 T4:', 'penalty 7 T4:', 'penalty 8 T4:', 'penalty 9 T4:', 'penalty 10 T4:', 'penalty 11 T4:', 'penalty 12 T4:', 'penalty 13 T4:', 'penalty 14 T4:', 'penalty 15 T4:', 'penalty 16 T4:', 'penalty 17 T4:', 'penalty 18 T4:', 'penalty 19 T4:', 'penalty 20 T4:', 'penaltys T4:']
L5 = ['penalty 1 T5:', 'penalty 2 T5:', 'penalty 3 T5:', 'penalty 4 T5:', 'penalty 5 T5:', 'penalty 6 T5:', 'penalty 7 T5:', 'penalty 8 T5:', 'penalty 9 T5:', 'penalty 10 T5:', 'penalty 11 T5:', 'penalty 12 T5:', 'penalty 13 T5:', 'penalty 14 T5:', 'penalty 15 T5:', 'penalty 16 T5:', 'penalty 17 T5:', 'penalty 18 T5:', 'penalty 19 T5:', 'penalty 20 T5:', 'penaltys T5:']
L6 = ['penalty 1 T6:', 'penalty 2 T6:', 'penalty 3 T6:', 'penalty 4 T6:', 'penalty 5 T6:', 'penalty 6 T6:', 'penalty 7 T6:', 'penalty 8 T6:', 'penalty 9 T6:', 'penalty 10 T6:', 'penalty 11 T6:', 'penalty 12 T6:', 'penalty 13 T6:', 'penalty 14 T6:', 'penalty 15 T6:', 'penalty 16 T6:', 'penalty 17 T6:', 'penalty 18 T6:', 'penalty 19 T6:', 'penalty 20 T6:', 'penaltys T6:']
L7 = ['penalty 1 T7:', 'penalty 2 T7:', 'penalty 3 T7:', 'penalty 4 T7:', 'penalty 5 T7:', 'penalty 6 T7:', 'penalty 7 T7:', 'penalty 8 T7:', 'penalty 9 T7:', 'penalty 10 T7:', 'penalty 11 T7:', 'penalty 12 T7:', 'penalty 13 T7:', 'penalty 14 T7:', 'penalty 15 T7:', 'penalty 16 T7:', 'penalty 17 T7:', 'penalty 18 T7:', 'penalty 19 T7:', 'penalty 20 T7:', 'penaltys T7:']
L8 = ['penalty 1 T8:', 'penalty 2 T8:', 'penalty 3 T8:', 'penalty 4 T8:', 'penalty 5 T8:', 'penalty 6 T8:', 'penalty 7 T8:', 'penalty 8 T8:', 'penalty 9 T8:', 'penalty 10 T8:', 'penalty 11 T8:', 'penalty 12 T8:', 'penalty 13 T8:', 'penalty 14 T8:', 'penalty 15 T8:', 'penalty 16 T8:', 'penalty 17 T8:', 'penalty 18 T8:', 'penalty 19 T8:', 'penalty 20 T8:', 'penaltys T8:']
L9 = ['penalty 1 T9:', 'penalty 2 T9:', 'penalty 3 T9:', 'penalty 4 T9:', 'penalty 5 T9:', 'penalty 6 T9:', 'penalty 7 T9:', 'penalty 8 T9:', 'penalty 9 T9:', 'penalty 10 T9:', 'penalty 11 T9:', 'penalty 12 T9:', 'penalty 13 T9:', 'penalty 14 T9:', 'penalty 15 T9:', 'penalty 16 T9:', 'penalty 17 T9:', 'penalty 18 T9:', 'penalty 19 T9:', 'penalty 20 T9:', 'penaltys T9:']
L10 = ['penalty 1 T10:', 'penalty 2 T10:', 'penalty 3 T10:', 'penalty 4 T10:', 'penalty 5 T10:', 'penalty 6 T10:', 'penalty 7 T10:', 'penalty 8 T10:', 'penalty 9 T10:', 'penalty 10 T10:', 'penalty 11 T10:', 'penalty 12 T10:', 'penalty 13 T10:', 'penalty 14 T10:', 'penalty 15 T10:', 'penalty 16 T10:', 'penalty 17 T10:', 'penalty 18 T10:', 'penalty 19 T10:', 'penalty 20 T10:', 'penaltys T10:']
L11 = ['penalty 1 T11:', 'penalty 2 T11:', 'penalty 3 T11:', 'penalty 4 T11:', 'penalty 5 T11:', 'penalty 6 T11:', 'penalty 7 T11:', 'penalty 8 T11:', 'penalty 9 T11:', 'penalty 10 T11:', 'penalty 11 T11:', 'penalty 12 T11:', 'penalty 13 T11:', 'penalty 14 T11:', 'penalty 15 T11:', 'penalty 16 T11:', 'penalty 17 T11:', 'penalty 18 T11:', 'penalty 19 T11:', 'penalty 20 T11:', 'penaltys T11:']
L12 = ['penalty 1 T12:', 'penalty 2 T12:', 'penalty 3 T12:', 'penalty 4 T12:', 'penalty 5 T12:', 'penalty 6 T12:', 'penalty 7 T12:', 'penalty 8 T12:', 'penalty 9 T12:', 'penalty 10 T12:', 'penalty 11 T12:', 'penalty 12 T12:', 'penalty 13 T12:', 'penalty 14 T12:', 'penalty 15 T12:', 'penalty 16 T12:', 'penalty 17 T12:', 'penalty 18 T12:', 'penalty 19 T12:', 'penalty 20 T12:', 'penaltys T12:']
L13 = ['penalty 1 T13:', 'penalty 2 T13:', 'penalty 3 T13:', 'penalty 4 T13:', 'penalty 5 T13:', 'penalty 6 T13:', 'penalty 7 T13:', 'penalty 8 T13:', 'penalty 9 T13:', 'penalty 10 T13:', 'penalty 11 T13:', 'penalty 12 T13:', 'penalty 13 T13:', 'penalty 14 T13:', 'penalty 15 T13:', 'penalty 16 T13:', 'penalty 17 T13:', 'penalty 18 T13:', 'penalty 19 T13:', 'penalty 20 T13:', 'penaltys T13:']
L14 = ['penalty 1 T14:', 'penalty 2 T14:', 'penalty 3 T14:', 'penalty 4 T14:', 'penalty 5 T14:', 'penalty 6 T14:', 'penalty 7 T14:', 'penalty 8 T14:', 'penalty 9 T14:', 'penalty 10 T14:', 'penalty 11 T14:', 'penalty 12 T14:', 'penalty 13 T14:', 'penalty 14 T14:', 'penalty 15 T14:', 'penalty 16 T14:', 'penalty 17 T14:', 'penalty 18 T14:', 'penalty 19 T14:', 'penalty 20 T14:', 'penaltys T14:']
L15 = ['penalty 1 T15:', 'penalty 2 T15:', 'penalty 3 T15:', 'penalty 4 T15:', 'penalty 5 T15:', 'penalty 6 T15:', 'penalty 7 T15:', 'penalty 8 T15:', 'penalty 9 T15:', 'penalty 10 T15:', 'penalty 11 T15:', 'penalty 12 T15:', 'penalty 13 T15:', 'penalty 14 T15:', 'penalty 15 T15:', 'penalty 16 T15:', 'penalty 17 T15:', 'penalty 18 T15:', 'penalty 19 T15:', 'penalty 20 T15:', 'penaltys T15:']
L16 = ['penalty 1 T16:', 'penalty 2 T16:', 'penalty 3 T16:', 'penalty 4 T16:', 'penalty 5 T16:', 'penalty 6 T16:', 'penalty 7 T16:', 'penalty 8 T16:', 'penalty 9 T16:', 'penalty 10 T16:', 'penalty 11 T16:', 'penalty 12 T16:', 'penalty 13 T16:', 'penalty 14 T16:', 'penalty 15 T16:', 'penalty 16 T16:', 'penalty 17 T16:', 'penalty 18 T16:', 'penalty 19 T16:', 'penalty 20 T16:', 'penaltys T16:']
L17 = ['penalty 1 T17:', 'penalty 2 T17:', 'penalty 3 T17:', 'penalty 4 T17:', 'penalty 5 T17:', 'penalty 6 T17:', 'penalty 7 T17:', 'penalty 8 T17:', 'penalty 9 T17:', 'penalty 10 T17:', 'penalty 11 T17:', 'penalty 12 T17:', 'penalty 13 T17:', 'penalty 14 T17:', 'penalty 15 T17:', 'penalty 16 T17:', 'penalty 17 T17:', 'penalty 18 T17:', 'penalty 19 T17:', 'penalty 20 T17:', 'penaltys T17:']
L18 = ['penalty 1 T18:', 'penalty 2 T18:', 'penalty 3 T18:', 'penalty 4 T18:', 'penalty 5 T18:', 'penalty 6 T18:', 'penalty 7 T18:', 'penalty 8 T18:', 'penalty 9 T18:', 'penalty 10 T18:', 'penalty 11 T18:', 'penalty 12 T18:', 'penalty 13 T18:', 'penalty 14 T18:', 'penalty 15 T18:', 'penalty 16 T18:', 'penalty 17 T18:', 'penalty 18 T18:', 'penalty 19 T18:', 'penalty 20 T18:', 'penaltys T18:']
L19 = ['penalty 1 T19:', 'penalty 2 T19:', 'penalty 3 T19:', 'penalty 4 T19:', 'penalty 5 T19:', 'penalty 6 T19:', 'penalty 7 T19:', 'penalty 8 T19:', 'penalty 9 T19:', 'penalty 10 T19:', 'penalty 11 T19:', 'penalty 12 T19:', 'penalty 13 T19:', 'penalty 14 T19:', 'penalty 15 T19:', 'penalty 16 T19:', 'penalty 17 T19:', 'penalty 18 T19:', 'penalty 19 T19:', 'penalty 20 T19:', 'penaltys T19:']
L20 = ['penalty 1 T20:', 'penalty 2 T20:', 'penalty 3 T20:', 'penalty 4 T20:', 'penalty 5 T20:', 'penalty 6 T20:', 'penalty 7 T20:', 'penalty 8 T20:', 'penalty 9 T20:', 'penalty 10 T20:', 'penalty 11 T20:', 'penalty 12 T20:', 'penalty 13 T20:', 'penalty 14 T20:', 'penalty 15 T20:', 'penalty 16 T20:', 'penalty 17 T20:', 'penalty 18 T20:', 'penalty 19 T20:', 'penalty 20 T20:', 'penaltys T20:']
L21 = ['penalty 1 T21:', 'penalty 2 T21:', 'penalty 3 T21:', 'penalty 4 T21:', 'penalty 5 T21:', 'penalty 6 T21:', 'penalty 7 T21:', 'penalty 8 T21:', 'penalty 9 T21:', 'penalty 10 T21:', 'penalty 11 T21:', 'penalty 12 T21:', 'penalty 13 T21:', 'penalty 14 T21:', 'penalty 15 T21:', 'penalty 16 T21:', 'penalty 17 T21:', 'penalty 18 T21:', 'penalty 19 T21:', 'penalty 20 T21:', 'penaltys T21:']
L22 = ['penalty 1 T22:', 'penalty 2 T22:', 'penalty 3 T22:', 'penalty 4 T22:', 'penalty 5 T22:', 'penalty 6 T22:', 'penalty 7 T22:', 'penalty 8 T22:', 'penalty 9 T22:', 'penalty 10 T22:', 'penalty 11 T22:', 'penalty 12 T22:', 'penalty 13 T22:', 'penalty 14 T22:', 'penalty 15 T22:', 'penalty 16 T22:', 'penalty 17 T22:', 'penalty 18 T22:', 'penalty 19 T22:', 'penalty 20 T22:', 'penaltys T22:']
L23 = ['penalty 1 T23:', 'penalty 2 T23:', 'penalty 3 T23:', 'penalty 4 T23:', 'penalty 5 T23:', 'penalty 6 T23:', 'penalty 7 T23:', 'penalty 8 T23:', 'penalty 9 T23:', 'penalty 10 T23:', 'penalty 11 T23:', 'penalty 12 T23:', 'penalty 13 T23:', 'penalty 14 T23:', 'penalty 15 T23:', 'penalty 16 T23:', 'penalty 17 T23:', 'penalty 18 T23:', 'penalty 19 T23:', 'penalty 20 T23:', 'penaltys T23:']
L24 = ['penalty 1 T24:', 'penalty 2 T24:', 'penalty 3 T24:', 'penalty 4 T24:', 'penalty 5 T24:', 'penalty 6 T24:', 'penalty 7 T24:', 'penalty 8 T24:', 'penalty 9 T24:', 'penalty 10 T24:', 'penalty 11 T24:', 'penalty 12 T24:', 'penalty 13 T24:', 'penalty 14 T24:', 'penalty 15 T24:', 'penalty 16 T24:', 'penalty 17 T24:', 'penalty 18 T24:', 'penalty 19 T24:', 'penalty 20 T24:', 'penaltys T24:']
L25 = ['penalty 1 T25:', 'penalty 2 T25:', 'penalty 3 T25:', 'penalty 4 T25:', 'penalty 5 T25:', 'penalty 6 T25:', 'penalty 7 T25:', 'penalty 8 T25:', 'penalty 9 T25:', 'penalty 10 T25:', 'penalty 11 T25:', 'penalty 12 T25:', 'penalty 13 T25:', 'penalty 14 T25:', 'penalty 15 T25:', 'penalty 16 T25:', 'penalty 17 T25:', 'penalty 18 T25:', 'penalty 19 T25:', 'penalty 20 T25:', 'penaltys T25:']
L26 = ['penalty 1 T26:', 'penalty 2 T26:', 'penalty 3 T26:', 'penalty 4 T26:', 'penalty 5 T26:', 'penalty 6 T26:', 'penalty 7 T26:', 'penalty 8 T26:', 'penalty 9 T26:', 'penalty 10 T26:', 'penalty 11 T26:', 'penalty 12 T26:', 'penalty 13 T26:', 'penalty 14 T26:', 'penalty 15 T26:', 'penalty 16 T26:', 'penalty 17 T26:', 'penalty 18 T26:', 'penalty 19 T26:', 'penalty 20 T26:', 'penaltys T26:']
L27 = ['penalty 1 T27:', 'penalty 2 T27:', 'penalty 3 T27:', 'penalty 4 T27:', 'penalty 5 T27:', 'penalty 6 T27:', 'penalty 7 T27:', 'penalty 8 T27:', 'penalty 9 T27:', 'penalty 10 T27:', 'penalty 11 T27:', 'penalty 12 T27:', 'penalty 13 T27:', 'penalty 14 T27:', 'penalty 15 T27:', 'penalty 16 T27:', 'penalty 17 T27:', 'penalty 18 T27:', 'penalty 19 T27:', 'penalty 20 T27:', 'penaltys T27:']
L28 = ['penalty 1 T28:', 'penalty 2 T28:', 'penalty 3 T28:', 'penalty 4 T28:', 'penalty 5 T28:', 'penalty 6 T28:', 'penalty 7 T28:', 'penalty 8 T28:', 'penalty 9 T28:', 'penalty 10 T28:', 'penalty 11 T28:', 'penalty 12 T28:', 'penalty 13 T28:', 'penalty 14 T28:', 'penalty 15 T28:', 'penalty 16 T28:', 'penalty 17 T28:', 'penalty 18 T28:', 'penalty 19 T28:', 'penalty 20 T28:', 'penaltys T28:']
L29 = ['penalty 1 T29:', 'penalty 2 T29:', 'penalty 3 T29:', 'penalty 4 T29:', 'penalty 5 T29:', 'penalty 6 T29:', 'penalty 7 T29:', 'penalty 8 T29:', 'penalty 9 T29:', 'penalty 10 T29:', 'penalty 11 T29:', 'penalty 12 T29:', 'penalty 13 T29:', 'penalty 14 T29:', 'penalty 15 T29:', 'penalty 16 T29:', 'penalty 17 T29:', 'penalty 18 T29:', 'penalty 19 T29:', 'penalty 20 T29:', 'penaltys T29:']
L30 = ['penalty 1 T30:', 'penalty 2 T30:', 'penalty 3 T30:', 'penalty 4 T30:', 'penalty 5 T30:', 'penalty 6 T30:', 'penalty 7 T30:', 'penalty 8 T30:', 'penalty 9 T30:', 'penalty 10 T30:', 'penalty 11 T30:', 'penalty 12 T30:', 'penalty 13 T30:', 'penalty 14 T30:', 'penalty 15 T30:', 'penalty 16 T30:', 'penalty 17 T30:', 'penalty 18 T30:', 'penalty 19 T30:', 'penalty 20 T30:', 'penaltys T30:']
L31 = ['penalty 1 T31:', 'penalty 2 T31:', 'penalty 3 T31:', 'penalty 4 T31:', 'penalty 5 T31:', 'penalty 6 T31:', 'penalty 7 T31:', 'penalty 8 T31:', 'penalty 9 T31:', 'penalty 10 T31:', 'penalty 11 T31:', 'penalty 12 T31:', 'penalty 13 T31:', 'penalty 14 T31:', 'penalty 15 T31:', 'penalty 16 T31:', 'penalty 17 T31:', 'penalty 18 T31:', 'penalty 19 T31:', 'penalty 20 T31:', 'penaltys T31:']
L32 = ['penalty 1 T32:', 'penalty 2 T32:', 'penalty 3 T32:', 'penalty 4 T32:', 'penalty 5 T32:', 'penalty 6 T32:', 'penalty 7 T32:', 'penalty 8 T32:', 'penalty 9 T32:', 'penalty 10 T32:', 'penalty 11 T32:', 'penalty 12 T32:', 'penalty 13 T32:', 'penalty 14 T32:', 'penalty 15 T32:', 'penalty 16 T32:', 'penalty 17 T32:', 'penalty 18 T32:', 'penalty 19 T32:', 'penalty 20 T32:', 'penaltys T32:']
L33 = ['penalty 1 T33:', 'penalty 2 T33:', 'penalty 3 T33:', 'penalty 4 T33:', 'penalty 5 T33:', 'penalty 6 T33:', 'penalty 7 T33:', 'penalty 8 T33:', 'penalty 9 T33:', 'penalty 10 T33:', 'penalty 11 T33:', 'penalty 12 T33:', 'penalty 13 T33:', 'penalty 14 T33:', 'penalty 15 T33:', 'penalty 16 T33:', 'penalty 17 T33:', 'penalty 18 T33:', 'penalty 19 T33:', 'penalty 20 T33:', 'penaltys T33:']
L34 = ['penalty 1 T34:', 'penalty 2 T34:', 'penalty 3 T34:', 'penalty 4 T34:', 'penalty 5 T34:', 'penalty 6 T34:', 'penalty 7 T34:', 'penalty 8 T34:', 'penalty 9 T34:', 'penalty 10 T34:', 'penalty 11 T34:', 'penalty 12 T34:', 'penalty 13 T34:', 'penalty 14 T34:', 'penalty 15 T34:', 'penalty 16 T34:', 'penalty 17 T34:', 'penalty 18 T34:', 'penalty 19 T34:', 'penalty 20 T34:', 'penaltys T34:']
L35 = ['penalty 1 T35:', 'penalty 2 T35:', 'penalty 3 T35:', 'penalty 4 T35:', 'penalty 5 T35:', 'penalty 6 T35:', 'penalty 7 T35:', 'penalty 8 T35:', 'penalty 9 T35:', 'penalty 10 T35:', 'penalty 11 T35:', 'penalty 12 T35:', 'penalty 13 T35:', 'penalty 14 T35:', 'penalty 15 T35:', 'penalty 16 T35:', 'penalty 17 T35:', 'penalty 18 T35:', 'penalty 19 T35:', 'penalty 20 T35:', 'penaltys T35:']
L36 = ['penalty 1 T36:', 'penalty 2 T36:', 'penalty 3 T36:', 'penalty 4 T36:', 'penalty 5 T36:', 'penalty 6 T36:', 'penalty 7 T36:', 'penalty 8 T36:', 'penalty 9 T36:', 'penalty 10 T36:', 'penalty 11 T36:', 'penalty 12 T36:', 'penalty 13 T36:', 'penalty 14 T36:', 'penalty 15 T36:', 'penalty 16 T36:', 'penalty 17 T36:', 'penalty 18 T36:', 'penalty 19 T36:', 'penalty 20 T36:', 'penaltys T36:']
L37 = ['penalty 1 T37:', 'penalty 2 T37:', 'penalty 3 T37:', 'penalty 4 T37:', 'penalty 5 T37:', 'penalty 6 T37:', 'penalty 7 T37:', 'penalty 8 T37:', 'penalty 9 T37:', 'penalty 10 T37:', 'penalty 11 T37:', 'penalty 12 T37:', 'penalty 13 T37:', 'penalty 14 T37:', 'penalty 15 T37:', 'penalty 16 T37:', 'penalty 17 T37:', 'penalty 18 T37:', 'penalty 19 T37:', 'penalty 20 T37:', 'penaltys T37:']
L38 = ['penalty 1 T38:', 'penalty 2 T38:', 'penalty 3 T38:', 'penalty 4 T38:', 'penalty 5 T38:', 'penalty 6 T38:', 'penalty 7 T38:', 'penalty 8 T38:', 'penalty 9 T38:', 'penalty 10 T38:', 'penalty 11 T38:', 'penalty 12 T38:', 'penalty 13 T38:', 'penalty 14 T38:', 'penalty 15 T38:', 'penalty 16 T38:', 'penalty 17 T38:', 'penalty 18 T38:', 'penalty 19 T38:', 'penalty 20 T38:', 'penaltys T38:']
L39 = ['penalty 1 T39:', 'penalty 2 T39:', 'penalty 3 T39:', 'penalty 4 T39:', 'penalty 5 T39:', 'penalty 6 T39:', 'penalty 7 T39:', 'penalty 8 T39:', 'penalty 9 T39:', 'penalty 10 T39:', 'penalty 11 T39:', 'penalty 12 T39:', 'penalty 13 T39:', 'penalty 14 T39:', 'penalty 15 T39:', 'penalty 16 T39:', 'penalty 17 T39:', 'penalty 18 T39:', 'penalty 19 T39:', 'penalty 20 T39:', 'penaltys T39:']
L40 = ['penalty 1 T40:', 'penalty 2 T40:', 'penalty 3 T40:', 'penalty 4 T40:', 'penalty 5 T40:', 'penalty 6 T40:', 'penalty 7 T40:', 'penalty 8 T40:', 'penalty 9 T40:', 'penalty 10 T40:', 'penalty 11 T40:', 'penalty 12 T40:', 'penalty 13 T40:', 'penalty 14 T40:', 'penalty 15 T40:', 'penalty 16 T40:', 'penalty 17 T40:', 'penalty 18 T40:', 'penalty 19 T40:', 'penalty 20 T40:', 'penaltys T40:']
L41 = ['penalty 1 T41:', 'penalty 2 T41:', 'penalty 3 T41:', 'penalty 4 T41:', 'penalty 5 T41:', 'penalty 6 T41:', 'penalty 7 T41:', 'penalty 8 T41:', 'penalty 9 T41:', 'penalty 10 T41:', 'penalty 11 T41:', 'penalty 12 T41:', 'penalty 13 T41:', 'penalty 14 T41:', 'penalty 15 T41:', 'penalty 16 T41:', 'penalty 17 T41:', 'penalty 18 T41:', 'penalty 19 T41:', 'penalty 20 T41:', 'penaltys T41:']
L42 = ['penalty 1 T42:', 'penalty 2 T42:', 'penalty 3 T42:', 'penalty 4 T42:', 'penalty 5 T42:', 'penalty 6 T42:', 'penalty 7 T42:', 'penalty 8 T42:', 'penalty 9 T42:', 'penalty 10 T42:', 'penalty 11 T42:', 'penalty 12 T42:', 'penalty 13 T42:', 'penalty 14 T42:', 'penalty 15 T42:', 'penalty 16 T42:', 'penalty 17 T42:', 'penalty 18 T42:', 'penalty 19 T42:', 'penalty 20 T42:', 'penaltys T42:']
L43 = ['penalty 1 T43:', 'penalty 2 T43:', 'penalty 3 T43:', 'penalty 4 T43:', 'penalty 5 T43:', 'penalty 6 T43:', 'penalty 7 T43:', 'penalty 8 T43:', 'penalty 9 T43:', 'penalty 10 T43:', 'penalty 11 T43:', 'penalty 12 T43:', 'penalty 13 T43:', 'penalty 14 T43:', 'penalty 15 T43:', 'penalty 16 T43:', 'penalty 17 T43:', 'penalty 18 T43:', 'penalty 19 T43:', 'penalty 20 T43:', 'penaltys T43:']
L44 = ['penalty 1 T44:', 'penalty 2 T44:', 'penalty 3 T44:', 'penalty 4 T44:', 'penalty 5 T44:', 'penalty 6 T44:', 'penalty 7 T44:', 'penalty 8 T44:', 'penalty 9 T44:', 'penalty 10 T44:', 'penalty 11 T44:', 'penalty 12 T44:', 'penalty 13 T44:', 'penalty 14 T44:', 'penalty 15 T44:', 'penalty 16 T44:', 'penalty 17 T44:', 'penalty 18 T44:', 'penalty 19 T44:', 'penalty 20 T44:', 'penaltys T44:']
L45 = ['penalty 1 T45:', 'penalty 2 T45:', 'penalty 3 T45:', 'penalty 4 T45:', 'penalty 5 T45:', 'penalty 6 T45:', 'penalty 7 T45:', 'penalty 8 T45:', 'penalty 9 T45:', 'penalty 10 T45:', 'penalty 11 T45:', 'penalty 12 T45:', 'penalty 13 T45:', 'penalty 14 T45:', 'penalty 15 T45:', 'penalty 16 T45:', 'penalty 17 T45:', 'penalty 18 T45:', 'penalty 19 T45:', 'penalty 20 T45:', 'penaltys T45:']
L46 = ['penalty 1 T46:', 'penalty 2 T46:', 'penalty 3 T46:', 'penalty 4 T46:', 'penalty 5 T46:', 'penalty 6 T46:', 'penalty 7 T46:', 'penalty 8 T46:', 'penalty 9 T46:', 'penalty 10 T46:', 'penalty 11 T46:', 'penalty 12 T46:', 'penalty 13 T46:', 'penalty 14 T46:', 'penalty 15 T46:', 'penalty 16 T46:', 'penalty 17 T46:', 'penalty 18 T46:', 'penalty 19 T46:', 'penalty 20 T46:', 'penaltys T46:']
L47 = ['penalty 1 T47:', 'penalty 2 T47:', 'penalty 3 T47:', 'penalty 4 T47:', 'penalty 5 T47:', 'penalty 6 T47:', 'penalty 7 T47:', 'penalty 8 T47:', 'penalty 9 T47:', 'penalty 10 T47:', 'penalty 11 T47:', 'penalty 12 T47:', 'penalty 13 T47:', 'penalty 14 T47:', 'penalty 15 T47:', 'penalty 16 T47:', 'penalty 17 T47:', 'penalty 18 T47:', 'penalty 19 T47:', 'penalty 20 T47:', 'penaltys T47:']
L48 = ['penalty 1 T48:', 'penalty 2 T48:', 'penalty 3 T48:', 'penalty 4 T48:', 'penalty 5 T48:', 'penalty 6 T48:', 'penalty 7 T48:', 'penalty 8 T48:', 'penalty 9 T48:', 'penalty 10 T48:', 'penalty 11 T48:', 'penalty 12 T48:', 'penalty 13 T48:', 'penalty 14 T48:', 'penalty 15 T48:', 'penalty 16 T48:', 'penalty 17 T48:', 'penalty 18 T48:', 'penalty 19 T48:', 'penalty 20 T48:', 'penaltys T48:']
L49 = ['penalty 1 T49:', 'penalty 2 T49:', 'penalty 3 T49:', 'penalty 4 T49:', 'penalty 5 T49:', 'penalty 6 T49:', 'penalty 7 T49:', 'penalty 8 T49:', 'penalty 9 T49:', 'penalty 10 T49:', 'penalty 11 T49:', 'penalty 12 T49:', 'penalty 13 T49:', 'penalty 14 T49:', 'penalty 15 T49:', 'penalty 16 T49:', 'penalty 17 T49:', 'penalty 18 T49:', 'penalty 19 T49:', 'penalty 20 T49:', 'penaltys T49:']
L50 = ['penalty 1 T50:', 'penalty 2 T50:', 'penalty 3 T50:', 'penalty 4 T50:', 'penalty 5 T50:', 'penalty 6 T50:', 'penalty 7 T50:', 'penalty 8 T50:', 'penalty 9 T50:', 'penalty 10 T50:', 'penalty 11 T50:', 'penalty 12 T50:', 'penalty 13 T50:', 'penalty 14 T50:', 'penalty 15 T50:', 'penalty 16 T50:', 'penalty 17 T50:', 'penalty 18 T50:', 'penalty 19 T50:', 'penalty 20 T50:', 'penaltys T50:']
L51 = ['penalty 1 T51:', 'penalty 2 T51:', 'penalty 3 T51:', 'penalty 4 T51:', 'penalty 5 T51:', 'penalty 6 T51:', 'penalty 7 T51:', 'penalty 8 T51:', 'penalty 9 T51:', 'penalty 10 T51:', 'penalty 11 T51:', 'penalty 12 T51:', 'penalty 13 T51:', 'penalty 14 T51:', 'penalty 15 T51:', 'penalty 16 T51:', 'penalty 17 T51:', 'penalty 18 T51:', 'penalty 19 T51:', 'penalty 20 T51:', 'penaltys T51:']
L52 = ['penalty 1 T52:', 'penalty 2 T52:', 'penalty 3 T52:', 'penalty 4 T52:', 'penalty 5 T52:', 'penalty 6 T52:', 'penalty 7 T52:', 'penalty 8 T52:', 'penalty 9 T52:', 'penalty 10 T52:', 'penalty 11 T52:', 'penalty 12 T52:', 'penalty 13 T52:', 'penalty 14 T52:', 'penalty 15 T52:', 'penalty 16 T52:', 'penalty 17 T52:', 'penalty 18 T52:', 'penalty 19 T52:', 'penalty 20 T52:', 'penaltys T52:']
L53 = ['penalty 1 T53:', 'penalty 2 T53:', 'penalty 3 T53:', 'penalty 4 T53:', 'penalty 5 T53:', 'penalty 6 T53:', 'penalty 7 T53:', 'penalty 8 T53:', 'penalty 9 T53:', 'penalty 10 T53:', 'penalty 11 T53:', 'penalty 12 T53:', 'penalty 13 T53:', 'penalty 14 T53:', 'penalty 15 T53:', 'penalty 16 T53:', 'penalty 17 T53:', 'penalty 18 T53:', 'penalty 19 T53:', 'penalty 20 T53:', 'penaltys T53:']
L54 = ['penalty 1 T54:', 'penalty 2 T54:', 'penalty 3 T54:', 'penalty 4 T54:', 'penalty 5 T54:', 'penalty 6 T54:', 'penalty 7 T54:', 'penalty 8 T54:', 'penalty 9 T54:', 'penalty 10 T54:', 'penalty 11 T54:', 'penalty 12 T54:', 'penalty 13 T54:', 'penalty 14 T54:', 'penalty 15 T54:', 'penalty 16 T54:', 'penalty 17 T54:', 'penalty 18 T54:', 'penalty 19 T54:', 'penalty 20 T54:', 'penaltys T54:']
L55 = ['penalty 1 T55:', 'penalty 2 T55:', 'penalty 3 T55:', 'penalty 4 T55:', 'penalty 5 T55:', 'penalty 6 T55:', 'penalty 7 T55:', 'penalty 8 T55:', 'penalty 9 T55:', 'penalty 10 T55:', 'penalty 11 T55:', 'penalty 12 T55:', 'penalty 13 T55:', 'penalty 14 T55:', 'penalty 15 T55:', 'penalty 16 T55:', 'penalty 17 T55:', 'penalty 18 T55:', 'penalty 19 T55:', 'penalty 20 T55:', 'penaltys T55:']
L56 = ['penalty 1 T56:', 'penalty 2 T56:', 'penalty 3 T56:', 'penalty 4 T56:', 'penalty 5 T56:', 'penalty 6 T56:', 'penalty 7 T56:', 'penalty 8 T56:', 'penalty 9 T56:', 'penalty 10 T56:', 'penalty 11 T56:', 'penalty 12 T56:', 'penalty 13 T56:', 'penalty 14 T56:', 'penalty 15 T56:', 'penalty 16 T56:', 'penalty 17 T56:', 'penalty 18 T56:', 'penalty 19 T56:', 'penalty 20 T56:', 'penaltys T56:']
L57 = ['penalty 1 T57:', 'penalty 2 T57:', 'penalty 3 T57:', 'penalty 4 T57:', 'penalty 5 T57:', 'penalty 6 T57:', 'penalty 7 T57:', 'penalty 8 T57:', 'penalty 9 T57:', 'penalty 10 T57:', 'penalty 11 T57:', 'penalty 12 T57:', 'penalty 13 T57:', 'penalty 14 T57:', 'penalty 15 T57:', 'penalty 16 T57:', 'penalty 17 T57:', 'penalty 18 T57:', 'penalty 19 T57:', 'penalty 20 T57:', 'penaltys T57:']
L58 = ['penalty 1 T58:', 'penalty 2 T58:', 'penalty 3 T58:', 'penalty 4 T58:', 'penalty 5 T58:', 'penalty 6 T58:', 'penalty 7 T58:', 'penalty 8 T58:', 'penalty 9 T58:', 'penalty 10 T58:', 'penalty 11 T58:', 'penalty 12 T58:', 'penalty 13 T58:', 'penalty 14 T58:', 'penalty 15 T58:', 'penalty 16 T58:', 'penalty 17 T58:', 'penalty 18 T58:', 'penalty 19 T58:', 'penalty 20 T58:', 'penaltys T58:']
L59 = ['penalty 1 T59:', 'penalty 2 T59:', 'penalty 3 T59:', 'penalty 4 T59:', 'penalty 5 T59:', 'penalty 6 T59:', 'penalty 7 T59:', 'penalty 8 T59:', 'penalty 9 T59:', 'penalty 10 T59:', 'penalty 11 T59:', 'penalty 12 T59:', 'penalty 13 T59:', 'penalty 14 T59:', 'penalty 15 T59:', 'penalty 16 T59:', 'penalty 17 T59:', 'penalty 18 T59:', 'penalty 19 T59:', 'penalty 20 T59:', 'penaltys T59:']
L60 = ['penalty 1 T60:', 'penalty 2 T60:', 'penalty 3 T60:', 'penalty 4 T60:', 'penalty 5 T60:', 'penalty 6 T60:', 'penalty 7 T60:', 'penalty 8 T60:', 'penalty 9 T60:', 'penalty 10 T60:', 'penalty 11 T60:', 'penalty 12 T60:', 'penalty 13 T60:', 'penalty 14 T60:', 'penalty 15 T60:', 'penalty 16 T60:', 'penalty 17 T60:', 'penalty 18 T60:', 'penalty 19 T60:', 'penalty 20 T60:', 'penaltys T60:']
L61 = ['penalty 1 T61:', 'penalty 2 T61:', 'penalty 3 T61:', 'penalty 4 T61:', 'penalty 5 T61:', 'penalty 6 T61:', 'penalty 7 T61:', 'penalty 8 T61:', 'penalty 9 T61:', 'penalty 10 T61:', 'penalty 11 T61:', 'penalty 12 T61:', 'penalty 13 T61:', 'penalty 14 T61:', 'penalty 15 T61:', 'penalty 16 T61:', 'penalty 17 T61:', 'penalty 18 T61:', 'penalty 19 T61:', 'penalty 20 T61:', 'penaltys T61:']
L62 = ['penalty 1 T62:', 'penalty 2 T62:', 'penalty 3 T62:', 'penalty 4 T62:', 'penalty 5 T62:', 'penalty 6 T62:', 'penalty 7 T62:', 'penalty 8 T62:', 'penalty 9 T62:', 'penalty 10 T62:', 'penalty 11 T62:', 'penalty 12 T62:', 'penalty 13 T62:', 'penalty 14 T62:', 'penalty 15 T62:', 'penalty 16 T62:', 'penalty 17 T62:', 'penalty 18 T62:', 'penalty 19 T62:', 'penalty 20 T62:', 'penaltys T62:']
L63 = ['penalty 1 T63:', 'penalty 2 T63:', 'penalty 3 T63:', 'penalty 4 T63:', 'penalty 5 T63:', 'penalty 6 T63:', 'penalty 7 T63:', 'penalty 8 T63:', 'penalty 9 T63:', 'penalty 10 T63:', 'penalty 11 T63:', 'penalty 12 T63:', 'penalty 13 T63:', 'penalty 14 T63:', 'penalty 15 T63:', 'penalty 16 T63:', 'penalty 17 T63:', 'penalty 18 T63:', 'penalty 19 T63:', 'penalty 20 T63:', 'penaltys T63:']
L64 = ['penalty 1 T64:', 'penalty 2 T64:', 'penalty 3 T64:', 'penalty 4 T64:', 'penalty 5 T64:', 'penalty 6 T64:', 'penalty 7 T64:', 'penalty 8 T64:', 'penalty 9 T64:', 'penalty 10 T64:', 'penalty 11 T64:', 'penalty 12 T64:', 'penalty 13 T64:', 'penalty 14 T64:', 'penalty 15 T64:', 'penalty 16 T64:', 'penalty 17 T64:', 'penalty 18 T64:', 'penalty 19 T64:', 'penalty 20 T64:', 'penaltys T64:']


Q = ['o placar dos penaltis T1 é:', 'o placar dos penaltis T2 é:', 'o placar dos penaltis T3 é:', 'o placar dos penaltis T4 é:', 'o placar dos penaltis T5 é:', 'o placar dos penaltis T6 é:', 'o placar dos penaltis T7 é:', 'o placar dos penaltis T8 é:',
     'o placar dos penaltis T9 é:', 'o placar dos penaltis T10 é:', 'o placar dos penaltis T11 é:', 'o placar dos penaltis T12 é:', 'o placar dos penaltis T13 é:', 'o placar dos penaltis T14 é:', 'o placar dos penaltis T15 é:', 'o placar dos penaltis T16 é:',
     'o placar dos penaltis T17 é:', 'o placar dos penaltis T18 é:', 'o placar dos penaltis T19 é:', 'o placar dos penaltis T20 é:', 'o placar dos penaltis T21 é:', 'o placar dos penaltis T22 é:', 'o placar dos penaltis T23 é:', 'o placar dos penaltis T24 é:',
     'o placar dos penaltis T25 é:', 'o placar dos penaltis T26 é:', 'o placar dos penaltis T27 é:', 'o placar dos penaltis T28 é:', 'o placar dos penaltis T29 é:', 'o placar dos penaltis T30 é:', 'o placar dos penaltis T31 é:', 'o placar dos penaltis T32 é:',
     'o placar dos penaltis T33 é:', 'o placar dos penaltis T34 é:', 'o placar dos penaltis T35 é:', 'o placar dos penaltis T36 é:', 'o placar dos penaltis T37 é:', 'o placar dos penaltis T38 é:', 'o placar dos penaltis T39 é:', 'o placar dos penaltis T40 é:',
     'o placar dos penaltis T41 é:', 'o placar dos penaltis T42 é:', 'o placar dos penaltis T43 é:', 'o placar dos penaltis T44 é:', 'o placar dos penaltis T45 é:', 'o placar dos penaltis T46 é:', 'o placar dos penaltis T47 é:', 'o placar dos penaltis T48 é:',
     'o placar dos penaltis T49 é:', 'o placar dos penaltis T50 é:', 'o placar dos penaltis T51 é:', 'o placar dos penaltis T52 é:', 'o placar dos penaltis T53 é:', 'o placar dos penaltis T54 é:', 'o placar dos penaltis T55 é:', 'o placar dos penaltis T56 é:',
     'o placar dos penaltis T57 é:', 'o placar dos penaltis T58 é:', 'o placar dos penaltis T59 é:', 'o placar dos penaltis T60 é:', 'o placar dos penaltis T61 é:', 'o placar dos penaltis T62 é:', 'o placar dos penaltis T63 é:', 'o placar dos penaltis T64 é:']

R = ['time 1 ganhou o jogo, +3pts', 'time 2 ganhou o jogo, +3pts', 'time 3 ganhou o jogo, +3pts', 'time 4 ganhou o jogo, +3pts', 'time 5 ganhou o jogo, +3pts', 'time 6 ganhou o jogo, +3pts', 'time 7 ganhou o jogo, +3pts', 'time 8 ganhou o jogo, +3pts',
     'time 9 ganhou o jogo, +3pts', 'time 10 ganhou o jogo, +3pts', 'time 11 ganhou o jogo, +3pts', 'time 12 ganhou o jogo, +3pts', 'time 13 ganhou o jogo, +3pts', 'time 14 ganhou o jogo, +3pts', 'time 15 ganhou o jogo, +3pts', 'time 16 ganhou o jogo, +3pts',
     'time 17 ganhou o jogo, +3pts', 'time 18 ganhou o jogo, +3pts', 'time 19 ganhou o jogo, +3pts', 'time 20 ganhou o jogo, +3pts', 'time 21 ganhou o jogo, +3pts', 'time 22 ganhou o jogo, +3pts', 'time 23 ganhou o jogo, +3pts', 'time 24 ganhou o jogo, +3pts',
     'time 25 ganhou o jogo, +3pts', 'time 26 ganhou o jogo, +3pts', 'time 27 ganhou o jogo, +3pts', 'time 28 ganhou o jogo, +3pts', 'time 29 ganhou o jogo, +3pts', 'time 30 ganhou o jogo, +3pts', 'time 31 ganhou o jogo, +3pts', 'time 32 ganhou o jogo, +3pts',
     'time 33 ganhou o jogo, +3pts', 'time 34 ganhou o jogo, +3pts', 'time 35 ganhou o jogo, +3pts', 'time 36 ganhou o jogo, +3pts', 'time 37 ganhou o jogo, +3pts', 'time 38 ganhou o jogo, +3pts', 'time 39 ganhou o jogo, +3pts', 'time 40 ganhou o jogo, +3pts',
     'time 41 ganhou o jogo, +3pts', 'time 42 ganhou o jogo, +3pts', 'time 43 ganhou o jogo, +3pts', 'time 44 ganhou o jogo, +3pts', 'time 45 ganhou o jogo, +3pts', 'time 46 ganhou o jogo, +3pts', 'time 47 ganhou o jogo, +3pts', 'time 48 ganhou o jogo, +3pts',
     'time 49 ganhou o jogo, +3pts', 'time 50 ganhou o jogo, +3pts', 'time 51 ganhou o jogo, +3pts', 'time 52 ganhou o jogo, +3pts', 'time 53 ganhou o jogo, +3pts', 'time 54 ganhou o jogo, +3pts', 'time 55 ganhou o jogo, +3pts', 'time 56 ganhou o jogo, +3pts',
     'time 57 ganhou o jogo, +3pts', 'time 58 ganhou o jogo, +3pts', 'time 59 ganhou o jogo, +3pts', 'time 60 ganhou o jogo, +3pts', 'time 61 ganhou o jogo, +3pts', 'time 62 ganhou o jogo, +3pts', 'time 63 ganhou o jogo, +3pts', 'time 64 ganhou o jogo, +3pts']

S = ['----------pontuacão atual do time 1 é:', '----------pontuacão atual do time 2 é:', '----------pontuacão atual do time 3 é:', '----------pontuacão atual do time 4 é:', '----------pontuacão atual do time 5 é:', '----------pontuacão atual do time 6 é:', '----------pontuacão atual do time 7 é:', '----------pontuacão atual do time 8 é:',
     '----------pontuacão atual do time 9 é:', '----------pontuacão atual do time 10 é:', '----------pontuacão atual do time 11 é:', '----------pontuacão atual do time 12 é:', '----------pontuacão atual do time 13 é:', '----------pontuacão atual do time 14 é:', '----------pontuacão atual do time 15 é:', '----------pontuacão atual do time 16 é:',
     '----------pontuacão atual do time 17 é:', '----------pontuacão atual do time 18 é:', '----------pontuacão atual do time 19 é:', '----------pontuacão atual do time 20 é:', '----------pontuacão atual do time 21 é:', '----------pontuacão atual do time 22 é:', '----------pontuacão atual do time 23 é:', '----------pontuacão atual do time 24 é:',
     '----------pontuacão atual do time 25 é:', '----------pontuacão atual do time 26 é:', '----------pontuacão atual do time 27 é:', '----------pontuacão atual do time 28 é:', '----------pontuacão atual do time 29 é:', '----------pontuacão atual do time 30 é:', '----------pontuacão atual do time 31 é:', '----------pontuacão atual do time 32 é:',
     '----------pontuacão atual do time 33 é:', '----------pontuacão atual do time 34 é:', '----------pontuacão atual do time 35 é:', '----------pontuacão atual do time 36 é:', '----------pontuacão atual do time 37 é:', '----------pontuacão atual do time 38 é:', '----------pontuacão atual do time 39 é:', '----------pontuacão atual do time 40 é:',
     '----------pontuacão atual do time 41 é:', '----------pontuacão atual do time 42 é:', '----------pontuacão atual do time 43 é:', '----------pontuacão atual do time 44 é:', '----------pontuacão atual do time 45 é:', '----------pontuacão atual do time 46 é:', '----------pontuacão atual do time 47 é:', '----------pontuacão atual do time 48 é:',
     '----------pontuacão atual do time 49 é:', '----------pontuacão atual do time 50 é:', '----------pontuacão atual do time 51 é:', '----------pontuacão atual do time 52 é:', '----------pontuacão atual do time 53 é:', '----------pontuacão atual do time 54 é:', '----------pontuacão atual do time 55 é:', '----------pontuacão atual do time 56 é:',
     '----------pontuacão atual do time 57 é:', '----------pontuacão atual do time 58 é:', '----------pontuacão atual do time 59 é:', '----------pontuacão atual do time 60 é:', '----------pontuacão atual do time 61 é:', '----------pontuacão atual do time 62 é:', '----------pontuacão atual do time 63 é:', '----------pontuacão atual do time 64 é:']

T = ['Manauara EC', 'Porto Velho', 'Princesa', 'Manaus', 'Trem', 'São Raimundo', 'Rio Branco', 'Humaitá', 'Maranhão', 'Altos', 'River', 'Tocantinópolis', 'Cametá', 'Fluminense-Pi', 'Moto Club', 'Águia de Marabá', 'Treze', 'Iguatu', 'América-RN', 'Atlético-CE', 'Souza', 'St Cruz de Natal', 'Maracanã', 'Potiguar', 'Itabaiana', 'Retrô', 'Jacuipense', 'ASA', 'CSE', 'Juazeirense', 'Petrolina', 'Sergipe', 'Brasiliense',  'Anápolis', 'Mixto',
     'CRAC', 'Iporá', 'União Rondonópolis', 'Real FC', 'Capital', 'Nova Iguaçu', 'Portuguesa-RJ', 'Itabuna', 'Real Noroeste', 'Serra', 'Ipatinga', 'Democrata SL', 'Audax Rio', 'Maringá', 'Inter de Limeira', 'Água Santa', 'Costa Rica MS', 'Santo André', 'Pouso Alegre', 'São José', 'Patrocinense', 'Cianorte', 'Brasil de Pelotas', 'Avenida', 'Novo Hamburgo', 'Hercílio Luz', 'Concórdia', 'Barra', 'FC Cascavel']

U = ['--------------------RODADA 1--------------------','--------------------RODADA 2--------------------','--------------------RODADA 3--------------------','--------------------RODADA 4--------------------','--------------------RODADA 5--------------------','--------------------RODADA 6--------------------','--------------------RODADA 7--------------------','--------------------RODADA 8--------------------','--------------------RODADA 9--------------------','--------------------RODADA 10--------------------','--------------------RODADA 11--------------------','--------------------RODADA 12--------------------','--------------------RODADA 13--------------------','--------------------RODADA 14--------------------','--casa--:','--visitante--']

V = ['partida 1','partida 2','partida 3','partida 4','partida 5','partida 6','partida 7','partida 8','partida 9','partida 10','partida 11','partida 12','partida 13','partida 14','partida 15','partida 16','partida 17','partida 18','partida 19','partida 20','partida 21','partida 22','partida 23','partida 24','partida 25','partida 26','partida 27','partida 28','partida 29','partida 30','partida 31','partida 32','partida 33','partida 34','partida 35','partida 36','partida 37','partida 38','partida 39','partida 40',
     'partida 41','partida 42','partida 43','partida 44','partida 45','partida 46','partida 47','partida 48','partida 49','partida 50','partida 51','partida 52','partida 53','partida 54','partida 55','partida 56']

pt1 = pt2 = pt3 = pt4 = pt5 = pt6 = pt7 = pt8 = pt9 = pt10 = pt11 = pt12 = pt13 = pt14 = pt15 = pt16 = pt17 = pt18 = pt19 = pt20 = pt21 = pt22 = pt23 = pt24 = pt25 = pt26 = pt27 = pt28 = pt29 = pt30 = pt31 = pt32 = pt33 = pt34 = pt35 = pt36 = pt37 = pt38 = pt39 = pt40 = pt41 = pt42 = pt43 = pt44 = pt45 = pt46 = pt47 = pt48 = pt49 = pt50 = pt51 = pt52 = pt53 = pt54 = pt55 = pt56 = pt57 = pt58 = pt59 = pt60 = pt61 = pt62 = pt63 = pt64 = 0
sgT1 = sgT2 = sgT3 = sgT4 = sgT5 = sgT6 = sgT7 = sgT8 = sgT9 = sgT10 = sgT11 = sgT12 = sgT13 = sgT14 = sgT15 = sgT16 = sgT17 = sgT18 = sgT19 = sgT20 = sgT21 = sgT22 = sgT23 = sgT24 = sgT25 = sgT26 = sgT27 = sgT28 = sgT29 = sgT30 = sgT31 = sgT32 = sgT33 = sgT34 = sgT35 = sgT36 = sgT37 = sgT38 = sgT39 = sgT40 = sgT41 = sgT42 = sgT43 = sgT44 = sgT45 = sgT46 = sgT47 = sgT48 = sgT49 = sgT50 = sgT51 = sgT52 = sgT53 = sgT54 = sgT55 = sgT56 = sgT57 = sgT58 = sgT59 = sgT60 = sgT61 = sgT62 = sgT63 = sgT64 = 0
SgT1 = SgT2 = SgT3 = SgT4 = SgT5 = SgT6 = SgT7 = SgT8 = SgT9 = SgT10 = SgT11 = SgT12 = SgT13 = SgT14 = SgT15 = SgT16 = SgT17 = SgT18 = SgT19 = SgT20 = SgT21 = SgT22 = SgT23 = SgT24 = SgT25 = SgT26 = SgT27 = SgT28 = SgT29 = SgT30 = SgT31 = SgT32 = SgT33 = SgT34 = SgT35 = SgT36 = SgT37 = SgT38 = SgT39 = SgT40 = SgT41 = SgT42 = SgT43 = SgT44 = SgT45 = SgT46 = SgT47 = SgT48 = SgT49 = SgT50 = SgT51 = SgT52 = SgT53 = SgT54 = SgT55 = SgT56 = SgT57 = SgT58 = SgT59 = SgT60 = SgT61 = SgT62 = SgT63 = SgT64 = 0
P = [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10, pt11, pt12, pt13, pt14, pt15, pt16, pt17, pt18, pt19, pt20, pt21, pt22, pt23, pt24, pt25, pt26, pt27, pt28, pt29, pt30, pt31, pt32, pt33, pt34, pt35, pt36, pt37, pt38, pt39, pt40, pt41, pt42, pt43, pt44, pt45, pt46, pt47, pt48, pt49, pt50, pt51, pt52, pt53, pt54, pt55, pt56, pt57, pt58, pt59, pt60, pt61, pt62, pt63, pt64]
SG = [sgT1, sgT2, sgT3, sgT4, sgT5, sgT6, sgT7, sgT8, sgT9, sgT10, sgT11, sgT12, sgT13, sgT14, sgT15, sgT16, sgT17, sgT18, sgT19, sgT20, sgT21, sgT22, sgT23, sgT24, sgT25, sgT26, sgT27, sgT28, sgT29, sgT30, sgT31, sgT32, sgT33, sgT34, sgT35, sgT36, sgT37, sgT38, sgT39, sgT40, sgT41 , sgT42 , sgT43 , sgT44 , sgT45 , sgT46 , sgT47 , sgT48 , sgT49 , sgT50 , sgT51 , sgT52 , sgT53 , sgT54 , sgT55 , sgT56 , sgT57 , sgT58 , sgT59 , sgT60 , sgT61 , sgT62 , sgT63 , sgT64]
Sg = [SgT1, SgT2, SgT3, SgT4, SgT5, SgT6, SgT7, SgT8, SgT9, SgT10, SgT11, SgT12, SgT13, SgT14, SgT15, SgT16, SgT17, SgT18, SgT19, SgT20, SgT21, SgT22, SgT23, SgT24, SgT25, SgT26, SgT27, SgT28, SgT29, SgT30, SgT31, SgT32, SgT33, SgT34, SgT35, SgT36, SgT37, SgT38, SgT39, SgT40, SgT41 , SgT42 , SgT43 , SgT44 , SgT45 , SgT46 , SgT47 , SgT48 , SgT49 , SgT50 , SgT51 , SgT52 , SgT53 , SgT54 , SgT55 , SgT56 , SgT57 , SgT58 , SgT59 , SgT60 , SgT61 , SgT62 , SgT63 , SgT64]
A = 8

p = [['X','O',L1,L2,Q[0],Q[1],R[0],R[1],S[0],S[1],P[0],P[1],SG[0],SG[1],U[0],V[0],U[14],T[0],U[15],T[1]],['X','O',L1,L3,Q[0],Q[2],R[0],R[2],S[0],S[2],P[0],P[2],SG[0],SG[2],U[0],V[1],U[14],T[0],U[15],T[2]],['X','O',L1,L4,Q[0],Q[3],R[0],R[3],S[0],S[3],P[0],P[3],SG[0],SG[3],U[0],V[2],U[14],T[0],U[15],T[3]],['X','O',L1,L5,Q[0],Q[4],R[0],R[4],S[0],S[4],P[0],P[4],SG[0],SG[4],U[0],V[3],U[14],T[0],U[15],T[4]],['X','O',L1,L6,Q[0],Q[5],R[0],R[5],S[0],S[5],P[0],P[5],SG[0],SG[5],U[1],V[4],U[14],T[0],U[15],T[5]],
['X','O',L1,L7,Q[0],Q[6],R[0],R[6],S[0],S[6],P[0],P[6],SG[0],SG[6],U[1],V[5],U[14],T[0],U[15],T[6]],['X','O',L1,L8,Q[0],Q[7],R[0],R[7],S[0],S[7],P[0],P[7],SG[0],SG[7],U[1],V[6],U[14],T[0],U[15],T[7]],['X','O',L2,L3,Q[1],Q[2],R[1],R[2],S[1],S[2],P[1],P[2],SG[1],SG[2],U[1],V[7],U[14],T[1],U[15],T[2]],['X','O',L2,L4,Q[1],Q[3],R[1],R[3],S[1],S[3],P[1],P[3],SG[1],SG[3],U[2],V[8],U[14],T[1],U[15],T[3]],['X','O',L2,L5,Q[1],Q[4],R[1],R[4],S[1],S[4],P[1],P[4],SG[1],SG[4],U[2],V[9],U[14],T[1],U[15],T[4]],
['X','O',L2,L6,Q[1],Q[5],R[1],R[5],S[1],S[5],P[1],P[5],SG[1],SG[5],U[2],V[10],U[14],T[1],U[15],T[5]],['X','O',L2,L7,Q[1],Q[6],R[1],R[6],S[1],S[6],P[1],P[6],SG[1],SG[6],U[2],V[11],U[14],T[1],U[15],T[6]],['X','O',L2,L8,Q[1],Q[7],R[1],R[7],S[1],S[7],P[1],P[7],SG[1],SG[7],U[3],V[12],U[14],T[1],U[15],T[7]],['X','O',L3,L4,Q[2],Q[3],R[2],R[3],S[2],S[3],P[2],P[3],SG[2],SG[3],U[3],V[13],U[14],T[2],U[15],T[3]],['X','O',L3,L5,Q[2],Q[4],R[2],R[4],S[2],S[4],P[2],P[4],SG[2],SG[4],U[3],V[14],U[14],T[2],U[15],T[4]],
['X','O',L3,L6,Q[2],Q[5],R[2],R[5],S[2],S[5],P[2],P[5],SG[2],SG[5],U[3],V[15],U[14],T[2],U[15],T[5]],['X','O',L3,L7,Q[2],Q[6],R[2],R[6],S[2],S[6],P[2],P[6],SG[2],SG[6],U[4],V[16],U[14],T[2],U[15],T[6]],['X','O',L3,L8,Q[2],Q[7],R[2],R[7],S[2],S[7],P[2],P[7],SG[2],SG[7],U[4],V[17],U[14],T[2],U[15],T[7]],['X','O',L4,L5,Q[3],Q[4],R[3],R[4],S[3],S[4],P[3],P[4],SG[3],SG[4],U[4],V[18],U[14],T[3],U[15],T[4]],['X','O',L4,L6,Q[3],Q[5],R[3],R[5],S[3],S[5],P[3],P[5],SG[3],SG[5],U[4],V[19],U[14],T[3],U[15],T[5]],
['X','O',L4,L7,Q[3],Q[6],R[3],R[6],S[3],S[6],P[3],P[6],SG[3],SG[6],U[5],V[20],U[14],T[3],U[15],T[6]],['X','O',L4,L8,Q[3],Q[7],R[3],R[7],S[3],S[7],P[3],P[7],SG[3],SG[7],U[5],V[21],U[14],T[3],U[15],T[7]],['X','O',L5,L6,Q[4],Q[5],R[4],R[5],S[4],S[5],P[4],P[5],SG[4],SG[5],U[5],V[22],U[14],T[4],U[15],T[5]],['X','O',L5,L7,Q[4],Q[6],R[4],R[6],S[4],S[6],P[4],P[6],SG[4],SG[6],U[5],V[23],U[14],T[4],U[15],T[6]],['X','O',L5,L8,Q[4],Q[7],R[4],R[7],S[4],S[7],P[4],P[7],SG[4],SG[7],U[6],V[24],U[14],T[4],U[15],T[7]],
['X','O',L6,L7,Q[5],Q[6],R[5],R[6],S[5],S[6],P[5],P[6],SG[5],SG[6],U[6],V[25],U[14],T[5],U[15],T[6]],['X','O',L6,L8,Q[5],Q[7],R[5],R[7],S[5],S[7],P[5],P[7],SG[5],SG[7],U[6],V[26],U[14],T[5],U[15],T[7]],['X','O',L7,L8,Q[6],Q[7],R[6],R[7],S[6],S[7],P[6],P[7],SG[6],SG[7],U[6],V[27],U[14],T[6],U[15],T[7]],['X','O',L2,L1,Q[1],Q[0],R[1],R[0],S[1],S[0],P[1],P[0],SG[1],SG[0],U[7],V[28],U[14],T[1],U[15],T[0]],['X','O',L3,L1,Q[2],Q[0],R[2],R[0],S[2],S[0],P[2],P[0],SG[2],SG[0],U[7],V[29],U[14],T[2],U[15],T[0]],
['X','O',L4,L1,Q[3],Q[0],R[3],R[0],S[3],S[0],P[3],P[0],SG[3],SG[0],U[7],V[30],U[14],T[3],U[15],T[0]],['X','O',L5,L1,Q[4],Q[0],R[4],R[0],S[4],S[0],P[4],P[0],SG[4],SG[0],U[7],V[31],U[14],T[4],U[15],T[0]],['X','O',L6,L1,Q[5],Q[0],R[5],R[0],S[5],S[0],P[5],P[0],SG[5],SG[0],U[8],V[32],U[14],T[5],U[15],T[0]],['X','O',L7,L1,Q[6],Q[0],R[6],R[0],S[6],S[0],P[6],P[0],SG[6],SG[0],U[8],V[33],U[14],T[6],U[15],T[0]],['X','O',L8,L1,Q[7],Q[0],R[7],R[0],S[7],S[0],P[7],P[0],SG[7],SG[0],U[8],V[34],U[14],T[7],U[15],T[0]],
['X','O',L3,L2,Q[2],Q[1],R[2],R[1],S[2],S[1],P[2],P[1],SG[2],SG[1],U[8],V[35],U[14],T[2],U[15],T[1]],['X','O',L4,L2,Q[3],Q[1],R[3],R[1],S[3],S[1],P[3],P[1],SG[3],SG[1],U[9],V[36],U[14],T[3],U[15],T[1]],['X','O',L5,L2,Q[4],Q[1],R[4],R[1],S[4],S[1],P[4],P[1],SG[4],SG[1],U[9],V[37],U[14],T[4],U[15],T[1]],['X','O',L6,L2,Q[5],Q[1],R[5],R[1],S[5],S[1],P[5],P[1],SG[5],SG[1],U[9],V[38],U[14],T[5],U[15],T[1]],['X','O',L7,L2,Q[6],Q[1],R[6],R[1],S[6],S[1],P[6],P[1],SG[6],SG[1],U[9],V[39],U[14],T[6],U[15],T[1]],
['X','O',L8,L2,Q[7],Q[1],R[7],R[1],S[7],S[1],P[7],P[1],SG[7],SG[1],U[10],V[40],U[14],T[7],U[15],T[1]],['X','O',L4,L3,Q[3],Q[2],R[3],R[2],S[3],S[2],P[3],P[2],SG[3],SG[2],U[10],V[41],U[14],T[3],U[15],T[2]],['X','O',L5,L3,Q[4],Q[2],R[4],R[2],S[4],S[2],P[4],P[2],SG[4],SG[2],U[10],V[42],U[14],T[4],U[15],T[2]],['X','O',L6,L3,Q[5],Q[2],R[5],R[2],S[5],S[2],P[5],P[2],SG[5],SG[2],U[10],V[43],U[14],T[5],U[15],T[2]],['X','O',L7,L3,Q[6],Q[2],R[6],R[2],S[6],S[2],P[6],P[2],SG[6],SG[2],U[11],V[44],U[14],T[6],U[15],T[2]],
['X','O',L8,L3,Q[7],Q[2],R[7],R[2],S[7],S[2],P[7],P[2],SG[7],SG[2],U[11],V[45],U[14],T[7],U[15],T[2]],['X','O',L5,L4,Q[4],Q[3],R[4],R[3],S[4],S[3],P[4],P[3],SG[4],SG[3],U[11],V[46],U[14],T[4],U[15],T[3]],['X','O',L6,L4,Q[5],Q[3],R[5],R[3],S[5],S[3],P[5],P[3],SG[5],SG[3],U[11],V[47],U[14],T[5],U[15],T[3]],['X','O',L7,L4,Q[6],Q[3],R[6],R[3],S[6],S[3],P[6],P[3],SG[6],SG[3],U[12],V[48],U[14],T[6],U[15],T[3]],['X','O',L8,L4,Q[7],Q[3],R[7],R[3],S[7],S[3],P[7],P[3],SG[7],SG[3],U[12],V[49],U[14],T[7],U[15],T[3]],
['X','O',L6,L5,Q[5],Q[4],R[5],R[4],S[5],S[4],P[5],P[4],SG[5],SG[4],U[12],V[50],U[14],T[5],U[15],T[4]],['X','O',L7,L5,Q[6],Q[4],R[6],R[4],S[6],S[4],P[6],P[4],SG[6],SG[4],U[12],V[51],U[14],T[6],U[15],T[4]],['X','O',L8,L5,Q[7],Q[4],R[7],R[4],S[7],S[4],P[7],P[4],SG[7],SG[4],U[13],V[52],U[14],T[7],U[15],T[4]],['X','O',L7,L6,Q[6],Q[5],R[6],R[5],S[6],S[5],P[6],P[5],SG[6],SG[5],U[13],V[53],U[14],T[6],U[15],T[5]],['X','O',L8,L6,Q[7],Q[5],R[7],R[5],S[7],S[5],P[7],P[5],SG[7],SG[5],U[13],V[54],U[14],T[7],U[15],T[5]],
['X','O',L8,L7,Q[7],Q[6],R[7],R[6],S[7],S[6],P[7],P[6],SG[7],SG[6],U[13],V[55],U[14],T[7],U[15],T[6]],['X','O',L9,L10,Q[0+A],Q[1+A],R[0+A],R[1+A],S[0+A],S[1+A],P[0+A],P[1+A],SG[0+A],SG[1+A],U[0],V[0],U[14],T[0+A],U[15],T[1+A]],['X','O',L9,L11,Q[0+A],Q[2+A],R[0+A],R[2+A],S[0+A],S[2+A],P[0+A],P[2+A],SG[0+A],SG[2+A],U[0],V[1],U[14],T[0+A],U[15],T[2+A]],['X','O',L9,L12,Q[0+A],Q[3+A],R[0+A],R[3+A],S[0+A],S[3+A],P[0+A],P[3+A],SG[0+A],SG[3+A],U[0],V[2],U[14],T[0+A],U[15],T[3+A]],['X','O',L9,L13,Q[0+A],Q[4+A],R[0+A],R[4+A],S[0+A],S[4+A],P[0+A],P[4+A],SG[0+A],SG[4+A],U[0],V[3],U[14],T[0+A],U[15],T[4+A]],
['X','O',L9,L14,Q[0+A],Q[5+A],R[0+A],R[5+A],S[0+A],S[5+A],P[0+A],P[5+A],SG[0+A],SG[5+A],U[1],V[4],U[14],T[0+A],U[15],T[5+A]],['X','O',L9,L15,Q[0+A],Q[6+A],R[0+A],R[6+A],S[0+A],S[6+A],P[0+A],P[6+A],SG[0+A],SG[6+A],U[1],V[5],U[14],T[0+A],U[15],T[6+A]],['X','O',L9,L16,Q[0+A],Q[7+A],R[0+A],R[7+A],S[0+A],S[7+A],P[0+A],P[7+A],SG[0+A],SG[7+A],U[1],V[6],U[14],T[0+A],U[15],T[7+A]],['X','O',L10,L11,Q[1+A],Q[2+A],R[1+A],R[2+A],S[1+A],S[2+A],P[1+A],P[2+A],SG[1+A],SG[2+A],U[1],V[7],U[14],T[1+A],U[15],T[2+A]],['X','O',L10,L12,Q[1+A],Q[3+A],R[1+A],R[3+A],S[1+A],S[3+A],P[1+A],P[3+A],SG[1+A],SG[3+A],U[2],V[8],U[14],T[1+A],U[15],T[3+A]],
['X','O',L10,L13,Q[1+A],Q[4+A],R[1+A],R[4+A],S[1+A],S[4+A],P[1+A],P[4+A],SG[1+A],SG[4+A],U[2],V[9],U[14],T[1+A],U[15],T[4+A]],['X','O',L10,L14,Q[1+A],Q[5+A],R[1+A],R[5+A],S[1+A],S[5+A],P[1+A],P[5+A],SG[1+A],SG[5+A],U[2],V[10],U[14],T[1+A],U[15],T[5+A]],['X','O',L10,L15,Q[1+A],Q[6+A],R[1+A],R[6+A],S[1+A],S[6+A],P[1+A],P[6+A],SG[1+A],SG[6+A],U[2],V[11],U[14],T[1+A],U[15],T[6+A]],['X','O',L10,L16,Q[1+A],Q[7+A],R[1+A],R[7+A],S[1+A],S[7+A],P[1+A],P[7+A],SG[1+A],SG[7+A],U[3],V[12],U[14],T[1+A],U[15],T[7+A]],['X','O',L11,L12,Q[2+A],Q[3+A],R[2+A],R[3+A],S[2+A],S[3+A],P[2+A],P[3+A],SG[2+A],SG[3+A],U[3],V[13],U[14],T[2+A],U[15],T[3+A]],
['X','O',L11,L13,Q[2+A],Q[4+A],R[2+A],R[4+A],S[2+A],S[4+A],P[2+A],P[4+A],SG[2+A],SG[4+A],U[3],V[14],U[14],T[2+A],U[15],T[4+A]],['X','O',L11,L14,Q[2+A],Q[5+A],R[2+A],R[5+A],S[2+A],S[5+A],P[2+A],P[5+A],SG[2+A],SG[5+A],U[3],V[15],U[14],T[2+A],U[15],T[5+A]],['X','O',L11,L15,Q[2+A],Q[6+A],R[2+A],R[6+A],S[2+A],S[6+A],P[2+A],P[6+A],SG[2+A],SG[6+A],U[4],V[16],U[14],T[2+A],U[15],T[6+A]],['X','O',L11,L16,Q[2+A],Q[7+A],R[2+A],R[7+A],S[2+A],S[7+A],P[2+A],P[7+A],SG[2+A],SG[7+A],U[4],V[17],U[14],T[2+A],U[15],T[7+A]],['X','O',L12,L13,Q[3+A],Q[4+A],R[3+A],R[4+A],S[3+A],S[4+A],P[3+A],P[4+A],SG[3+A],SG[4+A],U[4],V[18],U[14],T[3+A],U[15],T[4+A]],
['X','O',L12,L14,Q[3+A],Q[5+A],R[3+A],R[5+A],S[3+A],S[5+A],P[3+A],P[5+A],SG[3+A],SG[5+A],U[4],V[19],U[14],T[3+A],U[15],T[5+A]],['X','O',L12,L15,Q[3+A],Q[6+A],R[3+A],R[6+A],S[3+A],S[6+A],P[3+A],P[6+A],SG[3+A],SG[6+A],U[5],V[20],U[14],T[3+A],U[15],T[6+A]],['X','O',L12,L16,Q[3+A],Q[7+A],R[3+A],R[7+A],S[3+A],S[7+A],P[3+A],P[7+A],SG[3+A],SG[7+A],U[5],V[21],U[14],T[3+A],U[15],T[7+A]],['X','O',L13,L14,Q[4+A],Q[5+A],R[4+A],R[5+A],S[4+A],S[5+A],P[4+A],P[5+A],SG[4+A],SG[5+A],U[5],V[22],U[14],T[4+A],U[15],T[5+A]],['X','O',L13,L15,Q[4+A],Q[6+A],R[4+A],R[6+A],S[4+A],S[6+A],P[4+A],P[6+A],SG[4+A],SG[6+A],U[5],V[23],U[14],T[4+A],U[15],T[6+A]],
['X','O',L13,L16,Q[4+A],Q[7+A],R[4+A],R[7+A],S[4+A],S[7+A],P[4+A],P[7+A],SG[4+A],SG[7+A],U[6],V[24],U[14],T[4+A],U[15],T[7+A]],['X','O',L14,L15,Q[5+A],Q[6+A],R[5+A],R[6+A],S[5+A],S[6+A],P[5+A],P[6+A],SG[5+A],SG[6+A],U[6],V[25],U[14],T[5+A],U[15],T[6+A]],['X','O',L14,L16,Q[5+A],Q[7+A],R[5+A],R[7+A],S[5+A],S[7+A],P[5+A],P[7+A],SG[5+A],SG[7+A],U[6],V[26],U[14],T[5+A],U[15],T[7+A]],['X','O',L15,L16,Q[6+A],Q[7+A],R[6+A],R[7+A],S[6+A],S[7+A],P[6+A],P[7+A],SG[6+A],SG[7+A],U[6],V[27],U[14],T[6+A],U[15],T[7+A]],['X','O',L10,L9,Q[1+A],Q[0+A],R[1+A],R[0+A],S[1+A],S[0+A],P[1+A],P[0+A],SG[1+A],SG[0+A],U[7],V[28],U[14],T[1+A],U[15],T[0+A]],
['X','O',L11,L9,Q[2+A],Q[0+A],R[2+A],R[0+A],S[2+A],S[0+A],P[2+A],P[0+A],SG[2+A],SG[0+A],U[7],V[29],U[14],T[2+A],U[15],T[0+A]],['X','O',L12,L9,Q[3+A],Q[0+A],R[3+A],R[0+A],S[3+A],S[0+A],P[3+A],P[0+A],SG[3+A],SG[0+A],U[7],V[30],U[14],T[3+A],U[15],T[0+A]],['X','O',L13,L9,Q[4+A],Q[0+A],R[4+A],R[0+A],S[4+A],S[0+A],P[4+A],P[0+A],SG[4+A],SG[0+A],U[7],V[31],U[14],T[4+A],U[15],T[0+A]],['X','O',L14,L9,Q[5+A],Q[0+A],R[5+A],R[0+A],S[5+A],S[0+A],P[5+A],P[0+A],SG[5+A],SG[0+A],U[8],V[32],U[14],T[5+A],U[15],T[0+A]],['X','O',L15,L9,Q[6+A],Q[0+A],R[6+A],R[0+A],S[6+A],S[0+A],P[6+A],P[0+A],SG[6+A],SG[0+A],U[8],V[33],U[14],T[6+A],U[15],T[0+A]],
['X','O',L16,L9,Q[7+A],Q[0+A],R[7+A],R[0+A],S[7+A],S[0+A],P[7+A],P[0+A],SG[7+A],SG[0+A],U[8],V[34],U[14],T[7+A],U[15],T[0+A]],['X','O',L11,L10,Q[2+A],Q[1+A],R[2+A],R[1+A],S[2+A],S[1+A],P[2+A],P[1+A],SG[2+A],SG[1+A],U[8],V[35],U[14],T[2+A],U[15],T[1+A]],['X','O',L12,L10,Q[3+A],Q[1+A],R[3+A],R[1+A],S[3+A],S[1+A],P[3+A],P[1+A],SG[3+A],SG[1+A],U[9],V[36],U[14],T[3+A],U[15],T[1+A]],['X','O',L13,L10,Q[4+A],Q[1+A],R[4+A],R[1+A],S[4+A],S[1+A],P[4+A],P[1+A],SG[4+A],SG[1+A],U[9],V[37],U[14],T[4+A],U[15],T[1+A]],['X','O',L14,L10,Q[5+A],Q[1+A],R[5+A],R[1+A],S[5+A],S[1+A],P[5+A],P[1+A],SG[5+A],SG[1+A],U[9],V[38],U[14],T[5+A],U[15],T[1+A]],
['X','O',L15,L10,Q[6+A],Q[1+A],R[6+A],R[1+A],S[6+A],S[1+A],P[6+A],P[1+A],SG[6+A],SG[1+A],U[9],V[39],U[14],T[6+A],U[15],T[1+A]],['X','O',L16,L10,Q[7+A],Q[1+A],R[7+A],R[1+A],S[7+A],S[1+A],P[7+A],P[1+A],SG[7+A],SG[1+A],U[10],V[40],U[14],T[7+A],U[15],T[1+A]],['X','O',L12,L11,Q[3+A],Q[2+A],R[3+A],R[2+A],S[3+A],S[2+A],P[3+A],P[2+A],SG[3+A],SG[2+A],U[10],V[41],U[14],T[3+A],U[15],T[2+A]],['X','O',L13,L11,Q[4+A],Q[2+A],R[4+A],R[2+A],S[4+A],S[2+A],P[4+A],P[2+A],SG[4+A],SG[2+A],U[10],V[42],U[14],T[4+A],U[15],T[2+A]],['X','O',L14,L11,Q[5+A],Q[2+A],R[5+A],R[2+A],S[5+A],S[2+A],P[5+A],P[2+A],SG[5+A],SG[2+A],U[10],V[43],U[14],T[5+A],U[15],T[2+A]],
['X','O',L15,L11,Q[6+A],Q[2+A],R[6+A],R[2+A],S[6+A],S[2+A],P[6+A],P[2+A],SG[6+A],SG[2+A],U[11],V[44],U[14],T[6+A],U[15],T[2+A]],['X','O',L16,L11,Q[7+A],Q[2+A],R[7+A],R[2+A],S[7+A],S[2+A],P[7+A],P[2+A],SG[7+A],SG[2+A],U[11],V[45],U[14],T[7+A],U[15],T[2+A]],['X','O',L13,L12,Q[4+A],Q[3+A],R[4+A],R[3+A],S[4+A],S[3+A],P[4+A],P[3+A],SG[4+A],SG[3+A],U[11],V[46],U[14],T[4+A],U[15],T[3+A]],['X','O',L14,L12,Q[5+A],Q[3+A],R[5+A],R[3+A],S[5+A],S[3+A],P[5+A],P[3+A],SG[5+A],SG[3+A],U[11],V[47],U[14],T[5+A],U[15],T[3+A]],['X','O',L15,L12,Q[6+A],Q[3+A],R[6+A],R[3+A],S[6+A],S[3+A],P[6+A],P[3+A],SG[6+A],SG[3+A],U[12],V[48],U[14],T[6+A],U[15],T[3+A]],
['X','O',L16,L12,Q[7+A],Q[3+A],R[7+A],R[3+A],S[7+A],S[3+A],P[7+A],P[3+A],SG[7+A],SG[3+A],U[12],V[49],U[14],T[7+A],U[15],T[3+A]],['X','O',L14,L13,Q[5+A],Q[4+A],R[5+A],R[4+A],S[5+A],S[4+A],P[5+A],P[4+A],SG[5+A],SG[4+A],U[12],V[50],U[14],T[5+A],U[15],T[4+A]],['X','O',L15,L13,Q[6+A],Q[4+A],R[6+A],R[4+A],S[6+A],S[4+A],P[6+A],P[4+A],SG[6+A],SG[4+A],U[12],V[51],U[14],T[6+A],U[15],T[4+A]],['X','O',L16,L13,Q[7+A],Q[4+A],R[7+A],R[4+A],S[7+A],S[4+A],P[7+A],P[4+A],SG[7+A],SG[4+A],U[13],V[52],U[14],T[7+A],U[15],T[4+A]],['X','O',L15,L14,Q[6+A],Q[5+A],R[6+A],R[5+A],S[6+A],S[5+A],P[6+A],P[5+A],SG[6+A],SG[5+A],U[13],V[53],U[14],T[6+A],U[15],T[5+A]],
['X','O',L16,L14,Q[7+A],Q[5+A],R[7+A],R[5+A],S[7+A],S[5+A],P[7+A],P[5+A],SG[7+A],SG[5+A],U[13],V[54],U[14],T[7+A],U[15],T[5+A]],['X','O',L16,L15,Q[7+A],Q[6+A],R[7+A],R[6+A],S[7+A],S[6+A],P[7+A],P[6+A],SG[7+A],SG[6+A],U[13],V[55],U[14],T[7+A],U[15],T[6+A]],['X','O',L17,L18,Q[0+A*2],Q[1+A*2],R[0+A*2],R[1+A*2],S[0+A*2],S[1+A*2],P[0+A*2],P[1+A*2],SG[0+A*2],SG[1+A*2],U[0],V[0],U[14],T[0+A*2],U[15],T[1+A*2]],['X','O',L17,L19,Q[0+A*2],Q[2+A*2],R[0+A*2],R[2+A*2],S[0+A*2],S[2+A*2],P[0+A*2],P[2+A*2],SG[0+A*2],SG[2+A*2],U[0],V[1],U[14],T[0+A*2],U[15],T[2+A*2]],['X','O',L17,L20,Q[0+A*2],Q[3+A*2],R[0+A*2],R[3+A*2],S[0+A*2],S[3+A*2],P[0+A*2],P[3+A*2],SG[0+A*2],SG[3+A*2],U[0],V[2],U[14],T[0+A*2],U[15],T[3+A*2]],
['X','O',L17,L21,Q[0+A*2],Q[4+A*2],R[0+A*2],R[4+A*2],S[0+A*2],S[4+A*2],P[0+A*2],P[4+A*2],SG[0+A*2],SG[4+A*2],U[0],V[3],U[14],T[0+A*2],U[15],T[4+A*2]],['X','O',L17,L22,Q[0+A*2],Q[5+A*2],R[0+A*2],R[5+A*2],S[0+A*2],S[5+A*2],P[0+A*2],P[5+A*2],SG[0+A*2],SG[5+A*2],U[1],V[4],U[14],T[0+A*2],U[15],T[5+A*2]],['X','O',L17,L23,Q[0+A*2],Q[6+A*2],R[0+A*2],R[6+A*2],S[0+A*2],S[6+A*2],P[0+A*2],P[6+A*2],SG[0+A*2],SG[6+A*2],U[1],V[5],U[14],T[0+A*2],U[15],T[6+A*2]],['X','O',L17,L24,Q[0+A*2],Q[7+A*2],R[0+A*2],R[7+A*2],S[0+A*2],S[7+A*2],P[0+A*2],P[7+A*2],SG[0+A*2],SG[7+A*2],U[1],V[6],U[14],T[0+A*2],U[15],T[7+A*2]],['X','O',L18,L19,Q[1+A*2],Q[2+A*2],R[1+A*2],R[2+A*2],S[1+A*2],S[2+A*2],P[1+A*2],P[2+A*2],SG[1+A*2],SG[2+A*2],U[1],V[7],U[14],T[1+A*2],U[15],T[2+A*2]],
['X','O',L18,L20,Q[1+A*2],Q[3+A*2],R[1+A*2],R[3+A*2],S[1+A*2],S[3+A*2],P[1+A*2],P[3+A*2],SG[1+A*2],SG[3+A*2],U[2],V[8],U[14],T[1+A*2],U[15],T[3+A*2]],['X','O',L18,L21,Q[1+A*2],Q[4+A*2],R[1+A*2],R[4+A*2],S[1+A*2],S[4+A*2],P[1+A*2],P[4+A*2],SG[1+A*2],SG[4+A*2],U[2],V[9],U[14],T[1+A*2],U[15],T[4+A*2]],['X','O',L18,L22,Q[1+A*2],Q[5+A*2],R[1+A*2],R[5+A*2],S[1+A*2],S[5+A*2],P[1+A*2],P[5+A*2],SG[1+A*2],SG[5+A*2],U[2],V[10],U[14],T[1+A*2],U[15],T[5+A*2]],['X','O',L18,L23,Q[1+A*2],Q[6+A*2],R[1+A*2],R[6+A*2],S[1+A*2],S[6+A*2],P[1+A*2],P[6+A*2],SG[1+A*2],SG[6+A*2],U[2],V[11],U[14],T[1+A*2],U[15],T[6+A*2]],['X','O',L18,L24,Q[1+A*2],Q[7+A*2],R[1+A*2],R[7+A*2],S[1+A*2],S[7+A*2],P[1+A*2],P[7+A*2],SG[1+A*2],SG[7+A*2],U[3],V[12],U[14],T[1+A*2],U[15],T[7+A*2]],
['X','O',L19,L20,Q[2+A*2],Q[3+A*2],R[2+A*2],R[3+A*2],S[2+A*2],S[3+A*2],P[2+A*2],P[3+A*2],SG[2+A*2],SG[3+A*2],U[3],V[13],U[14],T[2+A*2],U[15],T[3+A*2]],['X','O',L19,L21,Q[2+A*2],Q[4+A*2],R[2+A*2],R[4+A*2],S[2+A*2],S[4+A*2],P[2+A*2],P[4+A*2],SG[2+A*2],SG[4+A*2],U[3],V[14],U[14],T[2+A*2],U[15],T[4+A*2]],['X','O',L19,L22,Q[2+A*2],Q[5+A*2],R[2+A*2],R[5+A*2],S[2+A*2],S[5+A*2],P[2+A*2],P[5+A*2],SG[2+A*2],SG[5+A*2],U[3],V[15],U[14],T[2+A*2],U[15],T[5+A*2]],['X','O',L19,L23,Q[2+A*2],Q[6+A*2],R[2+A*2],R[6+A*2],S[2+A*2],S[6+A*2],P[2+A*2],P[6+A*2],SG[2+A*2],SG[6+A*2],U[4],V[16],U[14],T[2+A*2],U[15],T[6+A*2]],['X','O',L19,L24,Q[2+A*2],Q[7+A*2],R[2+A*2],R[7+A*2],S[2+A*2],S[7+A*2],P[2+A*2],P[7+A*2],SG[2+A*2],SG[7+A*2],U[4],V[17],U[14],T[2+A*2],U[15],T[7+A*2]],
['X','O',L20,L21,Q[3+A*2],Q[4+A*2],R[3+A*2],R[4+A*2],S[3+A*2],S[4+A*2],P[3+A*2],P[4+A*2],SG[3+A*2],SG[4+A*2],U[4],V[18],U[14],T[3+A*2],U[15],T[4+A*2]],['X','O',L20,L22,Q[3+A*2],Q[5+A*2],R[3+A*2],R[5+A*2],S[3+A*2],S[5+A*2],P[3+A*2],P[5+A*2],SG[3+A*2],SG[5+A*2],U[4],V[19],U[14],T[3+A*2],U[15],T[5+A*2]],['X','O',L20,L23,Q[3+A*2],Q[6+A*2],R[3+A*2],R[6+A*2],S[3+A*2],S[6+A*2],P[3+A*2],P[6+A*2],SG[3+A*2],SG[6+A*2],U[5],V[20],U[14],T[3+A*2],U[15],T[6+A*2]],['X','O',L20,L24,Q[3+A*2],Q[7+A*2],R[3+A*2],R[7+A*2],S[3+A*2],S[7+A*2],P[3+A*2],P[7+A*2],SG[3+A*2],SG[7+A*2],U[5],V[21],U[14],T[3+A*2],U[15],T[7+A*2]],['X','O',L21,L22,Q[4+A*2],Q[5+A*2],R[4+A*2],R[5+A*2],S[4+A*2],S[5+A*2],P[4+A*2],P[5+A*2],SG[4+A*2],SG[5+A*2],U[5],V[22],U[14],T[4+A*2],U[15],T[5+A*2]],
['X','O',L21,L23,Q[4+A*2],Q[6+A*2],R[4+A*2],R[6+A*2],S[4+A*2],S[6+A*2],P[4+A*2],P[6+A*2],SG[4+A*2],SG[6+A*2],U[5],V[23],U[14],T[4+A*2],U[15],T[6+A*2]],['X','O',L21,L24,Q[4+A*2],Q[7+A*2],R[4+A*2],R[7+A*2],S[4+A*2],S[7+A*2],P[4+A*2],P[7+A*2],SG[4+A*2],SG[7+A*2],U[6],V[24],U[14],T[4+A*2],U[15],T[7+A*2]],['X','O',L22,L23,Q[5+A*2],Q[6+A*2],R[5+A*2],R[6+A*2],S[5+A*2],S[6+A*2],P[5+A*2],P[6+A*2],SG[5+A*2],SG[6+A*2],U[6],V[25],U[14],T[5+A*2],U[15],T[6+A*2]],['X','O',L22,L24,Q[5+A*2],Q[7+A*2],R[5+A*2],R[7+A*2],S[5+A*2],S[7+A*2],P[5+A*2],P[7+A*2],SG[5+A*2],SG[7+A*2],U[6],V[26],U[14],T[5+A*2],U[15],T[7+A*2]],['X','O',L23,L24,Q[6+A*2],Q[7+A*2],R[6+A*2],R[7+A*2],S[6+A*2],S[7+A*2],P[6+A*2],P[7+A*2],SG[6+A*2],SG[7+A*2],U[6],V[27],U[14],T[6+A*2],U[15],T[7+A*2]],
['X','O',L18,L17,Q[1+A*2],Q[0+A*2],R[1+A*2],R[0+A*2],S[1+A*2],S[0+A*2],P[1+A*2],P[0+A*2],SG[1+A*2],SG[0+A*2],U[7],V[28],U[14],T[1+A*2],U[15],T[0+A*2]],['X','O',L19,L17,Q[2+A*2],Q[0+A*2],R[2+A*2],R[0+A*2],S[2+A*2],S[0+A*2],P[2+A*2],P[0+A*2],SG[2+A*2],SG[0+A*2],U[7],V[29],U[14],T[2+A*2],U[15],T[0+A*2]],['X','O',L20,L17,Q[3+A*2],Q[0+A*2],R[3+A*2],R[0+A*2],S[3+A*2],S[0+A*2],P[3+A*2],P[0+A*2],SG[3+A*2],SG[0+A*2],U[7],V[30],U[14],T[3+A*2],U[15],T[0+A*2]],['X','O',L21,L17,Q[4+A*2],Q[0+A*2],R[4+A*2],R[0+A*2],S[4+A*2],S[0+A*2],P[4+A*2],P[0+A*2],SG[4+A*2],SG[0+A*2],U[7],V[31],U[14],T[4+A*2],U[15],T[0+A*2]],['X','O',L22,L17,Q[5+A*2],Q[0+A*2],R[5+A*2],R[0+A*2],S[5+A*2],S[0+A*2],P[5+A*2],P[0+A*2],SG[5+A*2],SG[0+A*2],U[8],V[32],U[14],T[5+A*2],U[15],T[0+A*2]],
['X','O',L23,L17,Q[6+A*2],Q[0+A*2],R[6+A*2],R[0+A*2],S[6+A*2],S[0+A*2],P[6+A*2],P[0+A*2],SG[6+A*2],SG[0+A*2],U[8],V[33],U[14],T[6+A*2],U[15],T[0+A*2]],['X','O',L24,L17,Q[7+A*2],Q[0+A*2],R[7+A*2],R[0+A*2],S[7+A*2],S[0+A*2],P[7+A*2],P[0+A*2],SG[7+A*2],SG[0+A*2],U[8],V[34],U[14],T[7+A*2],U[15],T[0+A*2]],['X','O',L19,L18,Q[2+A*2],Q[1+A*2],R[2+A*2],R[1+A*2],S[2+A*2],S[1+A*2],P[2+A*2],P[1+A*2],SG[2+A*2],SG[1+A*2],U[8],V[35],U[14],T[2+A*2],U[15],T[1+A*2]],['X','O',L20,L18,Q[3+A*2],Q[1+A*2],R[3+A*2],R[1+A*2],S[3+A*2],S[1+A*2],P[3+A*2],P[1+A*2],SG[3+A*2],SG[1+A*2],U[9],V[36],U[14],T[3+A*2],U[15],T[1+A*2]],['X','O',L21,L18,Q[4+A*2],Q[1+A*2],R[4+A*2],R[1+A*2],S[4+A*2],S[1+A*2],P[4+A*2],P[1+A*2],SG[4+A*2],SG[1+A*2],U[9],V[37],U[14],T[4+A*2],U[15],T[1+A*2]],
['X','O',L22,L18,Q[5+A*2],Q[1+A*2],R[5+A*2],R[1+A*2],S[5+A*2],S[1+A*2],P[5+A*2],P[1+A*2],SG[5+A*2],SG[1+A*2],U[9],V[38],U[14],T[5+A*2],U[15],T[1+A*2]],['X','O',L23,L18,Q[6+A*2],Q[1+A*2],R[6+A*2],R[1+A*2],S[6+A*2],S[1+A*2],P[6+A*2],P[1+A*2],SG[6+A*2],SG[1+A*2],U[9],V[39],U[14],T[6+A*2],U[15],T[1+A*2]],['X','O',L24,L18,Q[7+A*2],Q[1+A*2],R[7+A*2],R[1+A*2],S[7+A*2],S[1+A*2],P[7+A*2],P[1+A*2],SG[7+A*2],SG[1+A*2],U[10],V[40],U[14],T[7+A*2],U[15],T[1+A*2]],['X','O',L20,L19,Q[3+A*2],Q[2+A*2],R[3+A*2],R[2+A*2],S[3+A*2],S[2+A*2],P[3+A*2],P[2+A*2],SG[3+A*2],SG[2+A*2],U[10],V[41],U[14],T[3+A*2],U[15],T[2+A*2]],['X','O',L21,L19,Q[4+A*2],Q[2+A*2],R[4+A*2],R[2+A*2],S[4+A*2],S[2+A*2],P[4+A*2],P[2+A*2],SG[4+A*2],SG[2+A*2],U[10],V[42],U[14],T[4+A*2],U[15],T[2+A*2]],
['X','O',L22,L19,Q[5+A*2],Q[2+A*2],R[5+A*2],R[2+A*2],S[5+A*2],S[2+A*2],P[5+A*2],P[2+A*2],SG[5+A*2],SG[2+A*2],U[10],V[43],U[14],T[5+A*2],U[15],T[2+A*2]],['X','O',L23,L19,Q[6+A*2],Q[2+A*2],R[6+A*2],R[2+A*2],S[6+A*2],S[2+A*2],P[6+A*2],P[2+A*2],SG[6+A*2],SG[2+A*2],U[11],V[44],U[14],T[6+A*2],U[15],T[2+A*2]],['X','O',L24,L19,Q[7+A*2],Q[2+A*2],R[7+A*2],R[2+A*2],S[7+A*2],S[2+A*2],P[7+A*2],P[2+A*2],SG[7+A*2],SG[2+A*2],U[11],V[45],U[14],T[7+A*2],U[15],T[2+A*2]],['X','O',L21,L20,Q[4+A*2],Q[3+A*2],R[4+A*2],R[3+A*2],S[4+A*2],S[3+A*2],P[4+A*2],P[3+A*2],SG[4+A*2],SG[3+A*2],U[11],V[46],U[14],T[4+A*2],U[15],T[3+A*2]],['X','O',L22,L20,Q[5+A*2],Q[3+A*2],R[5+A*2],R[3+A*2],S[5+A*2],S[3+A*2],P[5+A*2],P[3+A*2],SG[5+A*2],SG[3+A*2],U[11],V[47],U[14],T[5+A*2],U[15],T[3+A*2]],
['X','O',L23,L20,Q[6+A*2],Q[3+A*2],R[6+A*2],R[3+A*2],S[6+A*2],S[3+A*2],P[6+A*2],P[3+A*2],SG[6+A*2],SG[3+A*2],U[12],V[48],U[14],T[6+A*2],U[15],T[3+A*2]],['X','O',L24,L20,Q[7+A*2],Q[3+A*2],R[7+A*2],R[3+A*2],S[7+A*2],S[3+A*2],P[7+A*2],P[3+A*2],SG[7+A*2],SG[3+A*2],U[12],V[49],U[14],T[7+A*2],U[15],T[3+A*2]],['X','O',L22,L21,Q[5+A*2],Q[4+A*2],R[5+A*2],R[4+A*2],S[5+A*2],S[4+A*2],P[5+A*2],P[4+A*2],SG[5+A*2],SG[4+A*2],U[12],V[50],U[14],T[5+A*2],U[15],T[4+A*2]],['X','O',L23,L21,Q[6+A*2],Q[4+A*2],R[6+A*2],R[4+A*2],S[6+A*2],S[4+A*2],P[6+A*2],P[4+A*2],SG[6+A*2],SG[4+A*2],U[12],V[51],U[14],T[6+A*2],U[15],T[4+A*2]],['X','O',L24,L21,Q[7+A*2],Q[4+A*2],R[7+A*2],R[4+A*2],S[7+A*2],S[4+A*2],P[7+A*2],P[4+A*2],SG[7+A*2],SG[4+A*2],U[13],V[52],U[14],T[7+A*2],U[15],T[4+A*2]],
['X','O',L23,L22,Q[6+A*2],Q[5+A*2],R[6+A*2],R[5+A*2],S[6+A*2],S[5+A*2],P[6+A*2],P[5+A*2],SG[6+A*2],SG[5+A*2],U[13],V[53],U[14],T[6+A*2],U[15],T[5+A*2]],['X','O',L24,L22,Q[7+A*2],Q[5+A*2],R[7+A*2],R[5+A*2],S[7+A*2],S[5+A*2],P[7+A*2],P[5+A*2],SG[7+A*2],SG[5+A*2],U[13],V[54],U[14],T[7+A*2],U[15],T[5+A*2]],['X','O',L24,L23,Q[7+A*2],Q[6+A*2],R[7+A*2],R[6+A*2],S[7+A*2],S[6+A*2],P[7+A*2],P[6+A*2],SG[7+A*2],SG[6+A*2],U[13],V[55],U[14],T[7+A*2],U[15],T[6+A*2]],['X','O',L25,L26,Q[0+A*3],Q[1+A*3],R[0+A*3],R[1+A*3],S[0+A*3],S[1+A*3],P[0+A*3],P[1+A*3],SG[0+A*3],SG[1+A*3],U[0],V[0],U[14],T[0+A*3],U[15],T[1+A*3]],['X','O',L25,L27,Q[0+A*3],Q[2+A*3],R[0+A*3],R[2+A*3],S[0+A*3],S[2+A*3],P[0+A*3],P[2+A*3],SG[0+A*3],SG[2+A*3],U[0],V[1],U[14],T[0+A*3],U[15],T[2+A*3]],
['X','O',L25,L28,Q[0+A*3],Q[3+A*3],R[0+A*3],R[3+A*3],S[0+A*3],S[3+A*3],P[0+A*3],P[3+A*3],SG[0+A*3],SG[3+A*3],U[0],V[2],U[14],T[0+A*3],U[15],T[3+A*3]],['X','O',L25,L29,Q[0+A*3],Q[4+A*3],R[0+A*3],R[4+A*3],S[0+A*3],S[4+A*3],P[0+A*3],P[4+A*3],SG[0+A*3],SG[4+A*3],U[0],V[3],U[14],T[0+A*3],U[15],T[4+A*3]],['X','O',L25,L30,Q[0+A*3],Q[5+A*3],R[0+A*3],R[5+A*3],S[0+A*3],S[5+A*3],P[0+A*3],P[5+A*3],SG[0+A*3],SG[5+A*3],U[1],V[4],U[14],T[0+A*3],U[15],T[5+A*3]],['X','O',L25,L31,Q[0+A*3],Q[6+A*3],R[0+A*3],R[6+A*3],S[0+A*3],S[6+A*3],P[0+A*3],P[6+A*3],SG[0+A*3],SG[6+A*3],U[1],V[5],U[14],T[0+A*3],U[15],T[6+A*3]],['X','O',L25,L32,Q[0+A*3],Q[7+A*3],R[0+A*3],R[7+A*3],S[0+A*3],S[7+A*3],P[0+A*3],P[7+A*3],SG[0+A*3],SG[7+A*3],U[1],V[6],U[14],T[0+A*3],U[15],T[7+A*3]],
['X','O',L26,L27,Q[1+A*3],Q[2+A*3],R[1+A*3],R[2+A*3],S[1+A*3],S[2+A*3],P[1+A*3],P[2+A*3],SG[1+A*3],SG[2+A*3],U[1],V[7],U[14],T[1+A*3],U[15],T[2+A*3]],['X','O',L26,L28,Q[1+A*3],Q[3+A*3],R[1+A*3],R[3+A*3],S[1+A*3],S[3+A*3],P[1+A*3],P[3+A*3],SG[1+A*3],SG[3+A*3],U[2],V[8],U[14],T[1+A*3],U[15],T[3+A*3]],['X','O',L26,L29,Q[1+A*3],Q[4+A*3],R[1+A*3],R[4+A*3],S[1+A*3],S[4+A*3],P[1+A*3],P[4+A*3],SG[1+A*3],SG[4+A*3],U[2],V[9],U[14],T[1+A*3],U[15],T[4+A*3]],['X','O',L26,L30,Q[1+A*3],Q[5+A*3],R[1+A*3],R[5+A*3],S[1+A*3],S[5+A*3],P[1+A*3],P[5+A*3],SG[1+A*3],SG[5+A*3],U[2],V[10],U[14],T[1+A*3],U[15],T[5+A*3]],['X','O',L26,L31,Q[1+A*3],Q[6+A*3],R[1+A*3],R[6+A*3],S[1+A*3],S[6+A*3],P[1+A*3],P[6+A*3],SG[1+A*3],SG[6+A*3],U[2],V[11],U[14],T[1+A*3],U[15],T[6+A*3]],
['X','O',L26,L32,Q[1+A*3],Q[7+A*3],R[1+A*3],R[7+A*3],S[1+A*3],S[7+A*3],P[1+A*3],P[7+A*3],SG[1+A*3],SG[7+A*3],U[3],V[12],U[14],T[1+A*3],U[15],T[7+A*3]],['X','O',L27,L28,Q[2+A*3],Q[3+A*3],R[2+A*3],R[3+A*3],S[2+A*3],S[3+A*3],P[2+A*3],P[3+A*3],SG[2+A*3],SG[3+A*3],U[3],V[13],U[14],T[2+A*3],U[15],T[3+A*3]],['X','O',L27,L29,Q[2+A*3],Q[4+A*3],R[2+A*3],R[4+A*3],S[2+A*3],S[4+A*3],P[2+A*3],P[4+A*3],SG[2+A*3],SG[4+A*3],U[3],V[14],U[14],T[2+A*3],U[15],T[4+A*3]],['X','O',L27,L30,Q[2+A*3],Q[5+A*3],R[2+A*3],R[5+A*3],S[2+A*3],S[5+A*3],P[2+A*3],P[5+A*3],SG[2+A*3],SG[5+A*3],U[3],V[15],U[14],T[2+A*3],U[15],T[5+A*3]],['X','O',L27,L31,Q[2+A*3],Q[6+A*3],R[2+A*3],R[6+A*3],S[2+A*3],S[6+A*3],P[2+A*3],P[6+A*3],SG[2+A*3],SG[6+A*3],U[4],V[16],U[14],T[2+A*3],U[15],T[6+A*3]],
['X','O',L27,L32,Q[2+A*3],Q[7+A*3],R[2+A*3],R[7+A*3],S[2+A*3],S[7+A*3],P[2+A*3],P[7+A*3],SG[2+A*3],SG[7+A*3],U[4],V[17],U[14],T[2+A*3],U[15],T[7+A*3]],['X','O',L28,L29,Q[3+A*3],Q[4+A*3],R[3+A*3],R[4+A*3],S[3+A*3],S[4+A*3],P[3+A*3],P[4+A*3],SG[3+A*3],SG[4+A*3],U[4],V[18],U[14],T[3+A*3],U[15],T[4+A*3]],['X','O',L28,L30,Q[3+A*3],Q[5+A*3],R[3+A*3],R[5+A*3],S[3+A*3],S[5+A*3],P[3+A*3],P[5+A*3],SG[3+A*3],SG[5+A*3],U[4],V[19],U[14],T[3+A*3],U[15],T[5+A*3]],['X','O',L28,L31,Q[3+A*3],Q[6+A*3],R[3+A*3],R[6+A*3],S[3+A*3],S[6+A*3],P[3+A*3],P[6+A*3],SG[3+A*3],SG[6+A*3],U[5],V[20],U[14],T[3+A*3],U[15],T[6+A*3]],['X','O',L28,L32,Q[3+A*3],Q[7+A*3],R[3+A*3],R[7+A*3],S[3+A*3],S[7+A*3],P[3+A*3],P[7+A*3],SG[3+A*3],SG[7+A*3],U[5],V[21],U[14],T[3+A*3],U[15],T[7+A*3]],
['X','O',L29,L30,Q[4+A*3],Q[5+A*3],R[4+A*3],R[5+A*3],S[4+A*3],S[5+A*3],P[4+A*3],P[5+A*3],SG[4+A*3],SG[5+A*3],U[5],V[22],U[14],T[4+A*3],U[15],T[5+A*3]],['X','O',L29,L31,Q[4+A*3],Q[6+A*3],R[4+A*3],R[6+A*3],S[4+A*3],S[6+A*3],P[4+A*3],P[6+A*3],SG[4+A*3],SG[6+A*3],U[5],V[23],U[14],T[4+A*3],U[15],T[6+A*3]],['X','O',L29,L32,Q[4+A*3],Q[7+A*3],R[4+A*3],R[7+A*3],S[4+A*3],S[7+A*3],P[4+A*3],P[7+A*3],SG[4+A*3],SG[7+A*3],U[6],V[24],U[14],T[4+A*3],U[15],T[7+A*3]],['X','O',L30,L31,Q[5+A*3],Q[6+A*3],R[5+A*3],R[6+A*3],S[5+A*3],S[6+A*3],P[5+A*3],P[6+A*3],SG[5+A*3],SG[6+A*3],U[6],V[25],U[14],T[5+A*3],U[15],T[6+A*3]],['X','O',L30,L32,Q[5+A*3],Q[7+A*3],R[5+A*3],R[7+A*3],S[5+A*3],S[7+A*3],P[5+A*3],P[7+A*3],SG[5+A*3],SG[7+A*3],U[6],V[26],U[14],T[5+A*3],U[15],T[7+A*3]],
['X','O',L31,L32,Q[6+A*3],Q[7+A*3],R[6+A*3],R[7+A*3],S[6+A*3],S[7+A*3],P[6+A*3],P[7+A*3],SG[6+A*3],SG[7+A*3],U[6],V[27],U[14],T[6+A*3],U[15],T[7+A*3]],['X','O',L26,L25,Q[1+A*3],Q[0+A*3],R[1+A*3],R[0+A*3],S[1+A*3],S[0+A*3],P[1+A*3],P[0+A*3],SG[1+A*3],SG[0+A*3],U[7],V[28],U[14],T[1+A*3],U[15],T[0+A*3]],['X','O',L27,L25,Q[2+A*3],Q[0+A*3],R[2+A*3],R[0+A*3],S[2+A*3],S[0+A*3],P[2+A*3],P[0+A*3],SG[2+A*3],SG[0+A*3],U[7],V[29],U[14],T[2+A*3],U[15],T[0+A*3]],['X','O',L28,L25,Q[3+A*3],Q[0+A*3],R[3+A*3],R[0+A*3],S[3+A*3],S[0+A*3],P[3+A*3],P[0+A*3],SG[3+A*3],SG[0+A*3],U[7],V[30],U[14],T[3+A*3],U[15],T[0+A*3]],['X','O',L29,L25,Q[4+A*3],Q[0+A*3],R[4+A*3],R[0+A*3],S[4+A*3],S[0+A*3],P[4+A*3],P[0+A*3],SG[4+A*3],SG[0+A*3],U[7],V[31],U[14],T[4+A*3],U[15],T[0+A*3]],
['X','O',L30,L25,Q[5+A*3],Q[0+A*3],R[5+A*3],R[0+A*3],S[5+A*3],S[0+A*3],P[5+A*3],P[0+A*3],SG[5+A*3],SG[0+A*3],U[8],V[32],U[14],T[5+A*3],U[15],T[0+A*3]],['X','O',L31,L25,Q[6+A*3],Q[0+A*3],R[6+A*3],R[0+A*3],S[6+A*3],S[0+A*3],P[6+A*3],P[0+A*3],SG[6+A*3],SG[0+A*3],U[8],V[33],U[14],T[6+A*3],U[15],T[0+A*3]],['X','O',L32,L25,Q[7+A*3],Q[0+A*3],R[7+A*3],R[0+A*3],S[7+A*3],S[0+A*3],P[7+A*3],P[0+A*3],SG[7+A*3],SG[0+A*3],U[8],V[34],U[14],T[7+A*3],U[15],T[0+A*3]],['X','O',L27,L26,Q[2+A*3],Q[1+A*3],R[2+A*3],R[1+A*3],S[2+A*3],S[1+A*3],P[2+A*3],P[1+A*3],SG[2+A*3],SG[1+A*3],U[8],V[35],U[14],T[2+A*3],U[15],T[1+A*3]],['X','O',L28,L26,Q[3+A*3],Q[1+A*3],R[3+A*3],R[1+A*3],S[3+A*3],S[1+A*3],P[3+A*3],P[1+A*3],SG[3+A*3],SG[1+A*3],U[9],V[36],U[14],T[3+A*3],U[15],T[1+A*3]],
['X','O',L29,L26,Q[4+A*3],Q[1+A*3],R[4+A*3],R[1+A*3],S[4+A*3],S[1+A*3],P[4+A*3],P[1+A*3],SG[4+A*3],SG[1+A*3],U[9],V[37],U[14],T[4+A*3],U[15],T[1+A*3]],['X','O',L30,L26,Q[5+A*3],Q[1+A*3],R[5+A*3],R[1+A*3],S[5+A*3],S[1+A*3],P[5+A*3],P[1+A*3],SG[5+A*3],SG[1+A*3],U[9],V[38],U[14],T[5+A*3],U[15],T[1+A*3]],['X','O',L31,L26,Q[6+A*3],Q[1+A*3],R[6+A*3],R[1+A*3],S[6+A*3],S[1+A*3],P[6+A*3],P[1+A*3],SG[6+A*3],SG[1+A*3],U[9],V[39],U[14],T[6+A*3],U[15],T[1+A*3]],['X','O',L32,L26,Q[7+A*3],Q[1+A*3],R[7+A*3],R[1+A*3],S[7+A*3],S[1+A*3],P[7+A*3],P[1+A*3],SG[7+A*3],SG[1+A*3],U[10],V[40],U[14],T[7+A*3],U[15],T[1+A*3]],['X','O',L28,L27,Q[3+A*3],Q[2+A*3],R[3+A*3],R[2+A*3],S[3+A*3],S[2+A*3],P[3+A*3],P[2+A*3],SG[3+A*3],SG[2+A*3],U[10],V[41],U[14],T[3+A*3],U[15],T[2+A*3]],
['X','O',L29,L27,Q[4+A*3],Q[2+A*3],R[4+A*3],R[2+A*3],S[4+A*3],S[2+A*3],P[4+A*3],P[2+A*3],SG[4+A*3],SG[2+A*3],U[10],V[42],U[14],T[4+A*3],U[15],T[2+A*3]],['X','O',L30,L27,Q[5+A*3],Q[2+A*3],R[5+A*3],R[2+A*3],S[5+A*3],S[2+A*3],P[5+A*3],P[2+A*3],SG[5+A*3],SG[2+A*3],U[10],V[43],U[14],T[5+A*3],U[15],T[2+A*3]],['X','O',L31,L27,Q[6+A*3],Q[2+A*3],R[6+A*3],R[2+A*3],S[6+A*3],S[2+A*3],P[6+A*3],P[2+A*3],SG[6+A*3],SG[2+A*3],U[11],V[44],U[14],T[6+A*3],U[15],T[2+A*3]],['X','O',L32,L27,Q[7+A*3],Q[2+A*3],R[7+A*3],R[2+A*3],S[7+A*3],S[2+A*3],P[7+A*3],P[2+A*3],SG[7+A*3],SG[2+A*3],U[11],V[45],U[14],T[7+A*3],U[15],T[2+A*3]],['X','O',L29,L28,Q[4+A*3],Q[3+A*3],R[4+A*3],R[3+A*3],S[4+A*3],S[3+A*3],P[4+A*3],P[3+A*3],SG[4+A*3],SG[3+A*3],U[11],V[46],U[14],T[4+A*3],U[15],T[3+A*3]],
['X','O',L30,L28,Q[5+A*3],Q[3+A*3],R[5+A*3],R[3+A*3],S[5+A*3],S[3+A*3],P[5+A*3],P[3+A*3],SG[5+A*3],SG[3+A*3],U[11],V[47],U[14],T[5+A*3],U[15],T[3+A*3]],['X','O',L31,L28,Q[6+A*3],Q[3+A*3],R[6+A*3],R[3+A*3],S[6+A*3],S[3+A*3],P[6+A*3],P[3+A*3],SG[6+A*3],SG[3+A*3],U[12],V[48],U[14],T[6+A*3],U[15],T[3+A*3]],['X','O',L32,L28,Q[7+A*3],Q[3+A*3],R[7+A*3],R[3+A*3],S[7+A*3],S[3+A*3],P[7+A*3],P[3+A*3],SG[7+A*3],SG[3+A*3],U[12],V[49],U[14],T[7+A*3],U[15],T[3+A*3]],['X','O',L30,L29,Q[5+A*3],Q[4+A*3],R[5+A*3],R[4+A*3],S[5+A*3],S[4+A*3],P[5+A*3],P[4+A*3],SG[5+A*3],SG[4+A*3],U[12],V[50],U[14],T[5+A*3],U[15],T[4+A*3]],['X','O',L31,L29,Q[6+A*3],Q[4+A*3],R[6+A*3],R[4+A*3],S[6+A*3],S[4+A*3],P[6+A*3],P[4+A*3],SG[6+A*3],SG[4+A*3],U[12],V[51],U[14],T[6+A*3],U[15],T[4+A*3]],
['X','O',L32,L29,Q[7+A*3],Q[4+A*3],R[7+A*3],R[4+A*3],S[7+A*3],S[4+A*3],P[7+A*3],P[4+A*3],SG[7+A*3],SG[4+A*3],U[13],V[52],U[14],T[7+A*3],U[15],T[4+A*3]],['X','O',L31,L30,Q[6+A*3],Q[5+A*3],R[6+A*3],R[5+A*3],S[6+A*3],S[5+A*3],P[6+A*3],P[5+A*3],SG[6+A*3],SG[5+A*3],U[13],V[53],U[14],T[6+A*3],U[15],T[5+A*3]],['X','O',L32,L30,Q[7+A*3],Q[5+A*3],R[7+A*3],R[5+A*3],S[7+A*3],S[5+A*3],P[7+A*3],P[5+A*3],SG[7+A*3],SG[5+A*3],U[13],V[54],U[14],T[7+A*3],U[15],T[5+A*3]],['X','O',L32,L31,Q[7+A*3],Q[6+A*3],R[7+A*3],R[6+A*3],S[7+A*3],S[6+A*3],P[7+A*3],P[6+A*3],SG[7+A*3],SG[6+A*3],U[13],V[55],U[14],T[7+A*3],U[15],T[6+A*3]],['X','O',L33,L34,Q[0+A*4],Q[1+A*4],R[0+A*4],R[1+A*4],S[0+A*4],S[1+A*4],P[0+A*4],P[1+A*4],SG[0+A*4],SG[1+A*4],U[0],V[0],U[14],T[0+A*4],U[15],T[1+A*4]],
['X','O',L33,L35,Q[0+A*4],Q[2+A*4],R[0+A*4],R[2+A*4],S[0+A*4],S[2+A*4],P[0+A*4],P[2+A*4],SG[0+A*4],SG[2+A*4],U[0],V[1],U[14],T[0+A*4],U[15],T[2+A*4]],['X','O',L33,L36,Q[0+A*4],Q[3+A*4],R[0+A*4],R[3+A*4],S[0+A*4],S[3+A*4],P[0+A*4],P[3+A*4],SG[0+A*4],SG[3+A*4],U[0],V[2],U[14],T[0+A*4],U[15],T[3+A*4]],['X','O',L33,L37,Q[0+A*4],Q[4+A*4],R[0+A*4],R[4+A*4],S[0+A*4],S[4+A*4],P[0+A*4],P[4+A*4],SG[0+A*4],SG[4+A*4],U[0],V[3],U[14],T[0+A*4],U[15],T[4+A*4]],['X','O',L33,L38,Q[0+A*4],Q[5+A*4],R[0+A*4],R[5+A*4],S[0+A*4],S[5+A*4],P[0+A*4],P[5+A*4],SG[0+A*4],SG[5+A*4],U[1],V[4],U[14],T[0+A*4],U[15],T[5+A*4]],['X','O',L33,L39,Q[0+A*4],Q[6+A*4],R[0+A*4],R[6+A*4],S[0+A*4],S[6+A*4],P[0+A*4],P[6+A*4],SG[0+A*4],SG[6+A*4],U[1],V[5],U[14],T[0+A*4],U[15],T[6+A*4]],
['X','O',L33,L40,Q[0+A*4],Q[7+A*4],R[0+A*4],R[7+A*4],S[0+A*4],S[7+A*4],P[0+A*4],P[7+A*4],SG[0+A*4],SG[7+A*4],U[1],V[6],U[14],T[0+A*4],U[15],T[7+A*4]],['X','O',L34,L35,Q[1+A*4],Q[2+A*4],R[1+A*4],R[2+A*4],S[1+A*4],S[2+A*4],P[1+A*4],P[2+A*4],SG[1+A*4],SG[2+A*4],U[1],V[7],U[14],T[1+A*4],U[15],T[2+A*4]],['X','O',L34,L36,Q[1+A*4],Q[3+A*4],R[1+A*4],R[3+A*4],S[1+A*4],S[3+A*4],P[1+A*4],P[3+A*4],SG[1+A*4],SG[3+A*4],U[2],V[8],U[14],T[1+A*4],U[15],T[3+A*4]],['X','O',L34,L37,Q[1+A*4],Q[4+A*4],R[1+A*4],R[4+A*4],S[1+A*4],S[4+A*4],P[1+A*4],P[4+A*4],SG[1+A*4],SG[4+A*4],U[2],V[9],U[14],T[1+A*4],U[15],T[4+A*4]],['X','O',L34,L38,Q[1+A*4],Q[5+A*4],R[1+A*4],R[5+A*4],S[1+A*4],S[5+A*4],P[1+A*4],P[5+A*4],SG[1+A*4],SG[5+A*4],U[2],V[10],U[14],T[1+A*4],U[15],T[5+A*4]],
['X','O',L34,L39,Q[1+A*4],Q[6+A*4],R[1+A*4],R[6+A*4],S[1+A*4],S[6+A*4],P[1+A*4],P[6+A*4],SG[1+A*4],SG[6+A*4],U[2],V[11],U[14],T[1+A*4],U[15],T[6+A*4]],['X','O',L34,L40,Q[1+A*4],Q[7+A*4],R[1+A*4],R[7+A*4],S[1+A*4],S[7+A*4],P[1+A*4],P[7+A*4],SG[1+A*4],SG[7+A*4],U[3],V[12],U[14],T[1+A*4],U[15],T[7+A*4]],['X','O',L35,L36,Q[2+A*4],Q[3+A*4],R[2+A*4],R[3+A*4],S[2+A*4],S[3+A*4],P[2+A*4],P[3+A*4],SG[2+A*4],SG[3+A*4],U[3],V[13],U[14],T[2+A*4],U[15],T[3+A*4]],['X','O',L35,L37,Q[2+A*4],Q[4+A*4],R[2+A*4],R[4+A*4],S[2+A*4],S[4+A*4],P[2+A*4],P[4+A*4],SG[2+A*4],SG[4+A*4],U[3],V[14],U[14],T[2+A*4],U[15],T[4+A*4]],['X','O',L35,L38,Q[2+A*4],Q[5+A*4],R[2+A*4],R[5+A*4],S[2+A*4],S[5+A*4],P[2+A*4],P[5+A*4],SG[2+A*4],SG[5+A*4],U[3],V[15],U[14],T[2+A*4],U[15],T[5+A*4]],
['X','O',L35,L39,Q[2+A*4],Q[6+A*4],R[2+A*4],R[6+A*4],S[2+A*4],S[6+A*4],P[2+A*4],P[6+A*4],SG[2+A*4],SG[6+A*4],U[4],V[16],U[14],T[2+A*4],U[15],T[6+A*4]],['X','O',L35,L40,Q[2+A*4],Q[7+A*4],R[2+A*4],R[7+A*4],S[2+A*4],S[7+A*4],P[2+A*4],P[7+A*4],SG[2+A*4],SG[7+A*4],U[4],V[17],U[14],T[2+A*4],U[15],T[7+A*4]],['X','O',L36,L37,Q[3+A*4],Q[4+A*4],R[3+A*4],R[4+A*4],S[3+A*4],S[4+A*4],P[3+A*4],P[4+A*4],SG[3+A*4],SG[4+A*4],U[4],V[18],U[14],T[3+A*4],U[15],T[4+A*4]],['X','O',L36,L38,Q[3+A*4],Q[5+A*4],R[3+A*4],R[5+A*4],S[3+A*4],S[5+A*4],P[3+A*4],P[5+A*4],SG[3+A*4],SG[5+A*4],U[4],V[19],U[14],T[3+A*4],U[15],T[5+A*4]],['X','O',L36,L39,Q[3+A*4],Q[6+A*4],R[3+A*4],R[6+A*4],S[3+A*4],S[6+A*4],P[3+A*4],P[6+A*4],SG[3+A*4],SG[6+A*4],U[5],V[20],U[14],T[3+A*4],U[15],T[6+A*4]],
['X','O',L36,L40,Q[3+A*4],Q[7+A*4],R[3+A*4],R[7+A*4],S[3+A*4],S[7+A*4],P[3+A*4],P[7+A*4],SG[3+A*4],SG[7+A*4],U[5],V[21],U[14],T[3+A*4],U[15],T[7+A*4]],['X','O',L37,L38,Q[4+A*4],Q[5+A*4],R[4+A*4],R[5+A*4],S[4+A*4],S[5+A*4],P[4+A*4],P[5+A*4],SG[4+A*4],SG[5+A*4],U[5],V[22],U[14],T[4+A*4],U[15],T[5+A*4]],['X','O',L37,L39,Q[4+A*4],Q[6+A*4],R[4+A*4],R[6+A*4],S[4+A*4],S[6+A*4],P[4+A*4],P[6+A*4],SG[4+A*4],SG[6+A*4],U[5],V[23],U[14],T[4+A*4],U[15],T[6+A*4]],['X','O',L37,L40,Q[4+A*4],Q[7+A*4],R[4+A*4],R[7+A*4],S[4+A*4],S[7+A*4],P[4+A*4],P[7+A*4],SG[4+A*4],SG[7+A*4],U[6],V[24],U[14],T[4+A*4],U[15],T[7+A*4]],['X','O',L38,L39,Q[5+A*4],Q[6+A*4],R[5+A*4],R[6+A*4],S[5+A*4],S[6+A*4],P[5+A*4],P[6+A*4],SG[5+A*4],SG[6+A*4],U[6],V[25],U[14],T[5+A*4],U[15],T[6+A*4]],
['X','O',L38,L40,Q[5+A*4],Q[7+A*4],R[5+A*4],R[7+A*4],S[5+A*4],S[7+A*4],P[5+A*4],P[7+A*4],SG[5+A*4],SG[7+A*4],U[6],V[26],U[14],T[5+A*4],U[15],T[7+A*4]],['X','O',L39,L40,Q[6+A*4],Q[7+A*4],R[6+A*4],R[7+A*4],S[6+A*4],S[7+A*4],P[6+A*4],P[7+A*4],SG[6+A*4],SG[7+A*4],U[6],V[27],U[14],T[6+A*4],U[15],T[7+A*4]],['X','O',L34,L33,Q[1+A*4],Q[0+A*4],R[1+A*4],R[0+A*4],S[1+A*4],S[0+A*4],P[1+A*4],P[0+A*4],SG[1+A*4],SG[0+A*4],U[7],V[28],U[14],T[1+A*4],U[15],T[0+A*4]],['X','O',L35,L33,Q[2+A*4],Q[0+A*4],R[2+A*4],R[0+A*4],S[2+A*4],S[0+A*4],P[2+A*4],P[0+A*4],SG[2+A*4],SG[0+A*4],U[7],V[29],U[14],T[2+A*4],U[15],T[0+A*4]],['X','O',L36,L33,Q[3+A*4],Q[0+A*4],R[3+A*4],R[0+A*4],S[3+A*4],S[0+A*4],P[3+A*4],P[0+A*4],SG[3+A*4],SG[0+A*4],U[7],V[30],U[14],T[3+A*4],U[15],T[0+A*4]],
['X','O',L37,L33,Q[4+A*4],Q[0+A*4],R[4+A*4],R[0+A*4],S[4+A*4],S[0+A*4],P[4+A*4],P[0+A*4],SG[4+A*4],SG[0+A*4],U[7],V[31],U[14],T[4+A*4],U[15],T[0+A*4]],['X','O',L38,L33,Q[5+A*4],Q[0+A*4],R[5+A*4],R[0+A*4],S[5+A*4],S[0+A*4],P[5+A*4],P[0+A*4],SG[5+A*4],SG[0+A*4],U[8],V[32],U[14],T[5+A*4],U[15],T[0+A*4]],['X','O',L39,L33,Q[6+A*4],Q[0+A*4],R[6+A*4],R[0+A*4],S[6+A*4],S[0+A*4],P[6+A*4],P[0+A*4],SG[6+A*4],SG[0+A*4],U[8],V[33],U[14],T[6+A*4],U[15],T[0+A*4]],['X','O',L40,L33,Q[7+A*4],Q[0+A*4],R[7+A*4],R[0+A*4],S[7+A*4],S[0+A*4],P[7+A*4],P[0+A*4],SG[7+A*4],SG[0+A*4],U[8],V[34],U[14],T[7+A*4],U[15],T[0+A*4]],['X','O',L35,L34,Q[2+A*4],Q[1+A*4],R[2+A*4],R[1+A*4],S[2+A*4],S[1+A*4],P[2+A*4],P[1+A*4],SG[2+A*4],SG[1+A*4],U[8],V[35],U[14],T[2+A*4],U[15],T[1+A*4]],
['X','O',L36,L34,Q[3+A*4],Q[1+A*4],R[3+A*4],R[1+A*4],S[3+A*4],S[1+A*4],P[3+A*4],P[1+A*4],SG[3+A*4],SG[1+A*4],U[9],V[36],U[14],T[3+A*4],U[15],T[1+A*4]],['X','O',L37,L34,Q[4+A*4],Q[1+A*4],R[4+A*4],R[1+A*4],S[4+A*4],S[1+A*4],P[4+A*4],P[1+A*4],SG[4+A*4],SG[1+A*4],U[9],V[37],U[14],T[4+A*4],U[15],T[1+A*4]],['X','O',L38,L34,Q[5+A*4],Q[1+A*4],R[5+A*4],R[1+A*4],S[5+A*4],S[1+A*4],P[5+A*4],P[1+A*4],SG[5+A*4],SG[1+A*4],U[9],V[38],U[14],T[5+A*4],U[15],T[1+A*4]],['X','O',L39,L34,Q[6+A*4],Q[1+A*4],R[6+A*4],R[1+A*4],S[6+A*4],S[1+A*4],P[6+A*4],P[1+A*4],SG[6+A*4],SG[1+A*4],U[9],V[39],U[14],T[6+A*4],U[15],T[1+A*4]],['X','O',L40,L34,Q[7+A*4],Q[1+A*4],R[7+A*4],R[1+A*4],S[7+A*4],S[1+A*4],P[7+A*4],P[1+A*4],SG[7+A*4],SG[1+A*4],U[10],V[40],U[14],T[7+A*4],U[15],T[1+A*4]],
['X','O',L36,L35,Q[3+A*4],Q[2+A*4],R[3+A*4],R[2+A*4],S[3+A*4],S[2+A*4],P[3+A*4],P[2+A*4],SG[3+A*4],SG[2+A*4],U[10],V[41],U[14],T[3+A*4],U[15],T[2+A*4]],['X','O',L37,L35,Q[4+A*4],Q[2+A*4],R[4+A*4],R[2+A*4],S[4+A*4],S[2+A*4],P[4+A*4],P[2+A*4],SG[4+A*4],SG[2+A*4],U[10],V[42],U[14],T[4+A*4],U[15],T[2+A*4]],['X','O',L38,L35,Q[5+A*4],Q[2+A*4],R[5+A*4],R[2+A*4],S[5+A*4],S[2+A*4],P[5+A*4],P[2+A*4],SG[5+A*4],SG[2+A*4],U[10],V[43],U[14],T[5+A*4],U[15],T[2+A*4]],['X','O',L39,L35,Q[6+A*4],Q[2+A*4],R[6+A*4],R[2+A*4],S[6+A*4],S[2+A*4],P[6+A*4],P[2+A*4],SG[6+A*4],SG[2+A*4],U[11],V[44],U[14],T[6+A*4],U[15],T[2+A*4]],['X','O',L40,L35,Q[7+A*4],Q[2+A*4],R[7+A*4],R[2+A*4],S[7+A*4],S[2+A*4],P[7+A*4],P[2+A*4],SG[7+A*4],SG[2+A*4],U[11],V[45],U[14],T[7+A*4],U[15],T[2+A*4]],
['X','O',L37,L36,Q[4+A*4],Q[3+A*4],R[4+A*4],R[3+A*4],S[4+A*4],S[3+A*4],P[4+A*4],P[3+A*4],SG[4+A*4],SG[3+A*4],U[11],V[46],U[14],T[4+A*4],U[15],T[3+A*4]],['X','O',L38,L36,Q[5+A*4],Q[3+A*4],R[5+A*4],R[3+A*4],S[5+A*4],S[3+A*4],P[5+A*4],P[3+A*4],SG[5+A*4],SG[3+A*4],U[11],V[47],U[14],T[5+A*4],U[15],T[3+A*4]],['X','O',L39,L36,Q[6+A*4],Q[3+A*4],R[6+A*4],R[3+A*4],S[6+A*4],S[3+A*4],P[6+A*4],P[3+A*4],SG[6+A*4],SG[3+A*4],U[12],V[48],U[14],T[6+A*4],U[15],T[3+A*4]],['X','O',L40,L36,Q[7+A*4],Q[3+A*4],R[7+A*4],R[3+A*4],S[7+A*4],S[3+A*4],P[7+A*4],P[3+A*4],SG[7+A*4],SG[3+A*4],U[12],V[49],U[14],T[7+A*4],U[15],T[3+A*4]],['X','O',L38,L37,Q[5+A*4],Q[4+A*4],R[5+A*4],R[4+A*4],S[5+A*4],S[4+A*4],P[5+A*4],P[4+A*4],SG[5+A*4],SG[4+A*4],U[12],V[50],U[14],T[5+A*4],U[15],T[4+A*4]],
['X','O',L39,L37,Q[6+A*4],Q[4+A*4],R[6+A*4],R[4+A*4],S[6+A*4],S[4+A*4],P[6+A*4],P[4+A*4],SG[6+A*4],SG[4+A*4],U[12],V[51],U[14],T[6+A*4],U[15],T[4+A*4]],['X','O',L40,L37,Q[7+A*4],Q[4+A*4],R[7+A*4],R[4+A*4],S[7+A*4],S[4+A*4],P[7+A*4],P[4+A*4],SG[7+A*4],SG[4+A*4],U[13],V[52],U[14],T[7+A*4],U[15],T[4+A*4]],['X','O',L39,L38,Q[6+A*4],Q[5+A*4],R[6+A*4],R[5+A*4],S[6+A*4],S[5+A*4],P[6+A*4],P[5+A*4],SG[6+A*4],SG[5+A*4],U[13],V[53],U[14],T[6+A*4],U[15],T[5+A*4]],['X','O',L40,L38,Q[7+A*4],Q[5+A*4],R[7+A*4],R[5+A*4],S[7+A*4],S[5+A*4],P[7+A*4],P[5+A*4],SG[7+A*4],SG[5+A*4],U[13],V[54],U[14],T[7+A*4],U[15],T[5+A*4]],['X','O',L40,L39,Q[7+A*4],Q[6+A*4],R[7+A*4],R[6+A*4],S[7+A*4],S[6+A*4],P[7+A*4],P[6+A*4],SG[7+A*4],SG[6+A*4],U[13],V[55],U[14],T[7+A*4],U[15],T[6+A*4]],
['X','O',L41,L42,Q[0+A*5],Q[1+A*5],R[0+A*5],R[1+A*5],S[0+A*5],S[1+A*5],P[0+A*5],P[1+A*5],SG[0+A*5],SG[1+A*5],U[0],V[0],U[14],T[0+A*5],U[15],T[1+A*5]],['X','O',L41,L43,Q[0+A*5],Q[2+A*5],R[0+A*5],R[2+A*5],S[0+A*5],S[2+A*5],P[0+A*5],P[2+A*5],SG[0+A*5],SG[2+A*5],U[0],V[1],U[14],T[0+A*5],U[15],T[2+A*5]],['X','O',L41,L44,Q[0+A*5],Q[3+A*5],R[0+A*5],R[3+A*5],S[0+A*5],S[3+A*5],P[0+A*5],P[3+A*5],SG[0+A*5],SG[3+A*5],U[0],V[2],U[14],T[0+A*5],U[15],T[3+A*5]],['X','O',L41,L45,Q[0+A*5],Q[4+A*5],R[0+A*5],R[4+A*5],S[0+A*5],S[4+A*5],P[0+A*5],P[4+A*5],SG[0+A*5],SG[4+A*5],U[0],V[3],U[14],T[0+A*5],U[15],T[4+A*5]],['X','O',L41,L46,Q[0+A*5],Q[5+A*5],R[0+A*5],R[5+A*5],S[0+A*5],S[5+A*5],P[0+A*5],P[5+A*5],SG[0+A*5],SG[5+A*5],U[1],V[4],U[14],T[0+A*5],U[15],T[5+A*5]],
['X','O',L41,L47,Q[0+A*5],Q[6+A*5],R[0+A*5],R[6+A*5],S[0+A*5],S[6+A*5],P[0+A*5],P[6+A*5],SG[0+A*5],SG[6+A*5],U[1],V[5],U[14],T[0+A*5],U[15],T[6+A*5]],['X','O',L41,L48,Q[0+A*5],Q[7+A*5],R[0+A*5],R[7+A*5],S[0+A*5],S[7+A*5],P[0+A*5],P[7+A*5],SG[0+A*5],SG[7+A*5],U[1],V[6],U[14],T[0+A*5],U[15],T[7+A*5]],['X','O',L42,L43,Q[1+A*5],Q[2+A*5],R[1+A*5],R[2+A*5],S[1+A*5],S[2+A*5],P[1+A*5],P[2+A*5],SG[1+A*5],SG[2+A*5],U[1],V[7],U[14],T[1+A*5],U[15],T[2+A*5]],['X','O',L42,L44,Q[1+A*5],Q[3+A*5],R[1+A*5],R[3+A*5],S[1+A*5],S[3+A*5],P[1+A*5],P[3+A*5],SG[1+A*5],SG[3+A*5],U[2],V[8],U[14],T[1+A*5],U[15],T[3+A*5]],['X','O',L42,L45,Q[1+A*5],Q[4+A*5],R[1+A*5],R[4+A*5],S[1+A*5],S[4+A*5],P[1+A*5],P[4+A*5],SG[1+A*5],SG[4+A*5],U[2],V[9],U[14],T[1+A*5],U[15],T[4+A*5]],
['X','O',L42,L46,Q[1+A*5],Q[5+A*5],R[1+A*5],R[5+A*5],S[1+A*5],S[5+A*5],P[1+A*5],P[5+A*5],SG[1+A*5],SG[5+A*5],U[2],V[10],U[14],T[1+A*5],U[15],T[5+A*5]],['X','O',L42,L47,Q[1+A*5],Q[6+A*5],R[1+A*5],R[6+A*5],S[1+A*5],S[6+A*5],P[1+A*5],P[6+A*5],SG[1+A*5],SG[6+A*5],U[2],V[11],U[14],T[1+A*5],U[15],T[6+A*5]],['X','O',L42,L48,Q[1+A*5],Q[7+A*5],R[1+A*5],R[7+A*5],S[1+A*5],S[7+A*5],P[1+A*5],P[7+A*5],SG[1+A*5],SG[7+A*5],U[3],V[12],U[14],T[1+A*5],U[15],T[7+A*5]],['X','O',L43,L44,Q[2+A*5],Q[3+A*5],R[2+A*5],R[3+A*5],S[2+A*5],S[3+A*5],P[2+A*5],P[3+A*5],SG[2+A*5],SG[3+A*5],U[3],V[13],U[14],T[2+A*5],U[15],T[3+A*5]],['X','O',L43,L45,Q[2+A*5],Q[4+A*5],R[2+A*5],R[4+A*5],S[2+A*5],S[4+A*5],P[2+A*5],P[4+A*5],SG[2+A*5],SG[4+A*5],U[3],V[14],U[14],T[2+A*5],U[15],T[4+A*5]],
['X','O',L43,L46,Q[2+A*5],Q[5+A*5],R[2+A*5],R[5+A*5],S[2+A*5],S[5+A*5],P[2+A*5],P[5+A*5],SG[2+A*5],SG[5+A*5],U[3],V[15],U[14],T[2+A*5],U[15],T[5+A*5]],['X','O',L43,L47,Q[2+A*5],Q[6+A*5],R[2+A*5],R[6+A*5],S[2+A*5],S[6+A*5],P[2+A*5],P[6+A*5],SG[2+A*5],SG[6+A*5],U[4],V[16],U[14],T[2+A*5],U[15],T[6+A*5]],['X','O',L43,L48,Q[2+A*5],Q[7+A*5],R[2+A*5],R[7+A*5],S[2+A*5],S[7+A*5],P[2+A*5],P[7+A*5],SG[2+A*5],SG[7+A*5],U[4],V[17],U[14],T[2+A*5],U[15],T[7+A*5]],['X','O',L44,L45,Q[3+A*5],Q[4+A*5],R[3+A*5],R[4+A*5],S[3+A*5],S[4+A*5],P[3+A*5],P[4+A*5],SG[3+A*5],SG[4+A*5],U[4],V[18],U[14],T[3+A*5],U[15],T[4+A*5]],['X','O',L44,L46,Q[3+A*5],Q[5+A*5],R[3+A*5],R[5+A*5],S[3+A*5],S[5+A*5],P[3+A*5],P[5+A*5],SG[3+A*5],SG[5+A*5],U[4],V[19],U[14],T[3+A*5],U[15],T[5+A*5]],
['X','O',L44,L47,Q[3+A*5],Q[6+A*5],R[3+A*5],R[6+A*5],S[3+A*5],S[6+A*5],P[3+A*5],P[6+A*5],SG[3+A*5],SG[6+A*5],U[5],V[20],U[14],T[3+A*5],U[15],T[6+A*5]],['X','O',L44,L48,Q[3+A*5],Q[7+A*5],R[3+A*5],R[7+A*5],S[3+A*5],S[7+A*5],P[3+A*5],P[7+A*5],SG[3+A*5],SG[7+A*5],U[5],V[21],U[14],T[3+A*5],U[15],T[7+A*5]],['X','O',L45,L46,Q[4+A*5],Q[5+A*5],R[4+A*5],R[5+A*5],S[4+A*5],S[5+A*5],P[4+A*5],P[5+A*5],SG[4+A*5],SG[5+A*5],U[5],V[22],U[14],T[4+A*5],U[15],T[5+A*5]],['X','O',L45,L47,Q[4+A*5],Q[6+A*5],R[4+A*5],R[6+A*5],S[4+A*5],S[6+A*5],P[4+A*5],P[6+A*5],SG[4+A*5],SG[6+A*5],U[5],V[23],U[14],T[4+A*5],U[15],T[6+A*5]],['X','O',L45,L48,Q[4+A*5],Q[7+A*5],R[4+A*5],R[7+A*5],S[4+A*5],S[7+A*5],P[4+A*5],P[7+A*5],SG[4+A*5],SG[7+A*5],U[6],V[24],U[14],T[4+A*5],U[15],T[7+A*5]],
['X','O',L46,L47,Q[5+A*5],Q[6+A*5],R[5+A*5],R[6+A*5],S[5+A*5],S[6+A*5],P[5+A*5],P[6+A*5],SG[5+A*5],SG[6+A*5],U[6],V[25],U[14],T[5+A*5],U[15],T[6+A*5]],['X','O',L46,L48,Q[5+A*5],Q[7+A*5],R[5+A*5],R[7+A*5],S[5+A*5],S[7+A*5],P[5+A*5],P[7+A*5],SG[5+A*5],SG[7+A*5],U[6],V[26],U[14],T[5+A*5],U[15],T[7+A*5]],['X','O',L47,L48,Q[6+A*5],Q[7+A*5],R[6+A*5],R[7+A*5],S[6+A*5],S[7+A*5],P[6+A*5],P[7+A*5],SG[6+A*5],SG[7+A*5],U[6],V[27],U[14],T[6+A*5],U[15],T[7+A*5]],['X','O',L42,L41,Q[1+A*5],Q[0+A*5],R[1+A*5],R[0+A*5],S[1+A*5],S[0+A*5],P[1+A*5],P[0+A*5],SG[1+A*5],SG[0+A*5],U[7],V[28],U[14],T[1+A*5],U[15],T[0+A*5]],['X','O',L43,L41,Q[2+A*5],Q[0+A*5],R[2+A*5],R[0+A*5],S[2+A*5],S[0+A*5],P[2+A*5],P[0+A*5],SG[2+A*5],SG[0+A*5],U[7],V[29],U[14],T[2+A*5],U[15],T[0+A*5]],
['X','O',L44,L41,Q[3+A*5],Q[0+A*5],R[3+A*5],R[0+A*5],S[3+A*5],S[0+A*5],P[3+A*5],P[0+A*5],SG[3+A*5],SG[0+A*5],U[7],V[30],U[14],T[3+A*5],U[15],T[0+A*5]],['X','O',L45,L41,Q[4+A*5],Q[0+A*5],R[4+A*5],R[0+A*5],S[4+A*5],S[0+A*5],P[4+A*5],P[0+A*5],SG[4+A*5],SG[0+A*5],U[7],V[31],U[14],T[4+A*5],U[15],T[0+A*5]],['X','O',L46,L41,Q[5+A*5],Q[0+A*5],R[5+A*5],R[0+A*5],S[5+A*5],S[0+A*5],P[5+A*5],P[0+A*5],SG[5+A*5],SG[0+A*5],U[8],V[32],U[14],T[5+A*5],U[15],T[0+A*5]],['X','O',L47,L41,Q[6+A*5],Q[0+A*5],R[6+A*5],R[0+A*5],S[6+A*5],S[0+A*5],P[6+A*5],P[0+A*5],SG[6+A*5],SG[0+A*5],U[8],V[33],U[14],T[6+A*5],U[15],T[0+A*5]],['X','O',L48,L41,Q[7+A*5],Q[0+A*5],R[7+A*5],R[0+A*5],S[7+A*5],S[0+A*5],P[7+A*5],P[0+A*5],SG[7+A*5],SG[0+A*5],U[8],V[34],U[14],T[7+A*5],U[15],T[0+A*5]],
['X','O',L43,L42,Q[2+A*5],Q[1+A*5],R[2+A*5],R[1+A*5],S[2+A*5],S[1+A*5],P[2+A*5],P[1+A*5],SG[2+A*5],SG[1+A*5],U[8],V[35],U[14],T[2+A*5],U[15],T[1+A*5]],['X','O',L44,L42,Q[3+A*5],Q[1+A*5],R[3+A*5],R[1+A*5],S[3+A*5],S[1+A*5],P[3+A*5],P[1+A*5],SG[3+A*5],SG[1+A*5],U[9],V[36],U[14],T[3+A*5],U[15],T[1+A*5]],['X','O',L45,L42,Q[4+A*5],Q[1+A*5],R[4+A*5],R[1+A*5],S[4+A*5],S[1+A*5],P[4+A*5],P[1+A*5],SG[4+A*5],SG[1+A*5],U[9],V[37],U[14],T[4+A*5],U[15],T[1+A*5]],['X','O',L46,L42,Q[5+A*5],Q[1+A*5],R[5+A*5],R[1+A*5],S[5+A*5],S[1+A*5],P[5+A*5],P[1+A*5],SG[5+A*5],SG[1+A*5],U[9],V[38],U[14],T[5+A*5],U[15],T[1+A*5]],['X','O',L47,L42,Q[6+A*5],Q[1+A*5],R[6+A*5],R[1+A*5],S[6+A*5],S[1+A*5],P[6+A*5],P[1+A*5],SG[6+A*5],SG[1+A*5],U[9],V[39],U[14],T[6+A*5],U[15],T[1+A*5]],
['X','O',L48,L42,Q[7+A*5],Q[1+A*5],R[7+A*5],R[1+A*5],S[7+A*5],S[1+A*5],P[7+A*5],P[1+A*5],SG[7+A*5],SG[1+A*5],U[10],V[40],U[14],T[7+A*5],U[15],T[1+A*5]],['X','O',L44,L43,Q[3+A*5],Q[2+A*5],R[3+A*5],R[2+A*5],S[3+A*5],S[2+A*5],P[3+A*5],P[2+A*5],SG[3+A*5],SG[2+A*5],U[10],V[41],U[14],T[3+A*5],U[15],T[2+A*5]],['X','O',L45,L43,Q[4+A*5],Q[2+A*5],R[4+A*5],R[2+A*5],S[4+A*5],S[2+A*5],P[4+A*5],P[2+A*5],SG[4+A*5],SG[2+A*5],U[10],V[42],U[14],T[4+A*5],U[15],T[2+A*5]],['X','O',L46,L43,Q[5+A*5],Q[2+A*5],R[5+A*5],R[2+A*5],S[5+A*5],S[2+A*5],P[5+A*5],P[2+A*5],SG[5+A*5],SG[2+A*5],U[10],V[43],U[14],T[5+A*5],U[15],T[2+A*5]],['X','O',L47,L43,Q[6+A*5],Q[2+A*5],R[6+A*5],R[2+A*5],S[6+A*5],S[2+A*5],P[6+A*5],P[2+A*5],SG[6+A*5],SG[2+A*5],U[11],V[44],U[14],T[6+A*5],U[15],T[2+A*5]],
['X','O',L48,L43,Q[7+A*5],Q[2+A*5],R[7+A*5],R[2+A*5],S[7+A*5],S[2+A*5],P[7+A*5],P[2+A*5],SG[7+A*5],SG[2+A*5],U[11],V[45],U[14],T[7+A*5],U[15],T[2+A*5]],['X','O',L45,L44,Q[4+A*5],Q[3+A*5],R[4+A*5],R[3+A*5],S[4+A*5],S[3+A*5],P[4+A*5],P[3+A*5],SG[4+A*5],SG[3+A*5],U[11],V[46],U[14],T[4+A*5],U[15],T[3+A*5]],['X','O',L46,L44,Q[5+A*5],Q[3+A*5],R[5+A*5],R[3+A*5],S[5+A*5],S[3+A*5],P[5+A*5],P[3+A*5],SG[5+A*5],SG[3+A*5],U[11],V[47],U[14],T[5+A*5],U[15],T[3+A*5]],['X','O',L47,L44,Q[6+A*5],Q[3+A*5],R[6+A*5],R[3+A*5],S[6+A*5],S[3+A*5],P[6+A*5],P[3+A*5],SG[6+A*5],SG[3+A*5],U[12],V[48],U[14],T[6+A*5],U[15],T[3+A*5]],['X','O',L48,L44,Q[7+A*5],Q[3+A*5],R[7+A*5],R[3+A*5],S[7+A*5],S[3+A*5],P[7+A*5],P[3+A*5],SG[7+A*5],SG[3+A*5],U[12],V[49],U[14],T[7+A*5],U[15],T[3+A*5]],
['X','O',L46,L45,Q[5+A*5],Q[4+A*5],R[5+A*5],R[4+A*5],S[5+A*5],S[4+A*5],P[5+A*5],P[4+A*5],SG[5+A*5],SG[4+A*5],U[12],V[50],U[14],T[5+A*5],U[15],T[4+A*5]],['X','O',L47,L45,Q[6+A*5],Q[4+A*5],R[6+A*5],R[4+A*5],S[6+A*5],S[4+A*5],P[6+A*5],P[4+A*5],SG[6+A*5],SG[4+A*5],U[12],V[51],U[14],T[6+A*5],U[15],T[4+A*5]],['X','O',L48,L45,Q[7+A*5],Q[4+A*5],R[7+A*5],R[4+A*5],S[7+A*5],S[4+A*5],P[7+A*5],P[4+A*5],SG[7+A*5],SG[4+A*5],U[13],V[52],U[14],T[7+A*5],U[15],T[4+A*5]],['X','O',L47,L46,Q[6+A*5],Q[5+A*5],R[6+A*5],R[5+A*5],S[6+A*5],S[5+A*5],P[6+A*5],P[5+A*5],SG[6+A*5],SG[5+A*5],U[13],V[53],U[14],T[6+A*5],U[15],T[5+A*5]],['X','O',L48,L46,Q[7+A*5],Q[5+A*5],R[7+A*5],R[5+A*5],S[7+A*5],S[5+A*5],P[7+A*5],P[5+A*5],SG[7+A*5],SG[5+A*5],U[13],V[54],U[14],T[7+A*5],U[15],T[5+A*5]],
['X','O',L48,L47,Q[7+A*5],Q[6+A*5],R[7+A*5],R[6+A*5],S[7+A*5],S[6+A*5],P[7+A*5],P[6+A*5],SG[7+A*5],SG[6+A*5],U[13],V[55],U[14],T[7+A*5],U[15],T[6+A*5]],['X','O',L49,L50,Q[0+A*6],Q[1+A*6],R[0+A*6],R[1+A*6],S[0+A*6],S[1+A*6],P[0+A*6],P[1+A*6],SG[0+A*6],SG[1+A*6],U[0],V[0],U[14],T[0+A*6],U[15],T[1+A*6]],['X','O',L49,L51,Q[0+A*6],Q[2+A*6],R[0+A*6],R[2+A*6],S[0+A*6],S[2+A*6],P[0+A*6],P[2+A*6],SG[0+A*6],SG[2+A*6],U[0],V[1],U[14],T[0+A*6],U[15],T[2+A*6]],['X','O',L49,L52,Q[0+A*6],Q[3+A*6],R[0+A*6],R[3+A*6],S[0+A*6],S[3+A*6],P[0+A*6],P[3+A*6],SG[0+A*6],SG[3+A*6],U[0],V[2],U[14],T[0+A*6],U[15],T[3+A*6]],['X','O',L49,L53,Q[0+A*6],Q[4+A*6],R[0+A*6],R[4+A*6],S[0+A*6],S[4+A*6],P[0+A*6],P[4+A*6],SG[0+A*6],SG[4+A*6],U[0],V[3],U[14],T[0+A*6],U[15],T[4+A*6]],
['X','O',L49,L54,Q[0+A*6],Q[5+A*6],R[0+A*6],R[5+A*6],S[0+A*6],S[5+A*6],P[0+A*6],P[5+A*6],SG[0+A*6],SG[5+A*6],U[1],V[4],U[14],T[0+A*6],U[15],T[5+A*6]],['X','O',L49,L55,Q[0+A*6],Q[6+A*6],R[0+A*6],R[6+A*6],S[0+A*6],S[6+A*6],P[0+A*6],P[6+A*6],SG[0+A*6],SG[6+A*6],U[1],V[5],U[14],T[0+A*6],U[15],T[6+A*6]],['X','O',L49,L56,Q[0+A*6],Q[7+A*6],R[0+A*6],R[7+A*6],S[0+A*6],S[7+A*6],P[0+A*6],P[7+A*6],SG[0+A*6],SG[7+A*6],U[1],V[6],U[14],T[0+A*6],U[15],T[7+A*6]],['X','O',L50,L51,Q[1+A*6],Q[2+A*6],R[1+A*6],R[2+A*6],S[1+A*6],S[2+A*6],P[1+A*6],P[2+A*6],SG[1+A*6],SG[2+A*6],U[1],V[7],U[14],T[1+A*6],U[15],T[2+A*6]],['X','O',L50,L52,Q[1+A*6],Q[3+A*6],R[1+A*6],R[3+A*6],S[1+A*6],S[3+A*6],P[1+A*6],P[3+A*6],SG[1+A*6],SG[3+A*6],U[2],V[8],U[14],T[1+A*6],U[15],T[3+A*6]],
['X','O',L50,L53,Q[1+A*6],Q[4+A*6],R[1+A*6],R[4+A*6],S[1+A*6],S[4+A*6],P[1+A*6],P[4+A*6],SG[1+A*6],SG[4+A*6],U[2],V[9],U[14],T[1+A*6],U[15],T[4+A*6]],['X','O',L50,L54,Q[1+A*6],Q[5+A*6],R[1+A*6],R[5+A*6],S[1+A*6],S[5+A*6],P[1+A*6],P[5+A*6],SG[1+A*6],SG[5+A*6],U[2],V[10],U[14],T[1+A*6],U[15],T[5+A*6]],['X','O',L50,L55,Q[1+A*6],Q[6+A*6],R[1+A*6],R[6+A*6],S[1+A*6],S[6+A*6],P[1+A*6],P[6+A*6],SG[1+A*6],SG[6+A*6],U[2],V[11],U[14],T[1+A*6],U[15],T[6+A*6]],['X','O',L50,L56,Q[1+A*6],Q[7+A*6],R[1+A*6],R[7+A*6],S[1+A*6],S[7+A*6],P[1+A*6],P[7+A*6],SG[1+A*6],SG[7+A*6],U[3],V[12],U[14],T[1+A*6],U[15],T[7+A*6]],['X','O',L51,L52,Q[2+A*6],Q[3+A*6],R[2+A*6],R[3+A*6],S[2+A*6],S[3+A*6],P[2+A*6],P[3+A*6],SG[2+A*6],SG[3+A*6],U[3],V[13],U[14],T[2+A*6],U[15],T[3+A*6]],
['X','O',L51,L53,Q[2+A*6],Q[4+A*6],R[2+A*6],R[4+A*6],S[2+A*6],S[4+A*6],P[2+A*6],P[4+A*6],SG[2+A*6],SG[4+A*6],U[3],V[14],U[14],T[2+A*6],U[15],T[4+A*6]],['X','O',L51,L54,Q[2+A*6],Q[5+A*6],R[2+A*6],R[5+A*6],S[2+A*6],S[5+A*6],P[2+A*6],P[5+A*6],SG[2+A*6],SG[5+A*6],U[3],V[15],U[14],T[2+A*6],U[15],T[5+A*6]],['X','O',L51,L55,Q[2+A*6],Q[6+A*6],R[2+A*6],R[6+A*6],S[2+A*6],S[6+A*6],P[2+A*6],P[6+A*6],SG[2+A*6],SG[6+A*6],U[4],V[16],U[14],T[2+A*6],U[15],T[6+A*6]],['X','O',L51,L56,Q[2+A*6],Q[7+A*6],R[2+A*6],R[7+A*6],S[2+A*6],S[7+A*6],P[2+A*6],P[7+A*6],SG[2+A*6],SG[7+A*6],U[4],V[17],U[14],T[2+A*6],U[15],T[7+A*6]],['X','O',L52,L53,Q[3+A*6],Q[4+A*6],R[3+A*6],R[4+A*6],S[3+A*6],S[4+A*6],P[3+A*6],P[4+A*6],SG[3+A*6],SG[4+A*6],U[4],V[18],U[14],T[3+A*6],U[15],T[4+A*6]],
['X','O',L52,L54,Q[3+A*6],Q[5+A*6],R[3+A*6],R[5+A*6],S[3+A*6],S[5+A*6],P[3+A*6],P[5+A*6],SG[3+A*6],SG[5+A*6],U[4],V[19],U[14],T[3+A*6],U[15],T[5+A*6]],['X','O',L52,L55,Q[3+A*6],Q[6+A*6],R[3+A*6],R[6+A*6],S[3+A*6],S[6+A*6],P[3+A*6],P[6+A*6],SG[3+A*6],SG[6+A*6],U[5],V[20],U[14],T[3+A*6],U[15],T[6+A*6]],['X','O',L52,L56,Q[3+A*6],Q[7+A*6],R[3+A*6],R[7+A*6],S[3+A*6],S[7+A*6],P[3+A*6],P[7+A*6],SG[3+A*6],SG[7+A*6],U[5],V[21],U[14],T[3+A*6],U[15],T[7+A*6]],['X','O',L53,L54,Q[4+A*6],Q[5+A*6],R[4+A*6],R[5+A*6],S[4+A*6],S[5+A*6],P[4+A*6],P[5+A*6],SG[4+A*6],SG[5+A*6],U[5],V[22],U[14],T[4+A*6],U[15],T[5+A*6]],['X','O',L53,L55,Q[4+A*6],Q[6+A*6],R[4+A*6],R[6+A*6],S[4+A*6],S[6+A*6],P[4+A*6],P[6+A*6],SG[4+A*6],SG[6+A*6],U[5],V[23],U[14],T[4+A*6],U[15],T[6+A*6]],
['X','O',L53,L56,Q[4+A*6],Q[7+A*6],R[4+A*6],R[7+A*6],S[4+A*6],S[7+A*6],P[4+A*6],P[7+A*6],SG[4+A*6],SG[7+A*6],U[6],V[24],U[14],T[4+A*6],U[15],T[7+A*6]],['X','O',L54,L55,Q[5+A*6],Q[6+A*6],R[5+A*6],R[6+A*6],S[5+A*6],S[6+A*6],P[5+A*6],P[6+A*6],SG[5+A*6],SG[6+A*6],U[6],V[25],U[14],T[5+A*6],U[15],T[6+A*6]],['X','O',L54,L56,Q[5+A*6],Q[7+A*6],R[5+A*6],R[7+A*6],S[5+A*6],S[7+A*6],P[5+A*6],P[7+A*6],SG[5+A*6],SG[7+A*6],U[6],V[26],U[14],T[5+A*6],U[15],T[7+A*6]],['X','O',L55,L56,Q[6+A*6],Q[7+A*6],R[6+A*6],R[7+A*6],S[6+A*6],S[7+A*6],P[6+A*6],P[7+A*6],SG[6+A*6],SG[7+A*6],U[6],V[27],U[14],T[6+A*6],U[15],T[7+A*6]],['X','O',L50,L49,Q[1+A*6],Q[0+A*6],R[1+A*6],R[0+A*6],S[1+A*6],S[0+A*6],P[1+A*6],P[0+A*6],SG[1+A*6],SG[0+A*6],U[7],V[28],U[14],T[1+A*6],U[15],T[0+A*6]],
['X','O',L51,L49,Q[2+A*6],Q[0+A*6],R[2+A*6],R[0+A*6],S[2+A*6],S[0+A*6],P[2+A*6],P[0+A*6],SG[2+A*6],SG[0+A*6],U[7],V[29],U[14],T[2+A*6],U[15],T[0+A*6]],['X','O',L52,L49,Q[3+A*6],Q[0+A*6],R[3+A*6],R[0+A*6],S[3+A*6],S[0+A*6],P[3+A*6],P[0+A*6],SG[3+A*6],SG[0+A*6],U[7],V[30],U[14],T[3+A*6],U[15],T[0+A*6]],['X','O',L53,L49,Q[4+A*6],Q[0+A*6],R[4+A*6],R[0+A*6],S[4+A*6],S[0+A*6],P[4+A*6],P[0+A*6],SG[4+A*6],SG[0+A*6],U[7],V[31],U[14],T[4+A*6],U[15],T[0+A*6]],['X','O',L54,L49,Q[5+A*6],Q[0+A*6],R[5+A*6],R[0+A*6],S[5+A*6],S[0+A*6],P[5+A*6],P[0+A*6],SG[5+A*6],SG[0+A*6],U[8],V[32],U[14],T[5+A*6],U[15],T[0+A*6]],['X','O',L55,L49,Q[6+A*6],Q[0+A*6],R[6+A*6],R[0+A*6],S[6+A*6],S[0+A*6],P[6+A*6],P[0+A*6],SG[6+A*6],SG[0+A*6],U[8],V[33],U[14],T[6+A*6],U[15],T[0+A*6]],
['X','O',L56,L49,Q[7+A*6],Q[0+A*6],R[7+A*6],R[0+A*6],S[7+A*6],S[0+A*6],P[7+A*6],P[0+A*6],SG[7+A*6],SG[0+A*6],U[8],V[34],U[14],T[7+A*6],U[15],T[0+A*6]],['X','O',L51,L50,Q[2+A*6],Q[1+A*6],R[2+A*6],R[1+A*6],S[2+A*6],S[1+A*6],P[2+A*6],P[1+A*6],SG[2+A*6],SG[1+A*6],U[8],V[35],U[14],T[2+A*6],U[15],T[1+A*6]],['X','O',L52,L50,Q[3+A*6],Q[1+A*6],R[3+A*6],R[1+A*6],S[3+A*6],S[1+A*6],P[3+A*6],P[1+A*6],SG[3+A*6],SG[1+A*6],U[9],V[36],U[14],T[3+A*6],U[15],T[1+A*6]],['X','O',L53,L50,Q[4+A*6],Q[1+A*6],R[4+A*6],R[1+A*6],S[4+A*6],S[1+A*6],P[4+A*6],P[1+A*6],SG[4+A*6],SG[1+A*6],U[9],V[37],U[14],T[4+A*6],U[15],T[1+A*6]],['X','O',L54,L50,Q[5+A*6],Q[1+A*6],R[5+A*6],R[1+A*6],S[5+A*6],S[1+A*6],P[5+A*6],P[1+A*6],SG[5+A*6],SG[1+A*6],U[9],V[38],U[14],T[5+A*6],U[15],T[1+A*6]],
['X','O',L55,L50,Q[6+A*6],Q[1+A*6],R[6+A*6],R[1+A*6],S[6+A*6],S[1+A*6],P[6+A*6],P[1+A*6],SG[6+A*6],SG[1+A*6],U[9],V[39],U[14],T[6+A*6],U[15],T[1+A*6]],['X','O',L56,L50,Q[7+A*6],Q[1+A*6],R[7+A*6],R[1+A*6],S[7+A*6],S[1+A*6],P[7+A*6],P[1+A*6],SG[7+A*6],SG[1+A*6],U[10],V[40],U[14],T[7+A*6],U[15],T[1+A*6]],['X','O',L52,L51,Q[3+A*6],Q[2+A*6],R[3+A*6],R[2+A*6],S[3+A*6],S[2+A*6],P[3+A*6],P[2+A*6],SG[3+A*6],SG[2+A*6],U[10],V[41],U[14],T[3+A*6],U[15],T[2+A*6]],['X','O',L53,L51,Q[4+A*6],Q[2+A*6],R[4+A*6],R[2+A*6],S[4+A*6],S[2+A*6],P[4+A*6],P[2+A*6],SG[4+A*6],SG[2+A*6],U[10],V[42],U[14],T[4+A*6],U[15],T[2+A*6]],['X','O',L54,L51,Q[5+A*6],Q[2+A*6],R[5+A*6],R[2+A*6],S[5+A*6],S[2+A*6],P[5+A*6],P[2+A*6],SG[5+A*6],SG[2+A*6],U[10],V[43],U[14],T[5+A*6],U[15],T[2+A*6]],
['X','O',L55,L51,Q[6+A*6],Q[2+A*6],R[6+A*6],R[2+A*6],S[6+A*6],S[2+A*6],P[6+A*6],P[2+A*6],SG[6+A*6],SG[2+A*6],U[11],V[44],U[14],T[6+A*6],U[15],T[2+A*6]],['X','O',L56,L51,Q[7+A*6],Q[2+A*6],R[7+A*6],R[2+A*6],S[7+A*6],S[2+A*6],P[7+A*6],P[2+A*6],SG[7+A*6],SG[2+A*6],U[11],V[45],U[14],T[7+A*6],U[15],T[2+A*6]],['X','O',L53,L52,Q[4+A*6],Q[3+A*6],R[4+A*6],R[3+A*6],S[4+A*6],S[3+A*6],P[4+A*6],P[3+A*6],SG[4+A*6],SG[3+A*6],U[11],V[46],U[14],T[4+A*6],U[15],T[3+A*6]],['X','O',L54,L52,Q[5+A*6],Q[3+A*6],R[5+A*6],R[3+A*6],S[5+A*6],S[3+A*6],P[5+A*6],P[3+A*6],SG[5+A*6],SG[3+A*6],U[11],V[47],U[14],T[5+A*6],U[15],T[3+A*6]],['X','O',L55,L52,Q[6+A*6],Q[3+A*6],R[6+A*6],R[3+A*6],S[6+A*6],S[3+A*6],P[6+A*6],P[3+A*6],SG[6+A*6],SG[3+A*6],U[12],V[48],U[14],T[6+A*6],U[15],T[3+A*6]],
['X','O',L56,L52,Q[7+A*6],Q[3+A*6],R[7+A*6],R[3+A*6],S[7+A*6],S[3+A*6],P[7+A*6],P[3+A*6],SG[7+A*6],SG[3+A*6],U[12],V[49],U[14],T[7+A*6],U[15],T[3+A*6]],['X','O',L54,L53,Q[5+A*6],Q[4+A*6],R[5+A*6],R[4+A*6],S[5+A*6],S[4+A*6],P[5+A*6],P[4+A*6],SG[5+A*6],SG[4+A*6],U[12],V[50],U[14],T[5+A*6],U[15],T[4+A*6]],['X','O',L55,L53,Q[6+A*6],Q[4+A*6],R[6+A*6],R[4+A*6],S[6+A*6],S[4+A*6],P[6+A*6],P[4+A*6],SG[6+A*6],SG[4+A*6],U[12],V[51],U[14],T[6+A*6],U[15],T[4+A*6]],['X','O',L56,L53,Q[7+A*6],Q[4+A*6],R[7+A*6],R[4+A*6],S[7+A*6],S[4+A*6],P[7+A*6],P[4+A*6],SG[7+A*6],SG[4+A*6],U[13],V[52],U[14],T[7+A*6],U[15],T[4+A*6]],['X','O',L55,L54,Q[6+A*6],Q[5+A*6],R[6+A*6],R[5+A*6],S[6+A*6],S[5+A*6],P[6+A*6],P[5+A*6],SG[6+A*6],SG[5+A*6],U[13],V[53],U[14],T[6+A*6],U[15],T[5+A*6]],
['X','O',L56,L54,Q[7+A*6],Q[5+A*6],R[7+A*6],R[5+A*6],S[7+A*6],S[5+A*6],P[7+A*6],P[5+A*6],SG[7+A*6],SG[5+A*6],U[13],V[54],U[14],T[7+A*6],U[15],T[5+A*6]],['X','O',L56,L55,Q[7+A*6],Q[6+A*6],R[7+A*6],R[6+A*6],S[7+A*6],S[6+A*6],P[7+A*6],P[6+A*6],SG[7+A*6],SG[6+A*6],U[13],V[55],U[14],T[7+A*6],U[15],T[6+A*6]],['X','O',L57,L58,Q[0+A*7],Q[1+A*7],R[0+A*7],R[1+A*7],S[0+A*7],S[1+A*7],P[0+A*7],P[1+A*7],SG[0+A*7],SG[1+A*7],U[0],V[0],U[14],T[0+A*7],U[15],T[1+A*7]],['X','O',L57,L59,Q[0+A*7],Q[2+A*7],R[0+A*7],R[2+A*7],S[0+A*7],S[2+A*7],P[0+A*7],P[2+A*7],SG[0+A*7],SG[2+A*7],U[0],V[1],U[14],T[0+A*7],U[15],T[2+A*7]],['X','O',L57,L60,Q[0+A*7],Q[3+A*7],R[0+A*7],R[3+A*7],S[0+A*7],S[3+A*7],P[0+A*7],P[3+A*7],SG[0+A*7],SG[3+A*7],U[0],V[2],U[14],T[0+A*7],U[15],T[3+A*7]],
['X','O',L57,L61,Q[0+A*7],Q[4+A*7],R[0+A*7],R[4+A*7],S[0+A*7],S[4+A*7],P[0+A*7],P[4+A*7],SG[0+A*7],SG[4+A*7],U[0],V[3],U[14],T[0+A*7],U[15],T[4+A*7]],['X','O',L57,L62,Q[0+A*7],Q[5+A*7],R[0+A*7],R[5+A*7],S[0+A*7],S[5+A*7],P[0+A*7],P[5+A*7],SG[0+A*7],SG[5+A*7],U[1],V[4],U[14],T[0+A*7],U[15],T[5+A*7]],['X','O',L57,L63,Q[0+A*7],Q[6+A*7],R[0+A*7],R[6+A*7],S[0+A*7],S[6+A*7],P[0+A*7],P[6+A*7],SG[0+A*7],SG[6+A*7],U[1],V[5],U[14],T[0+A*7],U[15],T[6+A*7]],['X','O',L57,L64,Q[0+A*7],Q[7+A*7],R[0+A*7],R[7+A*7],S[0+A*7],S[7+A*7],P[0+A*7],P[7+A*7],SG[0+A*7],SG[7+A*7],U[1],V[6],U[14],T[0+A*7],U[15],T[7+A*7]],['X','O',L58,L59,Q[1+A*7],Q[2+A*7],R[1+A*7],R[2+A*7],S[1+A*7],S[2+A*7],P[1+A*7],P[2+A*7],SG[1+A*7],SG[2+A*7],U[1],V[7],U[14],T[1+A*7],U[15],T[2+A*7]],
['X','O',L58,L60,Q[1+A*7],Q[3+A*7],R[1+A*7],R[3+A*7],S[1+A*7],S[3+A*7],P[1+A*7],P[3+A*7],SG[1+A*7],SG[3+A*7],U[2],V[8],U[14],T[1+A*7],U[15],T[3+A*7]],['X','O',L58,L61,Q[1+A*7],Q[4+A*7],R[1+A*7],R[4+A*7],S[1+A*7],S[4+A*7],P[1+A*7],P[4+A*7],SG[1+A*7],SG[4+A*7],U[2],V[9],U[14],T[1+A*7],U[15],T[4+A*7]],['X','O',L58,L62,Q[1+A*7],Q[5+A*7],R[1+A*7],R[5+A*7],S[1+A*7],S[5+A*7],P[1+A*7],P[5+A*7],SG[1+A*7],SG[5+A*7],U[2],V[10],U[14],T[1+A*7],U[15],T[5+A*7]],['X','O',L58,L63,Q[1+A*7],Q[6+A*7],R[1+A*7],R[6+A*7],S[1+A*7],S[6+A*7],P[1+A*7],P[6+A*7],SG[1+A*7],SG[6+A*7],U[2],V[11],U[14],T[1+A*7],U[15],T[6+A*7]],['X','O',L58,L64,Q[1+A*7],Q[7+A*7],R[1+A*7],R[7+A*7],S[1+A*7],S[7+A*7],P[1+A*7],P[7+A*7],SG[1+A*7],SG[7+A*7],U[3],V[12],U[14],T[1+A*7],U[15],T[7+A*7]],
['X','O',L59,L60,Q[2+A*7],Q[3+A*7],R[2+A*7],R[3+A*7],S[2+A*7],S[3+A*7],P[2+A*7],P[3+A*7],SG[2+A*7],SG[3+A*7],U[3],V[13],U[14],T[2+A*7],U[15],T[3+A*7]],['X','O',L59,L61,Q[2+A*7],Q[4+A*7],R[2+A*7],R[4+A*7],S[2+A*7],S[4+A*7],P[2+A*7],P[4+A*7],SG[2+A*7],SG[4+A*7],U[3],V[14],U[14],T[2+A*7],U[15],T[4+A*7]],['X','O',L59,L62,Q[2+A*7],Q[5+A*7],R[2+A*7],R[5+A*7],S[2+A*7],S[5+A*7],P[2+A*7],P[5+A*7],SG[2+A*7],SG[5+A*7],U[3],V[15],U[14],T[2+A*7],U[15],T[5+A*7]],['X','O',L59,L63,Q[2+A*7],Q[6+A*7],R[2+A*7],R[6+A*7],S[2+A*7],S[6+A*7],P[2+A*7],P[6+A*7],SG[2+A*7],SG[6+A*7],U[4],V[16],U[14],T[2+A*7],U[15],T[6+A*7]],['X','O',L59,L64,Q[2+A*7],Q[7+A*7],R[2+A*7],R[7+A*7],S[2+A*7],S[7+A*7],P[2+A*7],P[7+A*7],SG[2+A*7],SG[7+A*7],U[4],V[17],U[14],T[2+A*7],U[15],T[7+A*7]],
['X','O',L60,L61,Q[3+A*7],Q[4+A*7],R[3+A*7],R[4+A*7],S[3+A*7],S[4+A*7],P[3+A*7],P[4+A*7],SG[3+A*7],SG[4+A*7],U[4],V[18],U[14],T[3+A*7],U[15],T[4+A*7]],['X','O',L60,L62,Q[3+A*7],Q[5+A*7],R[3+A*7],R[5+A*7],S[3+A*7],S[5+A*7],P[3+A*7],P[5+A*7],SG[3+A*7],SG[5+A*7],U[4],V[19],U[14],T[3+A*7],U[15],T[5+A*7]],['X','O',L60,L63,Q[3+A*7],Q[6+A*7],R[3+A*7],R[6+A*7],S[3+A*7],S[6+A*7],P[3+A*7],P[6+A*7],SG[3+A*7],SG[6+A*7],U[5],V[20],U[14],T[3+A*7],U[15],T[6+A*7]],['X','O',L60,L64,Q[3+A*7],Q[7+A*7],R[3+A*7],R[7+A*7],S[3+A*7],S[7+A*7],P[3+A*7],P[7+A*7],SG[3+A*7],SG[7+A*7],U[5],V[21],U[14],T[3+A*7],U[15],T[7+A*7]],['X','O',L61,L62,Q[4+A*7],Q[5+A*7],R[4+A*7],R[5+A*7],S[4+A*7],S[5+A*7],P[4+A*7],P[5+A*7],SG[4+A*7],SG[5+A*7],U[5],V[22],U[14],T[4+A*7],U[15],T[5+A*7]],
['X','O',L61,L63,Q[4+A*7],Q[6+A*7],R[4+A*7],R[6+A*7],S[4+A*7],S[6+A*7],P[4+A*7],P[6+A*7],SG[4+A*7],SG[6+A*7],U[5],V[23],U[14],T[4+A*7],U[15],T[6+A*7]],['X','O',L61,L64,Q[4+A*7],Q[7+A*7],R[4+A*7],R[7+A*7],S[4+A*7],S[7+A*7],P[4+A*7],P[7+A*7],SG[4+A*7],SG[7+A*7],U[6],V[24],U[14],T[4+A*7],U[15],T[7+A*7]],['X','O',L62,L63,Q[5+A*7],Q[6+A*7],R[5+A*7],R[6+A*7],S[5+A*7],S[6+A*7],P[5+A*7],P[6+A*7],SG[5+A*7],SG[6+A*7],U[6],V[25],U[14],T[5+A*7],U[15],T[6+A*7]],['X','O',L62,L64,Q[5+A*7],Q[7+A*7],R[5+A*7],R[7+A*7],S[5+A*7],S[7+A*7],P[5+A*7],P[7+A*7],SG[5+A*7],SG[7+A*7],U[6],V[26],U[14],T[5+A*7],U[15],T[7+A*7]],['X','O',L63,L64,Q[6+A*7],Q[7+A*7],R[6+A*7],R[7+A*7],S[6+A*7],S[7+A*7],P[6+A*7],P[7+A*7],SG[6+A*7],SG[7+A*7],U[6],V[27],U[14],T[6+A*7],U[15],T[7+A*7]],
['X','O',L58,L57,Q[1+A*7],Q[0+A*7],R[1+A*7],R[0+A*7],S[1+A*7],S[0+A*7],P[1+A*7],P[0+A*7],SG[1+A*7],SG[0+A*7],U[7],V[28],U[14],T[1+A*7],U[15],T[0+A*7]],['X','O',L59,L57,Q[2+A*7],Q[0+A*7],R[2+A*7],R[0+A*7],S[2+A*7],S[0+A*7],P[2+A*7],P[0+A*7],SG[2+A*7],SG[0+A*7],U[7],V[29],U[14],T[2+A*7],U[15],T[0+A*7]],['X','O',L60,L57,Q[3+A*7],Q[0+A*7],R[3+A*7],R[0+A*7],S[3+A*7],S[0+A*7],P[3+A*7],P[0+A*7],SG[3+A*7],SG[0+A*7],U[7],V[30],U[14],T[3+A*7],U[15],T[0+A*7]],['X','O',L61,L57,Q[4+A*7],Q[0+A*7],R[4+A*7],R[0+A*7],S[4+A*7],S[0+A*7],P[4+A*7],P[0+A*7],SG[4+A*7],SG[0+A*7],U[7],V[31],U[14],T[4+A*7],U[15],T[0+A*7]],['X','O',L62,L57,Q[5+A*7],Q[0+A*7],R[5+A*7],R[0+A*7],S[5+A*7],S[0+A*7],P[5+A*7],P[0+A*7],SG[5+A*7],SG[0+A*7],U[8],V[32],U[14],T[5+A*7],U[15],T[0+A*7]],
['X','O',L63,L57,Q[6+A*7],Q[0+A*7],R[6+A*7],R[0+A*7],S[6+A*7],S[0+A*7],P[6+A*7],P[0+A*7],SG[6+A*7],SG[0+A*7],U[8],V[33],U[14],T[6+A*7],U[15],T[0+A*7]],['X','O',L64,L57,Q[7+A*7],Q[0+A*7],R[7+A*7],R[0+A*7],S[7+A*7],S[0+A*7],P[7+A*7],P[0+A*7],SG[7+A*7],SG[0+A*7],U[8],V[34],U[14],T[7+A*7],U[15],T[0+A*7]],['X','O',L59,L58,Q[2+A*7],Q[1+A*7],R[2+A*7],R[1+A*7],S[2+A*7],S[1+A*7],P[2+A*7],P[1+A*7],SG[2+A*7],SG[1+A*7],U[8],V[35],U[14],T[2+A*7],U[15],T[1+A*7]],['X','O',L60,L58,Q[3+A*7],Q[1+A*7],R[3+A*7],R[1+A*7],S[3+A*7],S[1+A*7],P[3+A*7],P[1+A*7],SG[3+A*7],SG[1+A*7],U[9],V[36],U[14],T[3+A*7],U[15],T[1+A*7]],['X','O',L61,L58,Q[4+A*7],Q[1+A*7],R[4+A*7],R[1+A*7],S[4+A*7],S[1+A*7],P[4+A*7],P[1+A*7],SG[4+A*7],SG[1+A*7],U[9],V[37],U[14],T[4+A*7],U[15],T[1+A*7]],
['X','O',L62,L58,Q[5+A*7],Q[1+A*7],R[5+A*7],R[1+A*7],S[5+A*7],S[1+A*7],P[5+A*7],P[1+A*7],SG[5+A*7],SG[1+A*7],U[9],V[38],U[14],T[5+A*7],U[15],T[1+A*7]],['X','O',L63,L58,Q[6+A*7],Q[1+A*7],R[6+A*7],R[1+A*7],S[6+A*7],S[1+A*7],P[6+A*7],P[1+A*7],SG[6+A*7],SG[1+A*7],U[9],V[39],U[14],T[6+A*7],U[15],T[1+A*7]],['X','O',L64,L58,Q[7+A*7],Q[1+A*7],R[7+A*7],R[1+A*7],S[7+A*7],S[1+A*7],P[7+A*7],P[1+A*7],SG[7+A*7],SG[1+A*7],U[10],V[40],U[14],T[7+A*7],U[15],T[1+A*7]],['X','O',L60,L59,Q[3+A*7],Q[2+A*7],R[3+A*7],R[2+A*7],S[3+A*7],S[2+A*7],P[3+A*7],P[2+A*7],SG[3+A*7],SG[2+A*7],U[10],V[41],U[14],T[3+A*7],U[15],T[2+A*7]],['X','O',L61,L59,Q[4+A*7],Q[2+A*7],R[4+A*7],R[2+A*7],S[4+A*7],S[2+A*7],P[4+A*7],P[2+A*7],SG[4+A*7],SG[2+A*7],U[10],V[42],U[14],T[4+A*7],U[15],T[2+A*7]],
['X','O',L62,L59,Q[5+A*7],Q[2+A*7],R[5+A*7],R[2+A*7],S[5+A*7],S[2+A*7],P[5+A*7],P[2+A*7],SG[5+A*7],SG[2+A*7],U[10],V[43],U[14],T[5+A*7],U[15],T[2+A*7]],['X','O',L63,L59,Q[6+A*7],Q[2+A*7],R[6+A*7],R[2+A*7],S[6+A*7],S[2+A*7],P[6+A*7],P[2+A*7],SG[6+A*7],SG[2+A*7],U[11],V[44],U[14],T[6+A*7],U[15],T[2+A*7]],['X','O',L64,L59,Q[7+A*7],Q[2+A*7],R[7+A*7],R[2+A*7],S[7+A*7],S[2+A*7],P[7+A*7],P[2+A*7],SG[7+A*7],SG[2+A*7],U[11],V[45],U[14],T[7+A*7],U[15],T[2+A*7]],['X','O',L61,L60,Q[4+A*7],Q[3+A*7],R[4+A*7],R[3+A*7],S[4+A*7],S[3+A*7],P[4+A*7],P[3+A*7],SG[4+A*7],SG[3+A*7],U[11],V[46],U[14],T[4+A*7],U[15],T[3+A*7]],['X','O',L62,L60,Q[5+A*7],Q[3+A*7],R[5+A*7],R[3+A*7],S[5+A*7],S[3+A*7],P[5+A*7],P[3+A*7],SG[5+A*7],SG[3+A*7],U[11],V[47],U[14],T[5+A*7],U[15],T[3+A*7]],
['X','O',L63,L60,Q[6+A*7],Q[3+A*7],R[6+A*7],R[3+A*7],S[6+A*7],S[3+A*7],P[6+A*7],P[3+A*7],SG[6+A*7],SG[3+A*7],U[12],V[48],U[14],T[6+A*7],U[15],T[3+A*7]],['X','O',L64,L60,Q[7+A*7],Q[3+A*7],R[7+A*7],R[3+A*7],S[7+A*7],S[3+A*7],P[7+A*7],P[3+A*7],SG[7+A*7],SG[3+A*7],U[12],V[49],U[14],T[7+A*7],U[15],T[3+A*7]],['X','O',L62,L61,Q[5+A*7],Q[4+A*7],R[5+A*7],R[4+A*7],S[5+A*7],S[4+A*7],P[5+A*7],P[4+A*7],SG[5+A*7],SG[4+A*7],U[12],V[50],U[14],T[5+A*7],U[15],T[4+A*7]],['X','O',L63,L61,Q[6+A*7],Q[4+A*7],R[6+A*7],R[4+A*7],S[6+A*7],S[4+A*7],P[6+A*7],P[4+A*7],SG[6+A*7],SG[4+A*7],U[12],V[51],U[14],T[6+A*7],U[15],T[4+A*7]],['X','O',L64,L61,Q[7+A*7],Q[4+A*7],R[7+A*7],R[4+A*7],S[7+A*7],S[4+A*7],P[7+A*7],P[4+A*7],SG[7+A*7],SG[4+A*7],U[13],V[52],U[14],T[7+A*7],U[15],T[4+A*7]],
['X','O',L63,L62,Q[6+A*7],Q[5+A*7],R[6+A*7],R[5+A*7],S[6+A*7],S[5+A*7],P[6+A*7],P[5+A*7],SG[6+A*7],SG[5+A*7],U[13],V[53],U[14],T[6+A*7],U[15],T[5+A*7]],['X','O',L64,L62,Q[7+A*7],Q[5+A*7],R[7+A*7],R[5+A*7],S[7+A*7],S[5+A*7],P[7+A*7],P[5+A*7],SG[7+A*7],SG[5+A*7],U[13],V[54],U[14],T[7+A*7],U[15],T[5+A*7]],['X','O',L64,L63,Q[7+A*7],Q[6+A*7],R[7+A*7],R[6+A*7],S[7+A*7],S[6+A*7],P[7+A*7],P[6+A*7],SG[7+A*7],SG[6+A*7],U[13],V[55],U[14],T[7+A*7],U[15],T[6+A*7]]]

def rodada_princ_penaltis(Y):
    def executar_cobranca(jogador, rodada, lista):
        chute = random.choice(lista)
        print(f"{jogador[rodada]} {chute}")
        return chute  
    print(Y[14])
    print(Y[15])
    print(Y[16], Y[17])
    print(Y[18], Y[19])
    lista = [Y[0], Y[1]]
    lista_PT1, lista_PT2 = [], []
    for rodada in range(5):  
        print(f"Rodada {rodada + 1}")
        escolha = input("Digite 1 para próxima rodada de pênaltis ou 0 para sair do jogo:")
        if escolha == 0:
            print("Fim do jogo!")
            return
        elif escolha == "1":
            chute_t1 = executar_cobranca(Y[2], rodada, lista)
            chute_t2 = executar_cobranca(Y[3], rodada, lista)
            lista_PT1.append(chute_t1)
            lista_PT2.append(chute_t2)
        else:
            print("Entrada inválida. Portanto perdeu essa cobrança de pênaltis!!!")
            chute_t1 = 'X'
            print(Y[2][rodada],chute_t1)
            chute_t2 = executar_cobranca(Y[3], rodada, lista)
            lista_PT1.append(chute_t1)
            lista_PT2.append(chute_t2)
    def contar_gols(lista_chutes):
        return sum(1 for chute in lista_chutes if chute != 'X')
    gols_T1 = contar_gols(lista_PT1)
    gols_T2 = contar_gols(lista_PT2)
    print(f"{Y[4]} {gols_T1}")
    print(f"{Y[5]} {gols_T2}")
    if gols_T1 > gols_T2:
        print(Y[6])
        Y[10] += 3
    elif gols_T1 < gols_T2:
        print(Y[7])
        Y[11] += 3
    else:
        print("Agora é disputa nas alternadas, até alguém errar!")
        rodada = 5
        while gols_T1 == gols_T2:
            print(f"Rodada Alternada {rodada + 1}")
            chute_t1 = executar_cobranca(Y[2], rodada, lista)
            chute_t2 = executar_cobranca(Y[3], rodada, lista)
            lista_PT1.append(chute_t1)
            lista_PT2.append(chute_t2)
            gols_T1 = contar_gols(lista_PT1)
            gols_T2 = contar_gols(lista_PT2)
            rodada += 1
        if gols_T1 > gols_T2:
            print(Y[6])
            Y[10] += 3
        elif gols_T1 < gols_T2:
            print(Y[7])
            Y[11] += 3
    Y[12] += gols_T1
    Y[13] += gols_T2
    print(f"Placar final: {Y[4]} {gols_T1}")
    print(f"Placar final: {Y[5]} {gols_T2}")
    return [Y[8], Y[10], Y[9], Y[11], Y[12], Y[13]]


def rodada_princ_pênaltis_PC(Y):
    def contar_gols(lista_chutes):
        return sum(1 for chute in lista_chutes if chute != 'X')
    def imprimir_resultados(lista_PT1, lista_PT2):
        print(f"{Y[2][20]}:", lista_PT1)
        print(f"{Y[3][20]}:", lista_PT2)
        gols_T1 = contar_gols(lista_PT1)
        gols_T2 = contar_gols(lista_PT2)
        print(f"{Y[4]}: {gols_T1}")
        print(f"{Y[5]}: {gols_T2}")
        return gols_T1, gols_T2
    print(Y[14])
    print(Y[15])
    print(Y[16], Y[17])
    print(Y[18], Y[19])
    lista = [Y[0], Y[1]]
    lista_PT1, lista_PT2 = [], []
    for rodada in range(5):
        lista_PT1.append(random.choice(lista))
        lista_PT2.append(random.choice(lista))
    gols_T1, gols_T2 = imprimir_resultados(lista_PT1, lista_PT2)
    if gols_T1 > gols_T2:
        print(Y[6])  
        Y[10] += 3
    elif gols_T1 < gols_T2:
        print(Y[7])  
        Y[11] += 3
    else:
        print("Agora é disputa nas alternadas, até alguém errar!")
        rodada = 5
        while gols_T1 == gols_T2:
            print(f"Rodada Alternada {rodada + 1}")
            lista_PT1.append(random.choice(lista))
            lista_PT2.append(random.choice(lista))
            gols_T1, gols_T2 = imprimir_resultados(lista_PT1, lista_PT2)
            rodada += 1
        if gols_T1 > gols_T2:
            print(Y[6]) 
            Y[10] += 3
        elif gols_T1 < gols_T2:
            print(Y[7])  
            Y[11] += 3
    Y[12] += contar_gols(lista_PT1)
    Y[13] += contar_gols(lista_PT2)
    return [Y[8], Y[10], Y[9], Y[11], Y[12], Y[13]]


def rodada_desempate_pênaltis(Y):
    lista = [Y[0], Y[1]]
    placar_t1 = 0
    placar_t2 = 0
    rodada = 0
    while True:
        p_t1 = random.choice(lista)
        p_t2 = random.choice(lista)
        print(f"{Y[2][rodada]} {p_t1}")
        print(f"{Y[3][rodada]} {p_t2}")
        if p_t1 != "X":
            placar_t1 += 1
        if p_t2 != "X":
            placar_t2 += 1
        print(f"{Y[4]}: {placar_t1}")
        print(f"{Y[5]}: {placar_t2}")
        escolha = input("\nDigite 1 para próxima rodada de pênaltis:")
        if escolha != "1":
            print("valor incorreto, portanto perdeu essa cobrança de pênaltis")
        rodada += 1
        if rodada >= 5 and placar_t1 != placar_t2:
            break
    vencedor = "4º lugar" if placar_t1 > placar_t2 else "5º lugar"
    mensagem = f"Parabéns, time do {vencedor} ganhou o jogo. CLASSIFICADO PARA 2ºF DA SÉRIE D!!!!!!!"
    return [mensagem, Y[6] if placar_t1 > placar_t2 else Y[7]]


print('---------------------------------GRUPO 1----------------------------')

Resultado1 = rodada_princ_penaltis(p[0])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_penaltis(p[1])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_penaltis(p[2])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_penaltis(p[3])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1, [5], [Resultado1]),(2, [5], [Resultado2]),(3, [5], [Resultado3]),(4, [5], [Resultado4]),(5, [0], []),(6, [0], []),(7, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('--------------------PONTUAÇÃO FINAL RODADA 1--------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado4[1],S[1]: Resultado1[3],S[2]: Resultado2[3],S[3]: Resultado3[3],S[4]: Resultado4[3],S[5]: P[5],S[6]: P[6],S[7]: P[7]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado4[1], Sg[0]),(T[1], Resultado1[3], Sg[1]),(T[2], Resultado2[3], Sg[2]),(T[3], Resultado3[3], Sg[3]),(T[4], Resultado4[3], Sg[4]),(T[5], P[5], Sg[5]),(T[6], P[6], Sg[6]),(T[7], P[7], Sg[7])]
tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

Resultado5 = rodada_princ_penaltis(p[4])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_penaltis(p[5])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_penaltis(p[6])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[7])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1, [4], [Resultado8]),(2, [5], [Resultado8]),(3, [5], [Resultado3]),(4, [5], [Resultado4]),(5, [5], [Resultado5]),(6, [5], [Resultado6]),(7, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1],S[1]: Resultado8[1],S[2]: Resultado8[3],S[3]: Resultado3[3],S[4]: Resultado4[3],S[5]: Resultado5[3],S[6]: Resultado6[3],S[7]: Resultado7[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado7[1], Sg[0]),(T[1], Resultado8[1], Sg[1]),(T[2], Resultado8[3], Sg[2]),(T[3], Resultado3[3], Sg[3]),(T[4], Resultado4[3], Sg[4]),(T[5], Resultado5[3], Sg[5]),(T[6], Resultado6[3], Sg[6]),(T[7], Resultado7[3], Sg[7])]
tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

Resultado9 = rodada_princ_pênaltis_PC(p[8])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[9])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[10])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[11])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3, [5], [Resultado9]),(4, [5], [Resultado10]),(5, [5], [Resultado11]),(6, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1],S[1]: Resultado12[1],S[2]: Resultado8[3],S[3]: Resultado9[3],S[4]: Resultado10[3],S[5]: Resultado11[3],S[6]: Resultado12[3],S[7]: Resultado7[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado7[1], Sg[0]),(T[1], Resultado12[1], Sg[1]),(T[2], Resultado8[3], Sg[2]),(T[3], Resultado9[3], Sg[3]),(T[4], Resultado10[3], Sg[4]), (T[5], Resultado11[3], Sg[5]), (T[6], Resultado12[3], Sg[6]), (T[7], Resultado7[3], Sg[7])]
tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado13 = rodada_princ_pênaltis_PC(p[12])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[13])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[14])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[15])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1, [4], [Resultado13]),(2, [5], [Resultado16]),(3, [5], [Resultado14]),(4, [5], [Resultado15]),(5, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('--------------------PONTUAÇÃO FINAL RODADA 4---------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1], S[1]: Resultado13[1], S[2]: Resultado16[1],S[3]: Resultado14[3], S[4]: Resultado15[3], S[5]: Resultado16[3],S[6]: Resultado12[3], S[7]: Resultado13[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
resultados = [(T[0], Resultado7[1], Sg[0]), (T[1], Resultado13[1], Sg[1]),(T[2], Resultado16[1], Sg[2]), (T[3], Resultado14[3], Sg[3]),(T[4], Resultado15[3], Sg[4]), (T[5], Resultado16[3], Sg[5]),(T[6], Resultado12[3], Sg[6]), (T[7], Resultado13[3], Sg[7])]
resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

Resultado17 = rodada_princ_pênaltis_PC(p[16])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[17])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[18])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[19])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2, [4, 4], [Resultado17, Resultado18]),(3, [4, 4], [Resultado19, Resultado20]),(4, [5], [Resultado19]),(5, [5], [Resultado20]),(6, [5], [Resultado17]),(7, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1],S[1]: Resultado13[1], S[2]: Resultado18[1], S[3]: Resultado20[1], S[4]: Resultado19[3], S[5]: Resultado20[3], S[6]: Resultado17[3], S[7]: Resultado18[3],}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(time, pontos)

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado7[1], Sg[0]),(T[1], Resultado13[1], Sg[1]),(T[2], Resultado18[1], Sg[2]),(T[3], Resultado20[1], Sg[3]),(T[4], Resultado19[3], Sg[4]),(T[5], Resultado20[3], Sg[5]),(T[6], Resultado17[3], Sg[6]),(T[7], Resultado18[3], Sg[7]),]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

Resultado21 = rodada_princ_pênaltis_PC(p[20])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[21])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[22])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[23])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3, 4, Resultado22),(4, 4, Resultado24),(5, 5, Resultado23),(6, 5, Resultado24),(7, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1],S[1]: Resultado13[1],S[2]: Resultado18[1],S[3]: Resultado22[1],S[4]: Resultado24[1],S[5]: Resultado23[3],S[6]: Resultado24[3],S[7]: Resultado22[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado7[1], Sg[0]),(T[1], Resultado13[1], Sg[1]),(T[2], Resultado18[1], Sg[2]), (T[3], Resultado22[1], Sg[3]), (T[4], Resultado24[1], Sg[4]), (T[5], Resultado23[3], Sg[5]), (T[6], Resultado24[3], Sg[6]), (T[7], Resultado22[3], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado25 = rodada_princ_pênaltis_PC(p[24])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[25])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[26])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[27])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4, [4], [Resultado25]),(5, [4, 4], [Resultado26, Resultado27]),(6, [5, 4], [Resultado26, Resultado28]),(7, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado7[1], S[1]: Resultado13[1], S[2]: Resultado18[1], S[3]: Resultado22[1], S[4]: Resultado25[1], S[5]: Resultado27[1], S[6]: Resultado28[1], S[7]: Resultado28[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado7[1], Sg[0]),(T[1], Resultado13[1], Sg[1]), (T[2], Resultado18[1], Sg[2]), (T[3], Resultado22[1], Sg[3]), (T[4], Resultado25[1], Sg[4]), (T[5], Resultado27[1], Sg[5]), (T[6], Resultado28[1], Sg[6]), (T[7], Resultado28[3], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

Resultado29 = rodada_princ_penaltis(p[28])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_penaltis(p[29])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_penaltis(p[30])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_penaltis(p[31])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1, [4], [Resultado29]),(2, [4], [Resultado30]),(3, [4], [Resultado31]),(4, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado32[3], S[1]: Resultado29[1], S[2]: Resultado30[1], S[3]: Resultado31[1], S[4]: Resultado32[1], S[5]: Resultado27[1], S[6]: Resultado28[1], S[7]: Resultado28[3]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado32[3], Sg[0]), (T[1], Resultado29[1], Sg[1]),  (T[2], Resultado30[1], Sg[2]), (T[3], Resultado31[1], Sg[3]), (T[4], Resultado32[1], Sg[4]), (T[5], Resultado27[1], Sg[5]), (T[6], Resultado28[1], Sg[6]), (T[7], Resultado28[3], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado33 = rodada_princ_penaltis(p[32])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_penaltis(p[33])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_penaltis(p[34])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[35])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1, [5], [Resultado36]),(2, [4], [Resultado36]),(5, [4], [Resultado33]),(6, [4], [Resultado34]),(7, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado35[3], S[1]: Resultado36[3], S[2]: Resultado36[1], S[3]: Resultado31[1], S[4]: Resultado32[1], S[5]: Resultado33[1], S[6]: Resultado34[1], S[7]: Resultado35[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado35[3], Sg[0]), (T[1], Resultado36[3], Sg[1]), (T[2], Resultado36[1], Sg[2]), (T[3], Resultado31[1], Sg[3]), (T[4], Resultado32[1], Sg[4]), (T[5], Resultado33[1], Sg[5]), (T[6], Resultado34[1], Sg[6]), (T[7], Resultado35[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado37 = rodada_princ_pênaltis_PC(p[36])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[37])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[38])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[39])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3, [4], [Resultado37]),(4, [4], [Resultado38]),(5, [4], [Resultado39]),(6, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado35[3], S[1]: Resultado40[3], S[2]: Resultado36[1],  S[3]: Resultado37[1], S[4]: Resultado38[1], S[5]: Resultado39[1],  S[6]: Resultado40[1],  S[7]: Resultado35[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado35[3], Sg[0]),  (T[1], Resultado40[3], Sg[1]), (T[2], Resultado36[1], Sg[2]), (T[3], Resultado37[1], Sg[3]), (T[4], Resultado38[1], Sg[4]), (T[5], Resultado39[1], Sg[5]), (T[6], Resultado40[1], Sg[6]), (T[7], Resultado35[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado41 = rodada_princ_pênaltis_PC(p[40])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[41])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[42])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[43])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1, [5], [Resultado41]),(2, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3, [4], [Resultado42]),(4, [4], [Resultado43]), (5, [4], [Resultado44]),(7, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

print('PONTUAÇÃO ATUAL')
pontuacao_atual = {S[0]: Resultado35[3],S[1]: Resultado41[3], S[2]: Resultado44[3], S[3]: Resultado42[1], S[4]: Resultado43[1], S[5]: Resultado44[1], S[6]: Resultado40[1], S[7]: Resultado41[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado35[3], Sg[0]), (T[1], Resultado41[3], Sg[1]), (T[2], Resultado44[3], Sg[2]), (T[3], Resultado42[1], Sg[3]), (T[4], Resultado43[1], Sg[4]), (T[5], Resultado44[1], Sg[5]), (T[6], Resultado40[1], Sg[6]), (T[7], Resultado41[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado45 = rodada_princ_pênaltis_PC(p[44])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[45])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[46])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[47])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2, [5, 5], [Resultado45, Resultado46]), (3, [5, 5], [Resultado47, Resultado48]), (4, [4], [Resultado47]), (5, [4], [Resultado48]),(6, [4], [Resultado45]), (7, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado35[3], S[1]: Resultado41[3], S[2]: Resultado46[3], S[3]: Resultado48[3], S[4]: Resultado47[1], S[5]: Resultado48[1], S[6]: Resultado45[1], S[7]: Resultado46[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado35[3], Sg[0]), (T[1], Resultado41[3], Sg[1]), (T[2], Resultado46[3], Sg[2]), (T[3], Resultado48[3], Sg[3]), (T[4], Resultado47[1], Sg[4]), (T[5], Resultado48[1], Sg[5]), (T[6], Resultado45[1], Sg[6]), (T[7], Resultado46[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado49 = rodada_princ_pênaltis_PC(p[48])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[49])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[50])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[51])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3, [5, 5], [Resultado49, Resultado50]),(4, [5, 5], [Resultado51, Resultado52]), (5, [4], [Resultado51]),(6, [4, 4], [Resultado49, Resultado52]),(7, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))
    
print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado35[3], S[1]: Resultado41[3], S[2]: Resultado46[3], S[3]: Resultado50[3], S[4]: Resultado52[3], S[5]: Resultado51[1], S[6]: Resultado52[1], S[7]: Resultado50[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[0], Resultado35[3], Sg[0]), (T[1], Resultado41[3], Sg[1]), (T[2], Resultado46[3], Sg[2]), (T[3], Resultado50[3], Sg[3]), (T[4], Resultado52[3], Sg[4]), (T[5], Resultado51[1], Sg[5]), (T[6], Resultado52[1], Sg[6]), (T[7], Resultado50[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')
    
Resultado53 = rodada_princ_pênaltis_PC(p[52])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[53])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[54])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[55])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4, [5], [Resultado53]), (5, [5, 5], [Resultado54, Resultado55]), (6, [4, 5], [Resultado54, Resultado56]), (7, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[0]: Resultado35[3], S[1]: Resultado41[3], S[2]: Resultado46[3], S[3]: Resultado50[3], S[4]: Resultado53[3], S[5]: Resultado55[3],  S[6]: Resultado56[3], S[7]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [  (T[0], Resultado35[3], Sg[0]),   (T[1], Resultado41[3], Sg[1]), (T[2], Resultado46[3], Sg[2]), (T[3], Resultado50[3], Sg[3]), (T[4], Resultado53[3], Sg[4]), (T[5], Resultado55[3], Sg[5]), (T[6], Resultado56[3], Sg[6]), (T[7], Resultado56[1], Sg[7])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f'{posicao}º, {time}, {pontos}, {saldo}')

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG1 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 1 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG1)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG1 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 1 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG1)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 2----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[56])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[57])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[58])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[59])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+A, [5], [Resultado1]),(2+A, [5], [Resultado2]),(3+A, [5], [Resultado3]),(4+A, [5], [Resultado4]),(5+A, [0], []),(6+A, [0], []),(7+A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 1--------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado4[1],S[9]: Resultado1[3],S[10]: Resultado2[3],S[11]: Resultado3[3],S[12]: Resultado4[3],S[13]: P[5],S[14]: P[6],S[15]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado4[1], Sg[8]),(T[9], Resultado1[3], Sg[9]),(T[10], Resultado2[3], Sg[10]),(T[11], Resultado3[3], Sg[11]),(T[12], Resultado4[3], Sg[12]),(T[13], P[5], Sg[13]),(T[14], 			P[6], Sg[14]),(T[15], P[7], Sg[15])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[60])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[61])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[62])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[63])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+A, [4], [Resultado8]),(2+A, [5], [Resultado8]),(3+A, [5], [Resultado3]),(4+A, [5], [Resultado4]),(5+A, [5], [Resultado5]),(6+A, [5], [Resultado6]),(7+A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1],S[9]: Resultado8[1],S[10]: Resultado8[3],S[11]: Resultado3[3],S[12]: Resultado4[3],S[13]: Resultado5[3],S[14]: Resultado6[3],S[15]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado7[1], Sg[8]),(T[9], Resultado8[1], Sg[9]),(T[10], Resultado8[3], Sg[10]),(T[11], Resultado3[3], Sg[11]),(T[12], Resultado4[3], Sg[12]),(T[13], Resultado5[3], Sg[13]),			(T[14], Resultado6[3], Sg[14]),(T[15], Resultado7[3], Sg[15])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[64])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[65])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[66])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[67])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+A, [5], [Resultado9]),(4+A, [5], [Resultado10]),(5+A, [5], [Resultado11]),(6+A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1],S[9]: Resultado12[1],S[10]: Resultado8[3],S[11]: Resultado9[3],S[12]: Resultado10[3],S[13]: Resultado11[3],S[14]: Resultado12[3],S[15]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado7[1], Sg[8]),(T[9], Resultado12[1], Sg[9]),(T[10], Resultado8[3], Sg[10]),(T[11], Resultado9[3], Sg[11]),(T[12], Resultado10[3], Sg[12]), (T[13], Resultado11[3], 				Sg[13]), (T[14], Resultado12[3], Sg[14]), (T[15], Resultado7[3], Sg[15])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[68])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[69])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[70])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[71])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+A, [4], [Resultado13]),(2+A, [5], [Resultado16]),(3+A, [5], [Resultado14]),(4+A, [5], [Resultado15]),(5+A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4--------------------\n')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1], S[9]: Resultado13[1], S[10]: Resultado16[1],S[11]: Resultado14[3], S[12]: Resultado15[3], S[13]: Resultado16[3],S[14]: Resultado12[3], S[15]: Resultado13[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[8], Resultado7[1], Sg[8]), (T[9], Resultado13[1], Sg[9]),(T[10], Resultado16[1], Sg[10]), (T[11], Resultado14[3], Sg[11]),(T[12], Resultado15[3], Sg[12]), (T[13], Resultado16[3], Sg[13]),(T[14], Resultado12[3], Sg[14]), (T[15], Resultado13[3], Sg[15])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[72])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[73])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[74])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[75])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+A, [4, 4], [Resultado17, Resultado18]),(3+A, [4, 4], [Resultado19, Resultado20]),(4+A, [5], [Resultado19]),(5+A, [5], [Resultado20]),(6+A, [5], [Resultado17]),(7+A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1],S[9]: Resultado13[1], S[10]: Resultado18[1], S[11]: Resultado20[1], S[12]: Resultado19[3], S[13]: Resultado20[3], S[14]: Resultado17[3], S[15]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado7[1], Sg[8]),(T[9], Resultado13[1], Sg[9]),(T[10], Resultado18[1], Sg[10]),(T[11], Resultado20[1], Sg[11]),(T[12], Resultado19[3], Sg[12]),(T[13], Resultado20[3], 			Sg[13]),(T[14], Resultado17[3], Sg[14]),(T[15], Resultado18[3], Sg[15]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[76])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[77])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[78])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[79])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+A, 4, Resultado22),(4+A, 4, Resultado24),(5+A, 5, Resultado23),(6+A, 5, Resultado24),(7+A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1],S[9]: Resultado13[1],S[10]: Resultado18[1],S[11]: Resultado22[1],S[12]: Resultado24[1],S[13]: Resultado23[3],S[14]: Resultado24[3],S[15]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado7[1], Sg[8]),(T[9], Resultado13[1], Sg[9]),(T[10], Resultado18[1], Sg[10]), (T[11], Resultado22[1], Sg[11]), (T[12], Resultado24[1], Sg[12]), (T[13], Resultado23[3], 			Sg[13]), (T[14], Resultado24[3], Sg[14]), (T[15], Resultado22[3], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[80])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[81])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[82])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[83])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+A, [4], [Resultado25]),(5+A, [4, 4], [Resultado26, Resultado27]),(6+A, [5, 4], [Resultado26, Resultado28]),(7+A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado7[1], S[9]: Resultado13[1], S[10]: Resultado18[1], S[11]: Resultado22[1], S[12]: Resultado25[1], S[13]: Resultado27[1], S[14]: Resultado28[1], S[15]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado7[1], Sg[8]),(T[9], Resultado13[1], Sg[9]), (T[10], Resultado18[1], Sg[10]), (T[11], Resultado22[1], Sg[11]), (T[12], Resultado25[1], Sg[12]), (T[13], Resultado27[1], 		Sg[13]), (T[14], Resultado28[1], Sg[14]), (T[15], Resultado28[3], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[84])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[85])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[86])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[87])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+A, [4], [Resultado29]),(2+A, [4], [Resultado30]),(3+A, [4], [Resultado31]),(4+A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado32[3], S[9]: Resultado29[1], S[10]: Resultado30[1], S[11]: Resultado31[1], S[12]: Resultado32[1], S[13]: Resultado27[1], S[14]: Resultado28[1], S[15]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado32[3], Sg[8]), (T[9], Resultado29[1], Sg[9]),  (T[10], Resultado30[1], Sg[10]),  (T[11], Resultado31[1], Sg[11]),  (T[12], Resultado32[1], Sg[12]),  (T[13], 					Resultado27[1], Sg[13]),  (T[14], Resultado28[1], Sg[14]),  (T[15], Resultado28[3], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[88])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[89])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[90])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[91])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+A, [5], [Resultado36]),(2+A, [4], [Resultado36]),(5+A, [4], [Resultado33]),(6+A, [4], [Resultado34]),(7+A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado35[3], S[9]: Resultado36[3], S[10]: Resultado36[1], S[11]: Resultado31[1], S[12]: Resultado32[1], S[13]: Resultado33[1], S[14]: Resultado34[1], S[15]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado35[3], Sg[8]), (T[9], Resultado36[3], Sg[9]), (T[10], Resultado36[1], Sg[10]), (T[11], Resultado31[1], Sg[11]), (T[12], Resultado32[1], Sg[12]), (T[13], Resultado33[1], 	Sg[13]), (T[14], Resultado34[1], Sg[14]), (T[15], Resultado35[1], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[92])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[93])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[94])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[95])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+A, [4], [Resultado37]),(4+A, [4], [Resultado38]),(5+A, [4], [Resultado39]),(6+A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado35[3], S[9]: Resultado40[3], S[10]: Resultado36[1],  S[11]: Resultado37[1], S[12]: Resultado38[1], S[13]: Resultado39[1],  S[14]: Resultado40[1],  S[15]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado35[3], Sg[8]),  (T[9], Resultado40[3], Sg[9]), (T[10], Resultado36[1], Sg[10]), (T[11], Resultado37[1], Sg[11]), (T[12], Resultado38[1], Sg[12]), (T[13], 						Resultado39[1], Sg[13]), (T[14], Resultado40[1], Sg[14]), (T[15], Resultado35[1], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[96])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[97])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[98])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[99])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+A, [5], [Resultado41]),(2+A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+A, [4], [Resultado42]),(4+A, [4], [Resultado43]), (5+A, [4], [Resultado44]),(7+A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[8]: Resultado35[3],S[9]: Resultado41[3], S[10]: Resultado44[3], S[11]: Resultado42[1], S[12]: Resultado43[1], S[13]: Resultado44[1], S[14]: Resultado40[1], S[15]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado35[3], Sg[8]), (T[9], Resultado41[3], Sg[9]), (T[10], Resultado44[3], Sg[10]), (T[11], Resultado42[1], Sg[11]), (T[12], Resultado43[1], Sg[12]), (T[13], Resultado44[1], 	Sg[13]), (T[14], Resultado40[1], Sg[14]), (T[15], Resultado41[1], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[100])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[101])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[102])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[103])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+A, [5, 5], [Resultado45, Resultado46]), (3+A, [5, 5], [Resultado47, Resultado48]), (4+A, [4], [Resultado47]), (5+A, [4], [Resultado48]),(6+A, [4], [Resultado45]), (7+A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado35[3], S[9]: Resultado41[3], S[10]: Resultado46[3], S[11]: Resultado48[3], S[12]: Resultado47[1], S[13]: Resultado48[1], S[14]: Resultado45[1], S[15]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado35[3], Sg[8]), (T[9], Resultado41[3], Sg[9]), (T[10], Resultado46[3], Sg[10]), (T[11], Resultado48[3], Sg[11]), (T[12], Resultado47[1], Sg[12]), (T[13], Resultado48[1], 	Sg[13]), (T[14], Resultado45[1], Sg[14]), (T[15], Resultado46[1], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[104])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[105])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[106])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[107])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+A, [5, 5], [Resultado49, Resultado50]),(4+A, [5, 5], [Resultado51, Resultado52]), (5+A, [4], [Resultado51]),(6+A, [4, 4], [Resultado49, Resultado52]),(7+A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')
    
    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[8]: Resultado35[3], S[9]: Resultado41[3], S[10]: Resultado46[3], S[11]: Resultado50[3], S[12]: Resultado52[3], S[13]: Resultado51[1], S[14]: Resultado52[1], S[15]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[8], Resultado35[3], Sg[8]), (T[9], Resultado41[3], Sg[9]), (T[10], Resultado46[3], Sg[10]), (T[11], Resultado50[3], Sg[11]), (T[12], Resultado52[3], Sg[12]), (T[13], Resultado51[1], 	Sg[13]), (T[14], Resultado52[1], Sg[14]), (T[15], Resultado50[1], Sg[15])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[108])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[109])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[110])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[111])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+A, [5], [Resultado53]), (5+A, [5, 5], [Resultado54, Resultado55]), (6+A, [4, 5], [Resultado54, Resultado56]), (7+A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[8]: Resultado35[3], S[9]: Resultado41[3], S[10]: Resultado46[3], S[11]: Resultado50[3], S[12]: Resultado53[3], S[13]: Resultado55[3],  S[14]: Resultado56[3], S[15]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[8], Resultado35[3], Sg[8]), (T[9], Resultado41[3], Sg[9]), (T[10], Resultado46[3], Sg[10]), (T[11], Resultado50[3], Sg[11]), (T[12], Resultado53[3], Sg[12]), (T[13], Resultado55[3], 	Sg[13]), (T[14], Resultado56[3], Sg[14]), (T[15], Resultado56[1], Sg[15])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG2 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 2 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG2)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG2 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 2 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG2)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 3----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[112])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[113])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[114])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[115])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+2*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+2*A, [5], [Resultado1]),(2+2*A, [5], [Resultado2]),(3+2*A, [5], [Resultado3]),(4+2*A, [5], [Resultado4]),(5+2*A, [0], []),(6+2*A, [0], []),(7+2*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[16]: Resultado4[1],S[17]: Resultado1[3],S[18]: Resultado2[3],S[19]: Resultado3[3],S[20]: Resultado4[3],S[21]: P[5],S[22]: P[6],S[23]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado4[1], Sg[16]),(T[17], Resultado1[3], Sg[17]),(T[18], Resultado2[3], Sg[18]),(T[19], Resultado3[3], Sg[19]),(T[20], Resultado4[3], Sg[20]),(T[21], P[5], Sg[21]),(T[22], 	P[6], Sg[22]),(T[23], P[7], Sg[23])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[116])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[117])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[118])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[119])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+2*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+2*A, [4], [Resultado8]),(2+2*A, [5], [Resultado8]),(3+2*A, [5], [Resultado3]),(4+2*A, [5], [Resultado4]),(5+2*A, [5], [Resultado5]),(6+2*A, [5], [Resultado6]),(7+2*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1],S[17]: Resultado8[1],S[18]: Resultado8[3],S[19]: Resultado3[3],S[20]: Resultado4[3],S[21]: Resultado5[3],S[22]: Resultado6[3],S[23]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado7[1], Sg[16]),(T[17], Resultado8[1], Sg[17]),(T[18], Resultado8[3], Sg[18]),(T[19], Resultado3[3], Sg[19]),(T[20], Resultado4[3], Sg[20]),(T[21], Resultado5[3], 				Sg[21]),(T[22], Resultado6[3], Sg[22]),(T[23], Resultado7[3], Sg[23])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[120])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[121])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[122])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[123])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+2*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+2*A, [5], [Resultado9]),(4+2*A, [5], [Resultado10]),(5+2*A, [5], [Resultado11]),(6+2*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1],S[17]: Resultado12[1],S[18]: Resultado8[3],S[19]: Resultado9[3],S[20]: Resultado10[3],S[21]: Resultado11[3],S[22]: Resultado12[3],S[23]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado7[1], Sg[16]),(T[17], Resultado12[1], Sg[17]),(T[18], Resultado8[3], Sg[18]),(T[19], Resultado9[3], Sg[19]),(T[20], Resultado10[3], Sg[20]), (T[21], Resultado11[3], 			Sg[21]), (T[22], Resultado12[3], Sg[22]), (T[23], Resultado7[3], Sg[23])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[124])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[125])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[126])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[127])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+2*A, [4], [Resultado13]),(2+2*A, [5], [Resultado16]),(3+2*A, [5], [Resultado14]),(4+2*A, [5], [Resultado15]),(5+2*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4--------------------\n')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1], S[17]: Resultado13[1], S[18]: Resultado16[1],S[19]: Resultado14[3], S[20]: Resultado15[3], S[21]: Resultado16[3],S[22]: Resultado12[3], S[23]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[16], Resultado7[1], Sg[16]), (T[17], Resultado13[1], Sg[17]),(T[18], Resultado16[1], Sg[18]), (T[19], Resultado14[3], Sg[19]),(T[20], Resultado15[3], Sg[20]), (T[21], Resultado16[3], 			Sg[21]),(T[22], Resultado12[3], Sg[22]), (T[23], Resultado13[3], Sg[23])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[128])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[129])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[130])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[131])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+2*A, [4, 4], [Resultado17, Resultado18]),(3+2*A, [4, 4], [Resultado19, Resultado20]),(4+2*A, [5], [Resultado19]),(5+2*A, [5], [Resultado20]),(6+2*A, [5], [Resultado17]),(7+2*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1],S[17]: Resultado13[1], S[18]: Resultado18[1], S[19]: Resultado20[1], S[20]: Resultado19[3], S[21]: Resultado20[3], S[22]: Resultado17[3], S[23]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado7[1], Sg[16]),(T[17], Resultado13[1], Sg[17]),(T[18], Resultado18[1], Sg[18]),(T[19], Resultado20[1], Sg[19]),(T[20], Resultado19[3], Sg[20]),(T[21], Resultado20[3], 		Sg[21]),(T[22], Resultado17[3], Sg[22]),(T[23], Resultado18[3], Sg[23]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[132])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[133])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[134])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[135])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+2*A, 4, Resultado22),(4+2*A, 4, Resultado24),(5+2*A, 5, Resultado23),(6+2*A, 5, Resultado24),(7+2*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1],S[17]: Resultado13[1],S[18]: Resultado18[1],S[19]: Resultado22[1],S[20]: Resultado24[1],S[21]: Resultado23[3],S[22]: Resultado24[3],S[23]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado7[1], Sg[16]),(T[17], Resultado13[1], Sg[17]),(T[18], Resultado18[1], Sg[18]), (T[19], Resultado22[1], Sg[19]), (T[20], Resultado24[1], Sg[20]), (T[21], 						Resultado23[3], Sg[21]), (T[22], Resultado24[3], Sg[22]), (T[23], Resultado22[3], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[136])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[137])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[138])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[139])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+2*A, [4], [Resultado25]),(5+2*A, [4, 4], [Resultado26, Resultado27]),(6+2*A, [5, 4], [Resultado26, Resultado28]),(7+2*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado7[1], S[17]: Resultado13[1], S[18]: Resultado18[1], S[19]: Resultado22[1], S[20]: Resultado25[1], S[21]: Resultado27[1], S[22]: Resultado28[1], S[23]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado7[1], Sg[16]),(T[17], Resultado13[1], Sg[17]), (T[18], Resultado18[1], Sg[18]), (T[19], Resultado22[1], Sg[19]), (T[20], Resultado25[1], Sg[20]), (T[21], 					Resultado27[1], Sg[21]), (T[22], Resultado28[1], Sg[22]), (T[23], Resultado28[3], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[140])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[141])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[142])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[143])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+2*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+2*A, [4], [Resultado29]),(2+2*A, [4], [Resultado30]),(3+2*A, [4], [Resultado31]),(4+2*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado32[3], S[17]: Resultado29[1], S[18]: Resultado30[1], S[19]: Resultado31[1], S[20]: Resultado32[1], S[21]: Resultado27[1], S[22]: Resultado28[1], S[23]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado32[3], Sg[16]), (T[17], Resultado29[1], Sg[17]),  (T[18], Resultado30[1], Sg[18]),  (T[19], Resultado31[1], Sg[19]),  (T[20], Resultado32[1], Sg[20]),  (T[21], 				Resultado27[1], Sg[21]),  (T[22], Resultado28[1], Sg[22]),  (T[23], Resultado28[3], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[144])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[145])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[146])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[147])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+2*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+2*A, [5], [Resultado36]),(2+2*A, [4], [Resultado36]),(5+2*A, [4], [Resultado33]),(6+2*A, [4], [Resultado34]),(7+2*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado35[3], S[17]: Resultado36[3], S[18]: Resultado36[1], S[19]: Resultado31[1], S[20]: Resultado32[1], S[21]: Resultado33[1], S[22]: Resultado34[1], S[23]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado35[3], Sg[16]), (T[17], Resultado36[3], Sg[17]), (T[18], Resultado36[1], Sg[18]), (T[19], Resultado31[1], Sg[19]), (T[20], Resultado32[1], Sg[20]), (T[21], 					Resultado33[1], Sg[21]), (T[22], Resultado34[1], Sg[22]), (T[23], Resultado35[1], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    

Resultado37 = rodada_princ_pênaltis_PC(p[148])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[149])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[150])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[151])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+2*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+2*A, [4], [Resultado37]),(4+2*A, [4], [Resultado38]),(5+2*A, [4], [Resultado39]),(6+2*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado35[3], S[17]: Resultado40[3], S[18]: Resultado36[1],  S[19]: Resultado37[1], S[20]: Resultado38[1], S[21]: Resultado39[1],  S[22]: Resultado40[1],  S[23]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado35[3], Sg[16]),  (T[17], Resultado40[3], Sg[17]), (T[18], Resultado36[1], Sg[18]), (T[19], Resultado37[1], Sg[19]), (T[20], Resultado38[1], Sg[20]), (T[21], 					Resultado39[1], Sg[21]), (T[22], Resultado40[1], Sg[22]), (T[23], Resultado35[1], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[152])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[153])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[154])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[155])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+2*A, [5], [Resultado41]),(2+2*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+2*A, [4], [Resultado42]),(4+2*A, [4], [Resultado43]), (5+2*A, [4], [Resultado44]),(7+2*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[16]: Resultado35[3],S[17]: Resultado41[3], S[18]: Resultado44[3], S[19]: Resultado42[1], S[20]: Resultado43[1], S[21]: Resultado44[1], S[22]: Resultado40[1], S[23]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado35[3], Sg[16]), (T[17], Resultado41[3], Sg[17]), (T[18], Resultado44[3], Sg[18]), (T[19], Resultado42[1], Sg[19]), (T[20], Resultado43[1], Sg[20]), (T[21], 					Resultado44[1], Sg[21]), (T[22], Resultado40[1], Sg[22]), (T[23], Resultado41[1], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[156])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[157])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[158])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[159])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+2*A, [5, 5], [Resultado45, Resultado46]), (3+2*A, [5, 5], [Resultado47, Resultado48]), (4+2*A, [4], [Resultado47]), (5+2*A, [4], [Resultado48]),(6+2*A, [4], [Resultado45]), (7+2*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado35[3], S[17]: Resultado41[3], S[18]: Resultado46[3], S[19]: Resultado48[3], S[20]: Resultado47[1], S[21]: Resultado48[1], S[22]: Resultado45[1], S[23]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado35[3], Sg[16]), (T[17], Resultado41[3], Sg[17]), (T[18], Resultado46[3], Sg[18]), (T[19], Resultado48[3], Sg[19]), (T[20], Resultado47[1], Sg[20]), (T[21], 					Resultado48[1], Sg[21]), (T[22], Resultado45[1], Sg[22]), (T[23], Resultado46[1], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[160])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[161])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[162])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[163])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+2*A, [5, 5], [Resultado49, Resultado50]),(4+2*A, [5, 5], [Resultado51, Resultado52]), (5+2*A, [4], [Resultado51]),(6+2*A, [4, 4], [Resultado49, Resultado52]),(7+2*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')
    
    pontuacao_atual = {S[16]: Resultado35[3], S[17]: Resultado41[3], S[18]: Resultado46[3], S[19]: Resultado50[3], S[20]: Resultado52[3], S[21]: Resultado51[1], S[22]: Resultado52[1], S[23]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')
    
    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[16], Resultado35[3], Sg[16]), (T[17], Resultado41[3], Sg[17]), (T[18], Resultado46[3], Sg[18]), (T[19], Resultado50[3], Sg[19]), (T[20], Resultado52[3], Sg[20]), (T[21], 					Resultado51[1], Sg[21]), (T[22], Resultado52[1], Sg[22]), (T[23], Resultado50[1], Sg[23])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[164])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[165])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[166])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[167])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+2*A, [5], [Resultado53]), (5+2*A, [5, 5], [Resultado54, Resultado55]), (6+2*A, [4, 5], [Resultado54, Resultado56]), (7+2*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[16]: Resultado35[3], S[17]: Resultado41[3], S[18]: Resultado46[3], S[19]: Resultado50[3], S[20]: Resultado53[3], S[21]: Resultado55[3],  S[22]: Resultado56[3], S[23]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[16], Resultado35[3], Sg[16]), (T[17], Resultado41[3], Sg[17]), (T[18], Resultado46[3], Sg[18]), (T[19], Resultado50[3], Sg[19]), (T[20], Resultado53[3], Sg[20]), (T[21], Resultado55[3], Sg[21]), (T[22], Resultado56[3], Sg[22]), (T[23], Resultado56[1], Sg[23])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG3 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 3 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG3)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG3 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 3 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG3)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 4----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[168])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[169])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[170])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[171])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+3*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+3*A, [5], [Resultado1]),(2+3*A, [5], [Resultado2]),(3+3*A, [5], [Resultado3]),(4+3*A, [5], [Resultado4]),(5+3*A, [0], []),(6+3*A, [0], []),(7+3*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado4[1],S[25]: Resultado1[3],S[26]: Resultado2[3],S[27]: Resultado3[3],S[28]: Resultado4[3],S[29]: P[5],S[30]: P[6],S[31]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado4[1], Sg[24]),(T[25], Resultado1[3], Sg[25]),(T[26], Resultado2[3], Sg[26]),(T[27], Resultado3[3], Sg[27]),(T[28], Resultado4[3], Sg[28]),(T[29], P[5], Sg[29]),(T[30], P[6], Sg[30]),(T[31], P[7], Sg[31])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[172])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[173])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[174])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[175])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+3*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+3*A, [4], [Resultado8]),(2+3*A, [5], [Resultado8]),(3+3*A, [5], [Resultado3]),(4+3*A, [5], [Resultado4]),(5+3*A, [5], [Resultado5]),(6+3*A, [5], [Resultado6]),(7+3*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1],S[25]: Resultado8[1],S[26]: Resultado8[3],S[27]: Resultado3[3],S[28]: Resultado4[3],S[29]: Resultado5[3],S[30]: Resultado6[3],S[31]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado7[1], Sg[24]),(T[25], Resultado8[1], Sg[25]),(T[26], Resultado8[3], Sg[26]),(T[27], Resultado3[3], Sg[27]),(T[28], Resultado4[3], Sg[28]),(T[29], Resultado5[3], Sg[29]),(T[30], Resultado6[3], Sg[30]),(T[31], Resultado7[3], Sg[31])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[176])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[177])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[178])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[179])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+3*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+3*A, [5], [Resultado9]),(4+3*A, [5], [Resultado10]),(5+3*A, [5], [Resultado11]),(6+3*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1],S[25]: Resultado12[1],S[26]: Resultado8[3],S[27]: Resultado9[3],S[28]: Resultado10[3],S[29]: Resultado11[3],S[30]: Resultado12[3],S[31]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado7[1], Sg[24]),(T[25], Resultado12[1], Sg[25]),(T[26], Resultado8[3], Sg[26]),(T[27], Resultado9[3], Sg[27]),(T[28], Resultado10[3], Sg[28]), (T[29], Resultado11[3], Sg[29]), (T[30], Resultado12[3], Sg[30]), (T[31], Resultado7[3], Sg[31])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[180])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[181])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[182])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[183])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+3*A, [4], [Resultado13]),(2+3*A, [5], [Resultado16]),(3+3*A, [5], [Resultado14]),(4+3*A, [5], [Resultado15]),(5+3*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4----------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1], S[25]: Resultado13[1], S[26]: Resultado16[1],S[27]: Resultado14[3], S[28]: Resultado15[3], S[29]: Resultado16[3],S[30]: Resultado12[3], S[31]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[24], Resultado7[1], Sg[24]), (T[25], Resultado13[1], Sg[25]),(T[26], Resultado16[1], Sg[26]), (T[27], Resultado14[3], Sg[27]),(T[28], Resultado15[3], Sg[28]), (T[29], Resultado16[3], Sg[29]),(T[30], Resultado12[3], Sg[30]), (T[31], Resultado13[3], Sg[31])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[184])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[185])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[186])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[187])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+3*A, [4, 4], [Resultado17, Resultado18]),(3+3*A, [4, 4], [Resultado19, Resultado20]),(4+3*A, [5], [Resultado19]),(5+3*A, [5], [Resultado20]),(6+3*A, [5], [Resultado17]),(7+3*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1],S[25]: Resultado13[1], S[26]: Resultado18[1], S[27]: Resultado20[1], S[28]: Resultado19[3], S[29]: Resultado20[3], S[30]: Resultado17[3], S[31]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado7[1], Sg[24]),(T[25], Resultado13[1], Sg[25]),(T[26], Resultado18[1], Sg[26]),(T[27], Resultado20[1], Sg[27]),(T[28], Resultado19[3], Sg[28]),(T[29], Resultado20[3], Sg[29]),(T[30], Resultado17[3], Sg[30]),(T[31], Resultado18[3], Sg[31]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[188])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[189])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[190])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[191])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+3*A, 4, Resultado22),(4+3*A, 4, Resultado24),(5+3*A, 5, Resultado23),(6+3*A, 5, Resultado24),(7+3*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1],S[25]: Resultado13[1],S[26]: Resultado18[1],S[27]: Resultado22[1],S[28]: Resultado24[1],S[29]: Resultado23[3],S[30]: Resultado24[3],S[31]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado7[1], Sg[24]),(T[25], Resultado13[1], Sg[25]),(T[26], Resultado18[1], Sg[26]), (T[27], Resultado22[1], Sg[27]), (T[28], Resultado24[1], Sg[28]), (T[29], Resultado23[3], Sg[29]), (T[30], Resultado24[3], Sg[30]), (T[31], Resultado22[3], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[192])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[193])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[194])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[195])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+3*A, [4], [Resultado25]),(5+3*A, [4, 4], [Resultado26, Resultado27]),(6+3*A, [5, 4], [Resultado26, Resultado28]),(7+3*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado7[1], S[25]: Resultado13[1], S[26]: Resultado18[1], S[27]: Resultado22[1], S[28]: Resultado25[1], S[29]: Resultado27[1], S[30]: Resultado28[1], S[31]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado7[1], Sg[24]),(T[25], Resultado13[1], Sg[25]), (T[26], Resultado18[1], Sg[26]), (T[27], Resultado22[1], Sg[27]), (T[28], Resultado25[1], Sg[28]), (T[29], Resultado27[1], Sg[29]), (T[30], Resultado28[1], Sg[30]), (T[31], Resultado28[3], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[196])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[197])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[198])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[199])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+3*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+3*A, [4], [Resultado29]),(2+3*A, [4], [Resultado30]),(3+3*A, [4], [Resultado31]),(4+3*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado32[3], S[25]: Resultado29[1], S[26]: Resultado30[1], S[27]: Resultado31[1], S[28]: Resultado32[1], S[29]: Resultado27[1], S[30]: Resultado28[1], S[31]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado32[3], Sg[24]), (T[25], Resultado29[1], Sg[25]),  (T[26], Resultado30[1], Sg[26]),  (T[27], Resultado31[1], Sg[27]),  (T[28], Resultado32[1], Sg[28]),  (T[29], Resultado27[1], Sg[29]),  (T[30], Resultado28[1], Sg[30]),  (T[31], Resultado28[3], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for i, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f'{i}º {time} - Pontuação: {pontos}, Saldo de Gols: {saldo}')
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[200])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[201])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[202])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[203])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+3*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+3*A, [5], [Resultado36]),(2+3*A, [4], [Resultado36]),(5+3*A, [4], [Resultado33]),(6+3*A, [4], [Resultado34]),(7+3*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado35[3], S[25]: Resultado36[3], S[26]: Resultado36[1], S[27]: Resultado31[1], S[28]: Resultado32[1], S[29]: Resultado33[1], S[30]: Resultado34[1], S[31]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado35[3], Sg[24]), (T[25], Resultado36[3], Sg[25]), (T[26], Resultado36[1], Sg[26]), (T[27], Resultado31[1], Sg[27]), (T[28], Resultado32[1], Sg[28]), (T[29], Resultado33[1], Sg[29]), (T[30], Resultado34[1], Sg[30]), (T[31], Resultado35[1], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[204])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[205])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[206])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[207])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+3*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+3*A, [4], [Resultado37]),(4+3*A, [4], [Resultado38]),(5+3*A, [4], [Resultado39]),(6+3*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado35[3], S[25]: Resultado40[3], S[26]: Resultado36[1],  S[27]: Resultado37[1], S[28]: Resultado38[1], S[29]: Resultado39[1],  S[30]: Resultado40[1],  S[31]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado35[3], Sg[24]),  (T[25], Resultado40[3], Sg[25]), (T[26], Resultado36[1], Sg[26]), (T[27], Resultado37[1], Sg[27]), (T[28], Resultado38[1], Sg[28]), (T[29], Resultado39[1], Sg[29]), (T[30], Resultado40[1], Sg[30]), (T[31], Resultado35[1], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[208])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[209])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[210])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[211])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+3*A, [5], [Resultado41]),(2+3*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+3*A, [4], [Resultado42]),(4+3*A, [4], [Resultado43]), (5+3*A, [4], [Resultado44]),(7+3*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[24]: Resultado35[3],S[25]: Resultado41[3], S[26]: Resultado44[3], S[27]: Resultado42[1], S[28]: Resultado43[1], S[29]: Resultado44[1], S[30]: Resultado40[1], S[31]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado35[3], Sg[24]), (T[25], Resultado41[3], Sg[25]), (T[26], Resultado44[3], Sg[26]), (T[27], Resultado42[1], Sg[27]), (T[28], Resultado43[1], Sg[28]), (T[29], Resultado44[1], Sg[29]), (T[30], Resultado40[1], Sg[30]), (T[31], Resultado41[1], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[212])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[213])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[214])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[215])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+3*A, [5, 5], [Resultado45, Resultado46]), (3+3*A, [5, 5], [Resultado47, Resultado48]), (4+3*A, [4], [Resultado47]), (5+3*A, [4], [Resultado48]),(6+3*A, [4], [Resultado45]), (7+3*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado35[3], S[25]: Resultado41[3], S[26]: Resultado46[3], S[27]: Resultado48[3], S[28]: Resultado47[1], S[29]: Resultado48[1], S[30]: Resultado45[1], S[31]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado35[3], Sg[24]), (T[25], Resultado41[3], Sg[25]), (T[26], Resultado46[3], Sg[26]), (T[27], Resultado48[3], Sg[27]), (T[28], Resultado47[1], Sg[28]), (T[29], Resultado48[1], Sg[29]), (T[30], Resultado45[1], Sg[30]), (T[31], Resultado46[1], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[216])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[217])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[218])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[219])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+3*A, [5, 5], [Resultado49, Resultado50]),(4+3*A, [5, 5], [Resultado51, Resultado52]), (5+3*A, [4], [Resultado51]),(6+3*A, [4, 4], [Resultado49, Resultado52]),(7+3*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[24]: Resultado35[3], S[25]: Resultado41[3], S[26]: Resultado46[3], S[27]: Resultado50[3], S[28]: Resultado52[3], S[29]: Resultado51[1], S[30]: Resultado52[1], S[31]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[24], Resultado35[3], Sg[24]), (T[25], Resultado41[3], Sg[25]), (T[26], Resultado46[3], Sg[26]), (T[27], Resultado50[3], Sg[27]), (T[28], Resultado52[3], Sg[28]), (T[29], Resultado51[1], Sg[29]), (T[30], Resultado52[1], Sg[30]), (T[31], Resultado50[1], Sg[31])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[220])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[221])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[222])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[223])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+3*A, [5], [Resultado53]), (5+3*A, [5, 5], [Resultado54, Resultado55]), (6+3*A, [4, 5], [Resultado54, Resultado56]), (7+3*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[24]: Resultado35[3], S[25]: Resultado41[3], S[26]: Resultado46[3], S[27]: Resultado50[3], S[28]: Resultado53[3], S[29]: Resultado55[3],  S[30]: Resultado56[3], S[31]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[24], Resultado35[3], Sg[24]), (T[25], Resultado41[3], Sg[25]), (T[26], Resultado46[3], Sg[26]), (T[27], Resultado50[3], Sg[27]), (T[28], Resultado53[3], Sg[28]), (T[29], Resultado55[3], Sg[29]), (T[30], Resultado56[3], Sg[30]), (T[31], Resultado56[1], Sg[31])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG4 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 4 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG4)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG4 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 4 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG4)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 5----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[224])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[225])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[226])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[227])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+4*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+4*A, [5], [Resultado1]),(2+4*A, [5], [Resultado2]),(3+4*A, [5], [Resultado3]),(4+4*A, [5], [Resultado4]),(5+4*A, [0], []),(6+4*A, [0], []),(7+4*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado4[1],S[33]: Resultado1[3],S[34]: Resultado2[3],S[35]: Resultado3[3],S[36]: Resultado4[3],S[37]: P[5],S[38]: P[6],S[39]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado4[1], Sg[32]),(T[33], Resultado1[3], Sg[33]),(T[34], Resultado2[3], Sg[34]),(T[35], Resultado3[3], Sg[35]),(T[36], Resultado4[3], Sg[36]),(T[37], P[5], Sg[37]),(T[38], P[6], Sg[38]),(T[39], P[7], Sg[39])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[228])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[229])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[230])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[231])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+4*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+4*A, [4], [Resultado8]),(2+4*A, [5], [Resultado8]),(3+4*A, [5], [Resultado3]),(4+4*A, [5], [Resultado4]),(5+4*A, [5], [Resultado5]),(6+4*A, [5], [Resultado6]),(7+4*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1],S[33]: Resultado8[1],S[34]: Resultado8[3],S[35]: Resultado3[3],S[36]: Resultado4[3],S[37]: Resultado5[3],S[38]: Resultado6[3],S[39]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado7[1], Sg[32]),(T[33], Resultado8[1], Sg[33]),(T[34], Resultado8[3], Sg[34]),(T[35], Resultado3[3], Sg[35]),(T[36], Resultado4[3], Sg[36]),(T[37], Resultado5[3], Sg[37]),(T[38], Resultado6[3], Sg[38]),(T[39], Resultado7[3], Sg[39])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[232])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[233])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[234])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[235])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+4*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+4*A, [5], [Resultado9]),(4+4*A, [5], [Resultado10]),(5+4*A, [5], [Resultado11]),(6+4*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1],S[33]: Resultado12[1],S[34]: Resultado8[3],S[35]: Resultado9[3],S[36]: Resultado10[3],S[37]: Resultado11[3],S[38]: Resultado12[3],S[39]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado7[1], Sg[32]),(T[33], Resultado12[1], Sg[33]),(T[34], Resultado8[3], Sg[34]),(T[35], Resultado9[3], Sg[35]),(T[36], Resultado10[3], Sg[36]), (T[37], Resultado11[3], Sg[37]), (T[38], Resultado12[3], Sg[38]), (T[39], Resultado7[3], Sg[39])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[236])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[237])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[238])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[239])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+4*A, [4], [Resultado13]),(2+4*A, [5], [Resultado16]),(3+4*A, [5], [Resultado14]),(4+4*A, [5], [Resultado15]),(5+4*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4----------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1], S[33]: Resultado13[1], S[34]: Resultado16[1],S[35]: Resultado14[3], S[36]: Resultado15[3], S[37]: Resultado16[3],S[38]: Resultado12[3], S[39]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[32], Resultado7[1], Sg[32]), (T[33], Resultado13[1], Sg[33]),(T[34], Resultado16[1], Sg[34]), (T[35], Resultado14[3], Sg[35]),(T[36], Resultado15[3], Sg[36]), (T[37], Resultado16[3], Sg[37]),(T[38], Resultado12[3], Sg[38]), (T[39], Resultado13[3], Sg[39])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[240])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[241])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[242])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[243])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+4*A, [4, 4], [Resultado17, Resultado18]),(3+4*A, [4, 4], [Resultado19, Resultado20]),(4+4*A, [5], [Resultado19]),(5+4*A, [5], [Resultado20]),(6+4*A, [5], [Resultado17]),(7+4*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1],S[33]: Resultado13[1], S[34]: Resultado18[1], S[35]: Resultado20[1], S[36]: Resultado19[3], S[37]: Resultado20[3], S[38]: Resultado17[3], S[39]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado7[1], Sg[32]),(T[33], Resultado13[1], Sg[33]),(T[34], Resultado18[1], Sg[34]),(T[35], Resultado20[1], Sg[35]),(T[36], Resultado19[3], Sg[36]),(T[37], Resultado20[3], Sg[37]),(T[38], Resultado17[3], Sg[38]),(T[39], Resultado18[3], Sg[39]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[244])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[245])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[246])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[247])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+4*A, 4, Resultado22),(4+4*A, 4, Resultado24),(5+4*A, 5, Resultado23),(6+4*A, 5, Resultado24),(7+4*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1],S[33]: Resultado13[1],S[34]: Resultado18[1],S[35]: Resultado22[1],S[36]: Resultado24[1],S[37]: Resultado23[3],S[38]: Resultado24[3],S[39]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado7[1], Sg[32]),(T[33], Resultado13[1], Sg[33]),(T[34], Resultado18[1], Sg[34]), (T[35], Resultado22[1], Sg[35]), (T[36], Resultado24[1], Sg[36]), (T[37], Resultado23[3], Sg[37]), (T[38], Resultado24[3], Sg[38]), (T[39], Resultado22[3], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[248])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[249])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[250])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[251])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+4*A, [4], [Resultado25]),(5+4*A, [4, 4], [Resultado26, Resultado27]),(6+4*A, [5, 4], [Resultado26, Resultado28]),(7+4*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado7[1], S[33]: Resultado13[1], S[34]: Resultado18[1], S[35]: Resultado22[1], S[36]: Resultado25[1], S[37]: Resultado27[1], S[38]: Resultado28[1], S[39]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado7[1], Sg[32]),(T[33], Resultado13[1], Sg[33]), (T[34], Resultado18[1], Sg[34]), (T[35], Resultado22[1], Sg[35]), (T[36], Resultado25[1], Sg[36]), (T[37], Resultado27[1], Sg[37]), (T[38], Resultado28[1], Sg[38]), (T[39], Resultado28[3], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[252])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[253])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[254])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[255])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+4*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+4*A, [4], [Resultado29]),(2+4*A, [4], [Resultado30]),(3+4*A, [4], [Resultado31]),(4+4*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado32[3], S[33]: Resultado29[1], S[34]: Resultado30[1], S[35]: Resultado31[1], S[36]: Resultado32[1], S[37]: Resultado27[1], S[38]: Resultado28[1], S[39]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado32[3], Sg[32]), (T[33], Resultado29[1], Sg[33]),  (T[34], Resultado30[1], Sg[34]),  (T[35], Resultado31[1], Sg[35]),  (T[36], Resultado32[1], Sg[36]),  (T[37], Resultado27[1], Sg[37]),  (T[38], Resultado28[1], Sg[38]),  (T[39], Resultado28[3], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for i, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f'{i}º {time} - Pontuação: {pontos}, Saldo de Gols: {saldo}')
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[256])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[257])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[258])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[259])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+4*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+4*A, [5], [Resultado36]),(2+4*A, [4], [Resultado36]),(5+4*A, [4], [Resultado33]),(6+4*A, [4], [Resultado34]),(7+4*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado35[3], S[33]: Resultado36[3], S[34]: Resultado36[1], S[35]: Resultado31[1], S[36]: Resultado32[1], S[37]: Resultado33[1], S[38]: Resultado34[1], S[39]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado35[3], Sg[32]), (T[33], Resultado36[3], Sg[33]), (T[34], Resultado36[1], Sg[34]), (T[35], Resultado31[1], Sg[35]), (T[36], Resultado32[1], Sg[36]), (T[37], Resultado33[1], Sg[37]), (T[38], Resultado34[1], Sg[38]), (T[39], Resultado35[1], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[260])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[261])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[262])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[263])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+4*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+4*A, [4], [Resultado37]),(4+4*A, [4], [Resultado38]),(5+4*A, [4], [Resultado39]),(6+4*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado35[3], S[33]: Resultado40[3], S[34]: Resultado36[1],  S[35]: Resultado37[1], S[36]: Resultado38[1], S[37]: Resultado39[1],  S[38]: Resultado40[1],  S[39]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado35[3], Sg[32]),  (T[33], Resultado40[3], Sg[33]), (T[34], Resultado36[1], Sg[34]), (T[35], Resultado37[1], Sg[35]), (T[36], Resultado38[1], Sg[36]), (T[37], Resultado39[1], Sg[37]), (T[38], Resultado40[1], Sg[38]), (T[39], Resultado35[1], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[264])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[265])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[266])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[267])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+4*A, [5], [Resultado41]),(2+4*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+4*A, [4], [Resultado42]),(4+4*A, [4], [Resultado43]), (5+4*A, [4], [Resultado44]),(7+4*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[32]: Resultado35[3],S[33]: Resultado41[3], S[34]: Resultado44[3], S[35]: Resultado42[1], S[36]: Resultado43[1], S[37]: Resultado44[1], S[38]: Resultado40[1], S[39]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado35[3], Sg[32]), (T[33], Resultado41[3], Sg[33]), (T[34], Resultado44[3], Sg[34]), (T[35], Resultado42[1], Sg[35]), (T[36], Resultado43[1], Sg[36]), (T[37], Resultado44[1], Sg[37]), (T[38], Resultado40[1], Sg[38]), (T[39], Resultado41[1], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[268])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[269])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[270])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[271])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+4*A, [5, 5], [Resultado45, Resultado46]), (3+4*A, [5, 5], [Resultado47, Resultado48]), (4+4*A, [4], [Resultado47]), (5+4*A, [4], [Resultado48]),(6+4*A, [4], [Resultado45]), (7+4*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado35[3], S[33]: Resultado41[3], S[34]: Resultado46[3], S[35]: Resultado48[3], S[36]: Resultado47[1], S[37]: Resultado48[1], S[38]: Resultado45[1], S[39]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado35[3], Sg[32]), (T[33], Resultado41[3], Sg[33]), (T[34], Resultado46[3], Sg[34]), (T[35], Resultado48[3], Sg[35]), (T[36], Resultado47[1], Sg[36]), (T[37], Resultado48[1], Sg[37]), (T[38], Resultado45[1], Sg[38]), (T[39], Resultado46[1], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[272])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[273])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[274])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[275])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+4*A, [5, 5], [Resultado49, Resultado50]),(4+4*A, [5, 5], [Resultado51, Resultado52]), (5+4*A, [4], [Resultado51]),(6+4*A, [4, 4], [Resultado49, Resultado52]),(7+4*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[32]: Resultado35[3], S[33]: Resultado41[3], S[34]: Resultado46[3], S[35]: Resultado50[3], S[36]: Resultado52[3], S[37]: Resultado51[1], S[38]: Resultado52[1], S[39]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[32], Resultado35[3], Sg[32]), (T[33], Resultado41[3], Sg[33]), (T[34], Resultado46[3], Sg[34]), (T[35], Resultado50[3], Sg[35]), (T[36], Resultado52[3], Sg[36]), (T[37], Resultado51[1], Sg[37]), (T[38], Resultado52[1], Sg[38]), (T[39], Resultado50[1], Sg[39])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[276])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[277])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[278])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[279])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+4*A, [5], [Resultado53]), (5+4*A, [5, 5], [Resultado54, Resultado55]), (6+4*A, [4, 5], [Resultado54, Resultado56]), (7+4*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[32]: Resultado35[3], S[33]: Resultado41[3], S[34]: Resultado46[3], S[35]: Resultado50[3], S[36]: Resultado53[3], S[37]: Resultado55[3],  S[38]: Resultado56[3], S[39]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[32], Resultado35[3], Sg[32]), (T[33], Resultado41[3], Sg[33]), (T[34], Resultado46[3], Sg[34]), (T[35], Resultado50[3], Sg[35]), (T[36], Resultado53[3], Sg[36]), (T[37], Resultado55[3], Sg[37]), (T[38], Resultado56[3], Sg[38]), (T[39], Resultado56[1], Sg[39])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG5 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 5 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG5)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG5 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 5 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG5)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
        
print('---------------------------------GRUPO 6----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[280])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[281])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[282])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[283])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+5*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+5*A, [5], [Resultado1]),(2+5*A, [5], [Resultado2]),(3+5*A, [5], [Resultado3]),(4+5*A, [5], [Resultado4]),(5+5*A, [0], []),(6+5*A, [0], []),(7+5*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado4[1],S[41]: Resultado1[3],S[42]: Resultado2[3],S[43]: Resultado3[3],S[44]: Resultado4[3],S[45]: P[5],S[46]: P[6],S[47]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado4[1], Sg[40]),(T[41], Resultado1[3], Sg[41]),(T[42], Resultado2[3], Sg[42]),(T[43], Resultado3[3], Sg[43]),(T[44], Resultado4[3], Sg[44]),(T[45], P[5], Sg[45]),(T[46], P[6], Sg[46]),(T[47], P[7], Sg[47])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[284])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[285])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[286])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[287])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+5*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+5*A, [4], [Resultado8]),(2+5*A, [5], [Resultado8]),(3+5*A, [5], [Resultado3]),(4+5*A, [5], [Resultado4]),(5+5*A, [5], [Resultado5]),(6+5*A, [5], [Resultado6]),(7+5*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1],S[41]: Resultado8[1],S[42]: Resultado8[3],S[43]: Resultado3[3],S[44]: Resultado4[3],S[45]: Resultado5[3],S[46]: Resultado6[3],S[47]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado7[1], Sg[40]),(T[41], Resultado8[1], Sg[41]),(T[42], Resultado8[3], Sg[42]),(T[43], Resultado3[3], Sg[43]),(T[44], Resultado4[3], Sg[44]),(T[45], Resultado5[3], Sg[45]),(T[46], Resultado6[3], Sg[46]),(T[47], Resultado7[3], Sg[47])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[288])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[289])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[290])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[291])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+5*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+5*A, [5], [Resultado9]),(4+5*A, [5], [Resultado10]),(5+5*A, [5], [Resultado11]),(6+5*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1],S[41]: Resultado12[1],S[42]: Resultado8[3],S[43]: Resultado9[3],S[44]: Resultado10[3],S[45]: Resultado11[3],S[46]: Resultado12[3],S[47]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado7[1], Sg[40]),(T[41], Resultado12[1], Sg[41]),(T[42], Resultado8[3], Sg[42]),(T[43], Resultado9[3], Sg[43]),(T[44], Resultado10[3], Sg[44]), (T[45], Resultado11[3], Sg[45]), (T[46], Resultado12[3], Sg[46]), (T[47], Resultado7[3], Sg[47])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[292])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[293])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[294])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[295])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+5*A, [4], [Resultado13]),(2+5*A, [5], [Resultado16]),(3+5*A, [5], [Resultado14]),(4+5*A, [5], [Resultado15]),(5+5*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4----------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1], S[41]: Resultado13[1], S[42]: Resultado16[1],S[43]: Resultado14[3], S[44]: Resultado15[3], S[45]: Resultado16[3],S[46]: Resultado12[3], S[47]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[40], Resultado7[1], Sg[40]), (T[41], Resultado13[1], Sg[41]),(T[42], Resultado16[1], Sg[42]), (T[43], Resultado14[3], Sg[43]),(T[44], Resultado15[3], Sg[44]), (T[45], Resultado16[3], Sg[45]),(T[46], Resultado12[3], Sg[46]), (T[47], Resultado13[3], Sg[47])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[296])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[297])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[298])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[299])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+5*A, [4, 4], [Resultado17, Resultado18]),(3+5*A, [4, 4], [Resultado19, Resultado20]),(4+5*A, [5], [Resultado19]),(5+5*A, [5], [Resultado20]),(6+5*A, [5], [Resultado17]),(7+5*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1],S[41]: Resultado13[1], S[42]: Resultado18[1], S[43]: Resultado20[1], S[44]: Resultado19[3], S[45]: Resultado20[3], S[46]: Resultado17[3], S[47]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado7[1], Sg[40]),(T[41], Resultado13[1], Sg[41]),(T[42], Resultado18[1], Sg[42]),(T[43], Resultado20[1], Sg[43]),(T[44], Resultado19[3], Sg[44]),(T[45], Resultado20[3], Sg[45]),(T[46], Resultado17[3], Sg[46]),(T[47], Resultado18[3], Sg[47]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[300])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[301])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[302])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[303])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+5*A, 4, Resultado22),(4+5*A, 4, Resultado24),(5+5*A, 5, Resultado23),(6+5*A, 5, Resultado24),(7+5*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1],S[41]: Resultado13[1],S[42]: Resultado18[1],S[43]: Resultado22[1],S[44]: Resultado24[1],S[45]: Resultado23[3],S[46]: Resultado24[3],S[47]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado7[1], Sg[40]),(T[41], Resultado13[1], Sg[41]),(T[42], Resultado18[1], Sg[42]), (T[43], Resultado22[1], Sg[43]), (T[44], Resultado24[1], Sg[44]), (T[45], Resultado23[3], Sg[45]), (T[46], Resultado24[3], Sg[46]), (T[47], Resultado22[3], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[304])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[305])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[306])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[307])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+5*A, [4], [Resultado25]),(5+5*A, [4, 4], [Resultado26, Resultado27]),(6+5*A, [5, 4], [Resultado26, Resultado28]),(7+5*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado7[1], S[41]: Resultado13[1], S[42]: Resultado18[1], S[43]: Resultado22[1], S[44]: Resultado25[1], S[45]: Resultado27[1], S[46]: Resultado28[1], S[47]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado7[1], Sg[40]),(T[41], Resultado13[1], Sg[41]), (T[42], Resultado18[1], Sg[42]), (T[43], Resultado22[1], Sg[43]), (T[44], Resultado25[1], Sg[44]), (T[45], Resultado27[1], Sg[45]), (T[46], Resultado28[1], Sg[46]), (T[47], Resultado28[3], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[308])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[309])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[310])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[311])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+5*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+5*A, [4], [Resultado29]),(2+5*A, [4], [Resultado30]),(3+5*A, [4], [Resultado31]),(4+5*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado32[3], S[41]: Resultado29[1], S[42]: Resultado30[1], S[43]: Resultado31[1], S[44]: Resultado32[1], S[45]: Resultado27[1], S[46]: Resultado28[1], S[47]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado32[3], Sg[40]), (T[41], Resultado29[1], Sg[41]),  (T[42], Resultado30[1], Sg[42]),  (T[43], Resultado31[1], Sg[43]),  (T[44], Resultado32[1], Sg[44]),  (T[45], Resultado27[1], Sg[45]),  (T[46], Resultado28[1], Sg[46]),  (T[47], Resultado28[3], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for i, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f'{i}º {time} - Pontuação: {pontos}, Saldo de Gols: {saldo}')
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[312])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[313])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[314])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[315])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+5*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+5*A, [5], [Resultado36]),(2+5*A, [4], [Resultado36]),(5+5*A, [4], [Resultado33]),(6+5*A, [4], [Resultado34]),(7+5*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado35[3], S[41]: Resultado36[3], S[42]: Resultado36[1], S[43]: Resultado31[1], S[44]: Resultado32[1], S[45]: Resultado33[1], S[46]: Resultado34[1], S[47]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado35[3], Sg[40]), (T[41], Resultado36[3], Sg[41]), (T[42], Resultado36[1], Sg[42]), (T[43], Resultado31[1], Sg[43]), (T[44], Resultado32[1], Sg[44]), (T[45], Resultado33[1], Sg[45]), (T[46], Resultado34[1], Sg[46]), (T[47], Resultado35[1], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[316])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[317])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[318])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[319])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+5*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+5*A, [4], [Resultado37]),(4+5*A, [4], [Resultado38]),(5+5*A, [4], [Resultado39]),(6+5*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado35[3], S[41]: Resultado40[3], S[42]: Resultado36[1],  S[43]: Resultado37[1], S[44]: Resultado38[1], S[45]: Resultado39[1],  S[46]: Resultado40[1],  S[47]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado35[3], Sg[40]),  (T[41], Resultado40[3], Sg[41]), (T[42], Resultado36[1], Sg[42]), (T[43], Resultado37[1], Sg[43]), (T[44], Resultado38[1], Sg[44]), (T[45], Resultado39[1], Sg[45]), (T[46], Resultado40[1], Sg[46]), (T[47], Resultado35[1], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[320])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[321])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[322])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[323])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+5*A, [5], [Resultado41]),(2+5*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+5*A, [4], [Resultado42]),(4+5*A, [4], [Resultado43]), (5+5*A, [4], [Resultado44]),(7+5*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[40]: Resultado35[3],S[41]: Resultado41[3], S[42]: Resultado44[3], S[43]: Resultado42[1], S[44]: Resultado43[1], S[45]: Resultado44[1], S[46]: Resultado40[1], S[47]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado35[3], Sg[40]), (T[41], Resultado41[3], Sg[41]), (T[42], Resultado44[3], Sg[42]), (T[43], Resultado42[1], Sg[43]), (T[44], Resultado43[1], Sg[44]), (T[45], Resultado44[1], Sg[45]), (T[46], Resultado40[1], Sg[46]), (T[47], Resultado41[1], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[324])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[325])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[326])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[327])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+5*A, [5, 5], [Resultado45, Resultado46]), (3+5*A, [5, 5], [Resultado47, Resultado48]), (4+5*A, [4], [Resultado47]), (5+5*A, [4], [Resultado48]),(6+5*A, [4], [Resultado45]), (7+5*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado35[3], S[41]: Resultado41[3], S[42]: Resultado46[3], S[43]: Resultado48[3], S[44]: Resultado47[1], S[45]: Resultado48[1], S[46]: Resultado45[1], S[47]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado35[3], Sg[40]), (T[41], Resultado41[3], Sg[41]), (T[42], Resultado46[3], Sg[42]), (T[43], Resultado48[3], Sg[43]), (T[44], Resultado47[1], Sg[44]), (T[45], Resultado48[1], Sg[45]), (T[46], Resultado45[1], Sg[46]), (T[47], Resultado46[1], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[328])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[329])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[330])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[331])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+5*A, [5, 5], [Resultado49, Resultado50]),(4+5*A, [5, 5], [Resultado51, Resultado52]), (5+5*A, [4], [Resultado51]),(6+5*A, [4, 4], [Resultado49, Resultado52]),(7+5*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[40]: Resultado35[3], S[41]: Resultado41[3], S[42]: Resultado46[3], S[43]: Resultado50[3], S[44]: Resultado52[3], S[45]: Resultado51[1], S[46]: Resultado52[1], S[47]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[40], Resultado35[3], Sg[40]), (T[41], Resultado41[3], Sg[41]), (T[42], Resultado46[3], Sg[42]), (T[43], Resultado50[3], Sg[43]), (T[44], Resultado52[3], Sg[44]), (T[45], Resultado51[1], Sg[45]), (T[46], Resultado52[1], Sg[46]), (T[47], Resultado50[1], Sg[47])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[332])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[333])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[334])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[335])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+5*A, [5], [Resultado53]), (5+5*A, [5, 5], [Resultado54, Resultado55]), (6+5*A, [4, 5], [Resultado54, Resultado56]), (7+5*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[40]: Resultado35[3], S[41]: Resultado41[3], S[42]: Resultado46[3], S[43]: Resultado50[3], S[44]: Resultado53[3], S[45]: Resultado55[3],  S[46]: Resultado56[3], S[47]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[40], Resultado35[3], Sg[40]), (T[41], Resultado41[3], Sg[41]), (T[42], Resultado46[3], Sg[42]), (T[43], Resultado50[3], Sg[43]), (T[44], Resultado53[3], Sg[44]), (T[45], Resultado55[3], Sg[45]), (T[46], Resultado56[3], Sg[46]), (T[47], Resultado56[1], Sg[47])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG6 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 6 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG6)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG6 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 6 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG6)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 7----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[336])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[337])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[338])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[339])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+6*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+6*A, [5], [Resultado1]),(2+6*A, [5], [Resultado2]),(3+6*A, [5], [Resultado3]),(4+6*A, [5], [Resultado4]),(5+6*A, [0], []),(6+6*A, [0], []),(7+6*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado4[1],S[49]: Resultado1[3],S[50]: Resultado2[3],S[51]: Resultado3[3],S[52]: Resultado4[3],S[53]: P[5],S[54]: P[6],S[55]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado4[1], Sg[48]),(T[49], Resultado1[3], Sg[49]),(T[50], Resultado2[3], Sg[50]),(T[51], Resultado3[3], Sg[51]),(T[52], Resultado4[3], Sg[52]),(T[53], P[5], Sg[53]),(T[54], P[6], Sg[54]),(T[55], P[7], Sg[55])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[340])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[341])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[342])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[343])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+6*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+6*A, [4], [Resultado8]),(2+6*A, [5], [Resultado8]),(3+6*A, [5], [Resultado3]),(4+6*A, [5], [Resultado4]),(5+6*A, [5], [Resultado5]),(6+6*A, [5], [Resultado6]),(7+6*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1],S[49]: Resultado8[1],S[50]: Resultado8[3],S[51]: Resultado3[3],S[52]: Resultado4[3],S[53]: Resultado5[3],S[54]: Resultado6[3],S[55]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado7[1], Sg[48]),(T[49], Resultado8[1], Sg[49]),(T[50], Resultado8[3], Sg[50]),(T[51], Resultado3[3], Sg[51]),(T[52], Resultado4[3], Sg[52]),(T[53], Resultado5[3], Sg[53]),(T[54], Resultado6[3], Sg[54]),(T[55], Resultado7[3], Sg[55])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[344])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[345])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[346])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[347])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+6*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+6*A, [5], [Resultado9]),(4+6*A, [5], [Resultado10]),(5+6*A, [5], [Resultado11]),(6+6*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1],S[49]: Resultado12[1],S[50]: Resultado8[3],S[51]: Resultado9[3],S[52]: Resultado10[3],S[53]: Resultado11[3],S[54]: Resultado12[3],S[55]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado7[1], Sg[48]),(T[49], Resultado12[1], Sg[49]),(T[50], Resultado8[3], Sg[50]),(T[51], Resultado9[3], Sg[51]),(T[52], Resultado10[3], Sg[52]), (T[53], Resultado11[3], Sg[53]), (T[54], Resultado12[3], Sg[54]), (T[55], Resultado7[3], Sg[55])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[348])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[349])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[350])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[351])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+6*A, [4], [Resultado13]),(2+6*A, [5], [Resultado16]),(3+6*A, [5], [Resultado14]),(4+6*A, [5], [Resultado15]),(5+6*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4----------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1], S[49]: Resultado13[1], S[50]: Resultado16[1],S[51]: Resultado14[3], S[52]: Resultado15[3], S[53]: Resultado16[3],S[54]: Resultado12[3], S[55]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[48], Resultado7[1], Sg[48]), (T[49], Resultado13[1], Sg[49]),(T[50], Resultado16[1], Sg[50]), (T[51], Resultado14[3], Sg[51]),(T[52], Resultado15[3], Sg[52]), (T[53], Resultado16[3], Sg[53]),(T[54], Resultado12[3], Sg[54]), (T[55], Resultado13[3], Sg[55])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[352])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[353])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[354])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[355])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+6*A, [4, 4], [Resultado17, Resultado18]),(3+6*A, [4, 4], [Resultado19, Resultado20]),(4+6*A, [5], [Resultado19]),(5+6*A, [5], [Resultado20]),(6+6*A, [5], [Resultado17]),(7+6*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1],S[49]: Resultado13[1], S[50]: Resultado18[1], S[51]: Resultado20[1], S[52]: Resultado19[3], S[53]: Resultado20[3], S[54]: Resultado17[3], S[55]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado7[1], Sg[48]),(T[49], Resultado13[1], Sg[49]),(T[50], Resultado18[1], Sg[50]),(T[51], Resultado20[1], Sg[51]),(T[52], Resultado19[3], Sg[52]),(T[53], Resultado20[3], Sg[53]),(T[54], Resultado17[3], Sg[54]),(T[55], Resultado18[3], Sg[55]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[356])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[357])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[358])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[359])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+6*A, 4, Resultado22),(4+6*A, 4, Resultado24),(5+6*A, 5, Resultado23),(6+6*A, 5, Resultado24),(7+6*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1],S[49]: Resultado13[1],S[50]: Resultado18[1],S[51]: Resultado22[1],S[52]: Resultado24[1],S[53]: Resultado23[3],S[54]: Resultado24[3],S[55]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado7[1], Sg[48]),(T[49], Resultado13[1], Sg[49]),(T[50], Resultado18[1], Sg[50]), (T[51], Resultado22[1], Sg[51]), (T[52], Resultado24[1], Sg[52]), (T[53], Resultado23[3], Sg[53]), (T[54], Resultado24[3], Sg[54]), (T[55], Resultado22[3], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[360])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[361])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[362])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[363])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+6*A, [4], [Resultado25]),(5+6*A, [4, 4], [Resultado26, Resultado27]),(6+6*A, [5, 4], [Resultado26, Resultado28]),(7+6*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado7[1], S[49]: Resultado13[1], S[50]: Resultado18[1], S[51]: Resultado22[1], S[52]: Resultado25[1], S[53]: Resultado27[1], S[54]: Resultado28[1], S[55]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado7[1], Sg[48]),(T[49], Resultado13[1], Sg[49]), (T[50], Resultado18[1], Sg[50]), (T[51], Resultado22[1], Sg[51]), (T[52], Resultado25[1], Sg[52]), (T[53], Resultado27[1], Sg[53]), (T[54], Resultado28[1], Sg[54]), (T[55], Resultado28[3], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[364])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[365])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[366])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[367])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+6*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+6*A, [4], [Resultado29]),(2+6*A, [4], [Resultado30]),(3+6*A, [4], [Resultado31]),(4+6*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado32[3], S[49]: Resultado29[1], S[50]: Resultado30[1], S[51]: Resultado31[1], S[52]: Resultado32[1], S[53]: Resultado27[1], S[54]: Resultado28[1], S[55]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado32[3], Sg[48]), (T[49], Resultado29[1], Sg[49]),  (T[50], Resultado30[1], Sg[50]),  (T[51], Resultado31[1], Sg[51]),  (T[52], Resultado32[1], Sg[52]),  (T[53], Resultado27[1], Sg[53]),  (T[54], Resultado28[1], Sg[54]),  (T[55], Resultado28[3], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for i, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f'{i}º {time} - Pontuação: {pontos}, Saldo de Gols: {saldo}')
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[368])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[369])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[370])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[371])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+6*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+6*A, [5], [Resultado36]),(2+6*A, [4], [Resultado36]),(5+6*A, [4], [Resultado33]),(6+6*A, [4], [Resultado34]),(7+6*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado35[3], S[49]: Resultado36[3], S[50]: Resultado36[1], S[51]: Resultado31[1], S[52]: Resultado32[1], S[53]: Resultado33[1], S[54]: Resultado34[1], S[55]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado35[3], Sg[48]), (T[49], Resultado36[3], Sg[49]), (T[50], Resultado36[1], Sg[50]), (T[51], Resultado31[1], Sg[51]), (T[52], Resultado32[1], Sg[52]), (T[53], Resultado33[1], Sg[53]), (T[54], Resultado34[1], Sg[54]), (T[55], Resultado35[1], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[372])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[373])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[374])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[375])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+6*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+6*A, [4], [Resultado37]),(4+6*A, [4], [Resultado38]),(5+6*A, [4], [Resultado39]),(6+6*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado35[3], S[49]: Resultado40[3], S[50]: Resultado36[1],  S[51]: Resultado37[1], S[52]: Resultado38[1], S[53]: Resultado39[1],  S[54]: Resultado40[1],  S[55]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado35[3], Sg[48]),  (T[49], Resultado40[3], Sg[49]), (T[50], Resultado36[1], Sg[50]), (T[51], Resultado37[1], Sg[51]), (T[52], Resultado38[1], Sg[52]), (T[53], Resultado39[1], Sg[53]), (T[54], Resultado40[1], Sg[54]), (T[55], Resultado35[1], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[376])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[377])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[378])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[379])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+6*A, [5], [Resultado41]),(2+6*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+6*A, [4], [Resultado42]),(4+6*A, [4], [Resultado43]), (5+6*A, [4], [Resultado44]),(7+6*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[48]: Resultado35[3],S[49]: Resultado41[3], S[50]: Resultado44[3], S[51]: Resultado42[1], S[52]: Resultado43[1], S[53]: Resultado44[1], S[54]: Resultado40[1], S[55]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado35[3], Sg[48]), (T[49], Resultado41[3], Sg[49]), (T[50], Resultado44[3], Sg[50]), (T[51], Resultado42[1], Sg[51]), (T[52], Resultado43[1], Sg[52]), (T[53], Resultado44[1], Sg[53]), (T[54], Resultado40[1], Sg[54]), (T[55], Resultado41[1], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[380])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[381])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[382])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[383])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+6*A, [5, 5], [Resultado45, Resultado46]), (3+6*A, [5, 5], [Resultado47, Resultado48]), (4+6*A, [4], [Resultado47]), (5+6*A, [4], [Resultado48]),(6+6*A, [4], [Resultado45]), (7+6*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado35[3], S[49]: Resultado41[3], S[50]: Resultado46[3], S[51]: Resultado48[3], S[52]: Resultado47[1], S[53]: Resultado48[1], S[54]: Resultado45[1], S[55]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado35[3], Sg[48]), (T[49], Resultado41[3], Sg[49]), (T[50], Resultado46[3], Sg[50]), (T[51], Resultado48[3], Sg[51]), (T[52], Resultado47[1], Sg[52]), (T[53], Resultado48[1], Sg[53]), (T[54], Resultado45[1], Sg[54]), (T[55], Resultado46[1], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[384])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[385])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[386])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[387])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+6*A, [5, 5], [Resultado49, Resultado50]),(4+6*A, [5, 5], [Resultado51, Resultado52]), (5+6*A, [4], [Resultado51]),(6+6*A, [4, 4], [Resultado49, Resultado52]),(7+6*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[48]: Resultado35[3], S[49]: Resultado41[3], S[50]: Resultado46[3], S[51]: Resultado50[3], S[52]: Resultado52[3], S[53]: Resultado51[1], S[54]: Resultado52[1], S[55]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[48], Resultado35[3], Sg[48]), (T[49], Resultado41[3], Sg[49]), (T[50], Resultado46[3], Sg[50]), (T[51], Resultado50[3], Sg[51]), (T[52], Resultado52[3], Sg[52]), (T[53], Resultado51[1], Sg[53]), (T[54], Resultado52[1], Sg[54]), (T[55], Resultado50[1], Sg[55])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[388])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[389])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[390])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[391])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+6*A, [5], [Resultado53]), (5+6*A, [5, 5], [Resultado54, Resultado55]), (6+6*A, [4, 5], [Resultado54, Resultado56]), (7+6*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[48]: Resultado35[3], S[49]: Resultado41[3], S[50]: Resultado46[3], S[51]: Resultado50[3], S[52]: Resultado53[3], S[53]: Resultado55[3],  S[54]: Resultado56[3], S[55]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[48], Resultado35[3], Sg[48]), (T[49], Resultado41[3], Sg[49]), (T[50], Resultado46[3], Sg[50]), (T[51], Resultado50[3], Sg[51]), (T[52], Resultado53[3], Sg[52]), (T[53], Resultado55[3], Sg[53]), (T[54], Resultado56[3], Sg[54]), (T[55], Resultado56[1], Sg[55])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG7 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 7 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG7)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG7 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 7 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG7)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print('---------------------------------GRUPO 8----------------------------')

Resultado1 = rodada_princ_pênaltis_PC(p[392])
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

Resultado2 = rodada_princ_pênaltis_PC(p[393])
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

Resultado3 = rodada_princ_pênaltis_PC(p[394])
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

Resultado4 = rodada_princ_pênaltis_PC(p[395])
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

operacoes = [(0+7*A, [4, 4, 4, 4], [Resultado1, Resultado2, Resultado3, Resultado4]),(1+7*A, [5], [Resultado1]),(2+7*A, [5], [Resultado2]),(3+7*A, [5], [Resultado3]),(4+7*A, [5], [Resultado4]),(5+7*A, [0], []),(6+7*A, [0], []),(7+7*A, [0], [])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] = sum(resultado[i] for i, resultado in zip(indices, resultados)) if resultados else 0

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado4[1],S[57]: Resultado1[3],S[58]: Resultado2[3],S[59]: Resultado3[3],S[60]: Resultado4[3],S[61]: P[5],S[62]: P[6],S[63]: P[7]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado4[1], Sg[56]),(T[57], Resultado1[3], Sg[57]),(T[58], Resultado2[3], Sg[58]),(T[59], Resultado3[3], Sg[59]),(T[60], Resultado4[3], Sg[60]),(T[61], P[5], Sg[61]),(T[62], P[6], Sg[62]),(T[63], P[7], Sg[63])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 2!!')
        
Resultado5 = rodada_princ_pênaltis_PC(p[396])
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

Resultado6 = rodada_princ_pênaltis_PC(p[397])
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

Resultado7 = rodada_princ_pênaltis_PC(p[398])
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

Resultado8 = rodada_princ_pênaltis_PC(p[399])
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

operacoes = [(0+7*A, [4, 4, 4], [Resultado5, Resultado6, Resultado7]),(1+7*A, [4], [Resultado8]),(2+7*A, [5], [Resultado8]),(3+7*A, [5], [Resultado3]),(4+7*A, [5], [Resultado4]),(5+7*A, [5], [Resultado5]),(6+7*A, [5], [Resultado6]),(7+7*A, [5], [Resultado7])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 2 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1],S[57]: Resultado8[1],S[58]: Resultado8[3],S[59]: Resultado3[3],S[60]: Resultado4[3],S[61]: Resultado5[3],S[62]: Resultado6[3],S[63]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado7[1], Sg[56]),(T[57], Resultado8[1], Sg[57]),(T[58], Resultado8[3], Sg[58]),(T[59], Resultado3[3], Sg[59]),(T[60], Resultado4[3], Sg[60]),(T[61], Resultado5[3], Sg[61]),(T[62], Resultado6[3], Sg[62]),(T[63], Resultado7[3], Sg[63])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 3!!')        

Resultado9 = rodada_princ_pênaltis_PC(p[400])
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

Resultado10 = rodada_princ_pênaltis_PC(p[401])
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

Resultado11 = rodada_princ_pênaltis_PC(p[402])
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

Resultado12 = rodada_princ_pênaltis_PC(p[403])
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])

operacoes = [(1+7*A, [4, 4, 4, 4], [Resultado9, Resultado10, Resultado11, Resultado12]), (3+7*A, [5], [Resultado9]),(4+7*A, [5], [Resultado10]),(5+7*A, [5], [Resultado11]),(6+7*A, [5], [Resultado12])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 3 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1],S[57]: Resultado12[1],S[58]: Resultado8[3],S[59]: Resultado9[3],S[60]: Resultado10[3],S[61]: Resultado11[3],S[62]: Resultado12[3],S[63]: Resultado7[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado7[1], Sg[56]),(T[57], Resultado12[1], Sg[57]),(T[58], Resultado8[3], Sg[58]),(T[59], Resultado9[3], Sg[59]),(T[60], Resultado10[3], Sg[60]), (T[61], Resultado11[3], Sg[61]), (T[62], Resultado12[3], Sg[62]), (T[63], Resultado7[3], Sg[63])]
    tabela_resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 4!!')        

Resultado13 = rodada_princ_pênaltis_PC(p[404])
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

Resultado14 = rodada_princ_pênaltis_PC(p[405])
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

Resultado15 = rodada_princ_pênaltis_PC(p[406])
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

Resultado16 = rodada_princ_pênaltis_PC(p[407])
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

operacoes = [(1+7*A, [4], [Resultado13]),(2+7*A, [5], [Resultado16]),(3+7*A, [5], [Resultado14]),(4+7*A, [5], [Resultado15]),(5+7*A, [5], [Resultado16])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 4----------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1], S[57]: Resultado13[1], S[58]: Resultado16[1],S[59]: Resultado14[3], S[60]: Resultado15[3], S[61]: Resultado16[3],S[62]: Resultado12[3], S[63]: Resultado13[3]}
    for time, pontos in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    resultados = [(T[56], Resultado7[1], Sg[56]), (T[57], Resultado13[1], Sg[57]),(T[58], Resultado16[1], Sg[58]), (T[59], Resultado14[3], Sg[59]),(T[60], Resultado15[3], Sg[60]), (T[61], Resultado16[3], Sg[61]),(T[62], Resultado12[3], Sg[62]), (T[63], Resultado13[3], Sg[63])]
    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(resultados, start=1):
        print(f'{posicao}º, {time}, {pontos}, {saldo}')
elif Permissão == 6:
    print('partiu: rodada 5!!')            

Resultado17 = rodada_princ_pênaltis_PC(p[408])
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

Resultado18 = rodada_princ_pênaltis_PC(p[409])
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

Resultado19 = rodada_princ_pênaltis_PC(p[410])
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

Resultado20 = rodada_princ_pênaltis_PC(p[411])
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

operacoes = [(2+7*A, [4, 4], [Resultado17, Resultado18]),(3+7*A, [4, 4], [Resultado19, Resultado20]),(4+7*A, [5], [Resultado19]),(5+7*A, [5], [Resultado20]),(6+7*A, [5], [Resultado17]),(7+7*A, [5], [Resultado18])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1],S[57]: Resultado13[1], S[58]: Resultado18[1], S[59]: Resultado20[1], S[60]: Resultado19[3], S[61]: Resultado20[3], S[62]: Resultado17[3], S[63]: Resultado18[3],}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(time, pontos)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado7[1], Sg[56]),(T[57], Resultado13[1], Sg[57]),(T[58], Resultado18[1], Sg[58]),(T[59], Resultado20[1], Sg[59]),(T[60], Resultado19[3], Sg[60]),(T[61], Resultado20[3], Sg[61]),(T[62], Resultado17[3], Sg[62]),(T[63], Resultado18[3], Sg[63]),]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 6!!')

Resultado21 = rodada_princ_pênaltis_PC(p[412])
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

Resultado22 = rodada_princ_pênaltis_PC(p[413])
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

Resultado23 = rodada_princ_pênaltis_PC(p[414])
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

Resultado24 = rodada_princ_pênaltis_PC(p[415])
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

operacoes = [(3+7*A, 4, Resultado22),(4+7*A, 4, Resultado24),(5+7*A, 5, Resultado23),(6+7*A, 5, Resultado24),(7+7*A, 5, Resultado22)]
for index_sg, index_resultado, resultado in operacoes:
    Sg[index_sg] += resultado[index_resultado]

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 6 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1],S[57]: Resultado13[1],S[58]: Resultado18[1],S[59]: Resultado22[1],S[60]: Resultado24[1],S[61]: Resultado23[3],S[62]: Resultado24[3],S[63]: Resultado22[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado7[1], Sg[56]),(T[57], Resultado13[1], Sg[57]),(T[58], Resultado18[1], Sg[58]), (T[59], Resultado22[1], Sg[59]), (T[60], Resultado24[1], Sg[60]), (T[61], Resultado23[3], Sg[61]), (T[62], Resultado24[3], Sg[62]), (T[63], Resultado22[3], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 7!!')
            
Resultado25 = rodada_princ_pênaltis_PC(p[416])
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

Resultado26 = rodada_princ_pênaltis_PC(p[417])
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

Resultado27 = rodada_princ_pênaltis_PC(p[418])
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

Resultado28 = rodada_princ_pênaltis_PC(p[419])
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

operacoes = [(4+7*A, [4], [Resultado25]),(5+7*A, [4, 4], [Resultado26, Resultado27]),(6+7*A, [5, 4], [Resultado26, Resultado28]),(7+7*A, [5, 5, 5], [Resultado25, Resultado27, Resultado28])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 7 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado7[1], S[57]: Resultado13[1], S[58]: Resultado18[1], S[59]: Resultado22[1], S[60]: Resultado25[1], S[61]: Resultado27[1], S[62]: Resultado28[1], S[63]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado7[1], Sg[56]),(T[57], Resultado13[1], Sg[57]), (T[58], Resultado18[1], Sg[58]), (T[59], Resultado22[1], Sg[59]), (T[60], Resultado25[1], Sg[60]), (T[61], Resultado27[1], Sg[61]), (T[62], Resultado28[1], Sg[62]), (T[63], Resultado28[3], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 8!!')
        
Resultado29 = rodada_princ_pênaltis_PC(p[420])
Resultado29[1] = Resultado29[1] + Resultado13[1]
Resultado29[3] = Resultado29[3] + (Resultado7[1])
print(Resultado29[0], Resultado29[1])
print(Resultado29[2], Resultado29[3])

Resultado30 = rodada_princ_pênaltis_PC(p[421])
Resultado30[1] = Resultado30[1] + Resultado18[1]
Resultado30[3] = Resultado30[3] + Resultado29[3]
print(Resultado30[0], Resultado30[1])
print(Resultado30[2], Resultado30[3])

Resultado31 = rodada_princ_pênaltis_PC(p[422])
Resultado31[1] = Resultado31[1] + Resultado22[1]
Resultado31[3] = Resultado31[3] + Resultado30[3]
print(Resultado31[0], Resultado31[1])
print(Resultado31[2], Resultado31[3])

Resultado32 = rodada_princ_pênaltis_PC(p[423])
Resultado32[1] = Resultado32[1] + Resultado25[1]
Resultado32[3] = Resultado32[3] + Resultado31[3]
print(Resultado32[0], Resultado32[1])
print(Resultado32[2], Resultado32[3])

operacoes = [(0+7*A, [5, 5, 5, 5], [Resultado29, Resultado30, Resultado31, Resultado32]),(1+7*A, [4], [Resultado29]),(2+7*A, [4], [Resultado30]),(3+7*A, [4], [Resultado31]),(4+7*A, [4], [Resultado32])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 8 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado32[3], S[57]: Resultado29[1], S[58]: Resultado30[1], S[59]: Resultado31[1], S[60]: Resultado32[1], S[61]: Resultado27[1], S[62]: Resultado28[1], S[63]: Resultado28[3]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado32[3], Sg[56]), (T[57], Resultado29[1], Sg[57]),  (T[58], Resultado30[1], Sg[58]),  (T[59], Resultado31[1], Sg[59]),  (T[60], Resultado32[1], Sg[60]),  (T[61], Resultado27[1], Sg[61]),  (T[62], Resultado28[1], Sg[62]),  (T[63], Resultado28[3], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for i, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f'{i}º {time} - Pontuação: {pontos}, Saldo de Gols: {saldo}')
elif Permissão == 6:
    print('partiu: rodada 9!!')
    
Resultado33 = rodada_princ_pênaltis_PC(p[424])
Resultado33[1] = Resultado33[1] + Resultado27[1]
Resultado33[3] = Resultado33[3] + Resultado32[3]
print(Resultado33[0], Resultado33[1])
print(Resultado33[2], Resultado33[3])

Resultado34 = rodada_princ_pênaltis_PC(p[425])
Resultado34[1] = Resultado34[1] + Resultado28[1]
Resultado34[3] = Resultado34[3] + Resultado33[3]
print(Resultado34[0], Resultado34[1])
print(Resultado34[2], Resultado34[3])

Resultado35 = rodada_princ_pênaltis_PC(p[426])
Resultado35[1] = Resultado35[1] + Resultado28[3]
Resultado35[3] = Resultado35[3] + Resultado34[3]
print(Resultado35[0], Resultado35[1])
print(Resultado35[2], Resultado35[3])

Resultado36 = rodada_princ_pênaltis_PC(p[427])
Resultado36[1] = Resultado36[1] + Resultado30[1]
Resultado36[3] = Resultado36[3] + Resultado29[1]
print(Resultado36[0], Resultado36[1])
print(Resultado36[2], Resultado36[3])

operacoes = [(0+7*A, [5, 5, 5], [Resultado33, Resultado34, Resultado35]),(1+7*A, [5], [Resultado36]),(2+7*A, [4], [Resultado36]),(5+7*A, [4], [Resultado33]),(6+7*A, [4], [Resultado34]),(7+7*A, [4], [Resultado35])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 9 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado35[3], S[57]: Resultado36[3], S[58]: Resultado36[1], S[59]: Resultado31[1], S[60]: Resultado32[1], S[61]: Resultado33[1], S[62]: Resultado34[1], S[63]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado35[3], Sg[56]), (T[57], Resultado36[3], Sg[57]), (T[58], Resultado36[1], Sg[58]), (T[59], Resultado31[1], Sg[59]), (T[60], Resultado32[1], Sg[60]), (T[61], Resultado33[1], Sg[61]), (T[62], Resultado34[1], Sg[62]), (T[63], Resultado35[1], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 10!!')
    
Resultado37 = rodada_princ_pênaltis_PC(p[428])
Resultado37[1] = Resultado37[1] + Resultado31[1]
Resultado37[3] = Resultado37[3] + Resultado36[3]
print(Resultado37[0], Resultado37[1])
print(Resultado37[2], Resultado37[3])

Resultado38 = rodada_princ_pênaltis_PC(p[429])
Resultado38[1] = Resultado38[1] + Resultado32[1]
Resultado38[3] = Resultado38[3] + Resultado37[3]
print(Resultado38[0], Resultado38[1])
print(Resultado38[2], Resultado38[3])

Resultado39 = rodada_princ_pênaltis_PC(p[430])
Resultado39[1] = Resultado39[1] + Resultado33[1]
Resultado39[3] = Resultado39[3] + Resultado38[3]
print(Resultado39[0], Resultado39[1])
print(Resultado39[2], Resultado39[3])

Resultado40 = rodada_princ_pênaltis_PC(p[431])
Resultado40[1] = Resultado40[1] + Resultado34[1]
Resultado40[3] = Resultado40[3] + Resultado39[3]
print(Resultado40[0], Resultado40[1])
print(Resultado40[2], Resultado40[3])

operacoes = [(1+7*A, [5, 5, 5, 5], [Resultado37, Resultado38, Resultado39, Resultado40]),(3+7*A, [4], [Resultado37]),(4+7*A, [4], [Resultado38]),(5+7*A, [4], [Resultado39]),(6+7*A, [4], [Resultado40])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 10 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado35[3], S[57]: Resultado40[3], S[58]: Resultado36[1],  S[59]: Resultado37[1], S[60]: Resultado38[1], S[61]: Resultado39[1],  S[62]: Resultado40[1],  S[63]: Resultado35[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado35[3], Sg[56]),  (T[57], Resultado40[3], Sg[57]), (T[58], Resultado36[1], Sg[58]), (T[59], Resultado37[1], Sg[59]), (T[60], Resultado38[1], Sg[60]), (T[61], Resultado39[1], Sg[61]), (T[62], Resultado40[1], Sg[62]), (T[63], Resultado35[1], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 11!!')
        
Resultado41 = rodada_princ_pênaltis_PC(p[432])
Resultado41[1] = Resultado41[1] + Resultado35[1]
Resultado41[3] = Resultado41[3] + Resultado40[3]
print(Resultado41[0], Resultado41[1])
print(Resultado41[2], Resultado41[3])

Resultado42 = rodada_princ_pênaltis_PC(p[433])
Resultado42[1] = Resultado42[1] + Resultado37[1]
Resultado42[3] = Resultado42[3] + Resultado36[1]
print(Resultado42[0], Resultado42[1])
print(Resultado42[2], Resultado42[3])

Resultado43 = rodada_princ_pênaltis_PC(p[434])
Resultado43[1] = Resultado43[1] + Resultado38[1]
Resultado43[3] = Resultado43[3] + Resultado42[3]
print(Resultado43[0], Resultado43[1])
print(Resultado43[2], Resultado43[3])

Resultado44 = rodada_princ_pênaltis_PC(p[435])
Resultado44[1] = Resultado44[1] + Resultado39[1]
Resultado44[3] = Resultado44[3] + Resultado43[3]
print(Resultado44[0], Resultado44[1])
print(Resultado44[2], Resultado44[3])

operacoes = [(1+7*A, [5], [Resultado41]),(2+7*A, [5, 5, 5], [Resultado42, Resultado43, Resultado44]),(3+7*A, [4], [Resultado42]),(4+7*A, [4], [Resultado43]), (5+7*A, [4], [Resultado44]),(7+7*A, [4], [Resultado41])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 11 --------------------')

    print('PONTUAÇÃO ATUAL')
    pontuacao_atual = {S[56]: Resultado35[3],S[57]: Resultado41[3], S[58]: Resultado44[3], S[59]: Resultado42[1], S[60]: Resultado43[1], S[61]: Resultado44[1], S[62]: Resultado40[1], S[63]: Resultado41[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda x: x[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado35[3], Sg[56]), (T[57], Resultado41[3], Sg[57]), (T[58], Resultado44[3], Sg[58]), (T[59], Resultado42[1], Sg[59]), (T[60], Resultado43[1], Sg[60]), (T[61], Resultado44[1], Sg[61]), (T[62], Resultado40[1], Sg[62]), (T[63], Resultado41[1], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 12!!')
        
Resultado45 = rodada_princ_pênaltis_PC(p[436])
Resultado45[1] = Resultado45[1] + Resultado40[1]
Resultado45[3] = Resultado45[3] + Resultado44[3]
print(Resultado45[0], Resultado45[1])
print(Resultado45[2], Resultado45[3])

Resultado46 = rodada_princ_pênaltis_PC(p[437])
Resultado46[1] = Resultado46[1] + Resultado41[1]
Resultado46[3] = Resultado46[3] + Resultado45[3]
print(Resultado46[0], Resultado46[1])
print(Resultado46[2], Resultado46[3])

Resultado47 = rodada_princ_pênaltis_PC(p[438])
Resultado47[1] = Resultado47[1] + Resultado43[1]
Resultado47[3] = Resultado47[3] + Resultado42[1]
print(Resultado47[0], Resultado47[1])
print(Resultado47[2], Resultado47[3])

Resultado48 = rodada_princ_pênaltis_PC(p[439])
Resultado48[1] = Resultado48[1] + Resultado44[1]
Resultado48[3] = Resultado48[3] + Resultado47[3]
print(Resultado48[0], Resultado48[1])
print(Resultado48[2], Resultado48[3])

operacoes = [(2+7*A, [5, 5], [Resultado45, Resultado46]), (3+7*A, [5, 5], [Resultado47, Resultado48]), (4+7*A, [4], [Resultado47]), (5+7*A, [4], [Resultado48]),(6+7*A, [4], [Resultado45]), (7+7*A, [4], [Resultado46])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 12 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado35[3], S[57]: Resultado41[3], S[58]: Resultado46[3], S[59]: Resultado48[3], S[60]: Resultado47[1], S[61]: Resultado48[1], S[62]: Resultado45[1], S[63]: Resultado46[1]}
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado35[3], Sg[56]), (T[57], Resultado41[3], Sg[57]), (T[58], Resultado46[3], Sg[58]), (T[59], Resultado48[3], Sg[59]), (T[60], Resultado47[1], Sg[60]), (T[61], Resultado48[1], Sg[61]), (T[62], Resultado45[1], Sg[62]), (T[63], Resultado46[1], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
        print('partiu: rodada 13!!')
    
Resultado49 = rodada_princ_pênaltis_PC(p[440])
Resultado49[1] = Resultado49[1] + Resultado45[1]
Resultado49[3] = Resultado49[3] + Resultado48[3]
print(Resultado49[0], Resultado49[1])
print(Resultado49[2], Resultado49[3])

Resultado50 = rodada_princ_pênaltis_PC(p[441])
Resultado50[1] = Resultado50[1] + Resultado46[1]
Resultado50[3] = Resultado50[3] + Resultado49[3]
print(Resultado50[0], Resultado50[1])
print(Resultado50[2], Resultado50[3])

Resultado51 = rodada_princ_pênaltis_PC(p[442])
Resultado51[1] = Resultado51[1] + Resultado48[1]
Resultado51[3] = Resultado51[3] + Resultado47[1]
print(Resultado51[0], Resultado51[1])
print(Resultado51[2], Resultado51[3])

Resultado52 = rodada_princ_pênaltis_PC(p[443])
Resultado52[1] = Resultado52[1] + Resultado49[1]
Resultado52[3] = Resultado52[3] + Resultado51[3]
print(Resultado52[0], Resultado52[1])
print(Resultado52[2], Resultado52[3])

operacoes = [(3+7*A, [5, 5], [Resultado49, Resultado50]),(4+7*A, [5, 5], [Resultado51, Resultado52]), (5+7*A, [4], [Resultado51]),(6+7*A, [4, 4], [Resultado49, Resultado52]),(7+7*A, [4], [Resultado50])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('digite: 5 para ver o resultado e caso não queira ver, basta digitar 6')
Permissão = int(input('digite a opção:' ))
while Permissão != 5 and Permissão != 6:
    print("tente novamente")
    Permissão = int(input('digite a opção:' ))
if Permissão == 5:
    print('-------------------- PONTUAÇÃO FINAL RODADA 13 --------------------')

    print('PONTUAÇÃO ATUAL')

    pontuacao_atual = {S[56]: Resultado35[3], S[57]: Resultado41[3], S[58]: Resultado46[3], S[59]: Resultado50[3], S[60]: Resultado52[3], S[61]: Resultado51[1], S[62]: Resultado52[1], S[63]: Resultado50[1]}
    for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
        print(f'{time}: {pontos}')

    print('TABELA ATUAL DOS RESULTADOS')
    print('(Posição, Time, Pontuação, Saldo de Gols)')
    tabela_resultados = [(T[56], Resultado35[3], Sg[56]), (T[57], Resultado41[3], Sg[57]), (T[58], Resultado46[3], Sg[58]), (T[59], Resultado50[3], Sg[59]), (T[60], Resultado52[3], Sg[60]), (T[61], Resultado51[1], Sg[61]), (T[62], Resultado52[1], Sg[62]), (T[63], Resultado50[1], Sg[63])]
    tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
    for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º", time, pontos, saldo)
elif Permissão == 6:
    print('partiu: rodada 14!!')
        
Resultado53 = rodada_princ_pênaltis_PC(p[444])
Resultado53[1] = Resultado53[1] + Resultado50[1]
Resultado53[3] = Resultado53[3] + Resultado52[3]
print(Resultado53[0], Resultado53[1])
print(Resultado53[2], Resultado53[3])

Resultado54 = rodada_princ_pênaltis_PC(p[445])
Resultado54[1] = Resultado54[1] + Resultado52[1]
Resultado54[3] = Resultado54[3] + Resultado51[1]
print(Resultado54[0], Resultado54[1])
print(Resultado54[2], Resultado54[3])

Resultado55 = rodada_princ_pênaltis_PC(p[446])
Resultado55[1] = Resultado55[1] + Resultado53[1]
Resultado55[3] = Resultado55[3] + Resultado54[3]
print(Resultado55[0], Resultado55[1])
print(Resultado55[2], Resultado55[3])

Resultado56 = rodada_princ_pênaltis_PC(p[447])
Resultado56[1] = Resultado56[1] + Resultado55[1]
Resultado56[3] = Resultado56[3] + Resultado54[1]
print(Resultado56[0], Resultado56[1])
print(Resultado56[2], Resultado56[3])

operacoes = [ (4+7*A, [5], [Resultado53]), (5+7*A, [5, 5], [Resultado54, Resultado55]), (6+7*A, [4, 5], [Resultado54, Resultado56]), (7+7*A, [4, 4, 4], [Resultado53, Resultado55, Resultado56])]
for index_sg, indices, resultados in operacoes:
    Sg[index_sg] += sum(resultado[i] for i, resultado in zip(indices, resultados))

print('-------------------- PONTUAÇÃO FINAL RODADA 14 --------------------')

print('PONTUAÇÃO ATUAL')

pontuacao_atual = {S[56]: Resultado35[3], S[57]: Resultado41[3], S[58]: Resultado46[3], S[59]: Resultado50[3], S[60]: Resultado53[3], S[61]: Resultado55[3],  S[62]: Resultado56[3], S[63]: Resultado56[1]}
for time, pontos in sorted(pontuacao_atual.items(), key=lambda item: item[1], reverse=True):
    print(f'{time}: {pontos}')

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
tabela_resultados = [(T[56], Resultado35[3], Sg[56]), (T[57], Resultado41[3], Sg[57]), (T[58], Resultado46[3], Sg[58]), (T[59], Resultado50[3], Sg[59]), (T[60], Resultado53[3], Sg[60]), (T[61], Resultado55[3], Sg[61]), (T[62], Resultado56[3], Sg[62]), (T[63], Resultado56[1], Sg[63])]
tabela_ordenada = sorted(tabela_resultados, key=lambda x: (x[1], x[2]), reverse=True)
for posicao, (time, pontos, saldo) in enumerate(tabela_ordenada, start=1):
    print(f"{posicao}º", time, pontos, saldo)

if tabela_ordenada[3][1] == tabela_ordenada[4][1] and tabela_ordenada[3][2] == tabela_ordenada[4][2]:
    print('----------COMEÇA A DECISÃO PELA 4º VAGA DA 2ºF SÉRIE D BRASILEIRÃO!!!!----------')
    print('--casa--:', tabela_ordenada[3][0])
    print('--visitante--:', tabela_ordenada[4][0])
    pd = ['X','O',L1,L2,Q[0],Q[1],tabela_ordenada[3][0],tabela_ordenada[4][0]]
    Resultado = rodada_desempate_pênaltis(pd)
    print(Resultado[0])
    CG8 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], Resultado[1]]
    print('---------CLASSIFICADOS DO GRUPO 8 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!--------------')
    print(CG8)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')
else:
    CG8 = [tabela_ordenada[0][0], tabela_ordenada[1][0], tabela_ordenada[2][0], tabela_ordenada[3][0]]
    print('------------CLASSIFICADOS DO GRUPO 8 PARA 2ºF SÉRIE D BRASILEIRÃO!!!!-----------')
    print(CG8)
    print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA 2ºF SÉRIE D BRASILEIRÃO!!!')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('-----------TMES CLASSIFICADOS PARA 2ºF SÉRIE D BRASILEIRÃO!!!!----------------')

for i in range(1, 9):
    print(f'Grupo {i}', globals()[f'CG{i}'])

print('----COMEÇA A SEGUNDA FASE DA SÉRIE D BRASILEIRÃO VALENDO VAGAS PARA 8ºS DE FINAS----')

print('--casa--:', CG1[0])
print('--visitante--:', CG1[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG1[0],CG1[1]]
Resultado = rodada_desempate_pênaltis(pd)
T1oitavas = (Resultado[1])
print("o time que ganhou a vaga 1 para oitavas de finais é:",T1oitavas)

print('--casa--:', CG1[2])
print('--visitante--:', CG1[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG1[2],CG1[3]]
Resultado = rodada_desempate_pênaltis(pd)
T2oitavas = (Resultado[1])
print("o time que ganhou a vaga 2 para oitavas de finais é:",T2oitavas)

print('--casa--:', CG2[0])
print('--visitante--:', CG2[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG2[0],CG2[1]]
Resultado = rodada_desempate_pênaltis(pd)
T3oitavas = (Resultado[1])
print("o time que ganhou a vaga 3 para oitavas de finais é:",T3oitavas)

print('--casa--:', CG2[2])
print('--visitante--:', CG2[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG2[2],CG2[3]]
Resultado = rodada_desempate_pênaltis(pd)
T4oitavas = (Resultado[1])
print("o time que ganhou a vaga 4 para oitavas de finais é:",T4oitavas)

print('--casa--:', CG3[0])
print('--visitante--:', CG3[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG3[0],CG3[1]]
Resultado = rodada_desempate_pênaltis(pd)
T5oitavas = (Resultado[1])
print("o time que ganhou a vaga 5 para oitavas de finais é:",T5oitavas)

print('--casa--:', CG3[2])
print('--visitante--:', CG3[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG3[2],CG3[3]]
Resultado = rodada_desempate_pênaltis(pd)
T6oitavas = (Resultado[1])
print("o time que ganhou a vaga 6 para oitavas de finais é:",T6oitavas)

print('--casa--:', CG4[0])
print('--visitante--:', CG4[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG4[0],CG4[1]]
Resultado = rodada_desempate_pênaltis(pd)
T7oitavas = (Resultado[1])
print("o time que ganhou a vaga 7 para oitavas de finais é:",T7oitavas)

print('--casa--:', CG4[2])
print('--visitante--:', CG4[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG4[2],CG4[3]]
Resultado = rodada_desempate_pênaltis(pd)
T8oitavas = (Resultado[1])
print("o time que ganhou a vaga 8 para oitavas de finais é:",T8oitavas)

print('--casa--:', CG5[0])
print('--visitante--:', CG5[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG5[0],CG5[1]]
Resultado = rodada_desempate_pênaltis(pd)
T9oitavas = (Resultado[1])
print("o time que ganhou a vaga 9 para oitavas de finais é:",T9oitavas)

print('--casa--:', CG5[2])
print('--visitante--:', CG5[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG5[2],CG5[3]]
Resultado = rodada_desempate_pênaltis(pd)
T10oitavas = (Resultado[1])
print("o time que ganhou a vaga 10 para oitavas de finais é:",T10oitavas)

print('--casa--:', CG6[0])
print('--visitante--:', CG6[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG6[0],CG6[1]]
Resultado = rodada_desempate_pênaltis(pd)
T11oitavas = (Resultado[1])
print("o time que ganhou a vaga 11 para oitavas de finais é:",T11oitavas)

print('--casa--:', CG6[2])
print('--visitante--:', CG6[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG6[2],CG6[3]]
Resultado = rodada_desempate_pênaltis(pd)
T12oitavas = (Resultado[1])
print("o time que ganhou a vaga 12 para oitavas de finais é:",T12oitavas)

print('--casa--:', CG7[0])
print('--visitante--:', CG7[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG7[0],CG7[1]]
Resultado = rodada_desempate_pênaltis(pd)
T13oitavas = (Resultado[1])
print("o time que ganhou a vaga 13 para oitavas de finais é:",T13oitavas)

print('--casa--:', CG7[2])
print('--visitante--:', CG7[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG7[2],CG7[3]]
Resultado = rodada_desempate_pênaltis(pd)
T14oitavas = (Resultado[1])
print("o time que ganhou a vaga 14 para oitavas de finais é:",T14oitavas)

print('--casa--:', CG8[0])
print('--visitante--:', CG8[1])
pd = ['X','O',L1,L2,Q[0],Q[1],CG8[0],CG8[1]]
Resultado = rodada_desempate_pênaltis(pd)
T15oitavas = (Resultado[1])
print("o time que ganhou a vaga 15 para oitavas de finais é:",T15oitavas)

print('--casa--:', CG8[2])
print('--visitante--:', CG8[3])
pd = ['X','O',L1,L2,Q[0],Q[1],CG8[2],CG8[3]]
Resultado = rodada_desempate_pênaltis(pd)
T16oitavas = (Resultado[1])
print("o time que ganhou a vaga 16 para oitavas de finais é:",T16oitavas)

LCOitavas = [T1oitavas, T2oitavas, T3oitavas, T4oitavas, T5oitavas, T6oitavas, T7oitavas, T8oitavas, T9oitavas, T10oitavas, T11oitavas, T12oitavas, T13oitavas, T14oitavas, T15oitavas, T16oitavas]

print('-----------TTIMES CLASSIFICADOS PARA 8ºs DE FINAIS SÉRIE D BRASILEIRÃO!!!!----------')
print(LCOitavas)
print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTAS 8ºs SÉRIE D BRASILEIRÃO!!!')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('---COMEÇA AS 8ºs DE FINAIS DA SÉRIE D BRASILEIRÃO VALENDO VAGAS PARA 4ºS DE FINAS---')

LCO = [T1oitavas, T2oitavas, T3oitavas, T4oitavas, T5oitavas, T6oitavas, T7oitavas, T8oitavas, T9oitavas, T10oitavas, T11oitavas, T12oitavas, T13oitavas, T14oitavas, T15oitavas, T16oitavas]

print('--casa--:', LCO[0])
print('--visitante--:', LCO[1])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[0],LCO[1]]
Resultado = rodada_desempate_pênaltis(pd)
T1quartas = (Resultado[1])
print("o time que ganhou a vaga 1 para quartas de finais é:",T1quartas)

print('--casa--:', LCO[2])
print('--visitante--:', LCO[3])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[2],LCO[3]]
Resultado = rodada_desempate_pênaltis(pd)
T2quartas = (Resultado[1])
print("o time que ganhou a vaga 2 para quartas de finais é:",T2quartas)

print('--casa--:', LCO[4])
print('--visitante--:', LCO[5])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[4],LCO[5]]
Resultado = rodada_desempate_pênaltis(pd)
T3quartas = (Resultado[1])
print("o time que ganhou a vaga 3 para quartas de finais é:",T3quartas)

print('--casa--:', LCO[6])
print('--visitante--:', LCO[7])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[6],LCO[7]]
Resultado = rodada_desempate_pênaltis(pd)
T4quartas = (Resultado[1])
print("o time que ganhou a vaga 4 para quartas de finais é:",T4quartas)

print('--casa--:', LCO[8])
print('--visitante--:', LCO[9])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[8],LCO[9]]
Resultado = rodada_desempate_pênaltis(pd)
T5quartas = (Resultado[1])
print("o time que ganhou a vaga 5 para quartas de finais é:",T5quartas)

print('--casa--:', LCO[10])
print('--visitante--:', LCO[11])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[10],LCO[11]]
Resultado = rodada_desempate_pênaltis(pd)
T6quartas = (Resultado[1])
print("o time que ganhou a vaga 6 para quartas de finais é:",T6quartas)

print('--casa--:', LCO[12])
print('--visitante--:', LCO[13])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[12],LCO[13]]
Resultado = rodada_desempate_pênaltis(pd)
T7quartas = (Resultado[1])
print("o time que ganhou a vaga 7 para quartas de finais é:",T7quartas)

print('--casa--:', LCO[14])
print('--visitante--:', LCO[15])
pd = ['X','O',L1,L2,Q[0],Q[1],LCO[14],LCO[15]]
Resultado = rodada_desempate_pênaltis(pd)
T8quartas = (Resultado[1])
print("o time que ganhou a vaga 8 para quartas de finais é:",T8quartas)

LCQuartas = [T1quartas, T2quartas, T3quartas, T4quartas, T5quartas, T6quartas, T7quartas, T8quartas]

print('-----------TTIMES CLASSIFICADOS PARA 4ºs DE FINAIS SÉRIE D BRASILEIRÃO!!!!----------')
print(LCQuartas)
print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTAS 4ºs SÉRIE D BRASILEIRÃO!!!')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('---COMEÇA AS 4ºs DE FINAIS DA SÉRIE D BRASILEIRÃO VALENDO VAGAS PARA SEMIFINAIS---')
print('---OBS: OS SEMIFINALISTAS CONQUISTAM TAMBÉM AS VAGAS PARA SÉRIE C DO PRÓXIMO ANO--')

LCQ = [T1quartas, T2quartas, T3quartas, T4quartas, T5quartas, T6quartas, T7quartas, T8quartas]

print('--casa--:', LCQ[0])
print('--visitante--:', LCQ[1])
pd = ['X','O',L1,L2,Q[0],Q[1],LCQ[0],LCQ[1]]
Resultado = rodada_desempate_pênaltis(pd)
T1semis = (Resultado[1])
print("o time que ganhou a vaga 1 para semifinais é:",T1semis)

print('--casa--:', LCQ[2])
print('--visitante--:', LCQ[3])
pd = ['X','O',L1,L2,Q[0],Q[1],LCQ[2],LCQ[3]]
Resultado = rodada_desempate_pênaltis(pd)
T2semis = (Resultado[1])
print("o time que ganhou a vaga 2 para semifinais é:",T2semis)

print('--casa--:', LCQ[4])
print('--visitante--:', LCQ[5])
pd = ['X','O',L1,L2,Q[0],Q[1],LCQ[4],LCQ[5]]
Resultado = rodada_desempate_pênaltis(pd)
T3semis = (Resultado[1])
print("o time que ganhou a vaga 3 para semifinais é:",T3semis)

print('--casa--:', LCQ[6])
print('--visitante--:', LCQ[7])
pd = ['X','O',L1,L2,Q[0],Q[1],LCQ[6],LCQ[7]]
Resultado = rodada_desempate_pênaltis(pd)
T4semis = (Resultado[1])
print("o time que ganhou a vaga 4 para semifinais é:",T4semis)

LCSemis = [T1semis, T2semis, T3semis, T4semis]

print('-----------TTIMES CLASSIFICADOS PARA SEMIFINAIS SÉRIE D BRASILEIRÃO!!!!----------')
print('-----------TTIMES CLASSIFICADOS PARA SÉRIE C BRASILEIRÃO DO PROX ANO!!!!---------')
print(LCSemis)
print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTAS SEMIS SÉRIE D BRASILEIRÃO!')
print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NA SÉRIE C BRASILEIRÃO PROX ANO!')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('---COMEÇA AS SENIFINAIS DA SÉRIE D BRASILEIRÃO VALENDO VAGAS PARA GRANDE FINAL')

LCS = [T1semis, T2semis, T3semis, T4semis]

print('--casa--:', LCS[0])
print('--visitante--:', LCS[1])
pd = ['X','O',L1,L2,Q[0],Q[1],LCS[0],LCS[1]]
Resultado = rodada_desempate_pênaltis(pd)
T1Final = (Resultado[1])
print("o time que ganhou a vaga 1 para grande final é:",T1Final)

print('--casa--:', LCS[2])
print('--visitante--:', LCS[3])
pd = ['X','O',L1,L2,Q[0],Q[1],LCS[2],LCS[3]]
Resultado = rodada_desempate_pênaltis(pd)
T2Final = (Resultado[1])
print("o time que ganhou a vaga 2 para grande final é:",T2Final)

LCFinal = [T1Final, T2Final]

print('-----------TTIMES CLASSIFICADOS PARA A GRANDE FINAL SÉRIE D BRASILEIRÃO!!!!----------')
print(LCFinal)
print('MUITÍSSIMOS PARABÉNS E QUE A SORTE OS ACOMPANHA NESTA GF SÉRIE D BRASILEIRÃO!')

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('---COMEÇA A GRANDE FINAL DA SÉRIE D BRASILEIRÃO!!!!! QUEM SERÁ O CAMPEÃO????---')

LCF = [T1Final, T2Final]

print('--casa--:', LCF[0])
print('--visitante--:', LCF[1])
pd = ['X','O',L1,L2,Q[0],Q[1],LCF[0],LCF[1]]
Resultado = rodada_desempate_pênaltis(pd)
TCampeão = (Resultado[1])
print("o time campeão da série D brasileirão é:",TCampeão)

print('MUITÍSSIMOS PARABÉNS A EQUIPE QUE GANHOU O CAMPEONATO BRASILEIRÃO SÉRIE D!!!!!',TCampeão)
