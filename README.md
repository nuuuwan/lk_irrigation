# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_21:04:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 21:04:57 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:04:44 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:04:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-28 21:03:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 21:03:57 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:03:54 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:03:42 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-28 21:03:38 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2025-12-28 21:02:50 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:46 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:43 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:36 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:34 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:29 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:33 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:32 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:25 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:11 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 21:00:42 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:00:42 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-28 21:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:46:25 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:27:20 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:22:01 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:21:21 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-28 20:18:39 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.046 |  |
| 2025-12-28 20:11:11 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:10:11 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.028 |  |
| 2025-12-28 20:09:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-28 20:08:29 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2025-12-28 20:07:28 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:07:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 20:21:21 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-28 21:00:42 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-28 21:01:11 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 21:01:32 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:29 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:11:11 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:00:42 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:00:16 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:05:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:50 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:43 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:04:44 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:36 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:18:39 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:46 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:03:57 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:33 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:02:34 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:05:30 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:04:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:04:57 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:01:25 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:01:33 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:03:54 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:03:28 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-28 20:09:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-28 21:03:42 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:05:49 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 21:03:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 20:08:29 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2025-12-28 20:03:46 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2025-12-28 20:10:11 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.028 |  |
| 2025-12-28 21:04:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-28 21:03:38 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2025-12-28 20:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)