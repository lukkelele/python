# Game Engine
---

\<insert details\>

---
## Rotating space

### 2D rotation
P(x,y) -> Q(x,y) <br>
P(1,1) -> Q(x,y) <br>
Rotating by theta, Qx = Ax + Bx  (Px\*Ax + Px\*Bx)   <br>
In the same manner -> Qy = Ay + By (Py\*Ay + Py\*By) <br>
<br>
Qx = Px\*Ax + Py\*Bx <br>
Qy = Px\*Ay + Py\*By <br>
<br>
Rotating 2D with three vectors. <br>
\[Px Py 1\] \* \[ Ax Ay 0 \] <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\[ Bx By 0 \] <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\[ Tx Ty 1 \] <br>
<br>
A = Forward vector  
B = Orthogonal vector  
T = Translation vector  

### 3D rotation
Rotating 3D with three vectors. <br>
*Point-at Matrix* <br>
\[Px Py 1\] \* \[ Ax Ay Az 0 \] <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\[ Bx By Bz 0 \] <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\[ Cx Cy Cz 0 \] <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\[ Tx Ty Tz 1 \] <br>
<br>
A = Forward vector  
B = Orthogonal vector  
C = Up vector  
T = Translation vector  
<br>
*Look-at Matrix*<br>
inverse(Point-at Matrix)
<br>
To gain camera perspective, take the inverse of the "point-at" matrix.

---
## Clipping


