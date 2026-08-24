# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_10:10:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,094 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 10:10:57 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.017 |  |
| 2026-08-24 10:09:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-24 10:08:13 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 10:07:29 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.009 |  |
| 2026-08-24 10:06:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-24 10:05:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:05:09 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:44 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:35 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-08-24 10:04:30 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:03 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:00 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:28 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.079 |  |
| 2026-08-24 10:02:54 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:54 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.395 |  |
| 2026-08-24 10:02:45 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:43 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.065 |  |
| 2026-08-24 10:02:28 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:26 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-24 10:02:18 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.020 |  |
| 2026-08-24 10:02:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:07 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:45 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:45 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-24 10:01:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:22 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:16 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.042 |  |
| 2026-08-24 10:00:55 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:00:52 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.042 |  |
| 2026-08-24 10:00:15 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-24 10:00:10 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-24 09:59:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 10:09:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-24 10:01:45 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-24 10:06:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-24 10:08:13 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 10:02:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-24 10:03:28 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:00:52 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:45 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:26 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:45 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:44 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:03 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:05:09 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:28 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:01:22 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:00:55 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:00 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:54 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:05:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:03:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:04:30 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:02:07 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 10:07:29 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.009 |  |
| 2026-08-24 10:00:15 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-24 09:59:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-08-24 10:10:57 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.017 |  |
| 2026-08-24 10:02:18 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.020 |  |
| 2026-08-24 10:04:35 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-08-24 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.042 |  |
| 2026-08-24 10:01:16 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.042 |  |
| 2026-08-24 10:02:43 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.065 |  |
| 2026-08-24 10:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.079 |  |
| 2026-08-24 10:02:54 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.395 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)