# Game Engine
---
\<insert details\>
---
## Rotating space
####2D
P(x,y) -> Q(x,y) <br>
P(1,1) -> Q(x,y) <br>
Rotating by theta, Qx = Ax + Bx  (Px\*Ax + Px\*Bx)   <br>
In the same manner -> Qy = Ay + By (Py\*Ay + Py\*By) <br>
<br>
Qx = Px\*Ax + Py\*Bx <br>
Qy = Px\*Ay + Py\*By <br>
<br>

### 3D
\[Px Py 1\] \* \[ Ax Ay 0 \] <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ Bx By 0 ] <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ Tx Ty 1 ] <br>
---
## Clipping


