__author__ = 'liu.xingjie'

def isHappy(n):
    val = set()
    while n not in val:
        val.add(n)
        newn = 0
        while n != 0:
            newn +=  (n % 10) * (n % 10)
            n /=  10
        n = newn
        if n == 1:
            return True
    return False

if __name__ == '__main__':
    result = isHappy(23)
    print result