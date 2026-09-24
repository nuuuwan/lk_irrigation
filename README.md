# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_13:14:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 13:14:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:11:17 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-24 13:11:07 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-24 13:11:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:09:17 | Urawa (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.073 |  |
| 2026-09-24 13:08:38 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-24 13:08:05 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:07:46 | Pitabeddara (Nilwala Ganga) | 4.40 | 🟡 Alert | -0.191 |  |
| 2026-09-24 13:07:03 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-24 13:06:26 | Holombuwa (Kelani Ganga) | 2.29 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-24 13:06:25 | Panadugama (Nilwala Ganga) | 6.71 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 13:06:02 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 13:05:29 | Peradeniya (Mahaweli Ganga) | 4.36 | 🟢 Normal | -0.051 |  |
| 2026-09-24 13:05:20 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.213 |  |
| 2026-09-24 13:04:52 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 13:04:36 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 13:04:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:04:32 | Glencourse (Kelani Ganga) | 13.41 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-24 13:04:32 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:03:50 | Nawalapitiya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.109 |  |
| 2026-09-24 13:03:45 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:03:32 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 13:03:19 | Baddegama (Gin Ganga) | 4.35 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-09-24 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 13:03:02 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:02:46 | Deraniyagala (Kelani Ganga) | 2.77 | 🟢 Normal | -0.202 |  |
| 2026-09-24 13:02:36 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:02:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:02:14 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-24 13:01:53 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 13:01:48 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 13:01:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:01:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:01:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-09-24 13:00:58 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-24 13:00:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:40 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 13:03:19 | Baddegama (Gin Ganga) | 4.35 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-09-24 13:06:25 | Panadugama (Nilwala Ganga) | 6.71 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 13:08:38 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-24 13:02:14 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-24 13:00:58 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-24 13:04:52 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 13:07:46 | Pitabeddara (Nilwala Ganga) | 4.40 | 🟡 Alert | -0.191 |  |
| 2026-09-24 13:06:26 | Holombuwa (Kelani Ganga) | 2.29 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-24 13:04:32 | Glencourse (Kelani Ganga) | 13.41 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-24 13:04:36 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 13:11:17 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-24 13:01:53 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 13:01:48 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 13:06:02 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 13:03:32 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 13:11:07 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-24 13:07:03 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-24 13:00:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:01:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:00:40 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:04:32 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:11:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:04:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:03:45 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:14:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:08:05 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:01:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:02:36 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:02:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:03:02 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-24 13:01:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-09-24 13:05:29 | Peradeniya (Mahaweli Ganga) | 4.36 | 🟢 Normal | -0.051 |  |
| 2026-09-24 13:09:17 | Urawa (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.073 |  |
| 2026-09-24 13:03:50 | Nawalapitiya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.109 |  |
| 2026-09-24 13:02:46 | Deraniyagala (Kelani Ganga) | 2.77 | 🟢 Normal | -0.202 |  |
| 2026-09-24 13:05:20 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)