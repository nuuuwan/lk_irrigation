# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_04:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Urawa — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 04:03:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-09-24 04:03:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:02:52 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | 0.186 | 🔺 Rising |
| 2026-09-24 04:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 04:02:13 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | -0.052 |  |
| 2026-09-24 04:02:09 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.066 |  |
| 2026-09-24 04:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:16 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:21 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.165 | 🔺 Rising |
| 2026-09-24 03:27:51 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.052 |  |
| 2026-09-24 03:27:09 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:23:49 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:23:14 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.027 |  |
| 2026-09-24 03:21:58 | Panadugama (Nilwala Ganga) | 5.09 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-09-24 03:21:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:21:19 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:20:28 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.165 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 04:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 03:06:21 | Urawa (Nilwala Ganga) | 3.02 | 🟡 Alert | 0.216 | 🔺 Rising |
| 2026-09-24 04:02:52 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | 0.186 | 🔺 Rising |
| 2026-09-24 04:00:21 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.165 | 🔺 Rising |
| 2026-09-24 03:21:58 | Panadugama (Nilwala Ganga) | 5.09 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-09-24 03:09:20 | Baddegama (Gin Ganga) | 3.90 | 🟡 Alert | 0.068 | 🔺 Rising |
| 2026-09-24 03:02:25 | Pitabeddara (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-09-24 03:03:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 03:08:24 | Hanwella (Kelani Ganga) | 4.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 03:06:07 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 03:06:22 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 03:04:21 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 03:05:32 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:03:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:21:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:03:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:09:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:04:36 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:13:35 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:06:02 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:58 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:27:09 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:23:49 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:30 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:16 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 04:03:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-09-24 03:23:14 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.027 |  |
| 2026-09-24 03:05:12 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-09-24 03:03:38 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-09-24 04:02:13 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | -0.052 |  |
| 2026-09-24 03:05:13 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.058 |  |
| 2026-09-24 04:02:09 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.066 |  |
| 2026-09-24 03:08:28 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)