# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_18:09:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 18:09:47 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:09:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:08:38 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:07:58 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:07:34 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:07:17 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-23 18:05:12 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 18:05:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2025-12-23 18:04:57 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:04:32 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:04:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2025-12-23 18:04:09 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2025-12-23 18:03:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:21 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2025-12-23 18:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:04 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 18:03:02 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2025-12-23 18:02:16 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2025-12-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.052 |  |
| 2025-12-23 18:02:12 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2025-12-23 18:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:08 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:56 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-23 18:01:49 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:28 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:24 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:32 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:11 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.065 |  |
| 2025-12-23 18:00:09 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 18:04:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2025-12-23 16:58:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-23 18:03:04 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 18:05:12 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 18:00:32 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:08 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:21 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:49 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:24 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:07:58 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:04:32 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:08:38 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:03:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:01:28 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:09:47 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:09:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:04:57 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:03:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:00:09 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:07:34 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:02 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-23 18:07:17 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-23 18:00:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-23 18:01:56 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-23 18:05:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2025-12-23 18:02:16 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2025-12-23 18:04:09 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2025-12-23 18:02:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2025-12-23 18:03:15 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2025-12-23 18:02:12 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2025-12-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.052 |  |
| 2025-12-23 18:00:11 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)