import numpy as np


'''
references:
-----------
	...	Egozcue, J.J., Pawlowsky-Glahn, V., Mateu-Figueras, G. et al.
		Isometric Logratio Transformations for Compositional Data Analysis.
		Mathematical Geology 35, 279–300 (2003).
		https://doi.org/10.1023/A:1023818214614
'''

def helmert(n):
	"""
	matrix with n rows and n-1 columns. Inspired from R helmert implementation, returns Helmert contrasts, 
	which contrasts second column with first, the third with the average of the first two and so on.

	Essential for building orthogonal matrices.

	Args:
	-----
		n (int): number of rows.
	
	Returns:
	--------
		(ndarray): (n,n-1) orthogonal matrix.
	"""

	if n == 1:
		raise ValueError(f'n should be >= 2, but got {n}')
	if n == 2:
		return np.array([-1,1])

	first_row = np.array([-1 for _ in range(n-1)])
	main_mat = np.diag(range(1,n))

	for r in range(main_mat.shape[0]-1):  # skip last row
		for c in range(main_mat.shape[1])[::-1]:  # from right to left
			if main_mat[r][c] != 0:
				break
			main_mat[r][c] = -1

	main_mat = np.vstack((first_row, main_mat))

	return main_mat


def clr(X):
	# row-wise geometric mean
	r_geo_mean = np.prod(X, axis=1, keepdims=True)**(1/X.shape[1])

	# clr computation
	y = np.log(X/r_geo_mean)
	
	return y


def clrInv(y):
	"""
	inverse function for centrered-log-ratio transformed dataset 

	Args:
		y (ndarray): (I,J) clr transformed matrix.

	Returns:
		(ndarray): (I,J) reconstructed X matrix from y.
	"""
	# softmax/normalized exponential function
	X = np.exp(y)/np.sum(np.exp(y), axis=1, keepdims=True)
	return X


def ilr(X):
	"""
	(Isometric log-ratio) transformation.

	Args:
	-----
		X (ndarray): (I,J) matrix to transform

	Returns:
	--------
		y (ndarray): (I,J-1) ilr transformed data.
	"""
	y = np.log(X)
	y = y - y.mean(axis=1, keepdims=True) # Recentered values
	
	k = y.shape[1]
	H = helmert(k)  # Dimensions k by k-1
	H = H.T / np.sqrt(np.array(range(2,k+1))*np.array(range(1,k))).reshape(-1,1)
	return y@H.T


def ilrInv(y):
	k = y.shape[1]+1

	H = helmert(k)  # Dimensions k by k-1
	H = H.T / np.sqrt(np.array(range(2,k+1))*np.array(range(1,k))).reshape(-1,1)

	y_ = y@H
	X = np.exp(y_)/np.sum(np.exp(y_), axis=1, keepdims=True)
	return X


def alr(X, ref=-1):
	"""
	Additive-Log-Ratio (ALR) implementation.

	Args:
	-----
		X (ndarray): (I,J) data matrix.
		ref (int, optional): column index to use as reference values. Defaults to -1 (last column) 

	Returns:
	--------
		(ndarray): (I,J-1) transformed matrix.
	"""
	
	if not isinstance(ref, int):
		raise ValueError('invalid reference value. check the manual for valid values.')

	X_d = X[:,ref].reshape(-1,1)  # reference column values
	y = np.log(np.delete(X, ref, axis=1)/X_d)
	return y


def alrInv(y):
	"""
	inverse addditive-log-ratio

	Args:
	-----
		y (ndarray): (I,J-1) matrix of alr transformed data.

	Returns:
	--------
		(ndarray): (I,J) reconstructed alr transformed data.
	"""
	ref_recon = np.ones(y.shape[0]).reshape(-1,1)
	X = np.hstack((np.exp(y), ref_recon))/(np.exp(y).sum(axis=1)+1).reshape(-1,1)
	return X

