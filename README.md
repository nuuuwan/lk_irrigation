# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_11:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 11:11:18 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:10:47 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-22 11:08:19 | Panadugama (Nilwala Ganga) | 4.94 | 🟢 Normal | -0.041 |  |
| 2026-09-22 11:08:01 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-22 11:05:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:05:50 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-22 11:05:42 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-09-22 11:05:33 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-09-22 11:05:14 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-09-22 11:05:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-22 11:05:00 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-22 11:04:56 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.183 |  |
| 2026-09-22 11:04:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 11:04:44 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.052 |  |
| 2026-09-22 11:04:31 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.181 |  |
| 2026-09-22 11:04:30 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.040 |  |
| 2026-09-22 11:04:27 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-09-22 11:04:25 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | -0.031 |  |
| 2026-09-22 11:04:18 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2026-09-22 11:04:00 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-22 11:03:29 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:03:18 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:03:02 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-22 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 11:02:32 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.081 |  |
| 2026-09-22 11:02:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 11:01:56 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 11:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:26 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:10 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 11:01:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:06 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:00:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:00:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:00:09 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 10:56:20 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 11:04:00 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-22 11:00:09 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 11:01:56 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 11:04:27 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-09-22 11:03:02 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-22 11:05:50 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-22 11:08:01 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-22 11:10:47 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-22 11:01:10 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 11:04:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 11:02:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 11:01:06 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:00:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:03:29 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:05:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:03:18 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:00:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:02:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:26 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:11:18 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:00:46 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:01:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:05:33 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-09-22 11:05:42 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-09-22 11:05:00 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-22 11:04:18 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2026-09-22 11:05:14 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-09-22 11:05:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-22 11:04:25 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | -0.031 |  |
| 2026-09-22 11:04:30 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.040 |  |
| 2026-09-22 11:08:19 | Panadugama (Nilwala Ganga) | 4.94 | 🟢 Normal | -0.041 |  |
| 2026-09-22 11:04:44 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.052 |  |
| 2026-09-22 11:02:32 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.081 |  |
| 2026-09-22 11:04:31 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.181 |  |
| 2026-09-22 11:04:56 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)