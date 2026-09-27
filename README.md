# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_03:30:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,904 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 03:30:42 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.014 |  |
| 2026-09-28 03:16:10 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:15:13 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.006 |  |
| 2026-09-28 03:13:13 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.054 |  |
| 2026-09-28 03:08:30 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-09-28 03:08:25 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 03:07:42 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.040 |  |
| 2026-09-28 03:07:38 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:06:46 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.003 |  |
| 2026-09-28 03:05:27 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | -0.038 |  |
| 2026-09-28 03:04:55 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:32 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:21 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.029 |  |
| 2026-09-28 03:03:45 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-09-28 03:03:33 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:21 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:03:10 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:03 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-09-28 03:03:01 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:02:55 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.107 |  |
| 2026-09-28 03:02:50 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:02:43 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-28 03:02:37 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:02:15 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:01:38 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:01:23 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 03:01:19 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:01:17 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-28 03:00:58 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:13 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:09 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 03:01:17 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-28 02:11:47 | Baddegama (Gin Ganga) | 4.34 | 🟠 Minor Flood | -0.047 |  |
| 2026-09-28 03:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.029 |  |
| 2026-09-28 03:08:25 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 03:01:23 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 03:02:43 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:01:38 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:01:19 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:21 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:02:15 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:33 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:04:55 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:13 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:09 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:01 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:07:38 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:58 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:16:10 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:10 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:06:46 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.003 |  |
| 2026-09-28 03:15:13 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.006 |  |
| 2026-09-28 03:08:30 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-09-28 03:02:50 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:03:21 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:02:37 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 03:30:42 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.014 |  |
| 2026-09-28 03:03:03 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-09-28 03:05:27 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | -0.038 |  |
| 2026-09-28 03:07:42 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.040 |  |
| 2026-09-28 03:13:13 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.054 |  |
| 2026-09-28 03:03:45 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-09-28 03:02:55 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.107 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)