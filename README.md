# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_01:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,119 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 01:18:08 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-22 01:10:34 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:09:17 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:08:13 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:07:58 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:07:46 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:05:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-22 01:05:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:05:37 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-01-22 01:05:02 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:48 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-22 01:04:38 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:15 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:03:49 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:03:31 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 01:03:24 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.078 |  |
| 2026-01-22 01:01:40 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:01:37 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-01-22 01:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-22 01:01:30 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:01:23 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-01-22 01:01:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:00:53 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:00:31 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:00:29 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-22 01:00:21 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:51:59 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:51:35 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:48:33 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:46:03 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:46:01 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:45:40 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2026-01-22 00:37:36 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 01:01:23 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-01-22 01:18:08 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-22 01:04:48 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-22 01:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-22 01:03:31 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 01:05:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-22 01:00:29 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-22 01:00:21 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:03:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:00:31 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:05:59 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:01:30 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:01:40 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:02:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:51:59 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:02:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:01:20 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:05:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:05:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:09:17 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:38 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:13:31 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:07:58 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:03:49 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:00:53 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:00:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:15 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:01:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:05:02 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:10:34 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:01:41 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:00:51 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:08:13 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 01:04:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:01:22 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-22 01:05:37 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-01-22 00:45:40 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2026-01-22 01:01:37 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-01-22 01:03:24 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)