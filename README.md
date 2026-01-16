# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_05:30:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,851 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 05:30:53 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:25:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:17:00 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.005 |  |
| 2026-01-16 05:15:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:15:12 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:14:11 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:12:21 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-16 05:11:12 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:10:50 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:09:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-01-16 05:08:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-16 05:07:04 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.014 |  |
| 2026-01-16 05:06:51 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 05:06:37 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:05:52 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-01-16 05:05:49 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -18.000 |  |
| 2026-01-16 05:05:47 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -18.000 |  |
| 2026-01-16 05:05:38 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:04:37 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-01-16 05:04:12 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:04:09 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:04:05 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-16 05:03:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:03:35 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:03:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:03:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-01-16 05:02:55 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:55 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:02:55 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:02:45 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:43 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.141 |  |
| 2026-01-16 05:02:04 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 05:02:00 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:59 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:18 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:46:32 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-16 04:45:56 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.132 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 05:04:05 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-16 05:12:21 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-16 05:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 05:08:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-16 05:06:51 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 04:01:33 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:18 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:45 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:10:50 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:30:53 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:15:12 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:04:12 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:14:11 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:06:37 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:03:35 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:00 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:04:09 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:02:55 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:25:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:03:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:15:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:01:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 05:17:00 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.005 |  |
| 2026-01-16 05:04:37 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-01-16 05:03:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:02:55 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:05:38 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:02:55 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 05:05:52 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-01-16 05:07:04 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.014 |  |
| 2026-01-16 05:09:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-16 05:03:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-01-16 05:02:43 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.141 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |
| 2026-01-16 05:05:49 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)