# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_11:26:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,919 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 11:26:54 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.008 |  |
| 2026-01-08 11:23:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:23:04 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-08 11:22:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-08 11:14:42 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:13:03 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.029 |  |
| 2026-01-08 11:09:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-08 11:09:38 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.079 |  |
| 2026-01-08 11:09:04 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-01-08 11:07:57 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-01-08 11:07:28 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:06:58 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:06:47 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.014 |  |
| 2026-01-08 11:05:33 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:04:47 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:04:36 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.081 |  |
| 2026-01-08 11:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-08 11:04:20 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:04:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-08 11:04:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:03:51 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:42 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 11:03:32 | Siyambalanduwa (Heda Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-08 11:03:28 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:03:26 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:15 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:06 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.059 |  |
| 2026-01-08 11:02:43 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:02:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:02:41 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-01-08 11:02:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:01:54 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.016 |  |
| 2026-01-08 11:01:47 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:01:03 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:00:49 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:00:44 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-01-08 11:00:36 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.070 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 11:04:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-08 11:00:36 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-08 11:09:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-08 11:03:42 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 11:23:04 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-08 11:00:49 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:01:03 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:02:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:07:28 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:23:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:06 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:15 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:02:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:26 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:02:43 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:05:33 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:06:58 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:03:51 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:04:47 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:14:42 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:26:54 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.008 |  |
| 2026-01-08 11:22:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-08 11:04:20 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:04:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:01:47 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:03:28 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-08 11:00:44 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-01-08 11:06:47 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.014 |  |
| 2026-01-08 11:01:54 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.016 |  |
| 2026-01-08 11:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-08 11:03:32 | Siyambalanduwa (Heda Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-08 11:02:41 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-01-08 11:07:57 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-01-08 11:13:03 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.029 |  |
| 2026-01-08 11:09:04 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-01-08 11:03:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.059 |  |
| 2026-01-08 11:09:38 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.079 |  |
| 2026-01-08 11:04:36 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)