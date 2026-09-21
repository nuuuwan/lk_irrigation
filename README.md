# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_16:05:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,083 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 16:05:27 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-21 16:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-21 16:05:23 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:04:58 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-09-21 16:04:51 | Hanwella (Kelani Ganga) | 5.68 | 🟢 Normal | -0.116 |  |
| 2026-09-21 16:04:16 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.029 |  |
| 2026-09-21 16:04:15 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.107 |  |
| 2026-09-21 16:04:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:03:40 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.059 |  |
| 2026-09-21 16:03:37 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 16:03:01 | Deraniyagala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.060 |  |
| 2026-09-21 16:02:52 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:02:45 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-21 16:02:41 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-21 16:02:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-21 16:01:56 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:49 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-21 16:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:44 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:38 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.049 |  |
| 2026-09-21 16:01:12 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-21 16:01:06 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 16:01:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:45 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:28 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:22:18 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 16:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-21 16:02:45 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-21 15:01:07 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-21 15:17:04 | Rathnapura (Kalu Ganga) | 5.59 | 🟡 Alert | -0.026 |  |
| 2026-09-21 16:04:16 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.029 |  |
| 2026-09-21 15:09:02 | Magura (Kalu Ganga) | 5.43 | 🟡 Alert | -0.043 |  |
| 2026-09-21 15:05:20 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-21 16:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-21 16:02:41 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-21 16:01:49 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-21 15:22:18 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-21 16:01:06 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 16:03:37 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 16:01:56 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:05:23 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:45 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:02:52 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:05:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:00:28 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:02:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:09 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:04:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:01:44 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 16:05:27 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-21 16:01:12 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-21 15:04:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-09-21 15:01:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.040 |  |
| 2026-09-21 16:01:38 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.049 |  |
| 2026-09-21 16:03:40 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.059 |  |
| 2026-09-21 16:03:01 | Deraniyagala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.060 |  |
| 2026-09-21 16:04:58 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-09-21 15:04:43 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.082 |  |
| 2026-09-21 15:04:02 | Glencourse (Kelani Ganga) | 12.95 | 🟢 Normal | -0.091 |  |
| 2026-09-21 16:04:15 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.107 |  |
| 2026-09-21 16:04:51 | Hanwella (Kelani Ganga) | 5.68 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)