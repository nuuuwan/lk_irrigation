# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_02:06:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 02:06:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-29 02:05:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-29 02:05:36 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:04:51 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 02:04:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:04:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:03:33 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:03:18 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2025-12-29 02:03:11 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:02:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 02:02:11 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:30 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:21 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:00:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 02:00:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:00:15 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-29 01:50:46 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.004 |  |
| 2025-12-29 01:45:45 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-29 01:36:47 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:34:41 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:16:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 01:13:23 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:06 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:04 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:09:45 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-29 01:08:43 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-29 01:08:05 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 21:07:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-29 01:05:01 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-29 02:04:51 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 02:06:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-29 01:45:45 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-29 02:00:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 01:50:46 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.004 |  |
| 2025-12-29 01:01:55 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:04:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:04:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:01:50 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:03:33 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:30 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:02:11 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:36:47 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:01:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:34:41 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:01:21 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:04:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:00:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 00:12:05 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:05:36 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:08:43 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 02:02:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 01:01:52 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-29 01:07:00 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-29 02:05:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-29 02:03:18 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2025-12-29 00:05:39 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-29 02:00:15 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-28 23:00:24 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-28 21:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2025-12-29 01:02:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)