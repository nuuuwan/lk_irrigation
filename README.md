# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_09:11:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,634 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 09:11:56 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:11:50 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.018 |  |
| 2025-12-06 09:08:32 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-06 09:06:40 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:06:29 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:06:27 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-06 09:06:13 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:05:59 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-06 09:05:51 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.246 |  |
| 2025-12-06 09:05:16 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-06 09:05:14 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-06 09:04:47 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.173 |  |
| 2025-12-06 09:04:38 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:04:24 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 09:04:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.095 |  |
| 2025-12-06 09:04:15 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.071 |  |
| 2025-12-06 09:04:09 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:03:52 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.023 |  |
| 2025-12-06 09:03:38 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.070 |  |
| 2025-12-06 09:03:33 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2025-12-06 09:02:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:45 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:45 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:23 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.081 |  |
| 2025-12-06 09:02:21 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:21 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-06 09:02:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-06 09:02:14 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2025-12-06 09:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:55 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:17 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 09:08:32 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-06 09:05:16 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-06 09:02:21 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-06 09:05:59 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-06 09:02:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-06 09:06:27 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-06 09:02:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:14 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:04:09 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:06:40 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:04:38 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:21 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:06:29 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:11:56 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:45 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:17 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:06:13 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:45 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:00:55 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:11:50 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.018 |  |
| 2025-12-06 09:03:52 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.023 |  |
| 2025-12-06 09:04:24 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 09:03:33 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2025-12-06 09:03:38 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.070 |  |
| 2025-12-06 09:04:15 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.071 |  |
| 2025-12-06 08:03:53 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2025-12-06 09:02:23 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.081 |  |
| 2025-12-06 09:04:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.095 |  |
| 2025-12-06 09:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2025-12-06 09:04:47 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.173 |  |
| 2025-12-06 09:05:51 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)