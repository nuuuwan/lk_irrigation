# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_01:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 01:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.013 |  |
| 2026-11-13 01:02:14 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-11-13 01:02:07 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.088 |  |
| 2026-11-13 01:02:06 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | -0.134 |  |
| 2026-11-13 01:02:05 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-13 01:01:35 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.110 |  |
| 2026-11-13 01:01:28 | Peradeniya (Mahaweli Ganga) | 4.35 | 🟢 Normal | -0.080 |  |
| 2026-11-13 01:01:20 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.000 |  |
| 2026-11-13 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-13 01:00:44 | Nakkala (Kumbukkan Oya) | 1.85 | 🟢 Normal | -0.169 |  |
| 2026-11-13 01:00:35 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 00:02:27 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 00:03:46 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 00:06:29 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 00:05:16 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.000 |  |
| 2026-11-13 01:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.013 |  |
| 2026-11-13 00:02:09 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.074 |  |
| 2026-11-13 00:14:38 | Magura (Kalu Ganga) | 4.52 | 🟡 Alert | -0.083 |  |
| 2026-11-13 00:11:38 | Norwood (Kelani Ganga) | 1.62 | 🟡 Alert | -0.084 |  |
| 2026-11-13 00:14:15 | Urawa (Nilwala Ganga) | 2.60 | 🟡 Alert | -0.222 |  |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-13 00:07:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-13 00:02:44 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 00:03:34 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 00:14:37 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-13 00:03:20 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 01:01:20 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-13 00:05:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-13 00:03:40 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-13 00:02:47 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-11-13 00:02:29 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-11-13 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-13 00:12:11 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-11-13 01:02:14 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-11-13 00:04:53 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-13 00:06:28 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.041 |  |
| 2026-11-13 01:02:05 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-13 00:05:00 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-11-13 00:07:49 | Wellawaya (Kirindi Oya) | 1.96 | 🟢 Normal | -0.053 |  |
| 2026-11-13 01:00:35 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.063 |  |
| 2026-11-13 00:06:47 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.074 |  |
| 2026-11-13 01:01:28 | Peradeniya (Mahaweli Ganga) | 4.35 | 🟢 Normal | -0.080 |  |
| 2026-11-13 01:02:07 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.088 |  |
| 2026-11-13 00:08:21 | Rathnapura (Kalu Ganga) | 4.63 | 🟢 Normal | -0.104 |  |
| 2026-11-13 01:01:35 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.110 |  |
| 2026-11-13 00:03:34 | Thaldena (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.119 |  |
| 2026-11-13 01:02:06 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | -0.134 |  |
| 2026-11-13 01:00:44 | Nakkala (Kumbukkan Oya) | 1.85 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)