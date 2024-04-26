# Python 3 program to find a prime factor of composite using
# Pollard's Rho algorithm
import random
import math


# Function to calculate (base^exponent)%modulus
def modular_pow(base, exponent, modulus):
    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result


# method to return prime divisor for n
def PollardRho(n):
    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_pow(x, 2, n) + c + n) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d

def calculate_PhiN(p, q):
    return (p-1)*(q-1)

def gcd(a, b):
	if(b == 0):
		return abs(a)
	else:
		return gcd(b, a % b)

def calculate_LambdaN(p, q):
    lambdaN = calculate_PhiN(p, q) // gcd(p-1, q-1)
    return lambdaN

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def decrypt(m, d, n):
    msg_decrypted = modular_pow(m, d, n)
    return msg_decrypted

# Driver function
if __name__ == "__main__":
    e = 1009
    n = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    p = PollardRho(n)
    q = n // p
    nPQ = q * p
    print("p = ", p)
    print("q = ", q)
    # print('npq = ', nPQ)
    if (nPQ != n):
        print('npq = ', nPQ)
        print('ERROR')

    # phiN = calculate_PhiN(p, q)
    lamN = calculate_LambdaN(p, q)
    d = modinv(e, lamN)
    print("d = ", d)
    g = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308
    cle = modular_pow(g, d, n)
    print("cle = ", cle)
    # m = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    # print(decrypt(m, d, n))

    # print("gcd test with 6 and 12346 = ", gcd(6, 12346))
    # print('lambda test with 7 and 12347 = ', calculate_LambdaN(7, 12347))
    # print('test calculate_D = ', modinv(5, calculate_LambdaN(7, 12347)))

