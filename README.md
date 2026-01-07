# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_07:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,865 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 07:15:48 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:15:46 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.016 |  |
| 2026-01-07 07:12:56 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-07 07:11:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-07 07:10:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:09:52 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-01-07 07:09:43 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 07:08:51 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:07:28 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:07:10 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-01-07 07:06:02 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.058 |  |
| 2026-01-07 07:05:59 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:05:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.094 |  |
| 2026-01-07 07:05:51 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:05:49 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-01-07 07:05:46 | Weraganthota (Mahaweli Ganga) | -0.80 | 🟢 Normal | -0.754 |  |
| 2026-01-07 07:05:19 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:04:34 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:03:48 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 07:03:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-07 07:03:33 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-07 07:03:08 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.130 |  |
| 2026-01-07 07:03:05 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-07 07:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:02:29 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-07 07:02:23 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.071 |  |
| 2026-01-07 07:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:01:44 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 07:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:01:13 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:01:11 | Manampitiya (Mahaweli Ganga) | 3.20 | 🟡 Alert | -0.165 |  |
| 2026-01-07 07:00:34 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:00:21 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:00:08 | Siyambalanduwa (Heda Oya) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-01-07 06:33:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 07:01:11 | Manampitiya (Mahaweli Ganga) | 3.20 | 🟡 Alert | -0.165 |  |
| 2026-01-07 07:05:49 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-01-07 07:03:05 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-07 07:03:33 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-07 07:02:29 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-07 07:03:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-07 07:12:56 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-07 07:03:48 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 07:11:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-07 06:11:32 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-07 07:09:43 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 07:01:44 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 07:00:34 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:05:59 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:15:48 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:07:28 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:08:51 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:08:50 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:10:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 07:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:33:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |
| 2026-01-07 07:05:51 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:00:21 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:05:19 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:02:23 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:01:13 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:04:34 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-07 07:15:46 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.016 |  |
| 2026-01-07 07:09:52 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-01-07 06:11:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-01-07 07:07:10 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-01-07 07:00:08 | Siyambalanduwa (Heda Oya) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-01-07 07:06:02 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.058 |  |
| 2026-01-07 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.071 |  |
| 2026-01-07 07:05:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.094 |  |
| 2026-01-07 07:03:08 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.130 |  |
| 2026-01-07 07:05:46 | Weraganthota (Mahaweli Ganga) | -0.80 | 🟢 Normal | -0.754 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)