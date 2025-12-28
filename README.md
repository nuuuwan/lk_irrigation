# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_03:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 03:03:13 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2025-12-29 03:03:08 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:03:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:32 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:25 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:20 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:02:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:01:57 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-29 03:01:44 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:24 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:01:07 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -1.946 |  |
| 2025-12-29 03:01:00 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:00:58 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:00:30 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -1.946 |  |
| 2025-12-29 03:00:22 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 02:58:01 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:52:40 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:52:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:52:37 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:52:36 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:52:34 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:45:34 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:45:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:44:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:44:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:11:45 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:11:44 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:10:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:10:12 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:08:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:08:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:07:48 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-29 02:06:39 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:06:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-29 02:05:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:05:36 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 03:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-29 02:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-29 01:05:01 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-29 02:04:51 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 03:00:22 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 01:45:45 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-29 02:00:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 01:50:46 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.004 |  |
| 2025-12-29 03:01:44 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:57 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:04:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:04:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:11:45 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:03:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:06:39 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:24 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:03:08 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:01:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:34:41 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:00 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:00:58 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:08:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:05:36 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:32 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:25 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:07:48 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:02:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:02:20 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-29 02:03:18 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2025-12-29 03:03:13 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2025-12-29 03:01:07 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -1.946 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)