# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_10:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,004 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-11-09 09:05:37 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-09 09:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-11-09 09:08:36 | Baddegama (Gin Ganga) | 3.63 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 09:07:31 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.000 |  |
| 2026-11-09 09:17:46 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 09:05:06 | Magura (Kalu Ganga) | 5.12 | 🟡 Alert | -0.084 |  |
| 2026-11-09 09:11:50 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-11-09 10:00:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-09 09:01:14 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 09:08:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-09 09:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:03:20 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:02:42 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:05:09 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:07:30 | Badalgama (Maha Oya) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:02:04 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:16:59 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-11-09 10:02:30 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-09 09:06:58 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-09 09:05:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-11-09 09:07:07 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-09 09:02:21 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:03:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:01:37 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-09 10:01:44 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-11-09 09:08:14 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-11-09 09:07:51 | Moragaswewa (Deduru Oya) | 2.81 | 🟢 Normal | -0.045 |  |
| 2026-11-09 09:04:32 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.057 |  |
| 2026-11-09 10:02:11 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.070 |  |
| 2026-11-09 10:01:44 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.071 |  |
| 2026-11-09 09:08:50 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.080 |  |
| 2026-11-09 10:03:06 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.087 |  |
| 2026-11-09 10:01:31 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.103 |  |
| 2026-11-09 09:02:57 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.103 |  |
| 2026-11-09 10:01:59 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.111 |  |
| 2026-11-09 10:01:53 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.112 |  |
| 2026-11-09 10:02:39 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | -0.140 |  |
| 2026-11-09 09:04:02 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.181 |  |
| 2026-11-09 10:00:27 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.213 |  |

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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