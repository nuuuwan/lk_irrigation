# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_16:34:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 16:34:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:15:27 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.026 |  |
| 2026-04-05 16:12:50 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-04-05 16:12:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 16:10:17 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.054 |  |
| 2026-04-05 16:09:49 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.028 |  |
| 2026-04-05 16:08:54 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:07:24 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-04-05 16:07:21 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-05 16:07:13 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:07:09 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-05 16:06:00 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-05 16:05:49 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 16:04:55 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 16:04:45 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:04:32 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:04:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 16:04:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:03:47 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-04-05 16:03:34 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-05 16:03:31 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:03:29 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:03:18 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-05 16:02:38 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:02:20 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:02:12 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-05 16:02:10 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-05 16:02:07 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 16:01:47 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.030 |  |
| 2026-04-05 16:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 16:01:35 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.110 |  |
| 2026-04-05 16:01:25 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:24 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-05 16:01:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:12 | Thanthirimale (Malwathu Oya) | 2.58 | 🟢 Normal | -0.110 |  |
| 2026-04-05 16:01:03 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-05 16:01:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 16:03:34 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-05 16:03:18 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-05 16:02:10 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-05 16:02:07 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 16:02:12 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-05 16:07:09 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-05 16:06:00 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-05 16:05:49 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 16:04:55 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 16:01:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 16:04:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 16:12:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 16:02:38 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:34:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:03:29 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:09:49 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:02:20 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:04:45 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:04:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:04:32 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:08:54 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:07:13 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:01:25 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:03:31 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 16:12:50 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-04-05 16:07:21 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-05 16:01:24 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-05 16:01:03 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-05 16:00:14 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-05 16:03:47 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-04-05 16:15:27 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.026 |  |
| 2026-04-05 16:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.028 |  |
| 2026-04-05 16:07:24 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-04-05 16:01:47 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.030 |  |
| 2026-04-05 16:10:17 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.054 |  |
| 2026-04-05 16:01:12 | Thanthirimale (Malwathu Oya) | 2.58 | 🟢 Normal | -0.110 |  |
| 2026-04-05 16:01:35 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)