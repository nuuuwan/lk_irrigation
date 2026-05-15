# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_02:10:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 02:10:37 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 02:10:21 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 02:09:36 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.030 |  |
| 2026-05-16 02:08:40 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-05-16 02:08:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-05-16 02:07:46 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.028 |  |
| 2026-05-16 02:06:30 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 1.569 | 🔺 Rising |
| 2026-05-16 02:06:17 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.037 |  |
| 2026-05-16 02:06:04 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.072 |  |
| 2026-05-16 02:05:59 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.020 |  |
| 2026-05-16 02:05:54 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:05:22 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | -0.019 |  |
| 2026-05-16 02:04:50 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:04:44 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.032 |  |
| 2026-05-16 02:04:27 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:04:12 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-16 02:03:56 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-16 02:03:25 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-16 02:03:20 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 02:03:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:57 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.100 |  |
| 2026-05-16 02:02:47 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:45 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.021 |  |
| 2026-05-16 02:02:39 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:24 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:13 | Moragaswewa (Deduru Oya) | 3.94 | 🟢 Normal | -0.015 |  |
| 2026-05-16 02:01:54 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:01:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.061 |  |
| 2026-05-16 02:01:05 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.021 |  |
| 2026-05-16 02:00:57 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.034 |  |
| 2026-05-16 02:00:23 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 1.569 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 02:03:20 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 01:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 02:00:57 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.034 |  |
| 2026-05-16 02:06:30 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 1.569 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 02:10:37 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 02:10:21 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 02:04:12 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:39 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:04:27 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:47 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:03:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:01:54 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:05:54 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:24 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:04:50 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:05:00 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:08:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-05-16 02:02:13 | Moragaswewa (Deduru Oya) | 3.94 | 🟢 Normal | -0.015 |  |
| 2026-05-16 02:08:40 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-05-16 02:05:22 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | -0.019 |  |
| 2026-05-16 02:03:56 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-16 02:05:59 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.020 |  |
| 2026-05-16 02:02:45 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.021 |  |
| 2026-05-16 02:01:05 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.021 |  |
| 2026-05-16 02:07:46 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.028 |  |
| 2026-05-16 02:03:25 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-16 02:09:36 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.030 |  |
| 2026-05-16 02:04:44 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.032 |  |
| 2026-05-16 02:06:17 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.037 |  |
| 2026-05-16 00:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-16 01:05:39 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.048 |  |
| 2026-05-16 02:01:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.061 |  |
| 2026-05-16 02:06:04 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.072 |  |
| 2026-05-16 01:01:33 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.073 |  |
| 2026-05-16 02:02:57 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)