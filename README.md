# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_16:32:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,851 measurements** from **39** stations.
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
| 2026-11-03 16:32:56 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.013 |  |
| 2026-11-03 16:21:44 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 16:20:28 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-03 16:20:22 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.038 |  |
| 2026-11-03 16:11:36 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:09:54 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:09:15 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 16:08:35 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-11-03 16:08:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 16:08:15 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.050 |  |
| 2026-11-03 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:06:52 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-03 16:06:45 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.018 |  |
| 2026-11-03 16:06:37 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-03 16:06:34 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.068 |  |
| 2026-11-03 16:06:23 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-03 16:06:16 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:05:01 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-11-03 16:05:01 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.091 |  |
| 2026-11-03 16:04:41 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 16:04:25 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.055 |  |
| 2026-11-03 16:04:12 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-03 16:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-11-03 16:03:47 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-11-03 16:03:36 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 16:03:28 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:03:22 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 16:03:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:03:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-03 16:03:04 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:02:51 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 16:02:22 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-11-03 16:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-03 16:01:59 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.112 |  |
| 2026-11-03 16:01:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:00:58 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.023 |  |
| 2026-11-03 16:00:33 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 16:06:23 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-03 16:03:22 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 16:20:28 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-03 16:09:15 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 16:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-03 16:03:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-03 16:08:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 16:02:51 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 16:04:41 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 16:03:36 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 16:21:44 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 16:06:52 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-03 16:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:03:04 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:03:28 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:11:36 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:06:16 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:09:54 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:00:33 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:08:35 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-11-03 16:06:37 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-03 16:01:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:03:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:32:56 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.013 |  |
| 2026-11-03 16:06:45 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.018 |  |
| 2026-11-03 16:03:47 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-11-03 16:04:12 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-03 16:05:01 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-11-03 16:00:58 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.023 |  |
| 2026-11-03 16:20:22 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.038 |  |
| 2026-11-03 16:02:22 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-11-03 16:08:15 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.050 |  |
| 2026-11-03 16:04:25 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.055 |  |
| 2026-11-03 16:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-11-03 16:06:34 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.068 |  |
| 2026-11-03 16:05:01 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.091 |  |
| 2026-11-03 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)