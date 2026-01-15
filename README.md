# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_20:19:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,535 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 20:19:53 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.032 |  |
| 2026-01-15 20:14:07 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:11:52 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-01-15 20:11:16 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.053 |  |
| 2026-01-15 20:08:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-15 20:07:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:07:35 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:07:20 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.076 |  |
| 2026-01-15 20:06:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:06:25 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 20:06:19 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-15 20:05:51 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-01-15 20:05:31 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-15 20:04:50 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 20:04:18 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:04:04 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:04:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:03:39 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:03:04 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:03:03 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:03:01 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:52 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:42 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:39 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-01-15 20:02:24 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:19 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-01-15 20:02:18 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:02:13 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.054 |  |
| 2026-01-15 20:02:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 20:01:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:18 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:16 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:00:34 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.013 |  |
| 2026-01-15 20:00:31 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 20:02:19 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-01-15 20:06:19 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-15 20:05:31 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-15 20:06:25 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 20:04:50 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 20:02:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 20:02:42 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:52 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:18 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:16 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:03:03 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:14:07 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:04:04 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:06:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:02:24 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:04:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:07:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:04:18 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:03:01 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:19:53 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 20:11:52 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-01-15 20:03:39 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:03:04 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:02:18 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:01:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 20:00:34 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.013 |  |
| 2026-01-15 20:00:31 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.018 |  |
| 2026-01-15 20:05:51 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-01-15 20:08:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-15 20:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.032 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-15 20:02:39 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-01-15 20:11:16 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.053 |  |
| 2026-01-15 20:02:13 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.054 |  |
| 2026-01-15 20:07:20 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.076 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)