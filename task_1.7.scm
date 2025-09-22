(define (sqrt-iter old-guess guess x)
	(if (good-enough? old-guess guess)
		guess
		(sqrt-iter guess (improve guess x) x)))

(define (good-enough? old-guess guess)
	(< (abs (- old-guess guess)) 0.001))

(define (improve guess x)
	(average guess (/ x guess)))

(define (average x y)
	(/ (+ x y) 2))

(define (abs x)
  (if (< x 0)
    (- 0 x)
    x))

(display (sqrt-iter 0.0 1.0 9.0))
(newline)

(exit)
