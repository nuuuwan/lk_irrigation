# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_10:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **50** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 10:13:34 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:12:47 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-09 10:12:46 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | -0.053 |  |
| 2026-11-09 10:10:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-11-09 10:10:01 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:09:29 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.147 |  |
| 2026-11-09 10:09:08 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.035 |  |
| 2026-11-09 10:06:54 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 10:06:44 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-09 10:05:48 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:05:45 | Dunamale (Aththanagalu Oya) | 4.42 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-09 10:05:32 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.042 |  |
| 2026-11-09 10:05:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:05:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:05:01 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-11-09 10:04:57 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-09 10:04:51 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:36 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:17 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.108 |  |
| 2026-11-09 10:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-11-09 10:03:57 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.075 |  |
| 2026-11-09 10:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-09 10:03:24 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | -0.021 |  |
| 2026-11-09 10:03:12 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:03:06 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.087 |  |
| 2026-11-09 10:03:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:02:39 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | -0.140 |  |
| 2026-11-09 10:02:30 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:02:11 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.070 |  |
| 2026-11-09 10:02:04 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:01:59 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.111 |  |
| 2026-11-09 10:01:53 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.112 |  |
| 2026-11-09 10:01:44 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-11-09 10:01:44 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.071 |  |
| 2026-11-09 10:01:37 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-09 10:01:31 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.103 |  |
| 2026-11-09 10:00:27 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.213 |  |
| 2026-11-09 10:00:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-09 09:51:11 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:51:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:51:05 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:51:03 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:51:00 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:50:57 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:50:54 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:50:52 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:50:49 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.111 |  |
| 2026-11-09 09:50:47 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.111 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 10:05:45 | Dunamale (Aththanagalu Oya) | 4.42 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-09 10:12:47 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-09 10:06:44 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 10:10:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-11-09 10:03:24 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | -0.021 |  |
| 2026-11-09 10:12:46 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | -0.053 |  |
| 2026-11-09 10:00:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-09 10:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-09 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-09 10:06:54 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 10:04:51 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:05:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:36 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:13:34 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:02:04 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-11-09 10:10:01 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:02:30 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:05:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:05:01 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-11-09 10:04:57 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-09 10:03:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:03:12 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:01:37 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-09 10:01:44 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-11-09 10:09:08 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.035 |  |
| 2026-11-09 10:05:32 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.042 |  |
| 2026-11-09 10:02:11 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.070 |  |
| 2026-11-09 10:01:44 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.071 |  |
| 2026-11-09 10:03:57 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.075 |  |
| 2026-11-09 10:03:06 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.087 |  |
| 2026-11-09 10:01:31 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.103 |  |
| 2026-11-09 10:04:17 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.108 |  |
| 2026-11-09 10:01:59 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.111 |  |
| 2026-11-09 10:01:53 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.112 |  |
| 2026-11-09 10:02:39 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | -0.140 |  |
| 2026-11-09 10:09:29 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.147 |  |
| 2026-11-09 10:00:27 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)