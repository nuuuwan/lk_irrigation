# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_19:15:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 19:15:21 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 19:14:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2026-08-08 19:11:36 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 19:09:59 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:09:11 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:08:52 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:07:15 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:06:52 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.038 |  |
| 2026-08-08 19:05:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:05:40 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:05:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.018 |  |
| 2026-08-08 19:04:56 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-08-08 19:04:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-08-08 19:04:36 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 19:04:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:04:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:03:36 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-08 19:03:32 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-08-08 19:03:05 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-08-08 19:03:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:03:00 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-08-08 19:02:58 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-08-08 19:02:28 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:02:23 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 19:02:22 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-08 19:02:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:55 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 19:01:44 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-08-08 19:01:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:23 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:09 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-08-08 19:00:46 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 19:04:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-08-08 19:03:00 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-08-08 19:02:22 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-08 19:03:36 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-08 19:02:23 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 19:15:21 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 19:00:46 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-08 19:04:36 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 19:01:55 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 19:11:36 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:02:28 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:03:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:02:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:07:15 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:05:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:02:18 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:09:59 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:05:40 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:23 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:04:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:09:11 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:04:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:01:44 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 19:03:05 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-08-08 19:04:56 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-08-08 19:01:09 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-08-08 19:01:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-08-08 19:05:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.018 |  |
| 2026-08-08 19:03:32 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-08-08 19:02:58 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-08-08 19:06:52 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.038 |  |
| 2026-08-08 19:14:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)