# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_11:20:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 11:20:21 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:13:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:12:20 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-07 11:11:53 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:10:42 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:09:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:46 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:43 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:39 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-07 11:08:16 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-08-07 11:08:12 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:09 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:07:29 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-07 11:07:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-07 11:07:16 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.029 |  |
| 2026-08-07 11:07:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:06:42 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:06:15 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:53 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:08 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 11:05:00 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-07 11:04:19 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-08-07 11:03:52 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:03:43 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.100 |  |
| 2026-08-07 11:03:03 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:02:56 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-07 11:02:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-07 11:02:30 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:02:09 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-07 11:01:46 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.031 |  |
| 2026-08-07 11:01:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:01:17 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 11:01:15 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-08-07 11:01:10 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-07 11:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-08-07 11:00:41 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:00:34 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-07 11:00:24 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:57:02 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 11:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-07 11:08:39 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-07 11:00:34 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-07 11:07:29 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-07 11:02:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-07 11:01:17 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 11:05:08 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 11:12:20 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-07 11:08:46 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:00:24 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:01:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:20:21 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:13:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:10:42 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:53 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:06:42 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:03:52 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:02:30 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:11:53 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:03:03 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:06:15 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:43 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:08:09 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:05:00 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:09:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:07:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:25:19 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-07 11:01:10 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-07 11:02:09 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-07 11:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-08-07 11:02:56 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-07 11:04:19 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-08-07 11:01:15 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-08-07 11:08:16 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-08-07 11:07:16 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.029 |  |
| 2026-08-07 11:01:46 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.031 |  |
| 2026-08-07 11:07:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-07 11:03:43 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)