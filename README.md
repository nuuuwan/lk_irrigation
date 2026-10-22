# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_20:08:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,178 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 20:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 20:07:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:06:50 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:06:25 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 20:05:43 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:05:42 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 20:05:20 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 20:05:15 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 20:05:15 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 20:05:05 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 20:04:53 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:04:45 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 20:04:39 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 20:04:21 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:04:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 20:03:54 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-10-22 20:03:51 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-22 20:03:40 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-10-22 20:03:40 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-22 20:03:29 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-22 20:03:26 | Holombuwa (Kelani Ganga) | 2.15 | 🟢 Normal | -0.268 |  |
| 2026-10-22 20:03:24 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.014 |  |
| 2026-10-22 20:03:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:03:15 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:57 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:02:54 | Moragaswewa (Deduru Oya) | 4.97 | 🟡 Alert | 0.193 | 🔺 Rising |
| 2026-10-22 20:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:02:32 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:31 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:15 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-22 20:02:01 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 20:01:43 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-22 20:01:40 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:01:26 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:01:16 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-22 20:00:14 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:31:27 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-10-22 19:29:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 20:02:54 | Moragaswewa (Deduru Oya) | 4.97 | 🟡 Alert | 0.193 | 🔺 Rising |
| 2026-10-22 20:03:29 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-22 20:03:40 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-22 20:01:16 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-22 20:02:15 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-22 20:05:05 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 20:05:15 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 20:05:42 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 20:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 20:04:39 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 20:02:01 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 20:05:20 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 20:06:25 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 20:05:15 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 20:04:53 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:07:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:06:50 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:05:43 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:00:14 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:32 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:31 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:03:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:01:40 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:01:26 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:02:57 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:04:21 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-22 20:03:24 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.014 |  |
| 2026-10-22 20:03:51 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-22 20:01:43 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-22 20:04:45 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 19:05:39 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-10-22 20:04:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 20:03:54 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-10-22 20:03:40 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 20:03:26 | Holombuwa (Kelani Ganga) | 2.15 | 🟢 Normal | -0.268 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)