# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_16:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 16:14:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:12:36 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-10 16:10:43 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2025-12-10 16:09:42 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-10 16:09:23 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-10 16:07:42 | Horowpothana (Yan Oya) | 5.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-10 16:07:29 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2025-12-10 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-10 16:05:51 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:05:50 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.037 |  |
| 2025-12-10 16:05:28 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:05:16 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:05:09 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.013 |  |
| 2025-12-10 16:04:43 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:04:31 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:04:22 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 16:03:30 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 16:03:19 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:46 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 16:02:42 | Hanwella (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-10 16:02:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:31 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2025-12-10 16:02:30 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-10 16:02:19 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:02:13 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:11 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 16:02:08 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.071 |  |
| 2025-12-10 16:02:05 | Manampitiya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2025-12-10 16:02:00 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-10 16:02:00 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:01:38 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.011 |  |
| 2025-12-10 16:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:01:13 | Yaka Wewa (Ma Oya) | 2.05 | 🟢 Normal | -0.151 |  |
| 2025-12-10 16:01:11 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:00:57 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:00:20 | Weraganthota (Mahaweli Ganga) | -1.05 | 🟢 Normal | -0.545 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 16:02:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-10 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-10 16:02:46 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 16:02:11 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 16:03:30 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 16:09:42 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-10 16:07:42 | Horowpothana (Yan Oya) | 5.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-10 16:12:36 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-10 16:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 16:02:13 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:00:57 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:14:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:02:30 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:04:43 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:05:28 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:05:16 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:03:19 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:01:11 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 16:09:23 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-10 16:04:31 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:04:22 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:02:19 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:02:00 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:05:51 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2025-12-10 16:01:38 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.011 |  |
| 2025-12-10 16:05:09 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.013 |  |
| 2025-12-10 16:10:43 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2025-12-10 16:07:29 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2025-12-10 16:02:05 | Manampitiya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2025-12-10 16:02:42 | Hanwella (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-10 16:02:00 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-10 16:05:50 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.037 |  |
| 2025-12-10 16:02:31 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2025-12-10 16:02:08 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.071 |  |
| 2025-12-10 16:01:13 | Yaka Wewa (Ma Oya) | 2.05 | 🟢 Normal | -0.151 |  |
| 2025-12-10 16:00:20 | Weraganthota (Mahaweli Ganga) | -1.05 | 🟢 Normal | -0.545 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)