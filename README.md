# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_10:03:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,503 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 10:03:33 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.063 |  |
| 2026-11-04 10:03:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 10:03:00 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.039 |  |
| 2026-11-04 10:02:37 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-11-04 10:02:28 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-04 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-04 10:02:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:02:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-04 10:02:02 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.033 |  |
| 2026-11-04 10:01:43 | Moragaswewa (Deduru Oya) | 4.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 10:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:30 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:21 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-11-04 10:01:17 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:15 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:10 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-11-04 10:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-04 10:00:57 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:00:30 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-11-04 10:00:21 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-04 09:00:39 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-04 09:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-04 09:06:38 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-04 09:10:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-04 10:01:43 | Moragaswewa (Deduru Oya) | 4.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 09:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 10:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:00:57 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:02:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:09 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:30 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:15 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:03:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:05:08 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-04 10:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 10:00:30 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-11-04 10:00:21 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:47 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-11-04 10:02:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-04 10:02:37 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-11-04 09:00:33 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 10:02:28 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-04 10:01:21 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-11-04 10:02:02 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.033 |  |
| 2026-11-04 10:03:00 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.039 |  |
| 2026-11-04 10:01:10 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-11-04 09:05:15 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-04 09:05:24 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:06:03 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:04:01 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.059 |  |
| 2026-11-04 10:03:33 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.063 |  |
| 2026-11-04 09:04:40 | Moraketiya (Walawe Ganga) | 1.67 | 🟢 Normal | -0.084 |  |
| 2026-11-04 09:09:43 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.097 |  |
| 2026-11-04 09:04:11 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.118 |  |
| 2026-11-04 09:02:40 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.124 |  |
| 2026-11-04 09:03:18 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.125 |  |
| 2026-11-04 09:06:13 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)