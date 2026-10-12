# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_01:36:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 01:36:06 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:18:47 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-13 01:18:24 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:17:44 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-13 01:12:44 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:07:32 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.033 |  |
| 2026-10-13 01:07:00 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:06:50 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-10-13 01:06:28 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.058 |  |
| 2026-10-13 01:06:12 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:05:27 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:04:48 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-10-13 01:04:35 | Urawa (Nilwala Ganga) | 2.96 | 🟡 Alert | -0.051 |  |
| 2026-10-13 01:04:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-13 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:37 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-13 01:03:22 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:22 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-10-13 01:03:21 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-13 01:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-13 01:03:04 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-13 01:02:42 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-10-13 01:02:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:01:39 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-13 01:01:35 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.059 |  |
| 2026-10-13 01:01:24 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.052 |  |
| 2026-10-13 01:00:24 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2026-10-13 01:00:10 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 00:09:32 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-10-13 01:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-13 01:04:35 | Urawa (Nilwala Ganga) | 2.96 | 🟡 Alert | -0.051 |  |
| 2026-10-13 00:17:28 | Pitabeddara (Nilwala Ganga) | 3.01 | 🟢 Normal | 23.220 | 🔺 Rising |
| 2026-10-13 00:07:01 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-10-13 01:04:48 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-10-13 01:03:04 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-13 01:18:47 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-13 01:03:21 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-13 01:01:39 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-13 01:17:44 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-13 00:00:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:36:06 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:04:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:22 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:07:00 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:02:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:18:24 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:06:12 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:12:44 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:00:10 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:05:27 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:03:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-13 01:00:24 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2026-10-13 00:02:50 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-13 01:02:42 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-10-13 01:03:37 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-13 01:07:32 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.033 |  |
| 2026-10-13 01:06:50 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-10-13 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.052 |  |
| 2026-10-13 01:06:28 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.058 |  |
| 2026-10-13 01:01:35 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.059 |  |
| 2026-10-13 01:03:22 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.070 |  |

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)