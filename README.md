# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_16:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,205 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 16:07:14 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 16:07:03 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:53 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-04 16:06:52 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:42 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.061 |  |
| 2025-12-04 16:04:54 | Weraganthota (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-04 16:04:18 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-04 16:04:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:04:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-04 16:03:30 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.060 |  |
| 2025-12-04 16:03:29 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-04 16:03:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-04 16:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:03:02 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:03:01 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:02:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:02:27 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:02:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:02:18 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-04 16:02:14 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:41 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 16:01:36 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:20 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:01:20 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:16 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.020 |  |
| 2025-12-04 16:01:15 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:01:12 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-04 16:01:09 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:01:02 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:17:32 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.061 |  |
| 2025-12-04 15:11:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.059 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 16:02:18 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-04 16:04:54 | Weraganthota (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-04 16:03:29 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-04 16:03:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-04 16:04:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-04 16:07:14 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 16:01:41 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 15:02:01 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 16:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:02:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:07:23 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:04 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:42 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:36 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:03:02 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:02:14 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:03:01 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:07:03 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:52 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:20 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:53 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-04 15:02:06 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:02:27 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:01:09 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:00:10 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:01:02 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:04:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:01:15 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:02:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:01:20 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:01:16 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.020 |  |
| 2025-12-04 16:01:12 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-04 16:04:18 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-04 15:11:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.059 |  |
| 2025-12-04 16:03:30 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.060 |  |
| 2025-12-04 16:06:42 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)