# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_05:18:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 05:18:50 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 05:17:51 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-05-01 05:15:11 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.017 |  |
| 2026-05-01 05:14:06 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.017 |  |
| 2026-05-01 05:12:53 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-05-01 05:11:59 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:11:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:09:53 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-01 05:09:06 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:07:25 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.023 |  |
| 2026-05-01 05:07:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:06:26 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -10.918 |  |
| 2026-05-01 05:05:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:04:56 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-01 05:04:41 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.069 |  |
| 2026-05-01 05:04:40 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-05-01 05:04:16 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.067 |  |
| 2026-05-01 05:04:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:03:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.098 |  |
| 2026-05-01 05:03:42 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:03:10 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.031 |  |
| 2026-05-01 05:03:09 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-01 05:02:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:02:32 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:02:22 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -10.918 |  |
| 2026-05-01 05:02:18 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-01 05:01:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:00:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:00:35 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.050 |  |
| 2026-05-01 04:40:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 04:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-05-01 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-01 05:09:53 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-01 04:00:51 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-01 05:04:56 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-01 05:18:50 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 05:00:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:40:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:09:06 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:07:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:05:06 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:04:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:02:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:11:59 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:12:53 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-05-01 04:09:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:03:42 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:05:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:01:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:11:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:02:32 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:03:09 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 05:14:06 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.017 |  |
| 2026-05-01 05:15:11 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.017 |  |
| 2026-05-01 05:02:18 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-01 05:07:25 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.023 |  |
| 2026-05-01 05:03:10 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.031 |  |
| 2026-05-01 05:17:51 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-05-01 05:04:40 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-05-01 05:00:35 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.050 |  |
| 2026-05-01 05:04:16 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.067 |  |
| 2026-05-01 05:04:41 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.069 |  |
| 2026-05-01 05:03:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.098 |  |
| 2026-05-01 05:06:26 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -10.918 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)