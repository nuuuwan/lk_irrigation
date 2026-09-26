# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_13:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 13:06:01 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:04:50 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:04:28 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:04:26 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:04:26 | Deraniyagala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-09-26 13:04:20 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-26 13:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:03:47 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.169 |  |
| 2026-09-26 13:03:45 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-26 13:03:40 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-26 13:03:40 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | -0.050 |  |
| 2026-09-26 13:03:32 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.049 |  |
| 2026-09-26 13:02:50 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:02:42 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:02:39 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-26 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 13:02:15 | Kithulgala (Kelani Ganga) | 2.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-26 13:02:08 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-26 13:02:01 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:02:00 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:30 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 13:01:29 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:24 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:10 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:00:53 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:00:26 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-26 12:26:05 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 13:02:39 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-26 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 13:03:40 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-26 12:26:05 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-26 12:09:09 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-09-26 13:04:26 | Deraniyagala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-09-26 13:00:26 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-26 13:02:08 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-26 13:03:45 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-26 13:02:15 | Kithulgala (Kelani Ganga) | 2.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-26 12:05:43 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 13:01:30 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 12:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:10 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:02:50 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:02:00 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:16 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:24 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:06:01 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:53 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:01:29 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:04:28 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:02:01 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:00:53 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 13:04:26 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:04:50 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:02:42 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:03:32 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:02:14 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:06:02 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | -0.021 |  |
| 2026-09-26 12:07:02 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.028 |  |
| 2026-09-26 13:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.049 |  |
| 2026-09-26 13:03:40 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | -0.050 |  |
| 2026-09-26 13:04:20 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-26 13:03:47 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)