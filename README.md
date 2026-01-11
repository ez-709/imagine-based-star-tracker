An algorithm has been developed to estimate the roll angle of a spacecraft using nadir-pointing images of the Earth. The method involves:  
1) threshold-based binarization of the image;  
2) detection of the Earth’s limb as the sequence of highest white pixels in each column;  
3) least-squares fitting of a circular arc to the limb;  
4) computation of the roll angle from the orientation of the fitted circle’s center.

The algorithm has been validated on daylight Earth images. Current limitations include failure on night-side imagery and sensitivity to bright artifacts such as the Sun or Moon. Extension to pitch estimation requires prior knowledge of camera intrinsic parameters.

<img width="1880" height="676" alt="изображение" src="https://github.com/user-attachments/assets/8ba9093b-c18e-45a3-88ba-db2e628e90a2" />
 
