(define (f_iter a b c count)
	(if (< count 3)
		c
		(f_iter(b c (+ a b c) (- count 1)))))

(define (f n)
	(if (< n 3)
		n
		(+ (f (- n 1)) (* 2 (f (- n 2) )) (* 3 (f (- n 3) )))))

(display (f 10))
(newline)
(exit)
