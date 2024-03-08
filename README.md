# This is A Project of Calculation and Design of Turbine Machine

> TMCAL

### INPUT DATA
- G - consumption of air
- $\pi_k$ - Overall degree of pressure increase
- $P_H$ - outside atmospheric pressure
- $T_H$ - outside temperature
- $\delta_{BX}$ - Total pressure recovery coefficient
- $\eta_K$ - Compressor overall efficiency


### Selecting parameters
#### *First Section*
- $\rho_{k1}$ - degree of reactivity
    > range (0.55 - 0.6)
    > selection 0.5
- $\overline{d}_{BT1}$ - relative diameter of the bushing of the first stage of the compressor of existing turbojet engines
    > range (0.35 - 0.45)
    > selection 0.4
- $U_{k1}$ - peripheral speed at the outer diameter of the first subsonic stage
    > range (330 - 400)
    > selection 360
- $U_{cp1}$ - peripheral speed at the average diameter of the first subsonic stage
    > formula $U_{cp1}=U_{k1}\sqrt{\frac{1+\overline{d}_{BT1}^2}{2}}=360\frac{1+0.4}{2}=252m/c$
    > range (? - ?)
    > calculation 274.168
    > verification $U_{cp1}=a_1M_u$
- $\overline{H}_{th1}$ - theoretical pressure coefficient at the average diameter of the first stage of subsonic turbojet compressors
    > range (0.25 - 0.4)
    > selection 0.315
- $H_{th1}$ - theoretical pressure at the average diameter of the first stage of subsonic TRD compressors
    > formula $H_{th1}=\overline{H}_{th1}U_{cp1}^2$
    > range (30 - 34)
    > calculation 23.678
- $\overline{C}_{1a}$ - coefficient of air inlet flow rate into the first stage wheel at the middle radius
    > formula $\overline{C}_{1a}=\frac{C_{1a}}{U_{cp1}}$
    > range (0.4 - 0.7)
    > selection 0.65
- $C_{1a}$ - axial speed of air entry into the first stage wheel at the middle radius
    > range (170 - 180)
    > calculation 178.209
- $ctg\alpha_1$ - cotangent of $\alpha_1$
    > formula $ctg\alpha_1=\frac{2(1-\rho_k)-\overline{H}_{th1}}{2\overline{C}_{1a}}$
    > calculation 0.527
- $\alpha_1$ - angle of air entry into the first stage wheel at medium radius
    > calculation 1.086 (radian), 62.214(degree)
- $a_{1kp}$ - local critical speed of sound in the first subsonic compressor stage
    > formula $a_{1kp}=18.3\sqrt{T_H^*}$
    > calculation 310.561
- $\lambda_1$ - superficial speed
    > formula $\lambda_{1}=\frac{\lambda_{1a}}{sin\alpha_1}=\frac{C_{1a}}{a_{1kp}sin\alpha_1}$
    > calculation 0.649
- $q(\lambda)$ - gas-dynamic flow function
    > formula $q(\lambda)=(\frac{k+1}{2})^{\frac{1}{k-1}}\lambda(1-\frac{k-1}{k+1}\lambda^2)^{\frac{1}{k-1}}$
- $\overline{G}_k$ - compressor first stage performance coefficient
    > formula $\overline{G}_k=(1-\overline{d}_{BT1}^2)q(\lambda_1)sin\alpha_1$
- $\lambda_u$ - superficial peripheral speed
    > formula $\lambda_u=\frac{U_{cp1}}{a_{1kp}}$
- $a_1$ - speed of sound at wheel entrance
    > formula $a_1=\frac{a_{1kp}}{\frac{a_{1kp}}{a_1}}$
    > where formula $\frac{a_{1kp}}{a_1}=\frac{1}{\sqrt{\frac{k+1}{2}\tau(\lambda_1)}}$
- $M_{w1}$ - Mach number at the entrance to the first stage impeller
    > $M_{w1}=\frac{a_{1kp}}{a_1}\sqrt{\lambda_1^2+\lambda_u^2-2\lambda_1\lambda_2cos\alpha_1}$
- $M_u$ - Mach number along the peripheral speed of the wheel
    > formula $M_u=\frac{M_{w1}}{\sqrt{\overline{C}_{1a}^2+(\rho_k+\frac{\overline{H}_{th1}}{2})^2}}$

#### *Second Section*
- $H_{k1}$ - work expended in the first stage
    > formula $H_{k1}=\frac{H_{th1}\Omega}{\eta_3\eta_f}$
    > for the first stage you can take $\eta_3\eta_f=0.97/0.98$ and $\Omega=0.98/1.0$. But we take them all 0.98.
    > so we take $H_{k1}=H_{th1}$

- $D_{k1}$ - diameter of the compressor first stage wheel
    > formula $D_{k1}=\sqrt{\frac{4G_B\sqrt{T_B^*}}{\pi S_BP_B^*\overline{G}_KK_G}}$
    > where  
    > $T_B^*=T_H^*$
    > $p_B^*=P_H^*\delta_{BX}$
    > $S_B=\sqrt{K(\frac{2}{k_1})^{\frac{k+1}{k-1}}\frac{1}{R}}$
    > where 
    > $\delta_{BX}$ - Total pressure recovery coefficient at entrance device
    > while K = 1.4 and R = 287.3 kJ/(kg*K), $S_B=0.0404$

#### Notation Rules
- $H_{th1}$ - use “_” to indicate subscript
- $T_{k1}^*$ - use "__" to indicate superscript
    > T_k1__tot = ?
- If subscript and superscript exist at the same time, you need to express the subscript first and then the superscript.
    > example: $T_{k1}^*$
    > notate as: T_k1__tot
- In particular, * (for example, total parameters of gas) is represented by tot
    > example: $T^*$
    > notate as: T__tot
- Greek letters are represented by Roman pronunciation
    > example: $\Omega$
    > notate as: Omega
    > example: $\eta$
    > notate as: eta
- If you encounter $\Delta$, for this Character, we use "d"
    > example: $\Delta\alpha$
    > notate as: dalpha
- If the subscript is very complicated, you can agree with the team members in advance on a simple writing method.
    > example: $(\Delta\alpha)_{\frac{b}{t}=1}$
    > notate as: dalpha_bt1
- If an overline appears, add one in front of the entire notation "_", but in python file, variables with "_" in the front can't be exported. so you need to add an "o" in the front, like "o_".
    > example: $\overline{\Delta\beta}$
    > notate as: o_dbeta
- If a division operation appears in the formula, add an underscore before the numerator and denominator, and add "frac" at the front
    > example: $\frac{b}{c}$
    > frac_b_c

#### Some examples
> example 1
> $(\overline{\Delta\alpha})_{\frac{b}{t}=1}$   
> notate as: o_dalpha_bt1
> example 2
> $(\frac{b}{t})_{c.a.}$
> notate as: frac_b_t_ca
