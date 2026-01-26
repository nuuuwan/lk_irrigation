# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_18:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,353 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 18:11:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-26 18:10:21 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-26 18:10:01 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-26 18:08:03 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:07:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:07:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-26 18:07:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-26 18:05:20 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:05:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:04:38 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:04:15 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:04:08 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:45 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-01-26 18:03:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:26 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-01-26 18:03:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:14 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 18:03:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:02:26 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.061 |  |
| 2026-01-26 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:43 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-26 18:01:40 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:01:24 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.034 |  |
| 2026-01-26 18:01:24 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:01:20 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-26 18:01:19 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:00:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:00:46 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:00:11 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 18:01:40 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-26 18:07:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-26 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-26 17:04:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-26 18:03:14 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 18:01:20 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-26 18:07:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-26 18:01:24 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:03:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:04:15 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:10:01 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:00:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:05:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:00:46 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:43 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:13:42 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:07:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:08:03 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:04:08 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:45 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:04:38 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:01:19 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:10:21 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-26 18:11:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:05:20 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:03:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:03:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-01-26 17:08:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-01-26 18:03:26 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-01-26 18:00:11 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-01-26 18:01:24 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.034 |  |
| 2026-01-26 18:02:26 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)