from expression import Expression

"""
1/L_1 <= positive_roots <= L
-L_2 <= negative_roots <= -1/L_3

L_i = 1 + (B / c_n)^(1 / (n - k))
"""

def lagrange(f: Expression):
	limits = []
	n = len(f.get_coeffs()) - 1
	for i in range(0, 3+1):
		polys = f.get_coeffs(i)
		k = 0
		for j in range(0, n+1):
			if polys[j] < 0: 
				k = n - j
				break
		B = min(polys + [0])
		limits.append( 1 + ( abs(B) / polys[0] )**( 1 / (n - k) ) )

	# [negative_roots_interval, positive_roots_interval]
	return [ [-limits[2], -1/limits[3]], [1/limits[1], limits[0]] ]
