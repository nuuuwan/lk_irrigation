# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_03:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 03:13:09 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-04-24 03:11:44 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 03:07:59 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-24 03:07:32 | Katharagama (Menik Ganga) | 1.79 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-24 03:07:30 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.046 |  |
| 2026-04-24 03:06:59 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-04-24 03:06:53 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.027 |  |
| 2026-04-24 03:06:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 03:05:45 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 03:05:07 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:04:27 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-04-24 03:04:24 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 03:04:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:04:00 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-24 03:03:35 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-24 03:03:14 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.109 |  |
| 2026-04-24 03:03:02 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-24 03:03:00 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-24 03:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-04-24 03:02:35 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-04-24 03:02:26 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-24 03:02:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:02:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:01:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 03:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:00:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.151 |  |
| 2026-04-24 03:00:27 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-04-24 02:59:33 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 03:07:59 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-24 03:07:32 | Katharagama (Menik Ganga) | 1.79 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-24 03:04:00 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-24 01:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-24 03:03:35 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-24 02:04:52 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 02:25:54 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-24 03:04:24 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 03:06:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 03:01:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 03:03:00 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-24 03:05:45 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 03:11:44 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:05:07 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:17:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:02:02 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:02:56 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:04:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:02:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 03:03:02 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 03:04:27 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-04-24 03:02:35 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-04-24 03:13:09 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-04-24 03:02:26 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-24 02:05:55 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-04-24 03:00:27 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-04-24 03:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-04-24 02:01:08 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.026 |  |
| 2026-04-24 03:06:53 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.027 |  |
| 2026-04-24 02:04:16 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-04-24 03:07:30 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.046 |  |
| 2026-04-24 03:06:59 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-04-24 02:03:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.090 |  |
| 2026-04-24 03:03:14 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.109 |  |
| 2026-04-24 03:00:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)