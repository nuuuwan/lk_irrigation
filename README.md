# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_15:20:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,699 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 15:20:54 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:17:59 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.081 |  |
| 2025-12-24 15:10:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:10:24 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:38 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.036 |  |
| 2025-12-24 15:07:31 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:21 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.147 |  |
| 2025-12-24 15:07:00 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:06:44 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 15:06:07 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 15:05:57 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:05:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:05:33 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-24 15:05:11 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:04:50 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 15:04:43 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-24 15:04:37 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:50 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-24 15:03:18 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:03:11 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-24 15:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:49 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:42 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2025-12-24 15:02:42 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2025-12-24 15:02:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:23 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.030 |  |
| 2025-12-24 15:02:13 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:01:54 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:01:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:01:42 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:01:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:00:32 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:00:17 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:00:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 15:02:42 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2025-12-24 15:03:11 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-24 15:00:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-24 15:04:43 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-24 15:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-24 15:04:50 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 15:06:07 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 15:06:44 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 15:01:54 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:07 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:20:54 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:04:37 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:05:57 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:05:11 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:01:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:50 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:49 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:13 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:00:17 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:00 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:05:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:10:24 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:10:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:07:31 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:03:18 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:01:42 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:00:32 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-24 15:02:42 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2025-12-24 15:02:23 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.030 |  |
| 2025-12-24 15:07:38 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.036 |  |
| 2025-12-24 15:05:33 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-24 15:17:59 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.081 |  |
| 2025-12-24 15:07:21 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)