# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_03:11:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 03:11:27 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.284 |  |
| 2026-04-07 03:10:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-07 03:08:26 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.065 |  |
| 2026-04-07 03:08:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:07:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:06:27 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-07 03:06:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-04-07 03:06:09 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:05:51 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-07 03:05:36 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-07 03:05:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.182 |  |
| 2026-04-07 03:05:24 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:05:00 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:04:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-04-07 03:04:09 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:04:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-04-07 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:03:35 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:03:17 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-07 03:03:01 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:02:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 03:02:40 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-07 03:02:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:02:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:29 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-04-07 03:01:10 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-04-07 03:00:29 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.060 |  |
| 2026-04-07 02:50:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.284 |  |
| 2026-04-07 02:47:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-04-07 02:30:56 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 03:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-04-07 03:01:10 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-04-07 03:06:27 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-07 00:06:35 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-07 03:02:40 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 03:10:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-07 03:03:17 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-07 03:02:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 03:05:51 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-07 03:01:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:02:36 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:06:09 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:02:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:03:01 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:02:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:07:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:04:09 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:01:29 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:05:24 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:05:36 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-07 03:04:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-07 03:04:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-04-07 02:08:07 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-04-07 03:05:00 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:08:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-07 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-07 03:06:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-04-07 03:00:29 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.060 |  |
| 2026-04-07 03:08:26 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.065 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-07 03:05:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.182 |  |
| 2026-04-07 03:11:27 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.284 |  |
| 2026-04-07 01:12:04 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)