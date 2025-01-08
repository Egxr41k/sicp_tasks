(define (f n) 
  (if (< n 3) 
      n 
      (+ (f (- n 1)) (f (- n 2)) (f (- n 3)))))

(display (f 10))
(newline)

(define (iterative-f n) 
  (f-iter 0 1 2 n))

(define (f-iter a b c count)
  (if (< count 3)
      c
      (f-iter b c (+ a b c) (- count 1))))

(display (iterative-f 10))
(newline)

