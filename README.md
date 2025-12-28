# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_10:12:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,066 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 10:12:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:08:42 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.018 |  |
| 2025-12-28 10:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2025-12-28 10:08:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:07:31 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:06:34 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-28 10:05:59 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-28 10:05:52 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:05:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:05:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |
| 2025-12-28 10:04:53 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-28 10:04:06 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:04:05 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:03:53 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:03:32 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:03:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.005 |  |
| 2025-12-28 10:03:13 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:03:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:02:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:53 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:43 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:02:41 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:22 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2025-12-28 10:02:05 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2025-12-28 10:01:43 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.012 |  |
| 2025-12-28 10:01:34 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:30 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:01:19 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:00:54 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:00:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 10:00:42 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:00:28 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 10:01:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2025-12-28 10:00:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 10:03:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.005 |  |
| 2025-12-28 10:02:05 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:00:42 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:01:59 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:00:54 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:53 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:12:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:04:05 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 09:03:15 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:03:32 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:03:13 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:19 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:04:06 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:05:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:01:34 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:41 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:06:34 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-28 10:05:59 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-28 10:05:52 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:08:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:02:43 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:07:31 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:03:53 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:03:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:01:30 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:01:43 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.012 |  |
| 2025-12-28 10:08:42 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.018 |  |
| 2025-12-28 10:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2025-12-28 10:04:53 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-28 10:00:28 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.022 |  |
| 2025-12-28 10:02:22 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2025-12-28 10:05:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)