def generate_sieve(limit):
    """
    Generate a list of boolean values representing the primality of numbers from 0 to limit.
    
    :param limit: The upper bound of the range to check for prime numbers.
    :return: A list where index i is True if i is a prime number, False otherwise.
    """
    # Step 1: Create a list of boolean values representing the primality of numbers
    sieve = [True] * (limit + 1)  # Initialize all entries to True
    sieve[0] = sieve[1] = False   # 0 and 1 are not primes
    
    # Step 2: Iterate through each number up to the square root of the limit
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:  # If start is still marked as prime
            # Step 3: Mark all multiples of start as not prime
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    
    return sieve  # Return the sieve array

def extract_primes(sieve):
    """
    Extract prime numbers from a boolean sieve list.
    
    :param sieve: A list of boolean values where True indicates a prime number.
    :return: A list of prime numbers.
    """
    return [i for i in range(len(sieve)) if sieve[i]]

# Example usage:
if __name__ == "__main__":
    n = 100  # Example limit
    sieve = generate_sieve(n)
    primes = extract_primes(sieve)
    print(f"Primes up to {n}: {primes}")
