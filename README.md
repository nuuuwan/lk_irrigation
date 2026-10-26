# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_17:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,636 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Rathnapura — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 17:11:28 | Moragaswewa (Deduru Oya) | 4.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-26 17:10:14 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.019 |  |
| 2026-10-26 17:09:43 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-10-26 17:09:26 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 17:09:20 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:09:04 | Urawa (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.065 |  |
| 2026-10-26 17:08:50 | Rathnapura (Kalu Ganga) | 8.12 | 🟠 Minor Flood | 0.048 | 🔺 Rising |
| 2026-10-26 17:07:58 | Nawalapitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 17:07:52 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | -0.308 |  |
| 2026-10-26 17:07:04 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | -0.515 |  |
| 2026-10-26 17:07:00 | Moraketiya (Walawe Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 17:06:37 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-26 17:06:08 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-26 17:06:04 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 17:05:57 | Peradeniya (Mahaweli Ganga) | 5.59 | 🟡 Alert | -0.031 |  |
| 2026-10-26 17:05:35 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.184 | 🔺 Rising |
| 2026-10-26 17:05:18 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 17:04:56 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.005 |  |
| 2026-10-26 17:04:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 17:04:51 | Galgamuwa (Mee Oya) | 4.15 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 17:04:49 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-26 17:04:48 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-10-26 17:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-10-26 17:03:42 | Ellagawa (Kalu Ganga) | 9.28 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-26 17:03:29 | Glencourse (Kelani Ganga) | 14.95 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-26 17:03:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:02:58 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.227 |  |
| 2026-10-26 17:02:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-26 17:02:36 | Badalgama (Maha Oya) | 4.39 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-26 17:02:25 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 17:02:09 | Norwood (Kelani Ganga) | 2.30 | 🟡 Alert | -0.085 |  |
| 2026-10-26 17:01:32 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:11 | Giriulla (Maha Oya) | 4.42 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-10-26 17:01:09 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:06 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | 0.690 | 🔺 Rising |
| 2026-10-26 17:01:01 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.110 |  |
| 2026-10-26 17:00:15 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 16:35:53 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | 0.690 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 17:08:50 | Rathnapura (Kalu Ganga) | 8.12 | 🟠 Minor Flood | 0.048 | 🔺 Rising |
| 2026-10-26 17:07:04 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | -0.515 |  |
| 2026-10-26 17:01:06 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | 0.690 | 🔺 Rising |
| 2026-10-26 17:05:35 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.184 | 🔺 Rising |
| 2026-10-26 17:09:43 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-10-26 17:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-10-26 17:05:57 | Peradeniya (Mahaweli Ganga) | 5.59 | 🟡 Alert | -0.031 |  |
| 2026-10-26 17:02:09 | Norwood (Kelani Ganga) | 2.30 | 🟡 Alert | -0.085 |  |
| 2026-10-26 16:04:37 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-26 17:01:11 | Giriulla (Maha Oya) | 4.42 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-10-26 17:06:08 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-26 17:03:29 | Glencourse (Kelani Ganga) | 14.95 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-26 17:04:49 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-26 17:06:37 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-26 17:02:36 | Badalgama (Maha Oya) | 4.39 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-26 17:04:51 | Galgamuwa (Mee Oya) | 4.15 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 17:11:28 | Moragaswewa (Deduru Oya) | 4.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-26 17:03:42 | Ellagawa (Kalu Ganga) | 9.28 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-26 17:06:04 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 17:09:26 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 17:07:58 | Nawalapitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 17:05:18 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 17:07:00 | Moraketiya (Walawe Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 17:04:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 17:02:25 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 17:00:15 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 17:04:56 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.005 |  |
| 2026-10-26 17:09:20 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:32 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:09 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:03:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:01:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 17:02:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-26 17:10:14 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.019 |  |
| 2026-10-26 17:04:48 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-10-26 17:09:04 | Urawa (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.065 |  |
| 2026-10-26 17:01:01 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.110 |  |
| 2026-10-26 17:02:58 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.227 |  |
| 2026-10-26 17:07:52 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | -0.308 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)