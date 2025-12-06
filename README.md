# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_11:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 11:14:53 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | -0.049 |  |
| 2025-12-06 11:12:43 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.017 |  |
| 2025-12-06 11:08:25 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:08:19 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:07:11 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.152 |  |
| 2025-12-06 11:06:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:06:44 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2025-12-06 11:06:17 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:06:09 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:05:08 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:04:35 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:04:28 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.065 |  |
| 2025-12-06 11:04:28 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-06 11:04:24 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2025-12-06 11:04:11 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 11:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:03:59 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.289 |  |
| 2025-12-06 11:03:44 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:03:37 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.051 |  |
| 2025-12-06 11:03:20 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.070 |  |
| 2025-12-06 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:03:04 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:52 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:02:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:33 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:02:27 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:19 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-06 11:02:19 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:02:19 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 11:02:16 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 11:01:54 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:01:13 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.024 |  |
| 2025-12-06 11:01:11 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:01:00 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:00:50 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-06 10:18:27 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 10:18:10 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 11:04:11 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 11:02:19 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 11:00:50 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-06 11:02:16 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 11:02:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:01:11 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:06:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:04:37 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:01:00 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:06:09 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:06:17 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:04:35 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:05:08 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:03:04 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:08:25 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:08:19 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:02:27 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:03:44 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 11:04:28 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-06 11:02:52 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:02:19 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:01:54 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:02:33 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-06 11:12:43 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.017 |  |
| 2025-12-06 11:02:19 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-06 11:04:24 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2025-12-06 11:01:13 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.024 |  |
| 2025-12-06 11:06:44 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2025-12-06 11:14:53 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | -0.049 |  |
| 2025-12-06 11:03:37 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.051 |  |
| 2025-12-06 11:04:28 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.065 |  |
| 2025-12-06 11:03:20 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.070 |  |
| 2025-12-06 11:07:11 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.152 |  |
| 2025-12-06 11:03:59 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)