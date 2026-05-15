# Axes

The axis convention is the same for all DVL models. Velocities and dead reckoning output use the vehicle frame. By default, the vehicle frame is the same as the body frame, but it can be adjusted to allow flexible mounting on the vehicle.


<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 89">
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
  <text text-anchor="left" x="60" y="55" font-size="0.275em" alignment-baseline="middle">y (Right)</text>
  <line stroke="black" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="30" y1="30" x2="30" y2="80"/>
  <line stroke="black" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="5" y1="55" x2="55" y2="55"/>
  <text text-anchor="left" x="32" y="50" font-size="0.275em" alignment-baseline="middle">z (Down)</text>
  <text text-anchor="middle" x="140" y="5" font-size="0.3em">Vehicle frame</text>
  <text text-anchor="middle" x="140" y="25" font-size="0.275em">x (Vehicle)</text>
  <text text-anchor="left" x="170" y="55" font-size="0.275em" alignment-baseline="middle">y (Vehicle)</text>
  <line stroke="black" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="140" y1="30" x2="140" y2="80"/>
  <line stroke="black" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="115" y1="55" x2="165" y2="55"/>
  <g transform="rotate(30, 140, 55)">
  <line stroke="black" stroke-width="0.5" marker-start="url(#leftarrowhead)" x1="140" y1="30" x2="140" y2="80"/>
  <line stroke="black" stroke-width="0.5" marker-end="url(#rightarrowhead)" x1="115" y1="55" x2="165" y2="55"/>
  <text text-anchor="middle" x="150" y="27.5" font-size="0.275em">x (Body)</text>
  <text text-anchor="left" x="160" y="50" font-size="0.275em" alignment-baseline="middle">y (Body)</text>
  </g>
  <text text-anchor="left" x="142" y="42.5" font-size="0.275em" alignment-baseline="middle">θ</text>
  <path d="M 140 45 a 4 4 0 0 1 4.5 2" fill="none" stroke="black" stroke-width="0.5"/>
  <!--- the path above gives an arc-ish figure but i have no idea how to do this properly -->
</svg>


## Body frame

The body frame axes of the DVL are as follows:

* X axis is pointing forward (LED is forward (only for A50/A125), cable backward)
* Y axis is pointing right
* Z axis is pointing down (metal back plate is up, transducers are down, LED is pointing down only for A100/A250)
* Origin is the center of the DVL on the transducer side.

<!-- TODO: Confirm whether a backplate distance should be documented separately for DVL A100 and DVL A250. -->

By default, the body frame and vehicle frame are the same and align with the frame used for dead reckoning.

## Transducer numbering and protocol IDs

Mechanical/transducer diagrams number the transducers from 1 to 4. In protocol messages and diagnostic logs, the transducer `id` uses zero-based numbering from 0 to 3. The `id` is therefore the transducer number minus 1.

## Vehicle frame

The DVL can be mounted at an angle to the forward direction of the vehicle (yaw).

The clockwise angle θ in degrees around the Z axis, in the X-Y plane, from the forward axis of the vehicle to the forward axis of the DVL can be entered as a mounting rotation offset in the [web GUI](configuration.md), or through the configuration method over the TCP JSON API or serial protocol.

The DVL will then output data in the vehicle frame obtained by rotating the [DVL body frame](#body-frame) anti-clockwise around the Z axis by θ degrees. The X axis of the velocity output will be aligned with the forward axis of the vehicle. At time zero, the X axis of the DVL's dead-reckoning frame will be aligned with the forward axis of the vehicle.

For example:

* If the DVL is mounted back-to-front (cable aligned with the forward axis of the vehicle), the mounting rotation offset should be set to 180 degrees.
* If the A50/A125 is mounted with the LED at 90 degrees clockwise from the forward axis of the vehicle, the mounting rotation offset should be set to 90 degrees.

## Mounting offset in pitch and roll

This is possible, but the translation will have to be done by the user as there are no internal functions to compensate for this.

The DVL will always assume it is facing perpendicular to the surface.
