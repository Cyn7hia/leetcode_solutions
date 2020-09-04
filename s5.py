class Solution:
    def longestPalindrome(self, s: str) -> str:

        alp_dic = dict()        
        for idx, alp in enumerate(s):
            if alp in alp_dic:
                alp_dic[alp].append(idx) 
            else:
                alp_dic[alp] = [idx]

        distance = []
        for key in alp_dic:
            for idx,pos in enumerate(alp_dic[key]):
                for pos_j in alp_dic[key][idx+1:]:
                    distance.append((pos,pos_j,pos_j-pos))
        del alp_dic
        
        if distance:
            distance_s = sorted(distance, key=lambda x:x[2], reverse=True)
            del distance

            for items in distance_s:
                pos,pos_j,dis = items
                l = s[pos:pos_j+1]
                '''if dis%2==0:
                    half = s[(pos+pos_j)//2+1:pos_j+1]
                    if s[pos:(pos+pos_j)//2] == half[::-1]:
                        return s[pos:(pos_j+1)]
                else:
                    half = s[1+(pos+pos_j)//2:pos_j+1]
                    if s[pos:1+(pos+pos_j)//2] == half[::-1]:
                        return s[pos:pos_j+1]'''
                if l==l[::-1]:
                    return l
            return s[0]
        else:
            return s if len(s)==0 else s[0]

