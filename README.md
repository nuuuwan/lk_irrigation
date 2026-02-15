# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_11:06:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 11:06:55 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.034 |  |
| 2026-02-15 11:06:08 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:05:30 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.009 |  |
| 2026-02-15 11:05:10 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-15 11:04:32 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:03:45 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 11:03:44 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:03:42 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 11:03:42 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 11:03:40 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-02-15 11:03:37 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-02-15 11:03:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-02-15 11:03:35 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-02-15 11:03:25 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-15 11:03:02 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.048 |  |
| 2026-02-15 11:02:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.064 |  |
| 2026-02-15 11:02:20 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-02-15 11:02:12 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:09 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-15 11:01:57 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:54 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:43 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:42 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-15 11:01:31 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:28 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:26 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-15 11:01:05 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:00:45 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:00:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 11:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 11:00:17 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:00:14 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.072 |  |
| 2026-02-15 10:14:38 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-02-15 10:14:18 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 11:01:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-15 11:02:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-02-15 11:03:25 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-15 11:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 11:00:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 11:03:45 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 11:03:42 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 11:03:42 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 11:01:57 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:28 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:54 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:12 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:02 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:20 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:00:45 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:05 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:00:17 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:03:44 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:02:09 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:43 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:31 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:06:08 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:04:32 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:01:26 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 11:05:30 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.009 |  |
| 2026-02-15 11:05:10 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-15 11:02:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-15 11:01:42 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-15 11:03:37 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-02-15 11:03:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-02-15 11:03:40 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-02-15 10:06:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-02-15 11:06:55 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.034 |  |
| 2026-02-15 11:03:35 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-02-15 11:03:02 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.048 |  |
| 2026-02-15 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.064 |  |
| 2026-02-15 10:03:28 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.068 |  |
| 2026-02-15 11:00:14 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)