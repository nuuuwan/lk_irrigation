# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_11:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 11:10:20 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:10:04 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:08:43 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-04-10 11:06:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:06:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-10 11:05:30 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:05:28 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:05:15 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:04:42 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.085 |  |
| 2026-04-10 11:04:38 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.062 |  |
| 2026-04-10 11:04:23 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2026-04-10 11:03:53 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:03:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:03:30 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2026-04-10 11:03:15 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:03:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:03:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:02:48 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:02:44 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:02:36 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:02:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-04-10 11:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.060 |  |
| 2026-04-10 11:02:06 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:35 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.125 |  |
| 2026-04-10 11:01:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:01:14 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:01:10 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:08 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:03 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:00:56 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:00:55 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:00:47 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:00:40 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:00:25 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:52:01 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.125 |  |
| 2026-04-10 10:19:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 11:02:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-04-10 11:02:44 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:00:55 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:03:53 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 11:05:28 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:03 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:02:48 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:08:22 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:10:20 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:00:40 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:10 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:00:25 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:06:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:03:15 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:03:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:10:04 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:19:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:08 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:08:43 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-04-10 11:06:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-10 10:07:32 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-10 11:05:15 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:00:56 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:00:47 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:01:14 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:02:36 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:03:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:05:30 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:04:23 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2026-04-10 11:02:06 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:01:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:03:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 11:03:30 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2026-04-10 11:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.060 |  |
| 2026-04-10 11:04:38 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.062 |  |
| 2026-04-10 11:04:42 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.085 |  |
| 2026-04-10 11:01:35 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)