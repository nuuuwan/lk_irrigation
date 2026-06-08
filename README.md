# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_03:32:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 03:32:29 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.005 |  |
| 2026-06-09 03:20:04 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.046 |  |
| 2026-06-09 03:15:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:10:29 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.018 |  |
| 2026-06-09 03:10:24 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 03:08:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-09 03:08:16 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.078 |  |
| 2026-06-09 03:08:14 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-09 03:08:01 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:07:52 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:06:31 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:06:27 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-09 03:05:40 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:05:26 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:05:11 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-09 03:04:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:15 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:03 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 03:03:56 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:43 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -2.118 |  |
| 2026-06-09 03:03:35 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.078 |  |
| 2026-06-09 03:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-06-09 03:03:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:09 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -2.118 |  |
| 2026-06-09 03:02:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:51 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:31 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 03:02:01 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:01:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 02:02:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-09 03:04:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-09 03:08:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-09 03:08:14 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-09 03:02:31 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-09 03:04:03 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 03:10:24 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 03:05:40 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:06:31 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:02:26 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:01:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:04:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:15:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:51 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:02:01 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:08:01 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:08:23 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:07:52 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:03:56 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 03:32:29 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.005 |  |
| 2026-06-09 02:03:54 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-09 03:10:29 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.018 |  |
| 2026-06-09 02:23:32 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-06-09 03:06:27 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-09 03:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-09 03:20:04 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.046 |  |
| 2026-06-09 03:08:16 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.078 |  |
| 2026-06-09 03:03:35 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.078 |  |
| 2026-06-09 00:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.084 |  |
| 2026-06-09 03:03:43 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -2.118 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)