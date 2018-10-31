FILE=DifferentialCryptoanalysis.py
reverse:
	python $(FILE) reverseSBOXES
DDT:
	python $(FILE) DDT
reverseDDT:
	python $(FILE) reverseDDT
undistributed:
	python $(FILE) UNDISTRIBUTED
lambda:
	python $(FILE) LAMBDAandMU
reverseLambda:
	python $(FILE) reverseLAMBDAandMU
LAT:
	python $(FILE) LAT
reverseLAT:
	python $(FILE) reverseLAT