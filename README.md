# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_09:31:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,801 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 09:31:12 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:30:51 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:13:50 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.035 |  |
| 2025-12-05 09:10:37 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.009 |  |
| 2025-12-05 09:09:49 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:54 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:34 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:28 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:12 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 09:07:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:22 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:16 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:13 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:07 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:06:05 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:05:34 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-05 09:05:29 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:05:15 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:05:11 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:04:56 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:04:44 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.138 |  |
| 2025-12-05 09:03:31 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:03:27 | Thanthirimale (Malwathu Oya) | 6.11 | 🟡 Alert | 0.474 | 🔺 Rising |
| 2025-12-05 09:03:25 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.040 |  |
| 2025-12-05 09:03:06 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:02:39 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.088 |  |
| 2025-12-05 09:02:28 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.072 |  |
| 2025-12-05 09:02:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2025-12-05 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.040 |  |
| 2025-12-05 09:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:01:55 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.050 |  |
| 2025-12-05 09:01:55 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.064 |  |
| 2025-12-05 09:01:47 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.050 |  |
| 2025-12-05 09:01:32 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.065 |  |
| 2025-12-05 09:00:49 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:00:25 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 09:03:27 | Thanthirimale (Malwathu Oya) | 6.11 | 🟡 Alert | 0.474 | 🔺 Rising |
| 2025-12-05 09:05:34 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-05 08:02:43 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-05 09:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:05 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:09:49 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:22 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:04:56 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:03:06 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:31:12 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:28 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:03:31 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:05:11 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:16 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:34 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:06:13 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:54 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:00:25 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:10:37 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.009 |  |
| 2025-12-05 09:06:07 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:00:49 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:05:15 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:07:12 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 09:02:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2025-12-05 09:13:50 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.035 |  |
| 2025-12-05 09:03:25 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.040 |  |
| 2025-12-05 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.040 |  |
| 2025-12-05 09:01:55 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.050 |  |
| 2025-12-05 09:01:47 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.050 |  |
| 2025-12-05 09:01:55 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.064 |  |
| 2025-12-05 09:01:32 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.065 |  |
| 2025-12-05 09:02:28 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.072 |  |
| 2025-12-05 09:02:39 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.088 |  |
| 2025-12-05 09:04:44 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.138 |  |
| 2025-12-05 08:04:02 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)