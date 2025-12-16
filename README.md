# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_01:44:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,948 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 01:44:33 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:29:16 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:16:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:16:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:13:39 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 01:09:21 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-17 01:08:51 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:07:46 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:07:33 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 01:07:03 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-17 01:06:42 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:06:08 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:04:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:04:32 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-17 01:04:24 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:04:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 01:04:04 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2025-12-17 01:03:57 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-17 01:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 01:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:33 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:22 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:02:45 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-17 01:02:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:01:00 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:00:44 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.000 |  |
| 2025-12-17 01:00:26 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:12 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 01:00:44 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.000 |  |
| 2025-12-17 00:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-17 01:04:32 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-17 01:03:57 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-17 01:09:21 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-17 01:04:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 01:07:03 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-17 01:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 01:13:39 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 01:07:33 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 01:06:08 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:04:04 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:06:42 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:12 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:16:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:44:33 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:04:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:16:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:29:16 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:26 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:07:46 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:04:24 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:01:00 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:08:51 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:33 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:03:22 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2025-12-17 01:02:45 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-17 00:01:24 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.051 |  |
| 2025-12-17 01:03:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)