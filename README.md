# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_15:13:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 15:13:10 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:09:59 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:08:30 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.049 |  |
| 2025-12-13 15:07:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2025-12-13 15:07:30 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:06:51 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2025-12-13 15:05:56 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:40 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.037 |  |
| 2025-12-13 15:05:36 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:35 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:21 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 15:04:25 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2025-12-13 15:04:14 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.126 |  |
| 2025-12-13 15:04:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2025-12-13 15:04:04 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:03:24 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:03:14 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:13 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:12 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 15:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:44 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2025-12-13 15:02:42 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.079 |  |
| 2025-12-13 15:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:32 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.015 |  |
| 2025-12-13 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:02:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 15:01:50 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:01:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:17 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2025-12-13 15:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.061 |  |
| 2025-12-13 15:01:09 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:59 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:42 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 15:02:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 15:05:21 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 15:03:12 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 15:01:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:17 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:36 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:13:10 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:09:59 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:35 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:07:30 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:05:56 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:59 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:04:14 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:03:13 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:14 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:50 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:03:24 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:04:04 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:02:32 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.015 |  |
| 2025-12-13 15:04:25 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2025-12-13 15:04:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2025-12-13 15:01:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2025-12-13 15:07:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2025-12-13 15:05:40 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.037 |  |
| 2025-12-13 15:06:51 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2025-12-13 15:08:30 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.049 |  |
| 2025-12-13 15:00:42 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | -0.051 |  |
| 2025-12-13 15:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.061 |  |
| 2025-12-13 15:02:42 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.079 |  |
| 2025-12-13 15:02:44 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2025-12-13 15:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)