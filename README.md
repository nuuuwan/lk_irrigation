# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_19:04:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,615 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 19:04:01 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:03:45 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.059 |  |
| 2026-09-27 19:03:37 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-09-27 19:03:33 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.070 |  |
| 2026-09-27 19:03:09 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-09-27 19:02:50 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:02:36 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-09-27 19:02:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:02:12 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.071 |  |
| 2026-09-27 19:02:09 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-09-27 19:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:58 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:57 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.081 |  |
| 2026-09-27 19:01:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:05 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:00:17 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:39:05 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:39:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

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
| 2026-09-27 19:00:17 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:58 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:02:50 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:05 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:04:01 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:03:12 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:01:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:02:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 19:03:09 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-09-27 19:02:09 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:09 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:52 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-27 18:02:12 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-09-27 19:02:36 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-09-27 19:03:37 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-09-27 18:11:15 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.026 |  |
| 2026-09-27 18:03:46 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-09-27 19:03:45 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.059 |  |
| 2026-09-27 18:04:24 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.069 |  |
| 2026-09-27 19:03:33 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.070 |  |
| 2026-09-27 19:02:12 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.071 |  |
| 2026-09-27 19:01:57 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.081 |  |
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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)