# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_21:09:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,022 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 21:09:41 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.030 |  |
| 2026-08-19 21:08:45 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:08:32 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:07:39 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:06:32 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:06:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.005 |  |
| 2026-08-19 21:05:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-19 21:05:29 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:04:24 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:04:24 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-08-19 21:04:08 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.197 |  |
| 2026-08-19 21:03:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:47 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 21:03:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:03:25 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-08-19 21:03:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:17 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:02:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:02:51 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:02:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-08-19 21:02:30 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.012 |  |
| 2026-08-19 21:02:06 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:01:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:42 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:33 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:01:31 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:14 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-08-19 21:00:16 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:00:12 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-19 20:28:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.179 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 21:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-19 21:01:14 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:03:17 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:02:06 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 21:03:47 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 21:06:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.005 |  |
| 2026-08-19 21:00:12 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:02:51 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:31 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:08:32 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:52 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:04:24 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:02:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:29 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:07:39 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:00:16 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:30 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:01:42 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:08:45 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:03:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:06:32 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:01:33 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.010 |  |
| 2026-08-19 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-19 21:02:30 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.012 |  |
| 2026-08-19 21:09:41 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.030 |  |
| 2026-08-19 20:03:58 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-08-19 21:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-08-19 21:03:25 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-08-19 20:08:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.035 |  |
| 2026-08-19 21:04:24 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-08-19 21:02:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-08-19 21:04:08 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)