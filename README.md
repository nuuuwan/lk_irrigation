# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_14:51:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 14:51:01 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.016 |  |
| 2025-12-23 14:24:05 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-23 14:12:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.018 |  |
| 2025-12-23 14:07:59 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.096 |  |
| 2025-12-23 14:07:51 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:07:35 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.018 |  |
| 2025-12-23 14:06:31 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:56 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-23 14:05:50 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.078 |  |
| 2025-12-23 14:05:35 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:03 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:04:43 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-23 14:04:02 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:42 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:03:28 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:03:23 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2025-12-23 14:03:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:03:05 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:38 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:35 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-23 14:02:27 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.080 |  |
| 2025-12-23 14:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:01:59 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:01:15 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:01:10 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-23 14:01:10 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.023 |  |
| 2025-12-23 14:01:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-23 14:00:47 | Thanthirimale (Malwathu Oya) | 3.23 | 🟢 Normal | -0.030 |  |
| 2025-12-23 14:00:31 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:00:14 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 14:04:43 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-23 14:02:35 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-23 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-23 14:24:05 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 14:01:15 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:00:14 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:05 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:07:51 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:04:02 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:02:27 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:42 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:03 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:35 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:28 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:06:31 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:05:56 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:00:31 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:03:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:01:59 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-23 14:01:10 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-23 14:01:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-23 14:51:01 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.016 |  |
| 2025-12-23 14:12:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.018 |  |
| 2025-12-23 14:07:35 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.018 |  |
| 2025-12-23 14:01:10 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.023 |  |
| 2025-12-23 14:03:23 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2025-12-23 14:00:47 | Thanthirimale (Malwathu Oya) | 3.23 | 🟢 Normal | -0.030 |  |
| 2025-12-23 14:05:50 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.078 |  |
| 2025-12-23 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.080 |  |
| 2025-12-23 14:07:59 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)