# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_05:24:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 05:24:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-24 05:15:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:14:52 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 05:09:16 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:09:03 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:08:44 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 05:08:11 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-08-24 05:07:42 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 05:07:41 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.020 |  |
| 2026-08-24 05:07:21 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-24 05:07:07 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:06:27 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:05:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:05:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:05:35 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:04:53 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:03:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.119 |  |
| 2026-08-24 05:03:12 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-24 05:02:53 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:02:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:02:06 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:56 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:49 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 05:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:46 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:24 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 05:01:21 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-24 05:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:45 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:38 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.574 |  |
| 2026-08-24 05:00:21 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:52:12 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 04:51:56 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.056 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 05:07:21 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-24 05:03:12 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-24 05:24:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-24 05:07:42 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 05:01:24 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 05:08:44 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 05:01:49 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 05:14:52 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 05:01:21 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-23 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:21 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:05:35 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:56 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:02:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:04:57 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:01:46 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:02:53 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:07:07 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:09:16 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:01:53 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:05:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:00:45 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:15:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:01:26 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:06:27 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:02:06 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 05:05:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:09:03 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:04:53 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-08-24 05:08:11 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-08-24 05:07:41 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.020 |  |
| 2026-08-24 04:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.043 |  |
| 2026-08-24 05:03:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.119 |  |
| 2026-08-24 05:00:38 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.574 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)