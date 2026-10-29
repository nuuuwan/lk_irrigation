# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_14:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 14:05:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:05:27 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 14:04:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-29 14:04:15 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:04:13 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:04:04 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.069 |  |
| 2026-10-29 14:04:01 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.043 |  |
| 2026-10-29 14:03:51 | Ellagawa (Kalu Ganga) | 9.93 | 🟢 Normal | -0.030 |  |
| 2026-10-29 14:03:06 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:03:00 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-10-29 14:02:59 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.089 |  |
| 2026-10-29 14:02:55 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:02:51 | Putupaula (Kalu Ganga) | 3.69 | 🟡 Alert | -0.010 |  |
| 2026-10-29 14:02:48 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 14:02:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 14:02:36 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:34 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:02:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:08 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.021 |  |
| 2026-10-29 14:01:39 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-29 14:01:19 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-29 14:00:52 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:00:44 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:00:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:32:14 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.014 |  |
| 2026-10-29 13:31:46 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:19:11 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 14:05:27 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 13:01:58 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.28 | 🟠 Minor Flood | -0.071 |  |
| 2026-10-29 13:10:02 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | -0.010 |  |
| 2026-10-29 14:02:51 | Putupaula (Kalu Ganga) | 3.69 | 🟡 Alert | -0.010 |  |
| 2026-10-29 14:04:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-29 14:02:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 14:02:48 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 14:00:44 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:16:57 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:34 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:36 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:13 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:00:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:00:52 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:02:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:06:25 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:17 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:03:06 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:07:09 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:05:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 14:04:15 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:04:13 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:02:55 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:01:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:00:44 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-29 14:03:00 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-10-29 13:32:14 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.014 |  |
| 2026-10-29 14:01:19 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-29 14:01:39 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-29 14:02:08 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.021 |  |
| 2026-10-29 14:03:51 | Ellagawa (Kalu Ganga) | 9.93 | 🟢 Normal | -0.030 |  |
| 2026-10-29 13:01:40 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.031 |  |
| 2026-10-29 14:04:01 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.043 |  |
| 2026-10-29 13:06:24 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.053 |  |
| 2026-10-29 14:04:04 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.069 |  |
| 2026-10-29 14:02:59 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.089 |  |
| 2026-10-29 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)