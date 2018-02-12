#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7766 = ref_278 # MOV operation
ref_8300 = ref_7766 # MOV operation
ref_8308 = (ref_8300 >> (0x5 & 0x3F)) # SHR operation
ref_8315 = ref_8308 # MOV operation
ref_8416 = ref_8315 # MOV operation
ref_8430 = (0x1376783EF7559EA & ref_8416) # AND operation
ref_8598 = ref_8430 # MOV operation
ref_8600 = ((ref_8598 >> 56) & 0xFF) # Byte reference - MOV operation
ref_8601 = ((ref_8598 >> 48) & 0xFF) # Byte reference - MOV operation
ref_8602 = ((ref_8598 >> 40) & 0xFF) # Byte reference - MOV operation
ref_8603 = ((ref_8598 >> 32) & 0xFF) # Byte reference - MOV operation
ref_8604 = ((ref_8598 >> 24) & 0xFF) # Byte reference - MOV operation
ref_8605 = ((ref_8598 >> 16) & 0xFF) # Byte reference - MOV operation
ref_8606 = ((ref_8598 >> 8) & 0xFF) # Byte reference - MOV operation
ref_8607 = (ref_8598 & 0xFF) # Byte reference - MOV operation
ref_11462 = ref_278 # MOV operation
ref_11843 = ref_11462 # MOV operation
ref_11849 = (0x1A5612E2 | ref_11843) # OR operation
ref_13599 = ref_8598 # MOV operation
ref_13680 = ref_13599 # MOV operation
ref_13694 = (0x7063FB7 & ref_13680) # AND operation
ref_13961 = ref_11849 # MOV operation
ref_13965 = ref_13694 # MOV operation
ref_13967 = ((ref_13965 + ref_13961) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14136 = ref_13967 # MOV operation
ref_14138 = ((ref_14136 >> 56) & 0xFF) # Byte reference - MOV operation
ref_14139 = ((ref_14136 >> 48) & 0xFF) # Byte reference - MOV operation
ref_14140 = ((ref_14136 >> 40) & 0xFF) # Byte reference - MOV operation
ref_14141 = ((ref_14136 >> 32) & 0xFF) # Byte reference - MOV operation
ref_14142 = ((ref_14136 >> 24) & 0xFF) # Byte reference - MOV operation
ref_14143 = ((ref_14136 >> 16) & 0xFF) # Byte reference - MOV operation
ref_14144 = ((ref_14136 >> 8) & 0xFF) # Byte reference - MOV operation
ref_14145 = (ref_14136 & 0xFF) # Byte reference - MOV operation
ref_17534 = ref_14136 # MOV operation
ref_18068 = ref_17534 # MOV operation
ref_18076 = (ref_18068 >> (0x3 & 0x3F)) # SHR operation
ref_18083 = ref_18076 # MOV operation
ref_18184 = ref_18083 # MOV operation
ref_18198 = (0xF & ref_18184) # AND operation
ref_18604 = ref_18198 # MOV operation
ref_18610 = (0x1 | ref_18604) # OR operation
ref_19056 = ref_18610 # MOV operation
ref_19058 = ((0x3162E74F << ((ref_19056 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21064 = ref_14136 # MOV operation
ref_21598 = ref_21064 # MOV operation
ref_21606 = (ref_21598 >> (0x3 & 0x3F)) # SHR operation
ref_21613 = ref_21606 # MOV operation
ref_21714 = ref_21613 # MOV operation
ref_21728 = (0xF & ref_21714) # AND operation
ref_22134 = ref_21728 # MOV operation
ref_22140 = (0x1 | ref_22134) # OR operation
ref_22685 = ref_22140 # MOV operation
ref_22687 = ((0x40 - ref_22685) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_22695 = ref_22687 # MOV operation
ref_22997 = ref_22695 # MOV operation
ref_22999 = (ref_22997 & 0xFFFFFFFF) # MOV operation
ref_23001 = (0x3162E74F >> ((ref_22999 & 0xFF) & 0x3F)) # SHR operation
ref_23008 = ref_23001 # MOV operation
ref_23153 = ref_19058 # MOV operation
ref_23157 = ref_23008 # MOV operation
ref_23159 = (ref_23157 | ref_23153) # OR operation
ref_23718 = ref_23159 # MOV operation
ref_23726 = (ref_23718 >> (0x4 & 0x3F)) # SHR operation
ref_23733 = ref_23726 # MOV operation
ref_23834 = ref_23733 # MOV operation
ref_23848 = (0x7 & ref_23834) # AND operation
ref_24254 = ref_23848 # MOV operation
ref_24260 = (0x1 | ref_24254) # OR operation
ref_25988 = ref_278 # MOV operation
ref_26240 = ref_25988 # MOV operation
ref_26254 = ((ref_26240 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_26262 = ref_26254 # MOV operation
ref_26435 = ref_26262 # MOV operation
ref_26447 = ref_24260 # MOV operation
ref_26449 = ((ref_26435 << ((ref_26447 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_26617 = ref_26449 # MOV operation
ref_29737 = ref_278 # MOV operation
ref_29989 = ref_29737 # MOV operation
ref_30003 = ((ref_29989 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_30011 = ref_30003 # MOV operation
ref_30174 = ref_30011 # MOV operation
ref_34918 = ref_30174 # MOV operation
ref_37387 = ref_14136 # MOV operation
ref_37468 = ref_37387 # MOV operation
ref_37482 = (0xF & ref_37468) # AND operation
ref_37660 = ref_37482 # MOV operation
ref_37674 = ((ref_37660 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37824 = ref_34918 # MOV operation
ref_37828 = ref_37674 # MOV operation
ref_37830 = (ref_37828 | ref_37824) # OR operation
ref_37998 = ref_37830 # MOV operation
ref_40884 = ref_26617 # MOV operation
ref_42865 = ref_37998 # MOV operation
ref_42946 = ref_42865 # MOV operation
ref_42960 = (0x1F & ref_42946) # AND operation
ref_43138 = ref_42960 # MOV operation
ref_43152 = ((ref_43138 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43302 = ref_40884 # MOV operation
ref_43306 = ref_43152 # MOV operation
ref_43308 = (ref_43306 | ref_43302) # OR operation
ref_43476 = ref_43308 # MOV operation
ref_46362 = ref_37998 # MOV operation
ref_48831 = ref_14136 # MOV operation
ref_48912 = ref_48831 # MOV operation
ref_48926 = (0xF & ref_48912) # AND operation
ref_49104 = ref_48926 # MOV operation
ref_49118 = ((ref_49104 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_49268 = ref_46362 # MOV operation
ref_49272 = ref_49118 # MOV operation
ref_49274 = (ref_49272 | ref_49268) # OR operation
ref_49442 = ref_49274 # MOV operation
ref_54674 = ref_49442 # MOV operation
ref_57143 = ref_49442 # MOV operation
ref_57224 = ref_57143 # MOV operation
ref_57238 = (0xF & ref_57224) # AND operation
ref_57416 = ref_57238 # MOV operation
ref_57430 = ((ref_57416 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_57580 = ref_54674 # MOV operation
ref_57584 = ref_57430 # MOV operation
ref_57586 = (ref_57584 | ref_57580) # OR operation
ref_57754 = ref_57586 # MOV operation
ref_60640 = ref_43476 # MOV operation
ref_62621 = ref_57754 # MOV operation
ref_62702 = ref_62621 # MOV operation
ref_62716 = (0x1F & ref_62702) # AND operation
ref_62894 = ref_62716 # MOV operation
ref_62908 = ((ref_62894 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_63058 = ref_60640 # MOV operation
ref_63062 = ref_62908 # MOV operation
ref_63064 = (ref_63062 | ref_63058) # OR operation
ref_63232 = ref_63064 # MOV operation
ref_63234 = ((ref_63232 >> 56) & 0xFF) # Byte reference - MOV operation
ref_63235 = ((ref_63232 >> 48) & 0xFF) # Byte reference - MOV operation
ref_63236 = ((ref_63232 >> 40) & 0xFF) # Byte reference - MOV operation
ref_63237 = ((ref_63232 >> 32) & 0xFF) # Byte reference - MOV operation
ref_63238 = ((ref_63232 >> 24) & 0xFF) # Byte reference - MOV operation
ref_63239 = ((ref_63232 >> 16) & 0xFF) # Byte reference - MOV operation
ref_63240 = ((ref_63232 >> 8) & 0xFF) # Byte reference - MOV operation
ref_63241 = (ref_63232 & 0xFF) # Byte reference - MOV operation
ref_66118 = ref_57754 # MOV operation
ref_68587 = ref_57754 # MOV operation
ref_68668 = ref_68587 # MOV operation
ref_68682 = (0xF & ref_68668) # AND operation
ref_68860 = ref_68682 # MOV operation
ref_68874 = ((ref_68860 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_69024 = ref_66118 # MOV operation
ref_69028 = ref_68874 # MOV operation
ref_69030 = (ref_69028 | ref_69024) # OR operation
ref_69198 = ref_69030 # MOV operation
ref_83086 = ref_69198 # MOV operation
ref_85067 = ref_63232 # MOV operation
ref_86536 = ref_63232 # MOV operation
ref_86778 = ref_85067 # MOV operation
ref_86782 = ref_86536 # MOV operation
ref_86784 = ((ref_86782 + ref_86778) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_86891 = ref_86784 # MOV operation
ref_86905 = (0x7 & ref_86891) # AND operation
ref_87083 = ref_86905 # MOV operation
ref_87097 = ((ref_87083 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_87247 = ref_83086 # MOV operation
ref_87251 = ref_87097 # MOV operation
ref_87253 = (ref_87251 | ref_87247) # OR operation
ref_87421 = ref_87253 # MOV operation
ref_90122 = ((((ref_63234) << 8 | ref_63235) << 8 | ref_63236) << 8 | ref_63237) # MOV operation
ref_90529 = (ref_90122 & 0xFFFFFFFF) # MOV operation
ref_93226 = ((((ref_63238) << 8 | ref_63239) << 8 | ref_63240) << 8 | ref_63241) # MOV operation
ref_96064 = (ref_93226 & 0xFFFFFFFF) # MOV operation
ref_96066 = (((ref_96064 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_96067 = (((ref_96064 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_96068 = (((ref_96064 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_96069 = ((ref_96064 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_96330 = (ref_90529 & 0xFFFFFFFF) # MOV operation
ref_99168 = (ref_96330 & 0xFFFFFFFF) # MOV operation
ref_99170 = (((ref_99168 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_99171 = (((ref_99168 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_99172 = (((ref_99168 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_99173 = ((ref_99168 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_102187 = ref_8602 # MOVZX operation
ref_102484 = (ref_102187 & 0xFF) # MOVZX operation
ref_107930 = ref_8603 # MOVZX operation
ref_108227 = (ref_107930 & 0xFF) # MOVZX operation
ref_108229 = (ref_108227 & 0xFF) # Byte reference - MOV operation
ref_111242 = (ref_102484 & 0xFF) # MOVZX operation
ref_111539 = (ref_111242 & 0xFF) # MOVZX operation
ref_111541 = (ref_111539 & 0xFF) # Byte reference - MOV operation
ref_114554 = ref_8601 # MOVZX operation
ref_114851 = (ref_114554 & 0xFF) # MOVZX operation
ref_120297 = ref_8607 # MOVZX operation
ref_120594 = (ref_120297 & 0xFF) # MOVZX operation
ref_120596 = (ref_120594 & 0xFF) # Byte reference - MOV operation
ref_123609 = (ref_114851 & 0xFF) # MOVZX operation
ref_123906 = (ref_123609 & 0xFF) # MOVZX operation
ref_123908 = (ref_123906 & 0xFF) # Byte reference - MOV operation
ref_126599 = ((((ref_14142) << 8 | ref_14143) << 8 | ref_14144) << 8 | ref_14145) # MOV operation
ref_127006 = (ref_126599 & 0xFFFFFFFF) # MOV operation
ref_129703 = ((((ref_14138) << 8 | ref_14139) << 8 | ref_14140) << 8 | ref_14141) # MOV operation
ref_132541 = (ref_129703 & 0xFFFFFFFF) # MOV operation
ref_132543 = (((ref_132541 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_132544 = (((ref_132541 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_132545 = (((ref_132541 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_132546 = ((ref_132541 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_132807 = (ref_127006 & 0xFFFFFFFF) # MOV operation
ref_135645 = (ref_132807 & 0xFFFFFFFF) # MOV operation
ref_135647 = (((ref_135645 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_135648 = (((ref_135645 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_135649 = (((ref_135645 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_135650 = ((ref_135645 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_140489 = ((((((((ref_135647) << 8 | ref_135648) << 8 | ref_135649) << 8 | ref_135650) << 8 | ref_132543) << 8 | ref_132544) << 8 | ref_132545) << 8 | ref_132546) # MOV operation
ref_142958 = ((((((((ref_8600) << 8 | ref_120596) << 8 | ref_108229) << 8 | ref_111541) << 8 | ref_8604) << 8 | ref_8605) << 8 | ref_8606) << 8 | ref_123908) # MOV operation
ref_143039 = ref_142958 # MOV operation
ref_143053 = (0x3F & ref_143039) # AND operation
ref_143231 = ref_143053 # MOV operation
ref_143245 = ((ref_143231 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_143395 = ref_140489 # MOV operation
ref_143399 = ref_143245 # MOV operation
ref_143401 = (ref_143399 | ref_143395) # OR operation
ref_143569 = ref_143401 # MOV operation
ref_149170 = ((((((((ref_96066) << 8 | ref_96067) << 8 | ref_96068) << 8 | ref_96069) << 8 | ref_99170) << 8 | ref_99171) << 8 | ref_99172) << 8 | ref_99173) # MOV operation
ref_151151 = ref_87421 # MOV operation
ref_152876 = ref_143569 # MOV operation
ref_153410 = ref_152876 # MOV operation
ref_153418 = (ref_153410 >> (0x3 & 0x3F)) # SHR operation
ref_153425 = ref_153418 # MOV operation
ref_153526 = ref_153425 # MOV operation
ref_153540 = (0xF & ref_153526) # AND operation
ref_153946 = ref_153540 # MOV operation
ref_153952 = (0x1 | ref_153946) # OR operation
ref_154255 = ref_151151 # MOV operation
ref_154259 = ref_153952 # MOV operation
ref_154261 = (ref_154259 & 0xFFFFFFFF) # MOV operation
ref_154263 = (ref_154255 >> ((ref_154261 & 0xFF) & 0x3F)) # SHR operation
ref_154270 = ref_154263 # MOV operation
ref_156015 = ref_143569 # MOV operation
ref_156549 = ref_156015 # MOV operation
ref_156557 = (ref_156549 >> (0x3 & 0x3F)) # SHR operation
ref_156564 = ref_156557 # MOV operation
ref_156665 = ref_156564 # MOV operation
ref_156679 = (0xF & ref_156665) # AND operation
ref_157085 = ref_156679 # MOV operation
ref_157091 = (0x1 | ref_157085) # OR operation
ref_157636 = ref_157091 # MOV operation
ref_157638 = ((0x40 - ref_157636) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_157646 = ref_157638 # MOV operation
ref_159135 = ref_87421 # MOV operation
ref_159288 = ref_159135 # MOV operation
ref_159300 = ref_157646 # MOV operation
ref_159302 = ((ref_159288 << ((ref_159300 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_159452 = ref_154270 # MOV operation
ref_159456 = ref_159302 # MOV operation
ref_159458 = (ref_159456 | ref_159452) # OR operation
ref_159564 = ref_159458 # MOV operation
ref_159578 = (0xF & ref_159564) # AND operation
ref_159756 = ref_159578 # MOV operation
ref_159770 = ((ref_159756 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_159920 = ref_149170 # MOV operation
ref_159924 = ref_159770 # MOV operation
ref_159926 = (ref_159924 | ref_159920) # OR operation
ref_160094 = ref_159926 # MOV operation
ref_163223 = ref_143569 # MOV operation
ref_163757 = ref_163223 # MOV operation
ref_163765 = (ref_163757 >> (0x3 & 0x3F)) # SHR operation
ref_163772 = ref_163765 # MOV operation
ref_163873 = ref_163772 # MOV operation
ref_163887 = (0x7 & ref_163873) # AND operation
ref_164293 = ref_163887 # MOV operation
ref_164299 = (0x1 | ref_164293) # OR operation
ref_165793 = ((((((((ref_8600) << 8 | ref_120596) << 8 | ref_108229) << 8 | ref_111541) << 8 | ref_8604) << 8 | ref_8605) << 8 | ref_8606) << 8 | ref_123908) # MOV operation
ref_165946 = ref_165793 # MOV operation
ref_165958 = ref_164299 # MOV operation
ref_165960 = ((ref_165946 << ((ref_165958 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_167454 = ref_160094 # MOV operation
ref_168923 = ref_87421 # MOV operation
ref_169048 = ref_167454 # MOV operation
ref_169052 = ref_168923 # MOV operation
ref_169054 = (ref_169052 | ref_169048) # OR operation
ref_169204 = ref_165960 # MOV operation
ref_169208 = ref_169054 # MOV operation
ref_169210 = (ref_169208 | ref_169204) # OR operation
ref_169378 = ref_169210 # MOV operation
ref_169743 = ref_169378 # MOV operation
ref_169745 = ref_169743 # MOV operation

print ref_169745 & 0xffffffffffffffff