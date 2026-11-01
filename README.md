<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="Aryan Teng, full-stack product engineer and ex-founding engineer. I build products from zero to production. Built and shipped at Awiros: the UVIP platform rebuild, CV app delivery, Developer Mode, Seek vector search, enterprise SSO, the Delhi IGI airport operations suite, two mobile apps and a ClickHouse event pipeline.">
</picture>

I build products from zero to production. I was the founding engineer at a climate-tech startup, and at [Awiros](https://www.awiros.com), which runs video AI for airports and smart cities, I design, build and ship products across the whole stack: the UX, web and mobile apps, services, data pipelines and the platform that installs them on customer sites. I like owning the whole loop, from the first Figma frame to fixing things on site. SDE II since June 2026; company-wide Best Performer two cycles running.

### What I've built at Awiros

<table>
<tr>
<td width="50%" valign="top">
<b>UVIP</b>&nbsp;&nbsp;<code>product · UX</code><br>
Awiros's video-intelligence platform. I led its ground-up rebuild in React 19 and TypeScript and owned the product and UX.<br>
<sub>31 modules · 300+ typed APIs on one live cache · I wrote 318 of its 372 test files</sub>
</td>
<td width="50%" valign="top">
<b>CV app delivery</b>&nbsp;&nbsp;<code>platform</code><br>
How 50 computer-vision apps reach customer sites. I re-architected it as versioned per-app Docker images that Kubernetes Jobs pull and install on site.<br>
<sub>Replaced a 3-hour monolithic Jenkins build · deploys 90%+ faster</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b>Developer Mode</b>&nbsp;&nbsp;<code>developer experience</code><br>
For computer-vision developers: mount an app's source onto a live pipeline and watch its alerts in real time.<br>
<sub>No release cycle between a code change and a real result</sub>
</td>
<td width="50%" valign="top">
<b>Seek</b>&nbsp;&nbsp;<code>search</code><br>
Natural-language person search across video alerts. I designed and built it in Go on Milvus, gRPC and Kafka.<br>
<sub>Used at 33 Indian airports · 650K alerts a day · median search 51 s → 4.7 s</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b>Enterprise SSO</b>&nbsp;&nbsp;<code>security</code><br>
LDAP/Active Directory and OIDC presets for Keycloak, Entra ID, Okta and Google Workspace, with just-in-time provisioning and group-to-role mapping.<br>
<sub>Shipped to customers</sub>
</td>
<td width="50%" valign="top">
<b>Delhi IGI Airport operations</b>&nbsp;&nbsp;<code>end to end</code><br>
The backend behind the airport's operations dashboards, which I built and ran in production on site.<br>
<sub>9,189 e-challans filed with Delhi Traffic Police · trolley planning per baggage belt from live AODB arrivals · a LightGBM forecasting service</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b>Two mobile apps</b>&nbsp;&nbsp;<code>React Native</code><br>
Built solo in Expo: GMR's airport operations app, and Aura Companion with alerts, live activity and an AI chat.<br>
<sub>Expo, RTK Query and EAS builds, from the first screen to release</sub>
</td>
<td width="50%" valign="top">
<b>Video summarisation and crowd estimation</b>&nbsp;&nbsp;<code>product</code><br>
Shipped for Delhi Safe City.<br>
<sub>Crowd analytics built for 2,500-camera sites on pre-aggregated ClickHouse tables</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b>Event pipeline</b>&nbsp;&nbsp;<code>data</code><br>
A ClickHouse pipeline I architected, handling 20M+ events a day.<br>
<sub>Bangalore Safe City (3,500+ cameras): downtime −99%, storage 5 TB → 450 GB</sub>
</td>
<td width="50%" valign="top">
<b>Vision-model playground</b>&nbsp;&nbsp;<code>product</code><br>
Both ends, NestJS API and React UI, of a catalog where users browse and compare computer-vision models.<br>
<sub>Built end to end</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b>Background-job engine</b>&nbsp;&nbsp;<code>reliability</code><br>
Bulk imports rebuilt as resumable background jobs with crash recovery, auto-retry and 60 s stall detection, plus report-kit, a shared PDF engine.<br>
<sub>Removed the record cap on reports</sub>
</td>
<td width="50%" valign="top">
<b>Live configuration and service split</b>&nbsp;&nbsp;<code>platform</code><br>
Per-site JSON config (hand-edited, restart to apply) became live settings managed from the UI, and the Node.js monolith became independently scaling API and Kafka-consumer services.<br>
<sub>Configuration changes without restarts</sub>
</td>
</tr>
</table>

<sub>This work lives in private company repositories. More detail on <a href="https://linkedin.com/in/aryanteng">LinkedIn</a>.</sub>

### Before Awiros

<table>
<tr>
<td width="50%" valign="top">
<b>Enveave</b>&nbsp;&nbsp;<code>founding engineer · 2022–24</code><br>
Co-led the climate-tech startup's 0-to-1 MVP with the founders: architected 6 core features and designed 15 Figma prototypes.<br>
<sub>AWS costs −33% · delivery time −50% with CI/CD</sub>
</td>
<td width="50%" valign="top">
<b>Tortoise</b>&nbsp;&nbsp;<code>2024</code><br>
Lessor and seller dashboards for an electronics rental platform with 10,000+ customers.<br>
<sub>Admin load time −40% with RTK Query caching</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<b><a href="https://cse.iiitd.ac.in">cse.iiitd.ac.in</a></b>&nbsp;&nbsp;<code>web</code><br>
The official IIIT-Delhi CSE department website, built in Next.js with five other students.<br>
<sub>Content lives in Google Sheets, so staff update it without code</sub>
</td>
<td width="50%" valign="top">
<b><a href="https://github.com/aryanteng/Sahaayak">Sahaayak</a></b>&nbsp;&nbsp;<code>bioinformatics</code><br>
Sequence-alignment and ORF tools for biology students, from my Computer Science and Biosciences degree.<br>
<sub>Next.js + Flask</sub>
</td>
</tr>
</table>

### What I build with

<table>
  <tr>
    <th align="left">Product and frontend</th>
    <th align="left">Backend and data</th>
    <th align="left">Infra and delivery</th>
  </tr>
  <tr valign="top">
    <td>
      <img alt="React" src="https://img.shields.io/badge/React-1E2220?style=flat-square&logo=react&logoColor=white">
      <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-1E2220?style=flat-square&logo=typescript&logoColor=white">
      <img alt="Next.js" src="https://img.shields.io/badge/Next.js-1E2220?style=flat-square&logo=nextdotjs&logoColor=white">
      <img alt="React Native · Expo" src="https://img.shields.io/badge/React_Native_·_Expo-1E2220?style=flat-square&logo=expo&logoColor=white">
      <img alt="RTK Query" src="https://img.shields.io/badge/RTK_Query-1E2220?style=flat-square&logo=redux&logoColor=white">
      <img alt="Angular" src="https://img.shields.io/badge/Angular-1E2220?style=flat-square&logo=angular&logoColor=white">
      <img alt="Tailwind" src="https://img.shields.io/badge/Tailwind-1E2220?style=flat-square&logo=tailwindcss&logoColor=white">
      <img alt="Figma" src="https://img.shields.io/badge/Figma-1E2220?style=flat-square&logo=figma&logoColor=white">
      <img alt="Socket.IO" src="https://img.shields.io/badge/Socket.IO-1E2220?style=flat-square&logo=socketdotio&logoColor=white">
    </td>
    <td>
      <img alt="Node.js" src="https://img.shields.io/badge/Node.js-1E2220?style=flat-square&logo=nodedotjs&logoColor=white">
      <img alt="NestJS" src="https://img.shields.io/badge/NestJS-1E2220?style=flat-square&logo=nestjs&logoColor=white">
      <img alt="Go" src="https://img.shields.io/badge/Go-1E2220?style=flat-square&logo=go&logoColor=white">
      <img alt="Python" src="https://img.shields.io/badge/Python-1E2220?style=flat-square&logo=python&logoColor=white">
      <img alt="Kafka" src="https://img.shields.io/badge/Kafka-1E2220?style=flat-square&logo=apachekafka&logoColor=white">
      <img alt="gRPC" src="https://img.shields.io/badge/gRPC-1E2220?style=flat-square">
      <img alt="ClickHouse" src="https://img.shields.io/badge/ClickHouse-1E2220?style=flat-square&logo=clickhouse&logoColor=white">
      <img alt="Milvus" src="https://img.shields.io/badge/Milvus-1E2220?style=flat-square&logo=milvus&logoColor=white">
      <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-1E2220?style=flat-square&logo=mongodb&logoColor=white">
      <img alt="Redis" src="https://img.shields.io/badge/Redis-1E2220?style=flat-square&logo=redis&logoColor=white">
    </td>
    <td>
      <img alt="Docker" src="https://img.shields.io/badge/Docker-1E2220?style=flat-square&logo=docker&logoColor=white">
      <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-1E2220?style=flat-square&logo=kubernetes&logoColor=white">
      <img alt="SSO · OIDC · LDAP" src="https://img.shields.io/badge/SSO_·_OIDC_·_LDAP-1E2220?style=flat-square&logo=openid&logoColor=white">
      <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-1E2220?style=flat-square&logo=githubactions&logoColor=white">
      <img alt="AWS" src="https://img.shields.io/badge/AWS-1E2220?style=flat-square">
    </td>
  </tr>
</table>

<sub>My work commits live in my employer's private repositories. A private repo here replays one timestamp per real commit, with no code or messages, so the graph matches my actual activity.</sub>
