# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_08:30:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 08:30:27 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:29:55 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:24:35 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.014 |  |
| 2026-01-08 08:23:56 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-01-08 08:19:38 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:18:06 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.068 |  |
| 2026-01-08 08:16:49 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:14:12 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.017 |  |
| 2026-01-08 08:13:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:12:36 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 08:11:45 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:09:41 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:08:24 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:08:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:08:13 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-01-08 08:06:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:06:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 08:06:00 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:05:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.244 |  |
| 2026-01-08 08:04:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 08:04:25 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:23 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:18 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-01-08 08:03:52 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-08 08:03:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-08 08:03:44 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-01-08 08:03:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-08 08:03:25 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:46 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:02:46 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.120 |  |
| 2026-01-08 08:02:36 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 08:02:26 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:10 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-01-08 08:00:55 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-01-08 08:00:40 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-01-08 07:55:15 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.244 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 08:00:40 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-01-08 08:03:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-08 08:04:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 08:03:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-08 08:03:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-08 08:02:36 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 08:06:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 08:12:36 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 08:13:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:26 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:25 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:30:27 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:06:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:16:49 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:11:45 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:52 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:25 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:23 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:19:38 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:29:55 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:08:24 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:09:41 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:06:00 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:08:13 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:02:46 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:04:18 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:00:55 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-01-08 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-01-08 08:24:35 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.014 |  |
| 2026-01-08 08:14:12 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.017 |  |
| 2026-01-08 08:03:44 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-01-08 08:23:56 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-01-08 08:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-01-08 08:18:06 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.068 |  |
| 2026-01-08 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-01-08 08:02:46 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.120 |  |
| 2026-01-08 08:05:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)