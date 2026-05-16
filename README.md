# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_00:35:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 00:35:48 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:17:53 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -54.000 |  |
| 2026-05-17 00:17:51 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -54.000 |  |
| 2026-05-17 00:17:49 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -54.000 |  |
| 2026-05-17 00:13:59 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:13:22 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -108.000 |  |
| 2026-05-17 00:13:20 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -108.000 |  |
| 2026-05-17 00:09:21 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.019 |  |
| 2026-05-17 00:08:36 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.057 |  |
| 2026-05-17 00:07:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-05-17 00:05:50 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:05:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-17 00:05:04 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:54 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:43 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:31 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:26 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:03:58 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 00:03:43 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.022 |  |
| 2026-05-17 00:03:41 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:03:34 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:03:18 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:02:54 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-05-17 00:02:38 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:02:17 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.051 |  |
| 2026-05-17 00:02:05 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:01:57 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.005 |  |
| 2026-05-17 00:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 00:01:51 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:01:49 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.020 |  |
| 2026-05-17 00:01:43 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:01:38 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-17 00:01:13 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:01:05 | Magura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.055 |  |
| 2026-05-17 00:00:19 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 00:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 00:01:49 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.020 |  |
| 2026-05-17 00:05:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-17 00:01:38 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 00:03:58 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 00:05:50 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:02:05 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:05:04 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:31 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:26 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:01:13 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:35:48 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:54 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:43 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:13:59 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:03:34 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:02:38 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:02:54 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:01:57 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.005 |  |
| 2026-05-17 00:03:41 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:01:51 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:01:43 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:03:18 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:00:19 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-05-17 00:09:21 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.019 |  |
| 2026-05-17 00:03:43 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.022 |  |
| 2026-05-17 00:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-05-17 00:07:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 00:02:17 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.051 |  |
| 2026-05-17 00:01:05 | Magura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.055 |  |
| 2026-05-17 00:08:36 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.057 |  |
| 2026-05-17 00:17:53 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -54.000 |  |
| 2026-05-17 00:13:22 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)