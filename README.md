# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_16:10:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 16:10:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-10 16:10:44 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-10 16:10:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-10 16:09:47 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:09:07 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:08:57 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:08:03 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-10 16:06:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 16:06:23 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:45 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-10 16:05:35 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.019 |  |
| 2026-04-10 16:05:24 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:18 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-10 16:05:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:04:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:04:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-10 16:03:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:03:42 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:03:24 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-10 16:03:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:03:01 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:02:56 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-04-10 16:02:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:02 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:22 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:20 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:15 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:04 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:00:40 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:00:39 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.021 |  |
| 2026-04-10 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.154 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 16:10:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-10 15:13:41 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-10 16:05:18 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-10 16:10:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-10 16:04:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-10 16:05:45 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-10 16:08:03 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-10 16:10:44 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-10 15:02:34 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 16:02:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:03:01 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:02:02 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 16:06:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 16:01:22 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:15 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:08:57 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:03:42 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:24 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:09:07 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:00:40 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:06:23 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:09:47 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:04:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:01:20 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 16:05:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:01:04 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:03:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-10 16:05:35 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.019 |  |
| 2026-04-10 16:00:39 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.021 |  |
| 2026-04-10 16:02:56 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-04-10 16:03:24 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-10 15:12:09 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.073 |  |
| 2026-04-10 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)