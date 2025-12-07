# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_09:13:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 09:13:03 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 09:10:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2025-12-07 09:08:01 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2025-12-07 09:07:49 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:07:26 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:06:53 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.069 |  |
| 2025-12-07 09:06:36 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.039 |  |
| 2025-12-07 09:06:26 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2025-12-07 09:06:15 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.205 |  |
| 2025-12-07 09:05:28 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:05:22 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:05:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 09:04:59 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:04:59 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.019 |  |
| 2025-12-07 09:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.061 |  |
| 2025-12-07 09:04:55 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:04:37 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:04:26 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-07 09:04:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:03:46 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-07 09:03:32 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.031 |  |
| 2025-12-07 09:03:25 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2025-12-07 09:02:49 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-07 09:02:38 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.031 |  |
| 2025-12-07 09:02:32 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.051 |  |
| 2025-12-07 09:02:18 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-07 09:02:15 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:02:09 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:54 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:01:35 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:21 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:11 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:01:09 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.040 |  |
| 2025-12-07 09:01:02 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:00:31 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:00:15 | Thanthirimale (Malwathu Oya) | 6.08 | 🟡 Alert | -0.056 |  |
| 2025-12-07 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 09:00:15 | Thanthirimale (Malwathu Oya) | 6.08 | 🟡 Alert | -0.056 |  |
| 2025-12-07 09:04:26 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-07 09:03:46 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-07 09:05:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 09:13:03 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:02:15 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:04:37 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:05:22 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:01:11 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:07:49 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:00:31 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:01:54 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:05:28 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:07:26 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 09:08:01 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2025-12-07 09:06:26 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2025-12-07 09:04:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:02:09 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:04:59 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:04:55 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:02 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:21 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:01:35 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:04:59 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.019 |  |
| 2025-12-07 09:02:49 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-07 09:03:25 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2025-12-07 09:02:18 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-07 09:03:32 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.031 |  |
| 2025-12-07 09:02:38 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.031 |  |
| 2025-12-07 09:06:36 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.039 |  |
| 2025-12-07 09:01:09 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.040 |  |
| 2025-12-07 09:02:32 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.051 |  |
| 2025-12-07 09:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.061 |  |
| 2025-12-07 09:10:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2025-12-07 09:06:53 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.069 |  |
| 2025-12-07 09:06:15 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)