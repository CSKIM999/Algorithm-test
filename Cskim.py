'''
내가 자주 틀리거나 혹은 내가 틀리고서 상당히 충격을 받은 부분을 라이브러리화 시켜서 정리하고자 한다
'''

import itertools
'''
파이썬의 기본 라이브러리중 하나인 itertools


product('ABCD', repeat=2) ///  AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
>> AA,DD 는 있고 AD 와 DA 는 다른 객체이다

permutations('ABCD', 2)   ///  AB AC AD BA BC BD CA CB CD DA DB DC
>> AA,DD 도 없으나, AB 와 BA 는 다르다

combinations('ABCD', 2)   /// AB AC AD BC BD CD
>> AA,DD 도 없고 AD 와 DA 는 같다

combinations_with_replacement('ABCD', 2)  ///AA AB AC AD BB BC BD CC CD DD
>> AA와 DD 는 있으나, AD와 DA 는 다르다


'''