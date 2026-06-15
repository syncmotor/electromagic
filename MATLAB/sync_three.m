 % Model         :   electromagic
% Description   :   A program to simulate rotating magnetic fields 
%                   OR travelling magnetic fields produced from 
%                   addition of three pulsating waveforms
%                   Press Ctrl+C to stop simulation!
% File name     :   sync_three.m
% contact       :   support@syncmotor.com

% Copyright 2025-26 Synchronous Drives & Inverters Private Limited

clear all;
d = [0:1:720];          %space in degrees or meters, x-axis of the plot.
x = [0:2*pi/360:4*pi];  %sine angle in radians, for calculation of amplitude.
f = 0.1;                %frequency of harmonic wave.
Ts = 100e-3;            %sec // sample time for simulation
T_simulation = 25;      %sec // total simulation time
display('Press Ctrl+C to stop simulation!')

for t = 0:Ts:T_simulation;
    y = 2*pi*f*t;
    z1 = sin(x)*sin(y);
    z2 = sin(x-(2*pi/3))*sin(y-(2*pi/3)); 
    z3 = sin(x-(-2*pi/3))*sin(y-(-2*pi/3)); 
    a = z1+z2+z3;
    axis([0 720 -2 2]);
    drawnow
    plot(d,z1,'r-',d,z2,'y-',d,z3,'b-',d,a,'c-')
    title('Rotating OR Travelling wave produced by three pulsating Waves !')
    xlabel('space in degrees or meters')
    ylabel('amplitude')
    text(480,-1.6,'concept: prof. krishan lal arora, SVNIT')
    text(480,-1.7,'re-created by: support@syncmotor.com')
end