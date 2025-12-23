# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_21:36:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 21:36:24 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-23 21:31:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:19:14 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:11:11 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-23 21:11:04 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:09:35 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-23 21:08:57 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:08:07 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:07:53 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:07:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:07:22 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:06:58 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:06:46 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.057 |  |
| 2025-12-23 21:06:43 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:05:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:05:47 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2025-12-23 21:05:06 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.074 |  |
| 2025-12-23 21:05:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:38 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2025-12-23 21:04:14 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:09 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:33 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:26 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:22 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:21 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:03:05 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:00 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.013 |  |
| 2025-12-23 21:02:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:02:23 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:02:18 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:02:07 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:01:33 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 21:01:14 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 21:11:11 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-23 21:09:35 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-23 21:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 21:36:24 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-23 21:02:18 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:38 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:33 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:19:14 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:26 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:31:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:07:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:05 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:00 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:06:43 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:01:33 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:22 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:02:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:07:22 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:11:04 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:14 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:05:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:04:09 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:08:57 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:08:07 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:03:21 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:07:53 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:02:07 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:05:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.013 |  |
| 2025-12-23 21:05:47 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2025-12-23 21:01:14 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.026 |  |
| 2025-12-23 21:06:46 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.057 |  |
| 2025-12-23 21:04:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2025-12-23 21:05:06 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)