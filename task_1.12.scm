;; Вычисляем отдельный элемент треугольника Паскаля
(define (pascal row col)
  (cond ((= col 0) 1)                     ; край слева
        ((= col row) 1)                   ; край справа
        (else (+ (pascal (- row 1) (- col 1))   ; сверху-слева
                 (pascal (- row 1) col)))))     ; сверху-справа

(define (print-row row col)
  (cond ((<= col row)
        (display (pascal row col))
        (display " ")            ; пробел для читаемости
        (print-row row (+ col 1)))))

(define (print-triangle n row)
    (cond ((< row n)
        (print-row row 0)
        (newline)
        (print-triangle n (+ row 1)))))

;; Запуск: 5 строк
(print-triangle 5 0)
(exit)
