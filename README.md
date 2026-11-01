<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="Aryan Teng, full-stack product engineer. I build AI products end to end, from the UX to the on-prem deploy: the UVIP rebuild with 300+ typed APIs, 90% faster deploys for 50 computer-vision apps, Seek search at 33 Indian airports and a ClickHouse pipeline at 20M+ events a day.">
</picture>

Full-stack product engineer at [Awiros](https://www.awiros.com), which runs video AI for airports and smart cities. I take products from the first prototype to the on-prem install: the UX, the React and React Native apps, the Node.js and Go services and data pipelines behind them, and the platform that ships them to customer sites. Promoted to SDE II in June 2026; company-wide Best Performer two cycles running.

### What I've built at Awiros

**Product and interfaces**

- Led the ground-up rebuild of **UVIP**, Awiros's video-intelligence platform, in React 19 and TypeScript, owning its product and UX: 31 modules and 300+ typed APIs on one live client cache. I also wrote most of its test suite (318 of 372 files).
- Shipped **video summarisation and crowd estimation** for Delhi Safe City, with crowd analytics built for 2,500-camera sites on pre-aggregated ClickHouse tables.
- Built two **React Native (Expo) apps** on my own: GMR's airport operations app and Aura Companion.
- Built both ends of a **vision-model playground** (NestJS API, React UI) where users browse and compare computer-vision models.

**Platform and delivery**

- Re-architected **computer-vision app delivery**. A 3-hour monolithic Jenkins build of 50 apps became versioned per-app Docker images that Kubernetes Jobs pull and install on site, and deployment time fell by 90%+.
- Shipped **enterprise SSO** to customers: LDAP/Active Directory and OIDC presets for Keycloak, Entra ID, Okta and Google Workspace, with just-in-time provisioning and group-to-role mapping.
- Split the **Node.js monolith** into independently scaling API and Kafka-consumer services, and replaced hand-edited per-site config files with live settings managed from the UI.

**Data, search and AI**

- **Seek**, natural-language search across video alerts, used at 33 Indian airports. I designed and built it in Go on Milvus, gRPC and Kafka; median search went from 51 s to 4.7 s at 650K alerts a day.
- A **ClickHouse event pipeline** at 20M+ events a day. At Bangalore Safe City (3,500+ cameras) it cut downtime 99% and storage from 5 TB to 450 GB.
- The **Delhi IGI Airport** operations backend: e-challan filing with Delhi Traffic Police (9,189 challans), per-belt trolley planning from live AODB arrivals, and a FastAPI and LightGBM forecasting service in the airport's traffic heatmap.

<sub>This work lives in private company repositories. More detail on <a href="https://linkedin.com/in/aryanteng">LinkedIn</a>.</sub>

### Before Awiros

- **Enveave**, a climate-tech startup, where I was the founding engineer (2022–24). I co-led the 0-to-1 MVP with the founders, architecting 6 core features and designing 15 Figma prototypes, and cut AWS costs 33%.
- **Tortoise**, an electronics rental platform (intern, 2024): lessor and seller dashboards for 10,000+ customers, where RTK Query caching cut admin load time 40%.
- [**cse.iiitd.ac.in**](https://cse.iiitd.ac.in), the official IIIT-Delhi CSE department website, built in Next.js with five other students. Content lives in Google Sheets, so department staff update the site without touching code.
- [**Sahaayak**](https://github.com/aryanteng/Sahaayak): sequence-alignment and ORF tools for biology students, from my Computer Science and Biosciences degree.

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
