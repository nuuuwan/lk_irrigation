# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_14:12:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Moraketiya — Major Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 14:12:54 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:11:12 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-14 14:09:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.100 |  |
| 2026-08-14 14:08:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:07:43 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:07:28 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-08-14 14:07:15 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.011 |  |
| 2026-08-14 14:07:03 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:06:15 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:05:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:05:38 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:04:44 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:04:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-14 14:03:15 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:03:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:03:10 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-08-14 14:03:06 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-14 14:03:02 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.030 |  |
| 2026-08-14 14:02:52 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-14 14:02:48 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:47 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:44 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.050 |  |
| 2026-08-14 14:02:24 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:19 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:16 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-08-14 14:02:14 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:08 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.029 |  |
| 2026-08-14 14:02:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:01:46 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-08-14 14:01:35 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-14 14:01:22 | Moraketiya (Walawe Ganga) | 8.62 | 🔴 Major Flood | 8.170 | 🔺 Rising |
| 2026-08-14 14:00:54 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:42 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 14:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 14:01:22 | Moraketiya (Walawe Ganga) | 8.62 | 🔴 Major Flood | 8.170 | 🔺 Rising |
| 2026-08-14 14:04:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-14 14:01:35 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-14 14:03:06 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-14 14:11:12 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-14 14:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 14:02:44 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:14 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:54 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:03:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:06:15 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:05:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:24 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:07:43 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:12:54 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-14 13:02:46 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:07:03 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:48 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 13:03:26 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:19 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:08:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:00:42 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 13:13:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:05:38 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:02:47 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:04:44 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 14:01:46 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-08-14 14:02:52 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-14 14:07:15 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.011 |  |
| 2026-08-14 14:03:10 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-08-14 14:02:16 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-08-14 14:07:28 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-08-14 14:02:08 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.029 |  |
| 2026-08-14 14:03:02 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.030 |  |
| 2026-08-14 14:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.050 |  |
| 2026-08-14 14:09:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)