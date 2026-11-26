# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_13:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,209 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 13:15:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:14:48 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-11-26 13:11:54 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-11-26 13:09:49 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:09:03 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-11-26 13:08:58 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.183 |  |
| 2026-11-26 13:08:25 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.045 |  |
| 2026-11-26 13:08:21 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.062 |  |
| 2026-11-26 13:07:37 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-11-26 13:07:36 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-11-26 13:06:06 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.102 |  |
| 2026-11-26 13:05:35 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-11-26 13:05:28 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.070 |  |
| 2026-11-26 13:05:16 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-11-26 13:05:14 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.069 |  |
| 2026-11-26 13:05:09 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-26 13:04:33 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:04:32 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-11-26 13:04:29 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.083 |  |
| 2026-11-26 13:04:10 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:03:55 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.962 |  |
| 2026-11-26 13:03:39 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.067 |  |
| 2026-11-26 13:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.010 |  |
| 2026-11-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-26 13:03:02 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.110 |  |
| 2026-11-26 13:02:49 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-11-26 13:02:49 | Moragaswewa (Deduru Oya) | 4.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-26 13:02:39 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:02:31 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:02:07 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-26 13:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:50 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:01:48 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:40 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 13:01:28 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-26 13:01:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 13:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.010 |  |
| 2026-11-26 13:03:39 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.067 |  |
| 2026-11-26 13:07:37 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-11-26 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-26 13:02:49 | Moragaswewa (Deduru Oya) | 4.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-26 13:05:09 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-26 13:01:40 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 13:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:09:49 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:48 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:04:10 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:15:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:14:48 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-11-26 13:02:39 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:01:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:01:28 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-26 12:11:12 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-26 13:09:03 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-11-26 13:07:36 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-11-26 12:11:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.017 |  |
| 2026-11-26 13:04:33 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:01:50 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:04:32 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-11-26 13:11:54 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-11-26 13:05:16 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-11-26 13:02:07 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-26 12:04:02 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.031 |  |
| 2026-11-26 13:08:25 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.045 |  |
| 2026-11-26 13:05:35 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-11-26 13:08:21 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.062 |  |
| 2026-11-26 13:05:14 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.069 |  |
| 2026-11-26 13:05:28 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.070 |  |
| 2026-11-26 13:02:49 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-11-26 13:04:29 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.083 |  |
| 2026-11-26 13:06:06 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.102 |  |
| 2026-11-26 13:03:02 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.110 |  |
| 2026-11-26 13:08:58 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.183 |  |
| 2026-11-26 13:03:55 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.962 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)