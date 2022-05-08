# 素数判定法と素因数分解アルゴリズム

## 概要

素数判定法と素因数分解アルゴリズムに関して、Pythonによるプログラム例を載せた教科書(になる予定)。

## 本文
[pdf](https://github.com/haru-44/prime_text/releases/latest/download/main.pdf)

以下のページは、pdfファイル出力用に作成したtexファイルから機械的に変換されています。
体裁不良がある場合はpdfファイルをご覧ください。

* 整数と素数、そして群
  * [数論の最初の一歩](https://haru-44.github.io/prime_text/html/first_step.html)
  * [試し割](https://haru-44.github.io/prime_text/html/trial_division.html)
  * [平方差法](https://haru-44.github.io/prime_text/html/fermat_factorization.html)
  * [剰余](https://haru-44.github.io/prime_text/html/modulo.html)
  * [群](https://haru-44.github.io/prime_text/html/group.html)
  * [Pollardのp-1法](https://haru-44.github.io/prime_text/html/p_minus_1.html)
* 平方剰余
  * [平方剰余と平方非剰余](https://haru-44.github.io/prime_text/html/quadratic_residue.html)
  * [Miller-Rabinテスト](https://haru-44.github.io/prime_text/html/miller_rabin.html)
  * [拡張Riemann予想とMillerテスト](https://haru-44.github.io/prime_text/html/riemann_miller.html)
* 原始根
  * [Lucasテスト](https://haru-44.github.io/prime_text/html/lucas_test.html)
  * [Pepinテスト](https://haru-44.github.io/prime_text/html/pepin_test.html)
  * [Pocklingtonテスト](https://haru-44.github.io/prime_text/html/pocklington_test.html)
* Fibonacci数列
  * [Fibonacci数列とLucas数列](https://haru-44.github.io/prime_text/html/fibonacci.html)
  * [環と体](https://haru-44.github.io/prime_text/html/ring.html)
  * [2次Frobeniusテスト](https://haru-44.github.io/prime_text/html/quadratic_frobenius_primality_test.html)
  * [Lucas-Lehmerテスト](https://haru-44.github.io/prime_text/html/lucas_lehmer_primality_test.html)
  * [Williamsのp+1法](https://haru-44.github.io/prime_text/html/p_plus_1.html)
* 篩
  * [Eratosthenesの篩](https://haru-44.github.io/prime_text/html/sieve.html)
  * [2次篩法](https://haru-44.github.io/prime_text/html/quadratic_sieve_algorithm.html)
  * [数体篩法](https://haru-44.github.io/prime_text/html/number_field_sieve.html)
* その他の方法
  * [Pollardのρ法](https://haru-44.github.io/prime_text/html/rho_method.html)
  * [2次形式](https://haru-44.github.io/prime_text/html/quadratic_form.html)
  * [AKSテスト](https://haru-44.github.io/prime_text/html/aks_test.html)
  * [楕円曲線](https://haru-44.github.io/prime_text/html/elliptic_curve.html)

## 解説アルゴリズム

* 素数判定法
  * Fermatテスト
    * [fermat_test.py](https://github.com/haru-44/prime_text/blob/main/src/fermat_test.py)
  * Solovay-Strassenテスト
    * [solovay_strassen_test.py](https://github.com/haru-44/prime_text/blob/main/src/solovay_strassen_test.py)
  * Miller-Rabinテスト
    * [miller_rabin_test.py](https://github.com/haru-44/prime_text/blob/main/src/miller_rabin_test.py)
  * Millerテスト
  * Lucasテスト
    * [lucas_primality_test.py](https://github.com/haru-44/prime_text/blob/main/src/lucas_primality_test.py)
  * Pepinテスト
    * [pepin_test.py](https://github.com/haru-44/prime_text/blob/main/src/pepin_test.py)
  * Pocklingtonテスト
    * [pocklington_test.py](https://github.com/haru-44/prime_text/blob/main/src/pocklington_test.py)
  * Prothテスト
    * [proth_test.py](https://github.com/haru-44/prime_text/blob/main/src/proth_test.py)
  * Fibonacci数列テスト
    * [fibonacci_pseudoprime_test.py](https://github.com/haru-44/prime_text/blob/main/src/fibonacci_pseudoprime_test.py)
  * Lucas数列テスト
    * [lucas_sequence_test.py](https://github.com/haru-44/prime_text/blob/main/src/lucas_sequence_test.py)
  * 2次Frobeniusテスト
  * Lucas-Lehmerテスト
    * [lucas_lehmer_primality_test.py](https://github.com/haru-44/prime_text/blob/main/src/lucas_lehmer_primality_test.py)
  * AKSテスト
    * [aks_test.py](https://github.com/haru-44/prime_text/blob/main/src/aks_test.py)
* 素因数分解アルゴリズム
  * 試し割
    * [trial_division.py](https://github.com/haru-44/prime_text/blob/main/src/trial_division.py)
  * Fermat法
    * [fermat_factorization_method.py](https://github.com/haru-44/prime_text/blob/main/src/fermat_factorization_method.py)
  * Lehman法
    * [lehman_method.py](https://github.com/haru-44/prime_text/blob/main/src/lehman_method.py)
  * p-1法
    * [p_minus_1_method.py](https://github.com/haru-44/prime_text/blob/main/src/p_minus_1_method.py)
    * [p_minus_1_method_stage2.py](https://github.com/haru-44/prime_text/blob/main/src/p_minus_1_method_stage2.py)
  * p+1法
    * [p_plus_1_method.py](https://github.com/haru-44/prime_text/blob/main/src/p_plus_1_method.py)
  * ρ法
    * [pollard_rho_algorithm.py](https://github.com/haru-44/prime_text/blob/main/src/pollard_rho_algorithm.py)
  * 楕円曲線法
    * [elliptic_curve_method.py](https://github.com/haru-44/prime_text/blob/main/src/elliptic_curve_method.py)
    * [elliptic_curve_method_fast.py](https://github.com/haru-44/prime_text/blob/main/src/elliptic_curve_method_fast.py)
  * 2次篩法
  * 数体篩法
* その他補助関数
  * 約数, 倍数
    * [gcd.py](https://github.com/haru-44/prime_text/blob/main/src/gcd.py)
    * [extended_gcd.py](https://github.com/haru-44/prime_text/blob/main/src/extended_gcd.py)
    * [lcm.py](https://github.com/haru-44/prime_text/blob/main/src/lcm.py)
    * [divisors.py](https://github.com/haru-44/prime_text/blob/main/src/divisors.py)
  * 逆元
    * [inverse_mod.py](https://github.com/haru-44/prime_text/blob/main/src/inverse_mod.py)
  * 累乗数判定
    * [is_perfect_power.py](https://github.com/haru-44/prime_text/blob/main/src/is_perfect_power.py)
  * 平方剰余
    * [legendre_symbol.py](https://github.com/haru-44/prime_text/blob/main/src/legendre_symbol.py)
    * [jacobi_symbol.py](https://github.com/haru-44/prime_text/blob/main/src/jacobi_symbol.py)
    * [tonelli_shanks_algorithm.py](https://github.com/haru-44/prime_text/blob/main/src/tonelli_shanks_algorithm.py)
    * [cipolla_algorithm.py](https://github.com/haru-44/prime_text/blob/main/src/cipolla_algorithm.py)
  * べき根
    * [sqrt_int.py](https://github.com/haru-44/prime_text/blob/main/src/sqrt_int.py)
    * [nth_root_int.py](https://github.com/haru-44/prime_text/blob/main/src/nth_root_int.py)
  * 位数
    * [n_order.py](https://github.com/haru-44/prime_text/blob/main/src/n_order.py)
  * 原始根
    * [primitive_root.py](https://github.com/haru-44/prime_text/blob/main/src/primitive_root.py)
  * 中国の剰余定理
    * [chainese_remainder_theorem.py](https://github.com/haru-44/prime_text/blob/main/src/chainese_remainder_theorem.py)
  * Fibonacci数列
    * [fibonacci_sequence.py](https://github.com/haru-44/prime_text/blob/main/src/fibonacci_sequence.py)
    * [lucas_sequence.py](https://github.com/haru-44/prime_text/blob/main/src/lucas_sequence.py)
    * [lucas_sequence_v.py](https://github.com/haru-44/prime_text/blob/main/src/lucas_sequence_v.py)
  * 篩
    * [sieve_of_eratosthenes.py](https://github.com/haru-44/prime_text/blob/main/src/sieve_of_eratosthenes.py)
    * [b_smooth_sieve.py](https://github.com/haru-44/prime_text/blob/main/src/b_smooth_sieve.py)
    * [factor_sieve.py](https://github.com/haru-44/prime_text/blob/main/src/factor_sieve.py)
  * 楕円曲線
    * [EllipticCurveAffine.py](https://github.com/haru-44/prime_text/blob/main/src/EllipticCurveAffine.py)
    * [elliptic_curve_order.py](https://github.com/haru-44/prime_text/blob/main/src/elliptic_curve_order.py)
    * [elliptic_curve_points.py](https://github.com/haru-44/prime_text/blob/main/src/elliptic_curve_points.py)
  * 数学関数
    * [totient_function.py](https://github.com/haru-44/prime_text/blob/main/src/totient_function.py)
    * [dickman_function.py](https://github.com/haru-44/prime_text/blob/main/src/dickman_function.py)
  * 高速べき乗演算
    * [n_times.py](https://github.com/haru-44/prime_text/blob/main/src/n_times.py)
  * その他
    * [split_int.py](https://github.com/haru-44/prime_text/blob/main/src/split_int.py)
    * [quadratic_form_reduction.py](https://github.com/haru-44/prime_text/blob/main/src/quadratic_form_reduction.py)

## 著者

[@haru_44](https://twitter.com/haru_44)
