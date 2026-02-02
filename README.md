# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_08:06:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 08:06:12 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.089 |  |
| 2026-02-02 08:05:45 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.021 |  |
| 2026-02-02 08:05:26 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:05:25 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-02-02 08:05:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:51 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:45 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 08:04:28 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:04:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-02 08:04:10 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:04:09 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-02 08:04:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:04:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:01 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-02 08:03:48 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:03:47 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-02 08:03:23 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:03:08 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.037 |  |
| 2026-02-02 08:03:01 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:02:47 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.071 |  |
| 2026-02-02 08:02:35 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-02 08:02:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:02:02 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:59 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:01:48 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:44 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:36 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 08:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:00:54 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:00:36 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:00:11 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:21:08 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.017 |  |
| 2026-02-02 07:19:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:18:09 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:14:59 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.037 |  |
| 2026-02-02 07:14:11 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.023 |  |
| 2026-02-02 07:13:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:13:09 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-02 07:12:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 08:02:35 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-02 08:03:47 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-02 08:02:47 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 08:04:01 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-02 08:01:36 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 08:04:45 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 08:00:54 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:04:28 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:05:26 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:03:01 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 08:01:59 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:51 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:03:23 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:01:48 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:05:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:05:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:02:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:19:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:02:02 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:18:09 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 07:09:23 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:04:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:03:48 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:04:10 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:01:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:04:09 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-02 07:21:08 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.017 |  |
| 2026-02-02 08:05:45 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.021 |  |
| 2026-02-02 08:05:25 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-02-02 08:03:08 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.037 |  |
| 2026-02-02 07:02:48 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.049 |  |
| 2026-02-02 07:03:50 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.055 |  |
| 2026-02-02 08:04:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-02 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.071 |  |
| 2026-02-02 07:12:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.083 |  |
| 2026-02-02 08:06:12 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)