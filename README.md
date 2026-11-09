# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_11:18:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 11:18:47 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-09 11:11:29 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:10:24 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:09:52 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:07:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.051 |  |
| 2026-11-09 11:07:05 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-11-09 11:06:41 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-09 11:05:56 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.102 |  |
| 2026-11-09 11:05:55 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-09 11:05:13 | Moragaswewa (Deduru Oya) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-11-09 11:05:10 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:04:43 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.130 |  |
| 2026-11-09 11:04:26 | Badalgama (Maha Oya) | 4.17 | 🟢 Normal | -0.106 |  |
| 2026-11-09 11:04:26 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:04:19 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 11:04:02 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:03:58 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-09 11:03:51 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:03:51 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | -0.060 |  |
| 2026-11-09 11:03:48 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.078 |  |
| 2026-11-09 11:03:44 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.147 |  |
| 2026-11-09 11:03:44 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.089 |  |
| 2026-11-09 11:03:13 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | -0.039 |  |
| 2026-11-09 11:03:04 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-09 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:52 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 11:02:29 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:23 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.068 |  |
| 2026-11-09 11:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:01:54 | Dunamale (Aththanagalu Oya) | 4.43 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-09 11:01:52 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-11-09 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:37 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:35 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:53 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 11:01:54 | Dunamale (Aththanagalu Oya) | 4.43 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-09 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-09 11:09:52 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:11:29 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:05:10 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 11:05:56 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.102 |  |
| 2026-11-09 11:05:55 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-09 11:03:58 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-09 11:06:41 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-09 11:00:53 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 11:18:47 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-09 11:04:19 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 11:04:26 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:10:24 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:01:35 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:03:04 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:29 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:02:52 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:37 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:04:02 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:03:51 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 11:07:05 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-11-09 11:03:13 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | -0.039 |  |
| 2026-11-09 11:05:13 | Moragaswewa (Deduru Oya) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-11-09 11:01:52 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-11-09 11:07:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.051 |  |
| 2026-11-09 11:03:51 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | -0.060 |  |
| 2026-11-09 11:02:23 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.068 |  |
| 2026-11-09 11:03:48 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.078 |  |
| 2026-11-09 11:03:44 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.089 |  |
| 2026-11-09 11:04:26 | Badalgama (Maha Oya) | 4.17 | 🟢 Normal | -0.106 |  |
| 2026-11-09 11:04:43 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.130 |  |
| 2026-11-09 11:03:44 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)