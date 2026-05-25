# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_03:09:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 03:09:25 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 03:08:39 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.030 |  |
| 2026-05-26 03:08:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-05-26 03:06:21 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | -0.019 |  |
| 2026-05-26 03:06:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:05:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-26 03:05:03 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-26 03:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-26 03:04:39 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-05-26 03:04:39 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 03:04:30 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-05-26 03:04:28 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-26 03:04:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:03:45 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:03:38 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:03:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:50 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-26 03:02:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:42 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-05-26 03:02:34 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-26 03:02:24 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.255 |  |
| 2026-05-26 03:02:20 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:11 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:02:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:07 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:03 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:01:59 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:01:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:01:38 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.022 |  |
| 2026-05-26 03:00:48 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-26 03:00:46 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:00:36 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:00:03 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.255 |  |
| 2026-05-26 02:48:14 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:38:23 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-26 02:38:08 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.483 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 03:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-05-26 03:05:03 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-26 03:04:30 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-05-26 03:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-26 03:02:50 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-26 02:11:12 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-26 03:04:28 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-26 03:00:48 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-26 03:04:39 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 03:09:25 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 03:05:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-26 02:38:23 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-26 03:02:07 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:03:38 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:03 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:01:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:08:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:06:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:03:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:04:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:00:46 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:04:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:02:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:14:37 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:02:11 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:01:59 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-26 03:03:45 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 03:06:21 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | -0.019 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 03:04:39 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-05-26 03:01:38 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.022 |  |
| 2026-05-26 03:08:39 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.030 |  |
| 2026-05-26 03:02:42 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-05-26 03:02:24 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.255 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)