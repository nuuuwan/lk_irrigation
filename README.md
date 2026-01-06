# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_12:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 12:14:33 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-06 12:14:28 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.040 |  |
| 2026-01-06 12:10:55 | Manampitiya (Mahaweli Ganga) | 3.47 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-01-06 12:09:59 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.081 |  |
| 2026-01-06 12:09:18 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:08:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-06 12:07:59 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-06 12:07:51 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:07:22 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:50 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -0.093 |  |
| 2026-01-06 12:05:38 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:30 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-01-06 12:05:25 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:57 | Thaldena (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 12:04:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:40 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 12:04:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.051 |  |
| 2026-01-06 12:04:26 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:20 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 12:03:39 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:03:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 12:03:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-06 12:02:57 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:55 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:55 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-01-06 12:02:53 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:50 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:32 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | -0.040 |  |
| 2026-01-06 12:02:18 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2026-01-06 12:01:45 | Siyambalanduwa (Heda Oya) | 5.31 | 🟡 Alert | 0.285 | 🔺 Rising |
| 2026-01-06 12:01:37 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-06 12:01:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-01-06 12:01:22 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.041 |  |
| 2026-01-06 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:01:04 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 12:00:24 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 12:01:45 | Siyambalanduwa (Heda Oya) | 5.31 | 🟡 Alert | 0.285 | 🔺 Rising |
| 2026-01-06 12:10:55 | Manampitiya (Mahaweli Ganga) | 3.47 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-01-06 12:01:37 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-06 12:08:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-06 12:00:24 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-06 12:07:59 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-06 12:03:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 12:04:20 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 12:02:18 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 12:04:57 | Thaldena (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 12:01:04 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 12:04:40 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 12:02:55 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:38 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:57 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:53 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:07:51 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:02:50 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:05:25 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:03:39 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:07:22 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:09:18 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:04:26 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-06 12:14:33 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-06 12:05:30 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-01-06 12:03:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-06 12:02:55 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-01-06 12:14:28 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.040 |  |
| 2026-01-06 12:02:32 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | -0.040 |  |
| 2026-01-06 12:01:22 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.041 |  |
| 2026-01-06 12:04:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.051 |  |
| 2026-01-06 12:01:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-01-06 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2026-01-06 12:09:59 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.081 |  |
| 2026-01-06 12:05:50 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)