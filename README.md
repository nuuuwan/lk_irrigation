# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_14:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 14:13:02 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-28 14:11:09 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:10:59 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:09:56 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-28 14:09:37 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:09:34 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:08:18 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:07:56 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:07:36 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -36.000 |  |
| 2026-01-28 14:07:35 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -36.000 |  |
| 2026-01-28 14:06:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:05:55 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.079 |  |
| 2026-01-28 14:05:50 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:54 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:50 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:35 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 14:03:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-28 14:03:11 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 14:02:56 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-01-28 14:02:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:47 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:41 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-28 14:02:13 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 14:02:11 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-28 14:01:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:43 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-28 14:01:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-28 14:01:14 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.171 |  |
| 2026-01-28 14:01:10 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:08 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:01:06 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-01-28 14:00:52 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:00:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 13:17:43 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-01-28 13:16:28 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 14:01:43 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-28 14:02:41 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-28 14:03:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-28 14:02:13 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 14:03:11 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 14:03:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 13:16:28 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-28 14:00:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:05:50 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:10 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:09:34 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:47 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:02:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:10:59 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:35 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:00:52 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:07:56 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:01:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:06:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:54 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:11:09 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-28 13:12:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 13:03:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:50 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 14:09:56 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-28 14:08:18 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:09:37 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:01:08 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-28 14:02:11 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-28 14:13:02 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-28 14:01:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-28 14:01:06 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-01-28 14:02:56 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-01-28 14:05:55 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.079 |  |
| 2026-01-28 14:01:14 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.171 |  |
| 2026-01-28 14:07:36 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)