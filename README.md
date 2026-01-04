# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_16:06:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 16:06:40 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-01-04 16:06:09 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-01-04 16:05:48 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:05:30 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:05:04 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.058 |  |
| 2026-01-04 16:04:39 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-04 16:04:37 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:04:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 16:04:29 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-04 16:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-01-04 16:03:57 | Galgamuwa (Mee Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:03:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:03:32 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 16:03:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:03:29 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:53 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:40 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-01-04 16:02:20 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:06 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:01 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:01:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-01-04 16:01:49 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:36 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:34 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:25 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:01:15 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:06 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:00:26 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:00:10 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 15:04:24 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-04 15:07:52 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-04 16:04:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 16:03:32 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 16:02:20 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:00:36 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:53 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:15 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:34 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:04:37 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:03:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:05:48 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:00:10 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:06 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:02:01 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:03:29 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:01:36 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:03:01 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:03:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 16:04:39 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-04 16:01:49 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:01:06 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:06:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:00:26 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:01:25 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:05:30 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:12 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:03:57 | Galgamuwa (Mee Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:02:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-04 16:06:40 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-01-04 16:04:29 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-04 16:02:40 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-01-04 16:06:09 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-01-04 16:05:04 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.058 |  |
| 2026-01-04 16:01:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-01-04 16:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-01-04 15:04:44 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)