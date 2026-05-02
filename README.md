# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_03:31:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 03:31:38 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-03 03:16:02 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-03 03:13:42 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-05-03 03:12:52 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 03:09:41 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 1.791 | 🔺 Rising |
| 2026-05-03 03:08:48 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:06:20 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 1.791 | 🔺 Rising |
| 2026-05-03 03:05:25 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-03 03:05:21 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:05:21 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-03 03:05:07 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:05:02 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:04:35 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 03:04:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-03 03:03:57 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:03:11 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-05-03 03:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-03 03:02:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-03 03:02:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:13 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:03 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:57 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:50 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:44 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 03:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-03 03:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-03 03:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:08 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:00:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.148 |  |
| 2026-05-03 03:00:43 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.277 |  |
| 2026-05-03 03:00:33 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-03 02:55:36 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 02:49:01 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 02:40:59 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 03:09:41 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 1.791 | 🔺 Rising |
| 2026-05-03 03:31:38 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-03 03:05:25 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-03 03:16:02 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-03 02:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-03 03:12:52 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 03:04:35 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 03:04:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-03 02:22:25 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-03 02:07:04 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 03:05:21 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-03 03:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-03 03:03:57 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:08 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:57 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:03 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:08:48 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-03 02:49:01 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:01:50 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:05:02 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:02:13 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:05:21 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 03:03:11 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-05-03 03:13:42 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-03 03:00:33 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-03 03:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-03 03:02:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-03 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-03 02:40:59 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.025 |  |
| 2026-05-03 00:02:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-05-03 03:00:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.148 |  |
| 2026-05-03 03:00:43 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.277 |  |
| 2026-05-03 00:18:31 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)