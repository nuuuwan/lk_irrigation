# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_00:20:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 00:20:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:17:28 | Pitabeddara (Nilwala Ganga) | 3.01 | 🟢 Normal | 23.220 | 🔺 Rising |
| 2026-10-13 00:12:13 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:12:10 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 00:09:32 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-10-12 23:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-13 00:05:19 | Urawa (Nilwala Ganga) | 3.01 | 🟡 Alert | -0.058 |  |
| 2026-10-13 00:17:28 | Pitabeddara (Nilwala Ganga) | 3.01 | 🟢 Normal | 23.220 | 🔺 Rising |
| 2026-10-13 00:07:01 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-10-13 00:04:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-12 23:04:25 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-13 00:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-13 00:01:31 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-13 00:04:42 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-13 00:03:57 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 00:03:22 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 00:09:47 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-13 00:08:24 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 00:00:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 00:07:11 | Peradeniya (Mahaweli Ganga) | 3.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 00:04:13 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:03:16 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:05:19 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:02:50 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:20:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:00:54 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:05:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:12:13 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:01:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:07:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:07:43 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-13 00:04:24 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-13 00:03:05 | Ellagawa (Kalu Ganga) | 6.85 | 🟢 Normal | -0.010 |  |
| 2026-10-13 00:02:25 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-13 00:04:08 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-13 00:02:50 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-13 00:03:21 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.031 |  |
| 2026-10-13 00:03:59 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.052 |  |
| 2026-10-13 00:01:03 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)