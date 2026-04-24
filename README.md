# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_16:23:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:13:58 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.027 |  |
| 2026-04-24 16:10:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-04-24 16:07:21 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:07:01 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-04-24 16:06:45 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:05:30 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:05:04 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 16:05:04 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.024 |  |
| 2026-04-24 16:04:57 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:04:53 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-04-24 16:04:40 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 16:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:04:08 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:03:34 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 16:03:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:03:19 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 16:03:11 | Katharagama (Menik Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-04-24 16:03:10 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-24 16:03:07 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.023 |  |
| 2026-04-24 16:02:57 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:56 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:43 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-24 16:02:31 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:02:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-04-24 16:02:20 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.040 |  |
| 2026-04-24 16:02:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:02:09 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:01:59 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:01:41 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 16:01:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 16:01:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-04-24 16:01:03 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 16:00:51 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:00:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 16:02:43 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-24 16:03:10 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-24 16:04:40 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 16:05:04 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 16:01:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 16:01:03 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 15:07:55 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 16:03:34 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 16:00:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 16:01:41 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 16:03:19 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 16:03:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:31 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:56 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:04:08 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:00:51 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:57 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:08 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:02:20 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:05:30 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:06:45 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:02:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:02:31 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:04:57 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:02:09 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:07:21 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:01:59 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-24 16:07:01 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-04-24 16:03:11 | Katharagama (Menik Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-04-24 16:03:07 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.023 |  |
| 2026-04-24 16:05:04 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.024 |  |
| 2026-04-24 16:13:58 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.027 |  |
| 2026-04-24 16:10:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-04-24 16:01:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-04-24 16:04:53 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-04-24 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.040 |  |
| 2026-04-24 16:02:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)