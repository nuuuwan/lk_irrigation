# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_06:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,889 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 06:13:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:12:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 06:09:51 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:06:58 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:06:28 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:06:28 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:06:14 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:06:06 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.015 |  |
| 2026-01-16 06:05:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-01-16 06:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:05:17 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:54 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:52 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.048 |  |
| 2026-01-16 06:04:47 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-16 06:04:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 06:04:34 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-01-16 06:04:15 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.013 |  |
| 2026-01-16 06:04:14 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:12 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:04:01 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-01-16 06:03:41 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-16 06:03:28 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:03:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:56 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:53 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:43 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:42 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:39 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-01-16 06:02:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 06:02:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:01:46 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-16 06:01:27 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.062 |  |
| 2026-01-16 06:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.069 |  |
| 2026-01-16 06:01:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:00:12 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 06:04:01 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-01-16 06:01:46 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-16 06:04:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 06:02:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 06:12:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 06:06:28 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 06:02:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:03:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:56 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:03:28 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:05:17 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:42 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:53 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:54 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:06:14 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:14 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:13:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:02:43 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:04:47 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-16 06:03:41 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-16 06:04:15 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.013 |  |
| 2026-01-16 06:06:06 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.015 |  |
| 2026-01-16 06:06:28 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:09:51 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-16 06:04:12 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:06:58 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:01:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-16 06:02:39 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-01-16 06:00:12 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-01-16 06:05:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-16 06:04:52 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.048 |  |
| 2026-01-16 06:04:34 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-01-16 06:01:27 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.062 |  |
| 2026-01-16 06:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)