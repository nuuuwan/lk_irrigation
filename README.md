# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_17:05:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,841 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 17:05:40 | Peradeniya (Mahaweli Ganga) | 4.31 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-24 17:05:24 | Urawa (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.168 |  |
| 2026-09-24 17:05:15 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 17:05:09 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-24 17:04:38 | Baddegama (Gin Ganga) | 4.44 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 17:04:10 | Nawalapitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 17:03:56 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:03:51 | Deraniyagala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:03:48 | Hanwella (Kelani Ganga) | 5.34 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-24 17:03:37 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 17:03:25 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 17:03:19 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-24 17:03:11 | Glencourse (Kelani Ganga) | 13.88 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-24 17:03:07 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:51 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:22 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 17:02:19 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:17 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 17:02:12 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 17:02:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 17:01:48 | Pitabeddara (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.311 |  |
| 2026-09-24 17:01:48 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.021 |  |
| 2026-09-24 17:01:41 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:01:21 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:01:08 | Moraketiya (Walawe Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 17:01:05 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 16:03:03 | Panadugama (Nilwala Ganga) | 6.75 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-09-24 17:04:38 | Baddegama (Gin Ganga) | 4.44 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 17:02:17 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 17:02:12 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 17:01:48 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.021 |  |
| 2026-09-24 16:04:16 | Thawalama (Gin Ganga) | 5.29 | 🟡 Alert | -0.032 |  |
| 2026-09-24 16:03:09 | Kithulgala (Kelani Ganga) | 2.70 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-09-24 17:03:48 | Hanwella (Kelani Ganga) | 5.34 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-24 17:03:11 | Glencourse (Kelani Ganga) | 13.88 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-24 17:05:40 | Peradeniya (Mahaweli Ganga) | 4.31 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-24 17:03:37 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 17:05:15 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 17:05:09 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-24 17:01:41 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 16:15:07 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-24 17:04:10 | Nawalapitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 17:02:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 17:03:25 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 17:03:19 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-24 17:01:08 | Moraketiya (Walawe Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 16:06:07 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 17:01:21 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:01:05 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 16:03:41 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:03:51 | Deraniyagala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:03:07 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:03:56 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:19 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:51 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 16:02:59 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 16:04:19 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 17:02:22 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 16:05:03 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.063 |  |
| 2026-09-24 17:05:24 | Urawa (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.168 |  |
| 2026-09-24 17:01:48 | Pitabeddara (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.311 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)