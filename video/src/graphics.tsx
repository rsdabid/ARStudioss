import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "./theme";

const pop = (frame: number, fps: number, at: number, damping = 12) =>
  spring({ frame: frame - at, fps, config: { damping, stiffness: 180 } });

export const Background: React.FC = () => {
  const frame = useCurrentFrame();
  const drift = (frame * 0.4) % 60;
  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse at 70% 30%, ${theme.bg2}, ${theme.bg} 70%)` }}>
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(${theme.panel}55 1px, transparent 1px), linear-gradient(90deg, ${theme.panel}55 1px, transparent 1px)`,
          backgroundSize: "60px 60px",
          backgroundPosition: `${drift}px ${drift}px`,
          opacity: 0.5,
        }}
      />
    </AbsoluteFill>
  );
};

// Words spring in one after another; CAPS words get the accent colour.
export const Kinetic: React.FC<{
  text: string;
  at: number;
  x: number;
  y: number;
  size?: number;
  color?: string;
  stagger?: number;
  align?: "left" | "center";
  out?: number;
}> = ({ text, at, x, y, size = 90, color = theme.ink, stagger = 4, align = "left", out }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const fade = out === undefined ? 1 : interpolate(frame, [out, out + 8], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  if (frame < at || fade === 0) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        transform: align === "center" ? "translateX(-50%)" : undefined,
        display: "flex",
        gap: size * 0.28,
        fontFamily: theme.font,
        fontWeight: 900,
        fontSize: size,
        letterSpacing: -1,
        lineHeight: 1,
        opacity: fade,
        whiteSpace: "nowrap",
      }}
    >
      {text.split(" ").map((w, i) => {
        const p = pop(frame, fps, at + i * stagger);
        const caps = w === w.toUpperCase() && /[A-Z]/.test(w);
        return (
          <span
            key={i}
            style={{
              display: "inline-block",
              color: caps && color === theme.ink ? theme.accent : color,
              transform: `translateY(${(1 - p) * 40}px) scale(${0.6 + 0.4 * p})`,
              opacity: Math.min(1, p * 1.5),
            }}
          >
            {w}
          </span>
        );
      })}
    </div>
  );
};

export const Building: React.FC<{
  x: number;
  y: number;
  scale?: number;
  at: number;
  windows: { label: string; offAt?: number; danger?: boolean }[];
  chipAt?: number;
  onAt?: number;
}> = ({ x, y, scale = 1, at, windows, chipAt, onAt }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = pop(frame, fps, at, 16);
  if (frame < at) return null;
  const chip = chipAt === undefined ? 0 : pop(frame, fps, chipAt, 9);
  const on = onAt !== undefined && frame >= onAt;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        transform: `translateY(${(1 - enter) * 300}px) scale(${scale})`,
        transformOrigin: "50% 100%",
        opacity: enter,
        fontFamily: theme.font,
      }}
    >
      <svg width={560} height={620} viewBox="0 0 560 620" style={{ overflow: "visible" }}>
        <rect x={40} y={80} width={480} height={540} rx={18} fill={theme.panel} stroke={theme.accent} strokeWidth={4} />
        <rect x={180} y={30} width={200} height={60} rx={10} fill={theme.panel} stroke={theme.accent} strokeWidth={4} />
        {windows.map((w, i) => {
          const col = i % 2;
          const row = Math.floor(i / 2);
          const off = w.offAt !== undefined && frame >= w.offAt;
          const flash = w.offAt === undefined ? 0 : interpolate(frame - w.offAt, [0, 3, 10], [0, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          const lit = off ? "#0D1838" : theme.warn;
          return (
            <g key={w.label}>
              <rect
                x={80 + col * 220}
                y={130 + row * 200}
                width={180}
                height={140}
                rx={10}
                fill={flash > 0 && w.danger ? theme.danger : lit}
                opacity={off ? 0.9 : 0.95}
              />
              <text
                x={170 + col * 220}
                y={210 + row * 200}
                textAnchor="middle"
                fontWeight={900}
                fontSize={34}
                fill={off ? theme.dim : theme.bg}
              >
                {w.label}
              </text>
            </g>
          );
        })}
        {chipAt !== undefined && frame >= chipAt && (
          <g transform={`translate(280 ${interpolate(chip, [0, 1], [-400, 560])})`}>
            <rect x={-70} y={-55} width={140} height={110} rx={18} fill={on ? theme.accent : theme.dim} />
            {[-40, 0, 40].map((d) => (
              <g key={d}>
                <rect x={d - 6} y={-75} width={12} height={20} fill={on ? theme.accent : theme.dim} />
                <rect x={d - 6} y={55} width={12} height={20} fill={on ? theme.accent : theme.dim} />
              </g>
            ))}
            <text y={14} textAnchor="middle" fontWeight={900} fontSize={44} fill={theme.bg}>
              AI
            </text>
          </g>
        )}
      </svg>
      {onAt !== undefined && frame >= onAt - 10 && <Toggle on={on} at={onAt - 10} />}
    </div>
  );
};

const Toggle: React.FC<{ on: boolean; at: number }> = ({ on, at }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = pop(frame, fps, at);
  const knob = spring({ frame: frame - at - 10, fps, config: { damping: 14 } });
  return (
    <div style={{ position: "absolute", left: 560, top: 470, transform: `scale(${p})`, display: "flex", alignItems: "center", gap: 18 }}>
      <div style={{ width: 130, height: 66, borderRadius: 40, background: on ? theme.accent : theme.dim, position: "relative" }}>
        <div style={{ position: "absolute", top: 7, left: 7 + knob * 64, width: 52, height: 52, borderRadius: 30, background: theme.ink }} />
      </div>
      <span style={{ fontWeight: 900, fontSize: 52, color: on ? theme.accent : theme.dim }}>{on ? "ON" : "OFF"}</span>
    </div>
  );
};

export const CandidateCard: React.FC<{ x: number; y: number; at: number }> = ({ x, y, at }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = pop(frame, fps, at);
  const bubble = pop(frame, fps, at + 10);
  if (frame < at) return null;
  return (
    <div style={{ position: "absolute", left: x, top: y, fontFamily: theme.font, transform: `scale(${p})`, transformOrigin: "50% 100%" }}>
      <div
        style={{
          background: theme.ink,
          color: theme.bg,
          fontWeight: 800,
          fontSize: 46,
          padding: "26px 36px",
          borderRadius: 28,
          transform: `scale(${bubble})`,
          transformOrigin: "20% 100%",
          marginBottom: 30,
          whiteSpace: "nowrap",
        }}
      >
        Why was I rejected?
      </div>
      <svg width={220} height={240} viewBox="0 0 220 240">
        <circle cx={110} cy={70} r={60} fill="#C9A27E" />
        <path d="M20,240 C20,150 200,150 200,240 Z" fill={theme.dim} />
      </svg>
      <div style={{ color: theme.dim, fontWeight: 700, fontSize: 28, marginTop: 8 }}>REJECTED CANDIDATE</div>
    </div>
  );
};

export const CalendarFlip: React.FC<{ x: number; y: number; at: number; out?: number }> = ({ x, y, at, out }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = pop(frame, fps, at);
  if (frame < at || (out !== undefined && frame > out)) return null;
  const n = Math.min(6, Math.max(0, Math.floor((frame - at) / 3)));
  return (
    <div style={{ position: "absolute", left: x, top: y, transform: `scale(${p})`, fontFamily: theme.font, textAlign: "center" }}>
      <div style={{ width: 230, background: theme.ink, borderRadius: 22, overflow: "hidden" }}>
        <div style={{ background: theme.danger, height: 56 }} />
        <div style={{ fontSize: 120, fontWeight: 900, color: theme.bg, padding: "6px 0 14px" }}>+{n}</div>
      </div>
      <div style={{ color: theme.ink, fontWeight: 900, fontSize: 44, marginTop: 16 }}>MONTHS</div>
    </div>
  );
};

// Empty slot for editor-supplied b-roll.
export const BrollSlot: React.FC<{ id: string; note: string }> = ({ id, note }) => (
  <AbsoluteFill
    style={{
      background: `repeating-linear-gradient(45deg, #1a1a1a, #1a1a1a 30px, #222 30px, #222 60px)`,
      alignItems: "center",
      justifyContent: "center",
      fontFamily: theme.font,
      color: theme.ink,
      textAlign: "center",
    }}
  >
    <div style={{ fontSize: 40, fontWeight: 900, color: theme.warn, letterSpacing: 4 }}>B-ROLL {id}</div>
    <div style={{ fontSize: 34, fontWeight: 600, maxWidth: 1300, marginTop: 20, lineHeight: 1.35 }}>{note}</div>
  </AbsoluteFill>
);

export const Flash: React.FC<{ at: number; color?: string }> = ({ at, color = theme.danger }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame - at, [0, 2, 10], [0, 0.5, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return <AbsoluteFill style={{ background: color, opacity: o, pointerEvents: "none" }} />;
};
