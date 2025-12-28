# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_17:53:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 17:53:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:44:27 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-28 17:14:36 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:11:01 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:10:09 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:08:55 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-28 17:08:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-28 17:08:07 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-28 17:08:06 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 17:07:43 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.050 |  |
| 2025-12-28 17:07:26 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:06:15 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:06:00 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:57 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-28 17:05:49 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-28 17:05:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:05:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:22 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2025-12-28 17:05:06 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:04:17 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:03:30 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:03:26 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:03:18 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:02:53 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:02:49 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 17:02:46 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:02:29 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2025-12-28 17:02:24 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-28 17:02:20 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:02:13 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.062 |  |
| 2025-12-28 17:01:44 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:01:35 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:01:31 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-28 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:00:53 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:00:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.030 |  |
| 2025-12-28 17:00:25 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 17:02:29 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2025-12-28 17:05:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-28 17:08:07 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-28 17:02:24 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-28 17:05:57 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-28 17:01:31 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-28 17:02:49 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 17:08:06 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 17:44:27 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-28 17:06:00 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:14:36 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:22 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:00:25 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:06:15 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:01:44 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:53:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:03:26 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:49 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:10:09 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:03:30 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:11:01 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:05:06 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:03:18 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:00:53 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:02:20 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:01:35 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 17:08:55 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2025-12-28 17:07:26 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:05:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:03:17 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:04:17 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:02:53 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-28 17:00:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.030 |  |
| 2025-12-28 17:08:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-28 17:07:43 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.050 |  |
| 2025-12-28 17:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2025-12-28 17:02:13 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)