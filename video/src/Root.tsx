import React from "react";
import { Composition } from "remotion";
import { OPENING_FRAMES, Opening } from "./Opening";
import { FPS } from "./theme";

export const Root: React.FC = () => (
  <Composition id="Opening" component={Opening} durationInFrames={OPENING_FRAMES} fps={FPS} width={1920} height={1080} />
);
