class mm:
    def __init__(self, s):
        self.s = s
        # TODO:
        # check if s is power of 2
        self.t = []

    def new(self, l):
        a = self._get_new_addr(l)
        if a != None:
            self.t.append((a, l))
        return a

    def free(self, a):
        for i in range(len(self.t)):
            if self.t[i][0] == a:
                del self.t[i]
                return

    def _get_new_addr(self, l):
        if len(self.t) == 0:
            if l <= self.s:
                return 0
        elif len(self.t) == 1:
            if l <= self.s-self.t[0][1]:
                return self.t[0][0] + self.t[0][1]
        else:
            raise Exception("not implemented. patches are welcome")
            
