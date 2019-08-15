import math
import scipy.stats as st
from scipy.stats import norm
from scipy.optimize import newton



def get_z_value(fz):
    return round(st.norm.ppf(fz), 4)

def get_lz_value(z_val):
    N = norm(0,1)
    return round(N.pdf(z_val) - z_val*(1-N.cdf(z_val)), 4) 

def get_z_value_from_lz_val(lz_val):
    def f(y): 
        return get_lz_value(y) - lz_val
    return newton(f, 1.0)

class EOQ:
    @staticmethod
    def get_eoq_q(lamb, K, h):
        return int(round(math.sqrt(2 * lamb * K / h)))

class QR:
    @staticmethod
    def get_FR(Q, h, p, lamb):
        return round(1 - ((Q * h)/(p * lamb)), 2)

    @staticmethod
    def get_R(sigma, z_val, mu):
        return int(round((sigma * z_val) + mu))

    @staticmethod
    def get_nr(sigma, lz_val):
        return round(sigma * lz_val , 2)

    @staticmethod
    def get_Q(lamb, k, p, nR_val, h):
        return int(round(math.sqrt(( 2* lamb * (k + (p*nR_val))) / h)))

    @staticmethod
    def get_holding_cost(h, s, Q):
        return round( h * (s + (Q/2)), 2)

    @staticmethod
    def get_fixed_cost(K, T):
        return round(K/T, 2)
    
    @staticmethod
    def get_shortage_cost(p, nR, T):
        return round(p * (nR/T), 2)

def midterm_QR_analyzed():
    lamb = 150
    c = 15
    K = 5
    i = 10
    h = 1.5
    p = 4
    T = 1.0/12.0
    mu = 50
    sigma = 28.87


    iter = 0
    Q = EOQ.get_eoq_q(lamb, K, h)
    FR = 0
    z = 0
    R = 0
    lz = 0
    nr = 0
    q_prev = Q
    r_prev = R

    while (iter < 5):
        print "-" * 20 + str(iter) + "-" * 20
        print 'Q: {}'.format(Q)
        FR = QR.get_FR(Q, h, p, lamb)
        print 'FR: {}'.format(FR)
        z = get_z_value(FR)
        print 'z: {}'.format(z)
        R = QR.get_R(sigma, z, mu)
        print 'R: {}'.format(R)
        lz = get_lz_value(z)
        print 'lz: {}'.format(lz)
        nr = QR.get_nr(sigma, lz)
        print 'nr: {}'.format(nr)
        Q = QR.get_Q(lamb, K, p, nr, h)
        print 'Q: {}'.format(Q)
        iter += 1
        if R == r_prev or Q == q_prev:
            break

        r_prev = R
        q_prev = Q

    safety_stock = R - mu
    h_cost = QR.get_holding_cost(h, safety_stock, Q)
    print 'holding cost: {}'.format(h_cost)

    f_cost = QR.get_fixed_cost(K, T)
    print 'fixed cost: {}'.format(f_cost)

    s_cost = QR.get_shortage_cost(p, nr, T)
    print 'shortage cost: {}'.format(s_cost)

    print 'total cost: {}'.format(h_cost + f_cost + s_cost)

# midterm_QR_analyzed()

# print get_lz_value(1.25)

print get_z_value(0.8)
print get_z_value(0.4736)
print get_z_value(0.421)


