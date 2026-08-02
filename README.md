# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_02:02:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 02:02:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:02:08 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:01:21 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-03 02:00:50 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-03 02:00:50 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:00:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.046 |  |
| 2026-08-03 01:33:31 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:21:51 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-08-03 01:21:24 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.046 |  |
| 2026-08-03 01:13:18 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 1.067 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 7.22 | 🔴 Major Flood | 1.649 | 🔺 Rising |
| 2026-08-03 01:06:46 | Norwood (Kelani Ganga) | 1.57 | 🟡 Alert | 0.179 | 🔺 Rising |
| 2026-08-03 01:02:42 | Kithulgala (Kelani Ganga) | 3.79 | 🟡 Alert | -0.781 |  |
| 2026-08-03 01:13:18 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 1.067 | 🔺 Rising |
| 2026-08-03 01:09:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 1.000 | 🔺 Rising |
| 2026-08-03 01:07:27 | Deraniyagala (Kelani Ganga) | 3.95 | 🟢 Normal | 0.998 | 🔺 Rising |
| 2026-08-03 01:21:51 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-08-03 01:03:50 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-08-03 00:02:06 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-03 02:01:21 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-03 01:08:14 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-03 01:02:52 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-03 01:06:07 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-03 01:06:40 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-03 00:04:55 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-03 02:00:50 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-03 01:00:59 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 00:01:50 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:00:50 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:02:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:02:28 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:03:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:07:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:01:51 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:06:44 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:02:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-03 02:02:08 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:33:31 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 01:03:02 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-03 01:02:15 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-08-03 01:04:28 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-03 00:11:43 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-03 02:00:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.046 |  |
| 2026-08-03 01:08:58 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)