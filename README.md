# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_15:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,047 measurements** from **39** stations.
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
| 2026-08-07 15:12:00 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:11:28 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:09:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-07 15:08:01 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-07 15:07:37 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-08-07 15:07:34 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-07 15:06:07 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.103 |  |
| 2026-08-07 15:06:00 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:05:42 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-07 15:05:32 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 15:04:59 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:04:20 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-08-07 15:04:09 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-07 15:03:40 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:03:21 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:03:09 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:58 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:02:56 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.042 |  |
| 2026-08-07 15:02:54 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-08-07 15:02:36 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-07 15:02:25 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-08-07 15:02:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:23 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-07 15:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.014 |  |
| 2026-08-07 15:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:48 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:33 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:23 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:23 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-08-07 15:01:17 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:12 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.053 |  |
| 2026-08-07 15:01:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:04 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:00:48 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:00:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 14:58:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-07 14:55:34 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 15:05:42 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-07 15:07:34 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-07 15:02:23 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-07 15:02:36 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-07 15:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-07 15:09:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-07 15:08:01 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-07 15:05:32 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 15:01:17 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:06:00 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:11:28 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:48 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:33 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 14:58:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:03:40 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:03:21 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 14:12:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:04:09 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:01:23 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:03:09 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:12:00 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:00:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:00:48 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 15:02:58 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:04:59 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:01:04 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-07 15:02:54 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-08-07 15:02:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.014 |  |
| 2026-08-07 15:07:37 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-08-07 15:01:23 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-08-07 15:04:20 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-08-07 15:02:56 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.042 |  |
| 2026-08-07 15:01:12 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.053 |  |
| 2026-08-07 15:02:25 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-08-07 15:06:07 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)