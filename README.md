# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_16:15:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 16:15:43 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-24 16:13:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.035 |  |
| 2026-11-24 16:11:43 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.018 |  |
| 2026-11-24 16:10:45 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-24 16:07:49 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.074 |  |
| 2026-11-24 16:07:14 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 16:07:10 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-24 16:06:57 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-24 16:06:53 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-24 16:06:42 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-24 16:06:30 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-11-24 16:05:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 16:05:35 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-24 16:05:25 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-11-24 16:05:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-11-24 16:05:12 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.020 |  |
| 2026-11-24 16:04:17 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-24 16:04:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:04:09 | Moraketiya (Walawe Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:03:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-24 16:03:28 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.120 |  |
| 2026-11-24 16:03:21 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:02:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 16:02:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 16:02:44 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:02:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:02:11 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:02:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 16:01:59 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-24 16:01:15 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-24 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-24 16:01:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:10 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 16:06:30 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-11-24 16:05:25 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-11-24 16:10:45 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-24 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-24 16:06:57 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-24 16:06:53 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-24 16:04:17 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-24 16:07:10 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-24 16:02:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 16:02:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 16:05:35 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-24 16:07:14 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:04:09 | Moraketiya (Walawe Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:15:43 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-24 16:02:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 16:05:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 16:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:59 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:04:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:02:44 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:02:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:03:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-24 16:11:43 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.018 |  |
| 2026-11-24 16:06:42 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-24 16:05:12 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.020 |  |
| 2026-11-24 16:01:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 16:00:10 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.032 |  |
| 2026-11-24 16:13:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.035 |  |
| 2026-11-24 16:01:15 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-24 16:02:11 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:03:21 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:07:49 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.074 |  |
| 2026-11-24 16:05:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-11-24 16:03:28 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)