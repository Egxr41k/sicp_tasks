(define (curt-iter old-guess guess x)
	(if (good-enough? old-guess guess)
		guess
		(curt-iter guess (improve guess x) x)))

(define (good-enough? old-guess guess)
	(< (abs (- old-guess guess)) 0.001))

(define (improve guess x)
	(/ (+ (/ x (* guess guess)) (* 2 guess)) 3))

(define (average x y)
	(/ (+ x y) 2))

(define (abs x)
(if (< x 0)
(- x)
x))

(display (curt-iter 10.0 9.0 64.0))
(newline)

(exit)
