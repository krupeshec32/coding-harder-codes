'''
Given an ip address as an input string, validate it and return True/False
192.0.2.1
'''


class IpAdderessValidator:

    def __init__(self, inputIp):
        self.inputIp = inputIp

    def isValid(self, inputIp):
        flag = True
        if inputIp.count('.') == 3 or inputIp.count(':') == 7:
            if inputIp.count('.') == 3:
                ipv4 = inputIp.split('.')
                for i in ipv4:
                    if 0 <= int(i) <= 255 and type(int(i)) == int:
                        pass
                    else:
                        return False
                return flag
            else:
                ipV6 = inputIp.split(':')
                for i in ipV6:
                    if not i.isalnum():
                        return False
                    else:
                        pass
                return flag
        else:
            return False

inputIp='2001:db8:3333:4444:5555:6666:7777:9999'
x=IpAdderessValidator(inputIp)
assert(x.isValid(inputIp))