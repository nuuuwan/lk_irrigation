# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_11:23:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 11:23:13 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.054 |  |
| 2026-04-24 11:21:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:14:57 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 11:13:12 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:07:26 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.118 |  |
| 2026-04-24 11:07:22 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:07:21 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:06:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-04-24 11:06:53 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.074 |  |
| 2026-04-24 11:06:45 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-24 11:06:20 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 11:06:18 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-04-24 11:05:35 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.068 |  |
| 2026-04-24 11:05:22 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-04-24 11:05:07 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:04:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:04:46 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.078 |  |
| 2026-04-24 11:03:50 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-24 11:03:46 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:03:25 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:03:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:03:12 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.050 |  |
| 2026-04-24 11:02:50 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:50 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:02:45 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:02:23 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:02:15 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:02:07 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.018 |  |
| 2026-04-24 11:01:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.067 |  |
| 2026-04-24 11:01:42 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:01:25 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | -0.022 |  |
| 2026-04-24 11:01:16 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:01:06 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:01:05 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:01:02 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:00:55 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-24 11:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:00:31 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 11:06:18 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-04-24 11:06:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-04-24 11:06:45 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-24 11:03:50 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-24 11:06:20 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 11:00:55 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-24 11:14:57 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 11:02:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:21:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:02:15 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:02:23 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:00:31 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:03:25 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:01:42 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:07:21 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:03:46 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 11:03:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:13:12 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:50 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:50 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:03:12 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:01:16 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 11:02:07 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.018 |  |
| 2026-04-24 11:07:22 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:01:02 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:02:45 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-04-24 11:01:25 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | -0.022 |  |
| 2026-04-24 11:04:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:05:07 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:01:06 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-24 11:05:22 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-04-24 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.050 |  |
| 2026-04-24 11:23:13 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.054 |  |
| 2026-04-24 11:01:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.067 |  |
| 2026-04-24 11:05:35 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.068 |  |
| 2026-04-24 11:06:53 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.074 |  |
| 2026-04-24 11:04:46 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.078 |  |
| 2026-04-24 11:07:26 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)