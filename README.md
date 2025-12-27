# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_04:04:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,828 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 04:04:46 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:03:39 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.080 |  |
| 2025-12-28 04:03:21 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 04:03:06 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-28 04:02:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:18 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 04:02:14 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:14 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-28 04:02:06 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2025-12-28 04:02:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 04:01:55 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.012 |  |
| 2025-12-28 04:01:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.017 |  |
| 2025-12-28 04:01:25 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:01:05 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:00:50 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 04:00:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.012 |  |
| 2025-12-28 03:40:52 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.006 |  |
| 2025-12-28 03:29:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:29:22 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:29:21 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:26:19 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.017 |  |
| 2025-12-28 03:13:01 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.203 |  |
| 2025-12-28 03:11:35 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.012 |  |
| 2025-12-28 03:10:50 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:10:29 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:10:10 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-28 03:09:42 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2025-12-28 03:08:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-28 03:07:55 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -18.000 |  |
| 2025-12-28 03:07:53 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -18.000 |  |
| 2025-12-28 03:07:52 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -18.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 03:01:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2025-12-28 03:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-28 03:08:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-28 04:03:21 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 04:00:50 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 04:02:18 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 04:02:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 03:10:10 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-28 04:01:25 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:03:06 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:02:58 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:29:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:06:12 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:14 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:01:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:04:46 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:14 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:01:05 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 03:01:25 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.006 |  |
| 2025-12-28 03:40:52 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.006 |  |
| 2025-12-28 02:39:50 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.006 |  |
| 2025-12-28 04:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-28 03:06:10 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 04:02:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-28 04:02:06 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2025-12-28 01:01:23 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-28 03:06:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2025-12-28 04:00:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.012 |  |
| 2025-12-28 04:01:55 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.012 |  |
| 2025-12-28 04:01:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.017 |  |
| 2025-12-28 03:05:34 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2025-12-28 04:03:39 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.080 |  |
| 2025-12-28 03:13:01 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.203 |  |
| 2025-12-28 03:07:55 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)