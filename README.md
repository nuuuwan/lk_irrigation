# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_18:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 18:11:15 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.026 |  |
| 2026-09-27 18:08:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |
| 2026-09-27 18:07:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:05:57 | Baddegama (Gin Ganga) | 4.52 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-27 18:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | -0.133 |  |
| 2026-09-27 18:04:43 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.123 |  |
| 2026-09-27 18:04:40 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-09-27 18:04:24 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.069 |  |
| 2026-09-27 18:04:01 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.021 |  |
| 2026-09-27 18:03:49 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-27 18:03:49 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:03:46 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-09-27 18:03:31 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:03:25 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.060 |  |
| 2026-09-27 18:03:12 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:03:03 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -0.072 |  |
| 2026-09-27 18:03:01 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.089 |  |
| 2026-09-27 18:02:55 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:52 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:43 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:39 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-27 18:02:31 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.095 |  |
| 2026-09-27 18:02:14 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:12 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:09 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:56 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.040 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |
| 2026-09-27 18:01:48 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -36.000 |  |
| 2026-09-27 18:01:44 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:00:50 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:00:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:00:20 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-27 18:00:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:00:14 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-09-27 18:00:07 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 18:03:49 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-27 18:05:57 | Baddegama (Gin Ganga) | 4.52 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-27 18:04:01 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.021 |  |
| 2026-09-27 18:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | -0.133 |  |
| 2026-09-27 18:00:20 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-27 18:02:39 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-27 18:00:07 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:00:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:07:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:03:31 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:44 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:55 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:03:12 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 18:02:14 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:03:49 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:09 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:00:50 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:52 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:00:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:43 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:12 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:00:14 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-09-27 18:11:15 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.026 |  |
| 2026-09-27 18:01:56 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.040 |  |
| 2026-09-27 18:04:40 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-09-27 18:03:46 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-09-27 18:03:25 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.060 |  |
| 2026-09-27 18:04:24 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.069 |  |
| 2026-09-27 18:03:03 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -0.072 |  |
| 2026-09-27 18:03:01 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.089 |  |
| 2026-09-27 18:02:31 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.095 |  |
| 2026-09-27 18:08:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |
| 2026-09-27 18:04:43 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.123 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)