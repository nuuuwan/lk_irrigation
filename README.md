# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_18:11:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 18:11:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.137 |  |
| 2026-10-13 18:10:30 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.863 | 🔺 Rising |
| 2026-10-13 18:08:03 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 18:06:42 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-10-13 18:06:36 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:22 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:10 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | -0.042 |  |
| 2026-10-13 18:05:04 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-13 18:04:31 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.064 |  |
| 2026-10-13 18:04:30 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:04:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:03:43 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 18:03:29 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-10-13 18:03:26 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 18:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.020 |  |
| 2026-10-13 18:02:47 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:02:45 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-10-13 18:02:42 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-13 18:02:38 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-13 18:02:28 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:02:11 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:02:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-13 18:02:03 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:01:43 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-10-13 18:01:40 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 18:01:39 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.104 |  |
| 2026-10-13 18:01:35 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.032 |  |
| 2026-10-13 18:01:33 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:01:17 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-13 18:00:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:00:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:18 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:00:14 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 18:08:03 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 18:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.020 |  |
| 2026-10-13 18:05:10 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | -0.042 |  |
| 2026-10-13 18:10:30 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.863 | 🔺 Rising |
| 2026-10-13 18:02:45 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-10-13 18:02:42 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-13 18:02:38 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-13 18:05:22 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-13 18:01:40 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 18:01:17 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-13 18:05:04 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-13 18:03:43 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 18:03:26 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 18:00:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:06:36 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:02:03 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:02:28 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:00:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:01:33 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:00:18 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:00:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:41 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:02:47 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:02:11 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:04:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:14 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:03:29 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-10-13 18:02:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-13 18:01:43 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-10-13 17:06:07 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-10-13 18:06:42 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-10-13 18:01:35 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.032 |  |
| 2026-10-13 18:04:31 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.064 |  |
| 2026-10-13 18:01:39 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.104 |  |
| 2026-10-13 18:11:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)