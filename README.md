# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_10:15:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,729 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 10:15:35 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.008 |  |
| 2025-12-31 10:15:18 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.013 |  |
| 2025-12-31 10:11:35 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2025-12-31 10:09:09 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.065 |  |
| 2025-12-31 10:09:00 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:08:13 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.082 |  |
| 2025-12-31 10:07:38 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:07:27 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.022 |  |
| 2025-12-31 10:07:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:07:04 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2025-12-31 10:06:10 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2025-12-31 10:06:07 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:06:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:02 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:41 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:13 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:08 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:06 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-31 10:03:57 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 10:03:11 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:02:51 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.190 |  |
| 2025-12-31 10:02:34 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 10:02:11 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 10:02:00 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:01:56 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:01:49 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2025-12-31 10:01:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:01:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-31 10:00:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-31 10:00:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 10:06:10 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2025-12-31 10:01:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-31 09:03:37 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-31 10:02:34 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 10:00:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-31 09:04:36 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 10:01:49 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 10:02:11 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 10:03:11 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:00:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:02:00 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:08 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:01:56 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:07:38 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:01:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:09:00 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:13 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:06:07 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:02 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:41 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:05:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:06:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:09:09 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:07:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:15:35 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.008 |  |
| 2025-12-31 10:07:04 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2025-12-31 10:11:35 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2025-12-31 10:03:57 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 10:04:06 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-31 10:15:18 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.013 |  |
| 2025-12-31 10:07:27 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.022 |  |
| 2025-12-31 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2025-12-31 10:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.065 |  |
| 2025-12-31 10:08:13 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.082 |  |
| 2025-12-31 10:02:51 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)