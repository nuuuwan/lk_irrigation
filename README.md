# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_09:25:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 09:25:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.008 |  |
| 2025-12-30 09:18:39 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.008 |  |
| 2025-12-30 09:15:36 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:09:28 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-30 09:07:10 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2025-12-30 09:06:52 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:06:24 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2025-12-30 09:06:22 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:06:20 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:51 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-30 09:05:17 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2025-12-30 09:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:07 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:04:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:04:57 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:04:18 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 09:04:08 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.097 |  |
| 2025-12-30 09:03:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2025-12-30 09:03:43 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:03:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:03:18 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.070 |  |
| 2025-12-30 09:03:07 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:03:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:56 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:02:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:31 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:16 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2025-12-30 09:02:01 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:40 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:26 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:09 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:04 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:00:38 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:00:12 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 09:05:17 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2025-12-30 09:05:51 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-30 09:04:18 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 09:06:52 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:04 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:40 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:07:19 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:03:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:03:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:31 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:01:26 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:01 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:06:20 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:04:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:04:57 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:02:16 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:07 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:00:38 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:03:43 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:15:36 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:00:12 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 09:18:39 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.008 |  |
| 2025-12-30 09:25:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.008 |  |
| 2025-12-30 09:09:28 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-30 09:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:06:22 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:03:07 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:02:56 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-30 09:07:10 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2025-12-30 09:03:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2025-12-30 09:06:24 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2025-12-30 09:03:18 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.070 |  |
| 2025-12-30 09:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2025-12-30 09:04:08 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)