# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_16:10:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 16:10:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-05 16:10:26 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:09:05 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:06:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2026-01-05 16:06:35 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:05:58 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 16:05:53 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:05:50 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:05:47 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-05 16:05:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:04:13 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 16:04:11 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:03:27 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:03:15 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:02:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-01-05 16:02:41 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:40 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:36 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:29 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:27 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:02:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 16:02:17 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-01-05 16:02:08 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:01:46 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 16:01:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:01:18 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:01:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:01:10 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:00:55 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:00:33 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:00:10 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:13:24 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:13:12 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 16:10:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-05 15:08:10 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-05 16:02:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 16:05:47 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-05 16:04:13 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 16:01:46 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 16:05:58 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 16:02:27 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:03:15 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:08:56 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:04:11 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:01:18 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:03:27 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 16:02:40 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:00:10 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:10:26 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:00:33 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:01:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:17 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:09:05 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:06:35 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:19 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:36 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:05:53 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:08 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:01:10 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:29 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:02:41 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:05:50 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:01:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:05:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:13:12 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-05 16:00:55 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:02:16 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-01-05 16:02:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-01-05 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-01-05 16:06:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2026-01-05 15:08:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)