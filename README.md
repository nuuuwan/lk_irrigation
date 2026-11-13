# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_14:31:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,765 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 14:31:49 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-11-13 14:24:56 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-13 14:19:16 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-11-13 14:15:11 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | -0.016 |  |
| 2026-11-13 14:09:46 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.020 |  |
| 2026-11-13 14:08:37 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | 4.125 | 🔺 Rising |
| 2026-11-13 14:08:18 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:07:12 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.055 |  |
| 2026-11-13 14:06:46 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:06:08 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:05:51 | Kuda Oya (Kirindi Oya) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-11-13 14:05:39 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-13 14:05:07 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:04:57 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-11-13 14:04:33 | Rathnapura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.083 |  |
| 2026-11-13 14:04:31 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.024 |  |
| 2026-11-13 14:03:55 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:03:40 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:03:33 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:03:15 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-13 14:03:02 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-11-13 14:02:46 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:02:41 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.040 |  |
| 2026-11-13 14:02:17 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:02:15 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:10 | Thanamalwila (Kirindi Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:04 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.060 |  |
| 2026-11-13 14:01:56 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:01:04 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-13 14:01:02 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.073 |  |
| 2026-11-13 14:00:57 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:00:38 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.051 |  |
| 2026-11-13 14:00:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 14:00:12 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-13 13:59:48 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 14:08:37 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | 4.125 | 🔺 Rising |
| 2026-11-13 14:03:15 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-13 14:05:39 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-13 14:09:46 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.020 |  |
| 2026-11-13 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.040 |  |
| 2026-11-13 14:00:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 14:02:17 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:00:12 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:01:56 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:03:40 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:02:46 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:00:57 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:06:08 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:03:33 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:15 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:10 | Thanamalwila (Kirindi Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:41 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:03:02 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:02:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-11-13 14:01:04 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-13 14:15:11 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | -0.016 |  |
| 2026-11-13 14:04:57 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-11-13 14:05:51 | Kuda Oya (Kirindi Oya) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-11-13 14:05:07 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:08:18 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:24:56 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-13 14:04:31 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.024 |  |
| 2026-11-13 14:31:49 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-11-13 13:02:47 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.029 |  |
| 2026-11-13 14:19:16 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-11-13 14:03:55 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:06:46 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:00:38 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.051 |  |
| 2026-11-13 14:07:12 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.055 |  |
| 2026-11-13 14:02:04 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.060 |  |
| 2026-11-13 14:01:02 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.073 |  |
| 2026-11-13 14:04:33 | Rathnapura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)