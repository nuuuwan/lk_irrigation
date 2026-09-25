# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_19:06:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 19:06:11 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 19:05:13 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:05:01 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 19:04:59 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-25 19:04:45 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:04:44 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.010 |  |
| 2026-09-25 19:04:33 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-09-25 19:04:25 | Hanwella (Kelani Ganga) | 5.94 | 🟢 Normal | -0.060 |  |
| 2026-09-25 19:04:19 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 19:04:10 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-25 19:03:57 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-09-25 19:03:33 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-09-25 19:03:28 | Glencourse (Kelani Ganga) | 13.61 | 🟢 Normal | -0.021 |  |
| 2026-09-25 19:02:52 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 19:02:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-09-25 19:02:27 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:02:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:37 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 19:01:30 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:22 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | -0.032 |  |
| 2026-09-25 19:01:16 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:16 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:00:46 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:18:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:02:08 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:04:28 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 19:05:01 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 19:04:44 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.010 |  |
| 2026-09-25 19:01:22 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | -0.032 |  |
| 2026-09-25 18:01:09 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.042 |  |
| 2026-09-25 19:04:10 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-25 18:05:06 | Nawalapitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-25 19:04:59 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-25 19:04:19 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 19:02:52 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 19:01:37 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 19:06:11 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 19:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:22 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:18:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:04:45 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:02:27 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:00:46 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:06:15 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:03 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:05:13 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:16 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:01:30 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:02:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:04:33 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-09-25 19:03:33 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 19:03:28 | Glencourse (Kelani Ganga) | 13.61 | 🟢 Normal | -0.021 |  |
| 2026-09-25 19:03:57 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-09-25 19:02:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-09-25 19:04:25 | Hanwella (Kelani Ganga) | 5.94 | 🟢 Normal | -0.060 |  |
| 2026-09-25 18:04:03 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -1.019 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)