# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_02:13:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 02:13:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.035 |  |
| 2026-08-08 02:11:15 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.018 |  |
| 2026-08-08 02:09:22 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -2.571 |  |
| 2026-08-08 02:09:08 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -2.571 |  |
| 2026-08-08 02:08:05 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.010 |  |
| 2026-08-08 02:06:04 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:05:38 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:05:18 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-08 02:04:51 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:04:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-08-08 02:04:20 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.029 |  |
| 2026-08-08 02:04:14 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.068 |  |
| 2026-08-08 02:04:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:03:55 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:03:48 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:03:05 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.041 |  |
| 2026-08-08 02:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:46 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-08-08 02:02:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:18 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:07 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-08 02:02:02 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-08-08 02:01:52 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:50 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:49 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:28 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 02:01:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.005 |  |
| 2026-08-08 02:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:18 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.020 |  |
| 2026-08-08 02:00:58 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 02:02:07 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-08 02:05:18 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-08 01:03:43 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-08 02:01:28 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 01:01:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:03:55 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:52 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:10:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:06:04 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:04:51 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:49 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:18 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:04:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:00:58 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:01:27 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:05:38 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:50 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:03:48 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:12:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-08 02:01:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.005 |  |
| 2026-08-08 01:26:31 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.008 |  |
| 2026-08-08 02:08:05 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.010 |  |
| 2026-08-08 02:11:15 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.018 |  |
| 2026-08-08 02:04:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-08-08 00:05:51 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-08-08 02:01:18 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.020 |  |
| 2026-08-08 02:04:20 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.029 |  |
| 2026-08-08 02:02:02 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-08-08 02:02:46 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-08-08 02:13:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.035 |  |
| 2026-08-08 02:03:05 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.041 |  |
| 2026-08-08 02:04:14 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.068 |  |
| 2026-08-08 02:09:22 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -2.571 |  |
| 2026-08-08 01:08:56 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)