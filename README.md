# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_00:15:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 00:15:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-30 00:12:17 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.027 |  |
| 2026-08-30 00:08:54 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 00:08:48 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.018 |  |
| 2026-08-30 00:08:48 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:08:00 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:07:54 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:06:56 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-08-30 00:05:42 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-30 00:05:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:05:20 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:05:07 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-08-30 00:05:02 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.108 |  |
| 2026-08-30 00:04:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:04:31 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-08-30 00:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-08-30 00:03:58 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:03:44 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.099 |  |
| 2026-08-30 00:03:27 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:46 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:37 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-30 00:02:34 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:31 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 00:02:26 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:15 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:06 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:01:49 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-08-30 00:01:44 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:01:39 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-08-30 00:01:22 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:01:16 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 00:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-08-30 00:05:42 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-30 00:02:37 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-30 00:02:31 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 00:08:54 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-30 00:05:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:03:58 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:01:22 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:05:20 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:00:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:15:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:04:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:46 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:26 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:34 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:08:00 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:01:44 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:08:48 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:29 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 00:03:27 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:15 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:06 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:07:54 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-30 00:04:31 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-08-30 00:01:49 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-08-30 00:08:48 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.018 |  |
| 2026-08-30 00:06:56 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-08-30 00:05:07 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-08-30 00:12:17 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.027 |  |
| 2026-08-30 00:01:39 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-30 00:03:44 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.099 |  |
| 2026-08-30 00:05:02 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)