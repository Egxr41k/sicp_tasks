(define (p) (p))
(define (test x y)
	(if (= x 0) 0 y))

; (test 0 (p)) 
; normal-order: error on line 1
; application-order: 0, test 0 always will return 0 
