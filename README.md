# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_09:10:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 09:10:12 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-28 09:09:22 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:07:18 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:07:04 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-28 09:07:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:06:55 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:06:45 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:05:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2025-12-28 09:05:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:04:20 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.013 |  |
| 2025-12-28 09:04:11 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.032 |  |
| 2025-12-28 09:04:06 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.054 |  |
| 2025-12-28 09:03:25 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:17 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:15 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:15 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:14 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:13 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.021 |  |
| 2025-12-28 09:03:04 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:56 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:52 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.105 |  |
| 2025-12-28 09:02:42 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 09:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:37 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-28 09:02:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-28 09:02:34 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-28 09:02:20 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-28 09:02:01 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 09:01:59 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-28 09:01:51 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:43 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:37 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:11 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 09:02:20 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-28 09:01:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-28 09:02:42 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 09:02:01 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 09:07:04 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-28 09:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:49 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:59 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:14 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:09:22 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:37 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:05:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:15 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:07:18 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:15 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:06:45 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:43 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:56 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:04 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:02:34 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:06:55 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:17 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:07:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:11 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:51 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:04:06 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:25 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:10:12 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-28 09:02:37 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-28 09:02:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-28 09:02:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-28 09:04:20 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.013 |  |
| 2025-12-28 09:03:13 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.021 |  |
| 2025-12-28 09:04:11 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.032 |  |
| 2025-12-28 09:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.054 |  |
| 2025-12-28 09:05:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2025-12-28 09:02:52 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)