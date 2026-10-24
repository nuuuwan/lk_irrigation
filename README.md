# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_22:17:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,032 measurements** from **39** stations.
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
| 2026-10-24 22:17:12 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:14:29 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.016 |  |
| 2026-10-24 22:11:52 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-24 22:10:54 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-10-24 22:09:08 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:07:49 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-24 22:07:17 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:06:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-24 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-10-24 22:05:46 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:05:34 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:05:29 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:05:17 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:04:52 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:04:36 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:04:03 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.030 |  |
| 2026-10-24 22:03:55 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:03:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:03:18 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 22:02:57 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:02:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:02:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-24 22:02:21 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 22:02:14 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 22:02:08 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 22:02:06 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-10-24 22:02:04 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:01:55 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.041 |  |
| 2026-10-24 22:01:49 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.058 |  |
| 2026-10-24 22:01:44 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:01:41 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:01:35 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:01:16 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-10-24 22:00:09 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 22:06:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-24 22:02:08 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 22:11:52 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-24 22:02:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-24 22:00:09 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-24 22:03:18 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 22:02:14 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 22:02:21 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 22:02:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:03:55 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:04:36 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-24 21:05:34 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:01:35 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:03:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:17:12 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:05:46 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:09:08 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:05:17 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:05:29 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:01:41 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 22:10:54 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-10-24 22:07:49 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-24 22:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:07:17 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:05:34 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:02:57 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:01:44 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:02:04 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-24 22:02:06 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-10-24 22:14:29 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.016 |  |
| 2026-10-24 22:01:16 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-24 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-10-24 21:12:32 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-24 22:04:03 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-24 22:01:55 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.041 |  |
| 2026-10-24 22:01:49 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)