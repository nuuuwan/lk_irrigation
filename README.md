# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_03:22:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 03:22:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:15:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-08-06 03:15:46 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.016 |  |
| 2026-08-06 03:12:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -144.000 |  |
| 2026-08-06 03:11:59 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -144.000 |  |
| 2026-08-06 03:11:58 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -144.000 |  |
| 2026-08-06 03:10:55 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-08-06 03:09:09 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-06 03:08:12 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.410 |  |
| 2026-08-06 03:08:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:06:35 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:06:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-08-06 03:05:37 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:05:28 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.005 |  |
| 2026-08-06 03:05:17 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.030 |  |
| 2026-08-06 03:05:08 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-08-06 03:04:49 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.005 |  |
| 2026-08-06 03:04:42 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:04:41 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.045 |  |
| 2026-08-06 03:04:40 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 03:04:34 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | -2.726 |  |
| 2026-08-06 03:04:19 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-08-06 03:04:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:04:01 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:03:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:56 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.063 |  |
| 2026-08-06 03:02:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:45 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.025 |  |
| 2026-08-06 03:02:27 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.160 |  |
| 2026-08-06 03:02:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-08-06 03:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:01:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:01:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:00:47 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:00:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:59:17 | Peradeniya (Mahaweli Ganga) | 4.76 | 🟢 Normal | -2.726 |  |
| 2026-08-06 02:57:07 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:56:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:50:39 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.410 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 03:06:35 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-06 03:09:09 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-06 03:04:40 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 03:05:28 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.005 |  |
| 2026-08-06 03:04:01 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:22:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:45 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:00:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:04:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:01:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:01:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:02:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:05:37 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:03:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:04:49 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.005 |  |
| 2026-08-06 03:15:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-08-06 03:04:42 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:08:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:00:47 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:05:08 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-08-06 03:02:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-08-06 03:15:46 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.016 |  |
| 2026-08-06 03:10:55 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-08-06 03:04:19 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-08-06 03:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.025 |  |
| 2026-08-06 03:05:17 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.030 |  |
| 2026-08-06 03:06:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-08-06 03:04:41 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.045 |  |
| 2026-08-06 03:02:56 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.063 |  |
| 2026-08-06 03:02:27 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.160 |  |
| 2026-08-06 03:08:12 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.410 |  |
| 2026-08-06 03:04:34 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | -2.726 |  |
| 2026-08-06 03:12:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)