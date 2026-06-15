% Model         :   electromagic
% Description   :   A program to simulate a pulsating waveform
%                   Press Ctrl+C to stop simulation!
% File name     :   sync_one.m
% contact       :   support@syncmotor.com

% Copyright 2025-26 Synchronous Drives & Inverters Private Limited

clear all;
d = [0:1:360];          %space angle in degrees, just for x-axis of the plot.
x = [0:2*pi/360:2*pi];  %sine angle in radians, for calculation of amplitude.
f = 0.1;                %frequency of harmonic wave.
Ts = 100e-3;            %sec // sample time for simulation
T_simulation = 25;      %sec // total simulation time
display('Press Ctrl+C to stop simulation!')

for t = 0:Ts:T_simulation;
    y = 2*pi*f*t;
    z = sin(x)*sin(y);
    axis([0 360 -2 2]);
    drawnow
    plot(d,z)
    title('A pulsating Waveform')
    xlabel('space in degrees or meters')
    ylabel('amplitude')
end