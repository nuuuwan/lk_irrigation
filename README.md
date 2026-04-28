# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_16:25:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,459 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 16:25:07 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.024 |  |
| 2026-04-28 16:16:35 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-04-28 16:15:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:14:51 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-04-28 16:12:02 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.754 | 🔺 Rising |
| 2026-04-28 16:09:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-04-28 16:08:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:07:11 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-04-28 16:06:53 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-28 16:06:42 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:06:20 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-04-28 16:05:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-04-28 16:04:38 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-28 16:04:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.042 |  |
| 2026-04-28 16:04:37 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:04:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:04:27 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-04-28 16:04:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:04:03 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:03:52 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:34 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.070 |  |
| 2026-04-28 16:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:20 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.049 |  |
| 2026-04-28 16:03:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-28 16:02:59 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.005 |  |
| 2026-04-28 16:02:51 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 16:02:46 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:02:25 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:02:24 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:02:22 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 16:01:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:01:40 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:01:35 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 16:01:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:00:57 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 16:12:02 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.754 | 🔺 Rising |
| 2026-04-28 16:09:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-04-28 16:02:51 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 16:01:35 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 16:02:22 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 16:04:38 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-28 16:06:53 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-28 16:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:01:40 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:08:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:00:57 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:02:25 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:01:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:02:46 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:04:03 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:52 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:04:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:15:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:03:34 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-28 16:02:59 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.005 |  |
| 2026-04-28 16:14:51 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-04-28 16:04:37 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:04:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:01:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:02:24 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:06:42 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:03:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 16:16:35 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-04-28 16:06:20 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-04-28 16:07:11 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-04-28 16:03:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-28 16:25:07 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.024 |  |
| 2026-04-28 15:02:30 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-04-28 16:04:27 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-04-28 16:04:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.042 |  |
| 2026-04-28 16:03:20 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.049 |  |
| 2026-04-28 16:03:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.070 |  |
| 2026-04-28 16:05:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)