# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_18:17:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 18:17:46 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-26 18:16:50 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-02-26 18:08:57 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-02-26 18:08:21 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:07:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.122 |  |
| 2026-02-26 18:06:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:06:29 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 18:06:09 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:06:04 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-02-26 18:05:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:27 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 18:04:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:14 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:01 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-26 18:03:26 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:20 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:16 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:03:15 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:09 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-26 18:03:06 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-26 18:02:42 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:02:32 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 18:02:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-02-26 18:02:05 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:02 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 18:01:36 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-02-26 18:01:35 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-26 18:00:29 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:00:26 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:00:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 18:00:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 17:29:50 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 18:02:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-26 18:04:01 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-26 18:02:02 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 18:00:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 18:01:35 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-26 18:00:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 18:02:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 18:04:27 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 18:06:29 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 18:00:29 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:14 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:20 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:32 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:15 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:08:21 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:06:09 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:06:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:38 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:00:26 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:26 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:05 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:05:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:04:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:03:06 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:17:46 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-26 18:16:50 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-02-26 18:08:57 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-02-26 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:02:42 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:03:16 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-02-26 18:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-26 18:06:04 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-02-26 18:03:09 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-26 18:01:36 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-02-26 18:07:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)