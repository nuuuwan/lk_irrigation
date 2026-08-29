# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_19:22:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,506 measurements** from **39** stations.
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
| 2026-08-29 19:22:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-29 19:17:09 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:16:43 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-08-29 19:14:18 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.017 |  |
| 2026-08-29 19:13:35 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:11:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.026 |  |
| 2026-08-29 19:09:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:08:50 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:08:13 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:07:55 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-29 19:07:19 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:06:56 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:06:07 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:05:54 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:05:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:24 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:19 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:04:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:03:52 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:03:45 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 19:03:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.089 |  |
| 2026-08-29 19:03:23 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:03:18 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-29 19:03:14 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:02:51 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:18 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:11 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-08-29 19:02:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:04 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:01:58 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-08-29 19:01:12 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-29 19:01:05 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:00:54 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:00:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 19:03:18 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-29 19:03:45 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 19:07:55 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-29 19:04:19 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:05:54 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:06:07 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 19:22:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-29 19:00:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:04 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:13:35 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:00:54 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:51 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:09:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:02:18 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:07:19 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:24 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:05:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:04:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:08:13 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:17:09 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:08:50 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:03:23 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:06:56 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 19:16:43 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-08-29 19:03:14 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:03:52 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:01:05 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-29 19:01:12 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-29 19:14:18 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.017 |  |
| 2026-08-29 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-08-29 19:11:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.026 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-29 19:02:11 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-08-29 19:03:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)