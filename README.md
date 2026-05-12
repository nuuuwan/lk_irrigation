# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_11:12:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 11:12:40 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.026 |  |
| 2026-05-12 11:11:07 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-12 11:09:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.021 |  |
| 2026-05-12 11:08:38 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:08:02 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:07:56 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:07:30 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:06:32 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-05-12 11:05:46 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:05:02 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-05-12 11:05:01 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 11:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:04:40 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:04:28 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-05-12 11:04:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.013 |  |
| 2026-05-12 11:04:05 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.090 |  |
| 2026-05-12 11:03:54 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 11:03:44 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:03:39 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 11:03:26 | Katharagama (Menik Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-05-12 11:03:12 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.062 |  |
| 2026-05-12 11:02:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-12 11:02:47 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-05-12 11:02:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:02:31 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-05-12 11:02:28 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:02:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.081 |  |
| 2026-05-12 11:02:07 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 11:01:42 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:01:24 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 11:01:20 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-12 11:01:20 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:01:18 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:01:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:01:08 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:00:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 11:00:14 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:00:07 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.102 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 11:02:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-12 11:01:20 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-12 11:11:07 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-12 11:05:01 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 11:03:54 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 11:00:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 11:01:24 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 11:02:07 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 11:03:39 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 11:01:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:07:56 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:01:42 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:07:30 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:08:38 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:08:02 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:02:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:02:28 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 11:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:03:44 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:01:08 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:00:14 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:04:40 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-12 11:04:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.013 |  |
| 2026-05-12 10:20:24 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.017 |  |
| 2026-05-12 11:01:20 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:01:18 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:05:46 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-05-12 11:09:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.021 |  |
| 2026-05-12 11:12:40 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.026 |  |
| 2026-05-12 11:03:26 | Katharagama (Menik Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-05-12 11:02:47 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-05-12 11:04:28 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-05-12 11:05:02 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-05-12 11:06:32 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-05-12 11:02:31 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-05-12 11:03:12 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.062 |  |
| 2026-05-12 11:02:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.081 |  |
| 2026-05-12 11:04:05 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.090 |  |
| 2026-05-12 11:00:07 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)