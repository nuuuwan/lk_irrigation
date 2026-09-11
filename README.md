# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_08:10:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **257,784 measurements** from **39** stations.
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
| 2026-09-11 08:10:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:09:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:09:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-09-11 08:07:51 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-09-11 08:07:45 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:07:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:07:15 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.052 |  |
| 2026-09-11 08:07:14 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 08:06:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.114 |  |
| 2026-09-11 08:05:47 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:04:45 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:04:43 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.202 |  |
| 2026-09-11 08:04:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:56 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:03:36 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:22 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:20 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.049 |  |
| 2026-09-11 08:03:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:06 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.025 |  |
| 2026-09-11 08:02:52 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:46 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:45 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-09-11 08:02:43 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:02:36 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-09-11 08:02:35 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.056 |  |
| 2026-09-11 08:02:14 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-11 08:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:01:26 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-11 08:00:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:52 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:35 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:26 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-11 08:00:22 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:40:49 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 08:07:51 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-09-11 08:00:26 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-11 08:01:26 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-11 08:07:14 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 08:00:22 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:36 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:46 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:10:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:09:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:10:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:52 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:22 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:07:45 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:04:45 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:03:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:05:47 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:02:35 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:52 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:04:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:00:35 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:07:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 08:09:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-09-11 07:10:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-09-11 08:03:56 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:03:20 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:02:43 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-11 08:02:14 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-11 08:03:06 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.025 |  |
| 2026-09-11 08:02:36 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-09-11 08:02:45 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-09-11 07:40:49 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-09-11 08:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.049 |  |
| 2026-09-11 08:07:15 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.052 |  |
| 2026-09-11 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.056 |  |
| 2026-09-11 08:06:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.114 |  |
| 2026-09-11 08:04:43 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)