# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_05:25:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 05:25:17 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.311 |  |
| 2026-10-22 05:22:26 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-22 05:18:22 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-22 05:18:11 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -20.769 |  |
| 2026-10-22 05:17:45 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -20.769 |  |
| 2026-10-22 05:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 1.331 | 🔺 Rising |
| 2026-10-22 05:12:24 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | -4.737 |  |
| 2026-10-22 05:11:46 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -4.737 |  |
| 2026-10-22 05:10:18 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-22 05:07:14 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-22 05:07:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 05:07:05 | Glencourse (Kelani Ganga) | 13.59 | 🟢 Normal | -0.009 |  |
| 2026-10-22 05:06:07 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-22 05:05:59 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 05:05:58 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-22 05:05:57 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.046 |  |
| 2026-10-22 05:04:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-10-22 05:04:05 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.091 |  |
| 2026-10-22 05:03:59 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-10-22 05:03:59 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-22 05:03:47 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 05:03:41 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-22 05:02:52 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-10-22 05:02:43 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 05:02:42 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.196 |  |
| 2026-10-22 05:02:12 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.030 |  |
| 2026-10-22 05:02:08 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.160 |  |
| 2026-10-22 05:01:36 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-22 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.082 |  |
| 2026-10-22 05:01:03 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 05:05:57 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.046 |  |
| 2026-10-22 05:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 1.331 | 🔺 Rising |
| 2026-10-22 05:02:52 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-10-22 05:03:59 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-10-22 05:03:41 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-22 05:05:58 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 05:03:47 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 05:07:14 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-22 04:06:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 05:00:33 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-22 05:06:07 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-22 05:18:22 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-22 05:02:43 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 05:05:59 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 05:22:26 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-22 04:40:43 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-22 05:07:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 05:00:27 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 05:07:05 | Glencourse (Kelani Ganga) | 13.59 | 🟢 Normal | -0.009 |  |
| 2026-10-22 05:01:36 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-22 05:03:59 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-22 03:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-10-22 03:13:14 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.028 |  |
| 2026-10-22 05:10:18 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-22 05:02:12 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:04:21 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-10-22 05:01:03 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-10-22 05:04:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-10-22 03:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.082 |  |
| 2026-10-22 05:04:05 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.091 |  |
| 2026-10-22 05:02:08 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.160 |  |
| 2026-10-22 05:02:42 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.196 |  |
| 2026-10-22 05:25:17 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.311 |  |
| 2026-10-22 05:12:24 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | -4.737 |  |
| 2026-10-22 05:18:11 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -20.769 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)