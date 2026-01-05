# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_10:11:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 10:11:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:11:21 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:09:48 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.046 |  |
| 2026-01-05 10:09:24 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.036 |  |
| 2026-01-05 10:08:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-01-05 10:07:48 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-05 10:07:25 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.014 |  |
| 2026-01-05 10:07:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:07:11 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-05 10:07:09 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-01-05 10:05:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:05:31 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:05:04 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-05 10:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-01-05 10:03:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:38 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.072 |  |
| 2026-01-05 10:03:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:01 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:56 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 10:02:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.089 |  |
| 2026-01-05 10:02:52 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 10:02:52 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:50 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:42 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.182 |  |
| 2026-01-05 10:02:40 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:02:31 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:02:27 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:27 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -90.000 |  |
| 2026-01-05 10:02:25 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -90.000 |  |
| 2026-01-05 10:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:01:50 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.011 |  |
| 2026-01-05 10:01:49 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:01:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:01:12 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-01-05 10:00:52 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:29 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:18 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:08 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:23:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 10:05:04 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-05 10:07:48 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-05 10:02:56 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 10:02:52 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 10:00:08 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:01:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:38 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:11:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:01 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:05:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:50 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:18 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:01:49 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:27 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:07:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:00:52 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:02:52 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:11:21 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:07:09 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-01-05 10:07:11 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-05 10:01:50 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.011 |  |
| 2026-01-05 10:07:25 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.014 |  |
| 2026-01-05 10:05:31 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:02:31 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:02:40 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-05 10:01:12 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-01-05 10:08:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-01-05 10:09:24 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.036 |  |
| 2026-01-05 10:09:48 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.046 |  |
| 2026-01-05 10:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-01-05 10:03:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.072 |  |
| 2026-01-05 10:02:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.089 |  |
| 2026-01-05 10:02:42 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.182 |  |
| 2026-01-05 10:02:27 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)