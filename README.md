# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_14:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 14:03:14 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:03:06 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.111 |  |
| 2026-11-14 14:02:57 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 14:02:46 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:02:40 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:02:35 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-11-14 14:02:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:02:03 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:54 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-14 14:01:46 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.043 |  |
| 2026-11-14 14:01:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-14 14:01:32 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 14:01:23 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:01:20 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-11-14 14:01:17 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:01:14 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:10 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:00:17 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 14:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:18:12 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 13:04:44 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 13:18:12 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | -0.026 |  |
| 2026-11-14 13:03:29 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.030 |  |
| 2026-11-14 13:04:35 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-14 13:03:02 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-14 14:01:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-14 14:00:17 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 13:03:19 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 14:01:32 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 14:02:57 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 14:01:17 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:02:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:06:54 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:03:03 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:11:25 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:02:46 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:02:03 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:05:20 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-14 14:01:23 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:04:40 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:02:40 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:06:43 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:10 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:14 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:03:06 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:01:49 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:03:14 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 14:01:20 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-11-14 13:04:27 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-14 13:04:15 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.020 |  |
| 2026-11-14 14:02:35 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-11-14 13:03:40 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2026-11-14 14:01:54 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-14 14:01:46 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.043 |  |
| 2026-11-14 13:02:46 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.044 |  |
| 2026-11-14 13:10:42 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-14 14:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)