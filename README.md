# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_16:33:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,370 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 16:33:51 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-01 16:20:21 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.008 |  |
| 2026-04-01 16:20:05 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:12:45 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:12:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-04-01 16:11:13 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-04-01 16:10:18 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-04-01 16:08:20 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:07:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-04-01 16:07:24 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 16:06:21 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-01 16:05:36 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:05:08 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:05:08 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 16:05:07 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:52 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-01 16:03:38 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:18 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-04-01 16:03:18 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 16:03:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:14 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-01 16:03:07 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-01 16:03:04 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:56 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 16:02:35 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:27 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-04-01 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 16:02:12 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:04 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:01:23 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.100 |  |
| 2026-04-01 16:01:13 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:01:07 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:00:49 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 16:00:49 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-01 16:33:51 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-01 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 16:06:21 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-01 16:03:18 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 16:02:15 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 16:07:24 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 16:05:08 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 16:02:56 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:12 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:04 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:12:45 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:05:07 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:08:20 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:35 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:01:07 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:20:05 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:05:08 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:03:38 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:01:13 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:05:36 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:04 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:20:21 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.008 |  |
| 2026-04-01 16:07:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-04-01 16:03:14 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-01 16:03:07 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-01 16:03:52 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-01 16:03:18 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-04-01 16:10:18 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-04-01 16:02:27 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-04-01 16:11:13 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-04-01 16:12:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-04-01 16:01:23 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)