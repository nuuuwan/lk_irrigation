# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_00:21:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,983 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 00:21:50 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-02-02 00:12:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:10:58 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.017 |  |
| 2026-02-02 00:10:45 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:10:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:54 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 00:07:38 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:22 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:06:59 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:06:20 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:05:52 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-02 00:05:17 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-02-02 00:05:07 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 00:04:56 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-02 00:04:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-02-02 00:04:06 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:58 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 00:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-02 00:03:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-02 00:03:40 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 00:03:39 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:39 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:32 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-02-02 00:03:08 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 00:02:57 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-02 00:02:35 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 00:02:28 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:02:27 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:01:28 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 00:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:00:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:00:12 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 23:23:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-02 00:01:28 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 00:03:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-02 00:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-02 00:07:54 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 00:03:08 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 00:02:35 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 00:03:40 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 00:05:07 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 00:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:04:06 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:00:12 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:38 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:06:59 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:02:28 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:12:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:39 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:10:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:22 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:06:20 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:00:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:39 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:02:57 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:03:42 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-02 00:05:52 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-02 00:03:32 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-02-01 23:47:08 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-02-02 00:10:58 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.017 |  |
| 2026-02-02 00:04:56 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-02 00:03:58 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 00:05:17 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-02-02 00:04:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-02-02 00:21:50 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)