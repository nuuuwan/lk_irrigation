# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_11:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 11:13:34 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:11:46 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:10:10 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.054 |  |
| 2026-01-16 11:09:31 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:08:46 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-01-16 11:08:20 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:08:09 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:07:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:07:46 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-01-16 11:06:52 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:06:27 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-16 11:05:53 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-01-16 11:05:19 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:05:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:04:59 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.013 |  |
| 2026-01-16 11:04:53 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:04:18 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 11:03:29 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:03:25 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-01-16 11:03:22 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 11:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:03:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:02:57 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:40 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:38 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:02:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-01-16 11:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 11:02:04 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:01 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:01:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-16 11:01:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:01:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:01:17 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-01-16 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:01:06 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:00:50 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:00:13 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 11:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-01-16 11:04:18 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 11:01:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-16 11:00:13 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-16 11:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 11:03:22 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 11:03:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:01:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:02:01 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:08:20 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:05:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 11:01:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:00:50 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:40 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:05:19 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:04 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:13:34 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:04:53 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:02:57 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:11:46 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:06:52 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:09:31 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:07:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:06:27 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-16 11:05:53 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-01-16 11:08:09 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:03:29 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:01:06 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:02:38 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:02:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:04:59 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.013 |  |
| 2026-01-16 10:02:18 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-16 11:03:25 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-01-16 11:07:46 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-01-16 11:01:17 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-01-16 11:08:46 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-01-16 11:10:10 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)