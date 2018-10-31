# Differential Cryptoanalysis of S-Boxes in a Block Cipher

**Prerequisites:** Python2 and MAKE

In this project, I analyzed S-Boxes in a block cipher.

The S-Boxes are enterred manually, to examine other S-Boxes the "SBoxes" variable in the script should be changed.

The python script has several capabilities:

1. Taking the inverse of the given S-Boxes.
2. Creating differential distribution tables (DDTs) and differential uniformities of S-Boxes and inverse S-Boxes.
3. Listing the indexes of the undistributed bits of S-Boxes.
4. Finding differential factor lambda and invariant output difference mu values of S-Boxes and inverse S-Boxes.
5. Creating linear approximation tables (LATs) and linear uniformity of S-Boxes.

## Usage:

**To take the inverse of the given S-Boxes:**  
>	$ make reverse

**To create DDTs of the given S-Boxes:**  
>	$ make DDT

**To create the inverse DDTs of the given S-Boxes:**  
>	$ make reverseDDT

**To list undistributed bits of the given S-Boxes:**  
>	$ make undistributed

**To find lambda and mu of the given S-Boxes:**  
>	$ make lambda

**To find lambda and mu of inverse of the given S-Boxes:**  
>	$ make reverseLAmbda

**To create LAT of the given S-Boxes:**  
>	$ make LAT

**To create LAT of inverse of the given S-Boxes:**  
>	$ make reverseLAT

For example outputs, you can see txt files named DDT, reverseDDT, LAMBDAandMU, reverseLAMBDAandMU, UNDISTRIBUTED, LAT and reverseLAT.

_For more information about differential cryptoanalysis, its importance and use-cases, you can refer [here](https://en.wikipedia.org/wiki/Differential_cryptanalysis)._
