---
layout: page
title: Research
permalink: /research/
---

The group's work follows the four lines that give the laboratory its name.

<style>
/* Riquadri e colori arrivano da /assets/css/stratus.css */
.research-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2em;
  margin: 2em 0;
}

.research-header {
  display: flex;
  align-items: center;
  gap: 0.8em;
  margin-bottom: 1em;
}

.research-header i {
  font-size: 2.2em;
  width: 44px;
  text-align: center;
}

.research-header h3 {
  margin: 0;
  font-size: 1.1em;
  line-height: 1.2;
}

.research-item p {
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0;
}

@media (max-width: 600px) {
  .research-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="research-grid">

  <div class="research-item">
    <div class="research-header">
      {% include icon.html name="shield-alt" %}
      <h3>Secure</h3>
    </div>
    <p>Industrial and automotive systems were built before the threats they now face. We work on post-quantum cryptography for legacy protocols such as Modbus, anomaly detection on automotive CAN buses, and formal verification of security properties in containerized IoT deployments.</p>
  </div>

  <div class="research-item">
    <div class="research-header">
      {% include icon.html name="key" %}
      <h3>TRustless</h3>
    </div>
    <p>Rather than hardening the central authority, we remove it: self-sovereign identity in place of central credential issuers, zero-trust architectures for software-defined vehicles, and federated learning that keeps data where it is produced — together with the attacks that federation does not, by itself, prevent.</p>
  </div>

  <div class="research-item">
    <div class="research-header">
      {% include icon.html name="cogs" %}
      <h3>Autonomous</h3>
    </div>
    <p>Machines that decide for themselves, within the limits of the hardware they run on: decentralized control migration for long-endurance robot swarms, reinforcement learning inside the memory budget of an edge device, and neuro-symbolic models that pair learning with domain knowledge.</p>
  </div>

  <div class="research-item">
    <div class="research-header">
      {% include icon.html name="cloud" %}
      <h3>Ubiquitous Systems</h3>
    </div>
    <p>The substrate everything else depends on, from the embedded device to the data center: virtualization of embedded FPGAs, distributed hypervisors, serverless orchestration across the cloud-to-things continuum, and the IoT infrastructure that ties them together.</p>
  </div>

</div>
