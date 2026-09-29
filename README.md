# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_14:22:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,221 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 14:22:36 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:18:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.046 |  |
| 2026-09-29 14:14:52 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.008 |  |
| 2026-09-29 14:13:13 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-09-29 14:10:39 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.027 |  |
| 2026-09-29 14:09:34 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-09-29 14:07:40 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.038 |  |
| 2026-09-29 14:07:34 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:06:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 14:06:23 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-09-29 14:05:49 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:31 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:30 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:04 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.051 |  |
| 2026-09-29 14:04:58 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:04:28 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-29 14:04:25 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-09-29 14:04:20 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:04:05 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:03:58 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:03:37 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:03:32 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 14:03:31 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-29 14:02:53 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:02:50 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:02:47 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.040 |  |
| 2026-09-29 14:02:43 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:02:42 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.051 |  |
| 2026-09-29 14:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:02:14 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-29 14:02:08 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:28 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:26 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-29 14:01:09 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:00:51 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-09-29 14:00:15 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-29 14:00:10 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-29 14:04:28 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-29 14:02:14 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-29 14:03:31 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-29 14:03:32 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 14:06:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 14:00:10 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:02:08 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:26 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:03:58 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:04:05 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:31 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:30 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:07:34 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:05:49 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:03:37 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:09 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:02:53 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:22:36 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:04:58 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:02:43 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:01:28 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-29 14:14:52 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.008 |  |
| 2026-09-29 14:04:20 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:02:50 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-09-29 14:06:23 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-09-29 14:09:34 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-09-29 14:04:25 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-09-29 14:00:15 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-29 14:13:13 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-09-29 14:10:39 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.027 |  |
| 2026-09-29 14:00:51 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-09-29 14:07:40 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.038 |  |
| 2026-09-29 14:02:47 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.040 |  |
| 2026-09-29 14:18:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.046 |  |
| 2026-09-29 14:05:04 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.051 |  |
| 2026-09-29 14:02:42 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)