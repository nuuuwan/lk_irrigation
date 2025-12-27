# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_01:01:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 01:01:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:01:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.013 |  |
| 2025-12-28 01:01:29 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:01:23 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-28 01:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:53 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:46 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 01:00:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:50:07 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-28 00:37:58 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:37:30 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:15:27 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.013 |  |
| 2025-12-28 00:12:05 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.003 |  |
| 2025-12-28 00:10:43 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2025-12-28 00:10:16 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.009 |  |
| 2025-12-28 00:07:48 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.014 |  |
| 2025-12-28 00:06:55 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:06:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:06:45 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:22 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:20 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.028 |  |
| 2025-12-28 00:05:14 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-28 00:05:05 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:04:29 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-28 00:04:16 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:03:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 00:04:29 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-28 00:03:09 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 01:00:46 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 00:00:44 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 00:50:07 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-28 00:00:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:54 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:04:16 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:37:58 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:02:41 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:22 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:02:12 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:02:53 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:01:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:03:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:02:16 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:00:53 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:01:29 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:00:45 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:09:15 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:06:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:06:55 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:12:05 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.003 |  |
| 2025-12-28 00:02:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.005 |  |
| 2025-12-28 00:10:16 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.009 |  |
| 2025-12-28 00:10:43 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 01:01:23 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-28 01:01:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.013 |  |
| 2025-12-28 00:07:48 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.014 |  |
| 2025-12-28 00:03:16 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-28 00:05:20 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.028 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)