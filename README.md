# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_14:09:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 14:09:06 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:08:08 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.047 |  |
| 2026-01-04 14:07:23 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-04 14:07:00 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:56 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:31 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:15 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:55 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:51 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-04 14:05:45 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-04 14:05:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-01-04 14:05:32 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:11 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.058 |  |
| 2026-01-04 14:05:04 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:05:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-04 14:04:31 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:04:21 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:03:03 | Galgamuwa (Mee Oya) | 2.54 | 🟢 Normal | -0.021 |  |
| 2026-01-04 14:02:59 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:48 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:42 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.058 |  |
| 2026-01-04 14:02:31 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:01 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:01:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:01:46 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 14:01:27 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:01:18 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:01:17 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:01:05 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:00:30 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 13:21:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.058 |  |
| 2026-01-04 13:14:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:13:46 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:13:26 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 14:05:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-04 14:05:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-04 14:05:51 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-04 14:01:46 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 14:00:30 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 14:07:23 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-04 14:01:27 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:45 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:31 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:42 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:59 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:31 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:55 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:02:48 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:15 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:06:56 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:01:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:07:00 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:04:31 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:01:18 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:07 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:32 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 14:05:04 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:04:21 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:02:01 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:01:17 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:01:05 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:09:06 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-04 14:05:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-01-04 14:03:03 | Galgamuwa (Mee Oya) | 2.54 | 🟢 Normal | -0.021 |  |
| 2026-01-04 13:11:48 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-01-04 14:08:08 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.047 |  |
| 2026-01-04 12:06:39 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-04 14:05:11 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.058 |  |
| 2026-01-04 14:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.058 |  |
| 2026-01-04 13:05:13 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.067 |  |
| 2026-01-04 13:13:26 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)