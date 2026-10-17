# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_19:27:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 19:27:36 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-10-17 19:24:21 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.007 |  |
| 2026-10-17 19:20:36 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | 0.000 |  |
| 2026-10-17 19:17:43 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 19:17:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-17 19:13:44 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 19:12:11 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -8.308 |  |
| 2026-10-17 19:11:58 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -8.308 |  |
| 2026-10-17 19:11:53 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 1.839 | 🔺 Rising |
| 2026-10-17 19:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.027 |  |
| 2026-10-17 19:09:42 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-17 19:08:50 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-17 19:08:28 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.300 |  |
| 2026-10-17 19:07:56 | Holombuwa (Kelani Ganga) | 2.74 | 🟢 Normal | 1.606 | 🔺 Rising |
| 2026-10-17 19:07:47 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-10-17 19:07:45 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | 0.000 |  |
| 2026-10-17 19:06:06 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.077 |  |
| 2026-10-17 19:06:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.090 |  |
| 2026-10-17 19:05:12 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 19:04:06 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:03:52 | Deraniyagala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.344 |  |
| 2026-10-17 19:03:49 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.029 |  |
| 2026-10-17 19:03:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-10-17 19:03:39 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-17 19:03:21 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-10-17 19:03:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:02:54 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:02:42 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-10-17 19:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:01:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 19:00:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 19:13:44 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 19:08:50 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-17 19:20:36 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | 0.000 |  |
| 2026-10-17 19:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.027 |  |
| 2026-10-17 19:11:53 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 1.839 | 🔺 Rising |
| 2026-10-17 19:07:56 | Holombuwa (Kelani Ganga) | 2.74 | 🟢 Normal | 1.606 | 🔺 Rising |
| 2026-10-17 19:03:21 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-10-17 19:03:39 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-17 18:04:11 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-17 19:17:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-17 19:05:12 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 19:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 19:17:43 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 19:09:42 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:02:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:00:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:03:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:24:21 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.007 |  |
| 2026-10-17 19:07:47 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-10-17 19:04:06 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:03:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-10-17 19:03:49 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.029 |  |
| 2026-10-17 19:27:36 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-10-17 19:01:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:02:54 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 19:02:42 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 19:06:06 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.077 |  |
| 2026-10-17 19:06:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.090 |  |
| 2026-10-17 19:08:28 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.300 |  |
| 2026-10-17 19:03:52 | Deraniyagala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.344 |  |
| 2026-10-17 19:12:11 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -8.308 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)