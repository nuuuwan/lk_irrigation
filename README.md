# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_10:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,950 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 10:29:48 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-08-31 10:21:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:16:29 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.008 |  |
| 2026-08-31 10:09:04 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:09:02 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:08:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-08-31 10:08:05 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:07:31 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.022 |  |
| 2026-08-31 10:07:05 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:49 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.032 |  |
| 2026-08-31 10:06:33 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:17 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:05:48 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 10:05:42 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:05:39 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-31 10:04:58 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:04:30 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.157 |  |
| 2026-08-31 10:03:59 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 10:03:32 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:03:24 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:12 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:04 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:02:58 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.090 |  |
| 2026-08-31 10:02:52 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.060 |  |
| 2026-08-31 10:02:37 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:01:45 | Manampitiya (Mahaweli Ganga) | -0.51 | 🟢 Normal | -0.020 |  |
| 2026-08-31 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:01:21 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:01:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.049 |  |
| 2026-08-31 10:01:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:00:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:16 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:12 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 10:05:39 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-31 10:05:48 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 10:03:59 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 10:00:16 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:21:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:09:02 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:01:21 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:09:04 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:12 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:24 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:01:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:04:58 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:03:04 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:17 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:04:30 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:06:33 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:08:05 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:25 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:05:42 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:00:12 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:07:05 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:16:29 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.008 |  |
| 2026-08-31 10:02:37 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:03:32 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-31 10:01:45 | Manampitiya (Mahaweli Ganga) | -0.51 | 🟢 Normal | -0.020 |  |
| 2026-08-31 10:29:48 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-08-31 10:07:31 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.022 |  |
| 2026-08-31 10:06:49 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.032 |  |
| 2026-08-31 10:01:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.049 |  |
| 2026-08-31 10:02:52 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.060 |  |
| 2026-08-31 10:02:58 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.090 |  |
| 2026-08-31 10:08:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-08-31 10:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)