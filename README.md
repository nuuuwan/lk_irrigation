# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_10:30:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,863 measurements** from **39** stations.
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
| 2026-10-01 10:30:27 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:24:23 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:24:19 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.008 |  |
| 2026-10-01 10:21:53 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-10-01 10:15:25 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-10-01 10:12:40 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.026 |  |
| 2026-10-01 10:08:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:07:28 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:07:16 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:07:09 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:06:01 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.019 |  |
| 2026-10-01 10:05:49 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:05:31 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-10-01 10:05:29 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:05:27 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:05:17 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.105 |  |
| 2026-10-01 10:05:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:04:55 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:04:45 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 10:04:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:03:50 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:03:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:03:12 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:02:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:46 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:36 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.121 |  |
| 2026-10-01 10:02:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:20 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:02:08 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:01:59 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:01:44 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:01:23 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.041 |  |
| 2026-10-01 10:01:09 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 10:01:01 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:00:58 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:00:57 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.100 |  |
| 2026-10-01 10:00:39 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 07:05:47 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-01 10:04:45 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 10:01:09 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 10:01:23 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:00:39 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:04:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:08 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:46 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:24:23 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:07:28 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:30:27 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:07:16 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:03:50 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:24:19 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.008 |  |
| 2026-10-01 10:15:25 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-10-01 10:01:44 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:05:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:03:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:00:58 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:05:27 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:08:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:05:49 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:04:55 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:06:01 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.019 |  |
| 2026-10-01 10:02:20 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:03:12 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:01:59 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:01:01 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-01 10:12:40 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.026 |  |
| 2026-10-01 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.041 |  |
| 2026-10-01 10:21:53 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-10-01 10:05:31 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-10-01 10:00:57 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.100 |  |
| 2026-10-01 10:05:17 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.105 |  |
| 2026-10-01 10:02:36 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)