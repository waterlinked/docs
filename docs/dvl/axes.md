# Axes

The axis convention is the same for all DVL models. Velocities and dead reckoning output use the vehicle frame. By default, the vehicle frame is the same as the body frame, but it can be adjusted to allow flexible mounting on the vehicle.

## Body frame

The DVL outputs velocity in a right-handed body frame:

* **x** points forward.
* **y** points right (starboard).
* **z** points down, toward the transducers (the metal back plate faces up).

Seen from above, with forward pointing up and ⊗ marking the **z** axis (pointing into the page, toward the seabed), the two model groups indicate forward differently:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 185 152" fill="currentColor" font-size="0.3em" text-anchor="middle">
  <defs>
    <marker id="ax-arrow-a" markerWidth="6" markerHeight="6" refX="4.5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z"/>
    </marker>
  </defs>
  <text x="80" y="14" font-size="1.5em">DVL A50 / A125</text>
  <circle cx="80" cy="92" r="36" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <circle cx="80" cy="92" r="4" fill="none" stroke="currentColor" stroke-width="0.6"/>
  <line x1="77.2" y1="89.2" x2="82.8" y2="94.8" stroke="currentColor" stroke-width="0.6"/>
  <line x1="82.8" y1="89.2" x2="77.2" y2="94.8" stroke="currentColor" stroke-width="0.6"/>
  <text x="71" y="94" text-anchor="end">z</text>
  <line x1="80" y1="88" x2="80" y2="30" stroke="currentColor" stroke-width="0.7" marker-end="url(#ax-arrow-a)"/>
  <text x="80" y="25">x (forward)</text>
  <line x1="84" y1="92" x2="150" y2="92" stroke="currentColor" stroke-width="0.7" marker-end="url(#ax-arrow-a)"/>
  <text x="154" y="94" text-anchor="start">y (right)</text>
  <circle cx="80" cy="61" r="2.3"/>
  <text x="90" y="54" text-anchor="start">LED</text>
  <line x1="88" y1="55" x2="81.5" y2="60" stroke="currentColor" stroke-width="0.3"/>
  <rect x="75.5" y="126" width="9" height="5" fill="currentColor" stroke="none"/>
  <line x1="80" y1="130" x2="80" y2="144" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
  <text x="91" y="141" text-anchor="start">Cable</text>
  <line x1="89" y1="139.5" x2="81.5" y2="140.5" stroke="currentColor" stroke-width="0.3"/>
</svg>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 185 152" fill="currentColor" font-size="0.3em" text-anchor="middle">
  <defs>
    <marker id="ax-arrow-b" markerWidth="6" markerHeight="6" refX="4.5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z"/>
    </marker>
  </defs>
  <text x="80" y="14" font-size="1.5em">DVL A100 / A250</text>
  <circle cx="80" cy="92" r="36" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <circle cx="80" cy="92" r="4" fill="none" stroke="currentColor" stroke-width="0.6"/>
  <line x1="77.2" y1="89.2" x2="82.8" y2="94.8" stroke="currentColor" stroke-width="0.6"/>
  <line x1="82.8" y1="89.2" x2="77.2" y2="94.8" stroke="currentColor" stroke-width="0.6"/>
  <text x="71" y="94" text-anchor="end">z</text>
  <line x1="80" y1="88" x2="80" y2="30" stroke="currentColor" stroke-width="0.7" marker-end="url(#ax-arrow-b)"/>
  <text x="80" y="25">x (forward)</text>
  <line x1="84" y1="92" x2="150" y2="92" stroke="currentColor" stroke-width="0.7" marker-end="url(#ax-arrow-b)"/>
  <text x="154" y="94" text-anchor="start">y (right)</text>
  <circle cx="80" cy="60" r="2.2" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <text x="90" y="53" text-anchor="start">FWD mark</text>
  <line x1="88" y1="54" x2="82" y2="58.5" stroke="currentColor" stroke-width="0.3"/>
  <circle cx="80" cy="112" r="4" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <circle cx="80" cy="112" r="1.6"/>
  <rect x="75.5" y="126" width="9" height="5" fill="currentColor" stroke="none"/>
  <line x1="80" y1="131" x2="80" y2="144" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
  <text x="116" y="116" text-anchor="start">Back-plate entry</text>
  <line x1="114" y1="114.5" x2="84.5" y2="112" stroke="currentColor" stroke-width="0.3"/>
  <text x="116" y="126" text-anchor="start">or side entry</text>
  <line x1="114" y1="124.5" x2="85" y2="129" stroke="currentColor" stroke-width="0.3"/>
</svg>

**Finding forward on the device.** On the DVL A50 and DVL A125, the status LED sits at the forward edge and marks **+x**. On the DVL A100 and DVL A250, the status LED faces down (the **z** direction), so forward is instead stamped **FWD** on the metal back plate. On all models the cable is toward the back of the housing, opposite forward (the **−x** side). On the DVL A100 and DVL A250 it enters either from the side or through the back plate (rear O-ring interface), as shown above. The mechanical drawings on the [DVL A100](dvl-a100.md) and [DVL A250](dvl-a250.md) pages show the FWD mark and cable position. 

### Origin

The origin of the body frame is the point at which the DVL measures velocity: the point on the DVL's central axis where the transducer beam axes intersect. In standard mounting orientation (transducers facing down, metal back plate up), it sits above the metal back plate, where the beam axes meet when extended upward:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 165" fill="currentColor" font-size="0.3em" text-anchor="middle">
  <defs>
    <marker id="vmo-beam" markerWidth="6" markerHeight="6" refX="4.5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z"/>
    </marker>
    <marker id="vmo-dim" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto-start-reverse">
      <path d="M0,0 L6,3 L0,6 Z"/>
    </marker>
  </defs>
  <line x1="100" y1="47" x2="100" y2="148" stroke="currentColor" stroke-width="0.3" stroke-dasharray="1,1.5" opacity="0.5"/>
  <path d="M58,85 L58,96.9 L88,111.1 L112,111.1 L142,96.9 L142,85 Z" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <rect x="58" y="82" width="84" height="3" fill="none" stroke="currentColor" stroke-width="0.7"/>
  <line x1="73" y1="104" x2="100" y2="47" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2,1.5"/>
  <line x1="127" y1="104" x2="100" y2="47" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2,1.5"/>
  <line x1="66" y1="101" x2="80" y2="107" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="120" y1="107" x2="134" y2="101" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="73" y1="104" x2="56" y2="140" stroke="currentColor" stroke-width="0.7" marker-end="url(#vmo-beam)"/>
  <line x1="127" y1="104" x2="144" y2="140" stroke="currentColor" stroke-width="0.7" marker-end="url(#vmo-beam)"/>
  <circle cx="100" cy="47" r="2"/>
  <line x1="103" y1="47" x2="154" y2="47" stroke="currentColor" stroke-width="0.3"/>
  <line x1="142" y1="82" x2="154" y2="82" stroke="currentColor" stroke-width="0.3"/>
  <line x1="152" y1="47" x2="152" y2="82" stroke="currentColor" stroke-width="0.5" marker-start="url(#vmo-dim)" marker-end="url(#vmo-dim)"/>
  <text x="100" y="42">Origin</text>
  <text x="52" y="84" text-anchor="end">Back plate</text>
  <line x1="54" y1="83.3" x2="58" y2="83.3" stroke="currentColor" stroke-width="0.3"/>
  <text x="34" y="121" text-anchor="end">Transducers</text>
  <line x1="36" y1="119.5" x2="68" y2="105" stroke="currentColor" stroke-width="0.3"/>
  <text x="100" y="150">Beams (to seabed)</text>
  <text x="157" y="62" text-anchor="start">d</text>
</svg>

The distance from the top of the back plate to the origin (shown as **d** above) depends on the model:

| Model | Distance from back plate to origin |
| :--- | :--- |
| DVL A50 | 28 mm |
| DVL A100 | 38 mm |
| DVL A125 | 70 mm |
| DVL A250 | 84 mm |

By default, the body frame and vehicle frame are the same and align with the frame used for dead reckoning.

## Transducer numbering and protocol IDs

Mechanical/transducer diagrams number the transducers from 1 to 4. In protocol messages and diagnostic logs, the transducer `id` uses zero-based numbering from 0 to 3. The `id` is therefore the transducer number minus 1.

## Vehicle frame

The DVL can be mounted at an angle to the forward direction of the vehicle (yaw).

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 89" fill="currentColor">
  <defs>
    <marker id="leftarrowhead" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <polygon points="6 0, 0 3, 6 6 " />
    </marker>
    <marker id="rightarrowhead" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6 " />
    </marker>
  </defs>
  <text text-anchor="middle" x="30" y="5" font-size="0.3em">Body frame</text>
  <text text-anchor="middle" x="30" y="25" font-size="0.275em">x (Forward)</text>
  <text text-anchor="start" x="60" y="55" font-size="0.275em" alignment-baseline="middle">y (Right)</text>
  <line stroke="currentColor" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="30" y1="30" x2="30" y2="80"/>
  <line stroke="currentColor" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="5" y1="55" x2="55" y2="55"/>
  <text text-anchor="start" x="32" y="50" font-size="0.275em" alignment-baseline="middle">z (Down)</text>
  <text text-anchor="middle" x="140" y="5" font-size="0.3em">Vehicle frame</text>
  <text text-anchor="middle" x="140" y="25" font-size="0.275em">x (Vehicle)</text>
  <text text-anchor="start" x="170" y="55" font-size="0.275em" alignment-baseline="middle">y (Vehicle)</text>
  <line stroke="currentColor" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="140" y1="30" x2="140" y2="80"/>
  <line stroke="currentColor" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="115" y1="55" x2="165" y2="55"/>
  <g transform="rotate(30, 140, 55)">
  <line stroke="currentColor" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="140" y1="30" x2="140" y2="80"/>
  <line stroke="currentColor" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="115" y1="55" x2="165" y2="55"/>
  <text text-anchor="middle" x="150" y="27.5" font-size="0.275em">x (Body)</text>
  <text text-anchor="start" x="160" y="50" font-size="0.275em" alignment-baseline="middle">y (Body)</text>
  </g>
  <text text-anchor="start" x="142" y="42.5" font-size="0.275em" alignment-baseline="middle">θ</text>
  <path d="M 140 45 a 4 4 0 0 1 4.5 2" fill="none" stroke="currentColor" stroke-width="0.5"/></svg>

The clockwise angle θ in degrees around the Z axis, in the X-Y plane, from the forward axis of the vehicle to the forward axis of the DVL can be entered as a mounting rotation offset in the [web GUI](configuration.md), or through the configuration method over the TCP JSON API or serial protocol.

The DVL will then output data in the vehicle frame obtained by rotating the [DVL body frame](#body-frame) anti-clockwise around the Z axis by θ degrees. The X axis of the velocity output will be aligned with the forward axis of the vehicle. At time zero, the X axis of the DVL's dead-reckoning frame will be aligned with the forward axis of the vehicle.

For example:

* If the DVL is mounted back-to-front (cable aligned with the forward axis of the vehicle), the mounting rotation offset should be set to 180 degrees.
* If the A50/A125 is mounted with the LED at 90 degrees clockwise from the forward axis of the vehicle, the mounting rotation offset should be set to 90 degrees.

## Mounting offset in pitch and roll

This is possible, but the translation will have to be done by the user as there are no internal functions to compensate for this.

The DVL will always assume it is facing perpendicular to the surface.
