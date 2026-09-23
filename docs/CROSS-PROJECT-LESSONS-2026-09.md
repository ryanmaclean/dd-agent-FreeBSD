# Cross-project lessons — 2026-09

This repo is prior art for **Datadog on FreeBSD** and should be consulted before adding telemetry machinery to smolFire/Moth.

## Boundary

The tiny guest should prefer:
- compact DogStatsD/UDP or equivalent event emission
- host-side Datadog Agent where possible
- no heavyweight observability daemon inside the microVM unless required

## Reuse/check

- FreeBSD build assumptions
- packaging/service quirks
- socket/network behavior
- native metrics/logging limitations

Moth already has an opt-in DogStatsD emitter; compare that against anything in this repo before building another telemetry client.

## Agent assignment

Copilot primary; `@codex` fallback.
