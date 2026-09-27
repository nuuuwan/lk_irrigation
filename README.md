# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_16:21:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 16:21:10 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-09-27 16:18:27 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:15:25 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.025 |  |
| 2026-09-27 16:10:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.048 |  |
| 2026-09-27 16:09:34 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-09-27 16:09:10 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.018 |  |
| 2026-09-27 16:08:53 | Baddegama (Gin Ganga) | 4.58 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 16:08:47 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.103 |  |
| 2026-09-27 16:08:30 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.055 |  |
| 2026-09-27 16:08:26 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:06:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-09-27 16:06:17 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.085 |  |
| 2026-09-27 16:05:58 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:05:42 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:04:13 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.070 |  |
| 2026-09-27 16:04:03 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:04:01 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 16:03:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.043 |  |
| 2026-09-27 16:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:35 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:33 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:03:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:24 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-27 16:02:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:32 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-27 16:02:31 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 16:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 16:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:02:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:01:34 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.094 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 16:02:31 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 16:08:53 | Baddegama (Gin Ganga) | 4.58 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 16:15:25 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.025 |  |
| 2026-09-27 16:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.094 |  |
| 2026-09-27 16:02:32 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-27 16:04:01 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:05:42 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:03:33 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:18:27 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:34 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 16:21:10 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-09-27 16:09:34 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-09-27 16:04:03 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:08:26 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:05:58 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:35 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:09:10 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.018 |  |
| 2026-09-27 16:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 16:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:00:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:03:24 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-27 16:03:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.043 |  |
| 2026-09-27 16:10:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.048 |  |
| 2026-09-27 16:08:30 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.055 |  |
| 2026-09-27 16:04:13 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.070 |  |
| 2026-09-27 16:06:17 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.085 |  |
| 2026-09-27 16:06:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-09-27 16:08:47 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)