# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_01:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 01:14:32 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-01-08 01:14:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:11:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:09:56 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:09:40 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:08:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-08 01:07:31 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-01-08 01:05:30 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-01-08 01:05:19 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.013 |  |
| 2026-01-08 01:05:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-08 01:04:24 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.116 |  |
| 2026-01-08 01:04:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:04:13 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-08 01:03:47 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:03:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-08 01:03:26 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-01-08 01:03:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:02:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:02:47 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.082 |  |
| 2026-01-08 01:02:45 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-01-08 01:02:24 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-08 01:02:08 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-01-08 01:01:52 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:00:44 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:50:29 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:48:10 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:23:59 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.130 |  |
| 2026-01-08 00:23:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 01:14:32 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-01-08 00:12:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-08 01:08:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-08 01:03:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-07 23:01:40 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 01:03:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:42 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:15:53 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:11:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:09:40 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:01:52 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:04:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:00:19 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:00:44 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:03:47 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:06:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:14:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:02:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:01:01 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-01-08 01:02:08 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-01-08 01:05:30 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-01-08 01:04:13 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:12 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:05:13 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-01-08 01:03:26 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-01-08 01:05:19 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.013 |  |
| 2026-01-08 01:07:31 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-01-08 01:02:24 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-08 01:05:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-08 01:02:45 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-01-08 00:05:13 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-01-08 00:00:42 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.071 |  |
| 2026-01-08 01:02:47 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.082 |  |
| 2026-01-08 01:04:24 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.116 |  |
| 2026-01-08 00:23:59 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)