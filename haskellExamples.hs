-- Function that multiplies two numbers --
answer x y = x * y -- Function inputs = what we want to do --

-- isPalindrome xs = xs == (reverse xs) --

-- isPalindrome x = show x == (reverse (show x)) --

-- isPalindrome 432 --
scale :: Num a => a -> a -> a
scale n f = n * f

scaleTuple  (a, b) f = (a * f, b * f)

dotProduct (a, b, c) (d, e, f) = a*d+b*e+c*f

doublePos xs = [x | x <- xs]

spaces n = [ ' ' | _ <- [1..n]]

mults  n = [ x | x <- [1..(n-1)]]

mults1  n = sum [ x | x <- [1..(n-1)],x `mod` 5 == 0 || x `mod` 3 == 0]

isMults x = x `mod` 5 == 0 || x `mod` 3 == 0
mults2 n = sum [ x | x <- [1..(n-1)],isMults x]

isPalindrome n = (show n) == (reverse (show n))

count 1000 = []
count n = n : count (n+1)

-- fib 0 == 0
-- fib 1 == 1
fib n = fib (n-1) + fib(n-2)



solve1 = maximum [x*y | x <- [10..99], y <- [10..99], isPalindrome (x*y)] -- Ctrl + C causes intrupptions to get out of outputs that do not stop --

-- solve2 = maximum [x*y | x <- [s..e], y <- [s..e], isPalindrome (x*y)] -- Ctrl + C causes intrupptions to get out of outputs that do not stop --

-- Project Euler used as test questions for Haskell --

sumOfReverse n = n + (read (reverse (show n)))

allDigitsOdd n = go (show n)
    where
go (x:xs)
    | even (charValue x) = False
    | null xs = True
    | otherwise = go xs

charValue c = (fromEnum c) - 48

howManyRevs n = length [x | x <- [1..(n-1)], allDigitsOdd (sumOfReverse x)]
lastDigitZero n = (last (show n)) == '0'
howManyRevs1 n = length [x | x <- [1..(n-1)], not (lastDigitZero x), allDigitsOdd(sumOfReverse x)]

isDivisibleBy1ToN v n = go v [1..n]
    where
    go v (x:xs)
        | v `mod` x /= 0 = False
        | null xs = True
        | otherwise = go v xs

isPrime n = ip n [2..(isqrt (n))]

    where

    ip _ [] = True

    ip n (x:xs)

        | n `mod` x == 0 = False

        | otherwise = ip n xs

isqrt :: Integral i => i -> i

isqrt = floor . sqrt . fromIntegral
primeFactors n = [ x | x <- [2..n], isPrime x, n `mod` x == 0]

primeList n = go n 1 2
    where
    go n c p
        | c > n = []
        | isPrime p = p : go n (c+1) (p+1)
        | otherwise = go n c (p+1)
findNthPrime n = last (primeList n)

--------------------------------------------------

-- Tuesday 23rd Janurary Notes --

-- In Haskell, the colon (:) operator is used for constructing lists. It is also referred to as the "cons" operator.
-- When used between an element and a list, it adds the element to the front of the list.
squareADigit c = ((fromEnum c)-48) ^2
processDigits xs = sum [squareADigit x | x <- xs]