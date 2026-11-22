# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_12:26:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,689 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 12:26:48 | Moragaswewa (Deduru Oya) | 3.47 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:19:11 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-11-22 12:14:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:12:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-11-22 12:11:04 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 12:10:58 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 12:09:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-11-22 12:09:08 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-11-22 12:08:34 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-11-22 12:08:21 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:07:47 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:07:28 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:06:48 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-22 12:06:14 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-11-22 12:06:11 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.019 |  |
| 2026-11-22 12:05:00 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-11-22 12:04:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.130 |  |
| 2026-11-22 12:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 12:04:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-22 12:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.068 |  |
| 2026-11-22 12:03:56 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-11-22 12:03:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-11-22 12:03:36 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 12:03:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 12:03:10 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:03:08 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-11-22 12:02:47 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 12:02:43 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:02:20 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-22 12:01:49 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-11-22 12:01:34 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:30 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:29 | Moragaswewa (Deduru Oya) | 3.47 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:21 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 12:01:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 12:01:10 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:00:39 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:00:34 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-11-22 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.030 |  |
| 2026-11-22 11:58:48 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 12:04:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-22 12:10:58 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 12:06:48 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-22 12:02:47 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 12:03:36 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 12:01:21 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 12:01:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 12:11:04 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 12:07:28 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:00:39 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:26:48 | Moragaswewa (Deduru Oya) | 3.47 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:34 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:10 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:03:10 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:07:47 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:08:21 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:02:43 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:14:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:30 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 12:03:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 12:08:34 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-11-22 12:19:11 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-11-22 12:06:11 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.019 |  |
| 2026-11-22 12:03:56 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-11-22 12:12:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-11-22 12:03:08 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-11-22 12:05:00 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-11-22 12:02:20 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-22 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.030 |  |
| 2026-11-22 12:03:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-11-22 12:00:34 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-11-22 12:09:08 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-11-22 12:01:49 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-11-22 12:06:14 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-11-22 12:09:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-11-22 12:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.068 |  |
| 2026-11-22 12:04:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)