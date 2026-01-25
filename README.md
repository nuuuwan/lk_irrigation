# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_05:23:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 05:23:21 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-25 05:22:35 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-25 05:19:38 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:16:51 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-25 05:11:11 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-25 05:10:33 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:10:10 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-25 05:08:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:06:48 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:05:49 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-25 05:05:47 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:04:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 05:03:59 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:03:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:03:40 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:59 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:58 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 05:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:24 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:14 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2026-01-25 05:01:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-25 05:01:51 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.108 |  |
| 2026-01-25 05:01:42 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -36.000 |  |
| 2026-01-25 05:01:41 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -36.000 |  |
| 2026-01-25 05:01:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:27 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 05:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-25 05:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 05:01:01 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.025 |  |
| 2026-01-25 05:01:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:50:50 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:45:20 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.639 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 05:02:14 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2026-01-25 05:01:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-25 05:22:35 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-25 05:11:11 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-25 04:01:55 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-25 05:01:27 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 05:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-25 05:04:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 05:10:10 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-25 05:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 05:16:51 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-25 05:23:21 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-24 23:03:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:51 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:24 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:03:40 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:05:47 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:03:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:06:48 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:33 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:59 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:02:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:03:59 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:19:38 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:08:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:10:33 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:10:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 05:02:58 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 05:05:49 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-25 05:01:01 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.025 |  |
| 2026-01-25 05:01:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.108 |  |
| 2026-01-25 05:01:42 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)