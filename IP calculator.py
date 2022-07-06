#Ahmed Hammad -> IP Calculator :) 
import math
while True :
        print('Enter your ip octet octet ')
        oc1 = int(input('Enter your first Octet ^__^  :'))
        if oc1 >= 256 :
            print('Error in the first Octet')
            
        oc2 = int(input('Enter your second Octet ^__^  :'))
        if oc2 >= 256:
            print('Error in the Second Octet')
        oc3 = int(input('Enter your Third Octet ^__^  :'))
        if oc3 > 256:
            print('Error in the Third Octet')
        oc4 = int(input('Enter your Forth Octet ^__^  :'))
        if oc4 > 256:
            print('Error in the Forth Octet')
        CIDR = int(input('Enter your CIDR to calculate NW address and broadcast address :'))
        if CIDR >= 33 :
            print('Incorrect CIDR')
        oc1b = format(oc1,'b') #oc1b ==>> octet 1 binary 
        oc2b = format(oc2,'b')
        oc3b = format(oc3,'b')
        oc4b = format(oc4,'b')
        ip =  str(oc1)+'.'+str(oc2)+'.'+str(oc3)+'.'+str(oc4)
        print('Your IP : %s/%s '%(ip,CIDR))
        print('Convert IP from Decimal To Binary :',oc1b+'.'+oc2b+'.'+oc3b+'.'+oc4b)


        if oc1 >= 1 and oc1 < 128:
            print('Your IP from class A')
        elif oc1 == 127 :
            print('This is loopback address')
        elif oc1 >= 129 and oc1 < 192 :
            print('Your IP from class B')
        elif oc1 >= 192 and oc1 < 224:
            print('Your IP from class C')
        elif oc1 >= 224 and oc1 < 240:
            print('Your IP from class D')
        elif oc1 >= 240 and oc1 < 255:
            print('Your IP from class E')
        else :
                print('Conifrm your inputs ^__^  ')

        #For definnig NW & BC address
        x1 = 255 #11111111
        x2 = 254 #11111110
        x3 = 252 #11111100 
        x4 = 248 #11111000
        x5 = 240 #11110000
        x6 = 224 #11100000 
        x7 = 192 #11000000
        x8 = 128 #10000000
        x9 =  0  #00000000

        if CIDR == 0 :
            nipoc1 = x9 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 0.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(x1)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(x1)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(x1)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 1 :
            nipoc1 = x8 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 128.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(255-x8)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x8)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+127)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 2 :
            nipoc1 = x7 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 224.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1+63)+'.'+str(255-nipoc2)+'.'+str(255-nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x7)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+63)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 3 :
            nipoc1 = x6 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 240.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1+31)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x6)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+31)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 4 :
            nipoc1 = x5 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 248.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1+15)+'.'+str(x1)+'.'+str(x1)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x5)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+15)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 5 :
            nipoc1 = x4 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 252.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            WC = str(255-x4)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            BC = str(nipoc1+7)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+7)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 6 :
            nipoc1 = x3 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            WC = str(255-x3)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            BC = str(nipoc1+3)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+3)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 7 :
            nipoc1 = x2 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 254.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1+1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x2)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(x9)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1+1)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 8 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x9 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.0.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(255-nipoc2)+'.'+str(255-nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(x9)+'.'+str(x1)+'.'+str(x1)+'.'+str(255)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(x1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 9 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x8 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.128.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(x1-x8)+'.'+str(255-nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x8)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(x1-x8)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 10 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x7 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.192.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(x1-x7)+'.'+str(255-nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x7)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(x1-x7)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 11 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x6 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.224.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2+31)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x6)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2+31)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 12 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x5 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.240.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2+15)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x5)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2+15)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 13 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x4 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.248.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2+7)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x4)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2+7)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 14 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x3 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.252.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2+3)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x3)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2+3)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 15 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x2 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.254.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2+1)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x2)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2+1)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 16 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x9 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.0.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(255-nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(x9)+'.'+str(255-x1)+'.'+str(x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x9)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(x1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 17 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x8 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.128.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+127)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x8)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+127)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
         #if CIDR == 18 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x7 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.192.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+63)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x7)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+63)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 19 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x6 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.224.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+31)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x6)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+31)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 20 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x5 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.240.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+15)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(x8)+'.'+str(x8)+'.'+str(255-x5)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+15)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 21 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x4 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.248.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+7)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x4)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+7)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 22 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x3 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.252.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x3)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+3)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 23 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x2 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.254.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+1)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x2)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3+1)+'.'+str(x1-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 24 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x9 & oc4
            print('Your Subnet Mask = 255.255.255.0')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(255 - nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(255 -nipoc4)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 25 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x8 & oc4
            print('Your Subnet Mask = 255.255.255.128')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+127))
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x8)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+127)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 26 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x7 & oc4
            print('Your Subnet Mask = 255.255.255.192')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+63))
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x7)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+63)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 27 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x6 & oc4
            print('Your Subnet Mask = 255.255.255.224')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+31))
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x6)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+31)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 28 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x5 & oc4
            print('Your Subnet Mask = 255.255.255.240')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+15))
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x5)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+15)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 29 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x4 & oc4
            print('Your Subnet Mask = 255.255.255.248')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+7))
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x4)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+7)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 30 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x3 & oc4
            print('Your Subnet Mask = 255.255.255.252')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+3)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x3)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+3)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 31 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x2 & oc4
            print('Your Subnet Mask = 255.255.255.254')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x2)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4+1)-1)
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        if CIDR == 32 :
            nipoc1 = x1 & oc1 #New IP octet 1
            nipoc2 = x1 & oc2
            nipoc3 = x1 & oc3
            nipoc4 = x1 & oc4
            print('Your Subnet Mask = 255.255.255.255')
            NW = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your NW address :%s/%s'%(NW,CIDR))
            BC = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4)
            print('Your BC address : %s/%s'%(BC,CIDR))
            WC = str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)+'.'+str(255-x1)
            print('Your WC address : %s/%s'%(WC,CIDR))
            Hostmin = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str(nipoc4+1)
            Hostmax = str(nipoc1)+'.'+str(nipoc2)+'.'+str(nipoc3)+'.'+str((nipoc4))
            print('First IP = %s\nLast IP =%s'%(Hostmin,Hostmax))
            addr = pow(2,32-CIDR) - 2
            NET = pow(2,CIDR)
            print('Number of Networks = %d and every NW has %d of address'%(NET,addr))
        print('======================================================================================================================')
#Ahmed Salah Hammad
