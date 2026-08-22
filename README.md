# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_06:34:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 06:34:27 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | -0.001 |  |
| 2026-08-22 06:11:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:09:54 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-22 06:09:06 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.060 |  |
| 2026-08-22 06:08:00 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-08-22 06:07:17 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.031 |  |
| 2026-08-22 06:07:07 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.009 |  |
| 2026-08-22 06:07:04 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:06:32 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-08-22 06:06:08 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:06:05 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:05:44 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.246 |  |
| 2026-08-22 06:05:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:05:16 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:04:51 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:04:33 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-08-22 06:04:30 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-22 06:03:40 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 06:03:02 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:03:02 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:52 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-22 06:02:40 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-08-22 06:02:31 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:18 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:09 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-22 06:02:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:07 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:01:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:01:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-22 06:01:31 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-08-22 06:01:23 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 06:00:52 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:37 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-08-22 06:00:11 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 06:02:40 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-08-22 06:02:09 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-22 06:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-22 06:01:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-22 06:01:23 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 06:09:54 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-22 06:03:40 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 06:00:11 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:06:08 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:07 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:18 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:52 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:03:02 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:52 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:05:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:00:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:05:16 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:31 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:07:04 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:11:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:02:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:03:02 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:06:05 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:01:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:04:51 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:34:27 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | -0.001 |  |
| 2026-08-22 06:07:07 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.009 |  |
| 2026-08-22 06:08:00 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-08-22 06:00:37 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-08-22 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-22 06:06:32 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-08-22 06:01:31 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-08-22 06:07:17 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.031 |  |
| 2026-08-22 06:04:33 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-08-22 06:09:06 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.060 |  |
| 2026-08-22 06:05:44 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)