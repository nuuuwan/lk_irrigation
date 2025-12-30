# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_19:36:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 19:36:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.013 |  |
| 2025-12-30 19:20:08 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:16:07 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:13:52 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:11:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:10:14 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:09:26 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:08:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:08:04 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:07:43 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:07:22 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 19:07:02 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:06:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:06:06 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.060 |  |
| 2025-12-30 19:05:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.029 |  |
| 2025-12-30 19:05:09 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:47 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-30 19:04:10 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:06 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.069 |  |
| 2025-12-30 19:03:40 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2025-12-30 19:03:34 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:14 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:02 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 19:02:56 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 19:02:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:02:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-30 19:02:11 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:02:11 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-30 19:02:05 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:01:43 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:01:36 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.005 |  |
| 2025-12-30 19:01:31 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2025-12-30 19:00:55 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:00:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 19:01:31 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2025-12-30 19:02:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-30 19:04:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 19:02:56 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 19:07:22 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 19:01:43 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:07:02 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:20:08 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:11:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:06 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:00:55 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:13:52 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:02:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:47 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:06:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:00:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:34 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:02:05 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:14 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:05:09 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:08:04 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:04:10 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:10:14 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:02:11 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 19:03:40 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2025-12-30 19:01:36 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.005 |  |
| 2025-12-30 19:16:07 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:09:26 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:08:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:07:43 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.009 |  |
| 2025-12-30 19:02:11 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-30 19:03:02 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 19:36:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.013 |  |
| 2025-12-30 19:05:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.029 |  |
| 2025-12-30 19:06:06 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.060 |  |
| 2025-12-30 19:03:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)