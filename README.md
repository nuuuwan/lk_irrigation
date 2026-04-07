# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_17:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 17:03:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-07 17:03:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:05 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-07 17:03:04 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:03:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 17:02:57 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-04-07 17:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-07 17:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:02:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.080 |  |
| 2026-04-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:46 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 17:01:34 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:00:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-07 17:00:53 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:58:40 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:34:19 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:16:33 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-07 16:14:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 17:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-07 17:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-07 17:00:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-07 17:03:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-07 16:08:54 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-07 17:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:02:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 16:07:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 17:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 16:02:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:03:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:00:53 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:34:19 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:34 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:24 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:01 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:06:18 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:00:59 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:08:27 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:06:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:06:28 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:09:20 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | -0.005 |  |
| 2026-04-07 16:03:04 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:03:04 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:01:46 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:06:28 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.019 |  |
| 2026-04-07 17:02:57 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-04-07 16:05:51 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-04-07 17:03:05 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-07 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)