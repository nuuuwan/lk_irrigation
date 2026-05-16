# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_21:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 21:22:58 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:12:41 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | -0.044 |  |
| 2026-05-16 21:10:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.036 |  |
| 2026-05-16 21:08:58 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:08:09 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-16 21:06:41 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.061 |  |
| 2026-05-16 21:06:22 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.158 |  |
| 2026-05-16 21:06:11 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 21:05:17 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-05-16 21:05:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:04:59 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-16 21:04:46 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:04:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 21:04:28 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:04:18 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:04:09 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-16 21:03:54 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 6.000 | 🔺 Rising |
| 2026-05-16 21:03:43 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:03:42 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-05-16 21:03:30 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | 6.000 | 🔺 Rising |
| 2026-05-16 21:03:08 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 21:03:07 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:02:49 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-16 21:02:36 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.031 |  |
| 2026-05-16 21:02:27 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:02:25 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:02:19 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:02:07 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:50 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:48 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:45 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:40 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-16 21:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-05-16 21:01:23 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 21:01:22 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:00:51 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.051 |  |
| 2026-05-16 21:00:47 | Moragaswewa (Deduru Oya) | 2.63 | 🟢 Normal | -0.115 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 21:04:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 21:12:41 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | -0.044 |  |
| 2026-05-16 21:03:54 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 6.000 | 🔺 Rising |
| 2026-05-16 21:08:09 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-16 21:04:09 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-16 21:06:11 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 21:01:23 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 21:02:49 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 21:01:40 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-16 21:03:08 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 21:02:07 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:02:27 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:50 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:04:28 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:45 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:01:48 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:05:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:08:58 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:22:58 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:03:07 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:02:25 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:04:18 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:02:19 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:03:43 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:01:22 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-05-16 21:05:17 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-05-16 21:04:59 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-16 21:03:42 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 21:02:36 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.031 |  |
| 2026-05-16 21:10:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.036 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 21:00:51 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.051 |  |
| 2026-05-16 21:06:41 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.061 |  |
| 2026-05-16 21:00:47 | Moragaswewa (Deduru Oya) | 2.63 | 🟢 Normal | -0.115 |  |
| 2026-05-16 21:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-05-16 21:06:22 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)