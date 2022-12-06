class Count(object):
    """docstring for Count"""
    def __init__(self,*args):
        super(Count, self).__init__()
        self.s = args[0]
        self.dict1={}
        if len(args)>1:
            self.s1= args[1]

    """count frequency of each character"""
    def count_string(self):
        for i in range(len(self.s)):
            c=0
            for j in range(len(self.s)):
                if(self.s[i]==self.s[j]):
                    c+=1
            self.dict1[self.s[i]]=c
        return self.dict1

    """replace not poor! with Good! otherwise unchanged"""
    def not_poor_check(self):
        p1=self.s.find('poor!')
        p2=self.s.find('not')
        if p2<p1 and p2>0 and p1>0:
            self.s1=self.s[:p2]+"Good!"
        else:
            self.s1=self.s
        return self.s1

    """sort by length of word"""
    def longest_word(self,list1):
        list1.sort(key=len)
        print(list1)
        return list1[len(list1)-1] #list1[-1]

if __name__ == '__main__':
    s="The lyrics is not that poor!"
    c=Count(s.replace(" ",""))
    #c=Count(s.strip().split()) # split by words
    d=c.count_string()
    for key,val in d.items():
        print("key - {0} , val - {1}".format(key,val))
    
    c=Count("The lyrics is poor!","")
    print(c.not_poor_check())

    li = ['these','are','the','longest','words']
    print(c.longest_word(li))