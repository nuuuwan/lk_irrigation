# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_19:30:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,491 measurements** from **39** stations.
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
| 2026-08-14 19:30:16 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:28:02 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:20:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.008 |  |
| 2026-08-14 19:17:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:11:40 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:11:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:09:40 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:08:03 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:07:57 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-14 19:07:50 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:07:42 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-14 19:05:50 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:05:23 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:05:03 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:04:29 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.058 |  |
| 2026-08-14 19:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 19:03:38 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:03:14 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:59 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:57 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:57 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-08-14 19:02:54 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-08-14 19:02:41 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:25 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:02:05 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:01 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-14 19:01:48 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 19:01:42 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:01:41 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:01:28 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.124 |  |
| 2026-08-14 19:00:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:00:45 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-14 19:00:24 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:00:09 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.187 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 19:00:09 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-08-14 19:07:42 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-14 19:07:57 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-14 19:02:01 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-14 19:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 19:01:48 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 19:01:28 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:01:42 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:03:38 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:00:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:03:14 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:30:16 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:01:41 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:28:02 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:41 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:05:50 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:05:03 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:05:23 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:07:50 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:11:40 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:17:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:11:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:59 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:02:57 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 19:20:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.008 |  |
| 2026-08-14 19:02:25 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:09:40 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:00:24 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:02:05 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 19:00:45 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-14 19:02:54 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-14 19:04:29 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.058 |  |
| 2026-08-14 19:02:57 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-08-14 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)