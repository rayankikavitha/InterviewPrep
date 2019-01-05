"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Given :
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.


"""
def isInterleave(self,S1,S2,S3):
    if len(S3) == 1:
        return ( len(S1)==0 and S3[0] == S2[0] ) or ( len(S2)==0 and S3[0] == S1[0] )
    if len(S1)>0 and len(S2)>0:

        return ( S3[0]==S1[0] and self.isInterleave(S1[1:],S2,S3[1:]) ) or ( S3[0]==S2[0] and self.isInterleave(S1,S2[1:],S3[1:]) )
    elif len(S2)==0:
        return ( S3[0]==S1[0] and self.isInterleave(S1[1:],S2,S3[1:]) )
    elif len(S1)==0:
        return ( S3[0]==S2[0] and self.isInterleave(S1,S2[1:],S3[1:]) )


