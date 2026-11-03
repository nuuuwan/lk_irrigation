# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_19:18:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,965 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 19:18:19 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.016 |  |
| 2026-11-03 19:16:20 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-03 19:15:22 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-03 19:12:18 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:10:45 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:09:58 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 19:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.018 |  |
| 2026-11-03 19:07:53 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.018 |  |
| 2026-11-03 19:07:49 | Urawa (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-11-03 19:07:46 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.019 |  |
| 2026-11-03 19:06:10 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-11-03 19:05:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 19:04:58 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:04:57 | Moragaswewa (Deduru Oya) | 4.22 | 🟢 Normal | -0.009 |  |
| 2026-11-03 19:04:52 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-03 19:04:38 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 19:04:37 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-03 19:04:12 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:04:02 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 19:03:45 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-03 19:03:45 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.096 |  |
| 2026-11-03 19:03:29 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-11-03 19:03:19 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 19:02:57 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:02:52 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-03 19:02:29 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-11-03 19:02:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-11-03 19:01:55 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:01:25 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 19:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:00:40 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 19:00:24 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.252 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 19:07:49 | Urawa (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-11-03 19:03:29 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 19:04:38 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 19:15:22 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-03 19:04:37 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-03 19:16:20 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 19:09:58 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 19:01:25 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 19:04:52 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-03 19:03:19 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 19:00:40 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 19:03:45 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-03 19:05:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 19:04:02 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 19:02:52 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:29 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:04:58 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:01:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:04:57 | Moragaswewa (Deduru Oya) | 4.22 | 🟢 Normal | -0.009 |  |
| 2026-11-03 19:04:12 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:02:57 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:55 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:18:19 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.016 |  |
| 2026-11-03 19:10:45 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:12:18 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.018 |  |
| 2026-11-03 19:07:53 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.018 |  |
| 2026-11-03 19:07:46 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.019 |  |
| 2026-11-03 19:06:10 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-11-03 19:02:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-03 19:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-11-03 19:02:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-11-03 19:03:45 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.096 |  |
| 2026-11-03 19:00:24 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.252 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)