# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_20:14:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 20:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.046 |  |
| 2025-12-28 20:11:11 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:10:11 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.028 |  |
| 2025-12-28 20:09:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-28 20:08:29 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2025-12-28 20:07:28 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:07:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:06:07 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-28 20:05:49 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:05:30 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:04:56 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-28 20:04:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:04:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:46 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2025-12-28 20:03:33 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:03:31 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:28 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 20:03:11 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:02:52 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:23 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:02:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:01 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:01:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 20:01:49 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2025-12-28 20:01:33 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:01:20 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:00:58 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:00:38 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 20:00:16 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:00:14 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:38:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 19:27:06 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:22:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 20:06:07 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-28 20:04:56 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-28 19:38:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 20:01:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 20:00:38 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 20:03:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 20:02:52 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:07:28 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:04:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:11:11 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:00:16 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:05:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:00:45 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:01 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:05:30 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:00:58 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:04:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:02:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:17 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:01:33 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:07:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:28 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:09:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-28 20:03:33 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:02:23 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:05:49 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:01:20 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:03:11 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:08:29 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2025-12-28 20:03:46 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2025-12-28 20:10:11 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.028 |  |
| 2025-12-28 20:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.046 |  |
| 2025-12-28 20:01:49 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)