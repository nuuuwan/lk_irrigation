# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_11:40:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,178 measurements** from **39** stations.
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
| 2026-08-14 11:40:46 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-14 11:12:06 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-14 11:10:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:10:37 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-08-14 11:09:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:09:25 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:08:30 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 11:07:10 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:05:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:05:55 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:35 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:26 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:05:24 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:05:15 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.029 |  |
| 2026-08-14 11:04:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:04:53 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:04:47 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:04:42 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:04:38 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.050 |  |
| 2026-08-14 11:04:22 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:04:11 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-08-14 11:04:06 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:03:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.100 |  |
| 2026-08-14 11:02:48 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-08-14 11:02:44 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:02:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-14 11:02:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:02:21 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:01:40 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-14 11:01:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:01:02 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:00:32 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:00:08 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 11:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-14 11:01:40 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-14 11:12:06 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-14 11:00:32 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:04:06 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:04:53 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 11:05:26 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:04:47 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:07:10 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 11:08:30 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 11:40:46 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-14 11:02:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:02:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:04:42 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:04:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:01:02 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:02:44 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:05:24 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:05:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:09:25 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:09:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 10:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-08-14 11:04:11 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-08-14 11:10:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:15 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:04:22 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:55 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:02:21 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:01:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:05:35 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-14 11:00:08 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-08-14 11:02:48 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-08-14 11:10:37 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-08-14 11:05:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.029 |  |
| 2026-08-14 11:04:38 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.050 |  |
| 2026-08-14 11:03:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)