# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_12:11:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,163 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 12:11:53 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-31 12:09:38 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:08:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:07:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:07:05 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:06:36 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-07-31 12:06:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.050 |  |
| 2026-07-31 12:06:13 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-07-31 12:05:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-31 12:05:41 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:05:40 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:05:20 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-31 12:05:06 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 12:05:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-31 12:04:54 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-31 12:03:37 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-07-31 12:05:20 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-31 12:02:24 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-31 12:01:31 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 12:03:07 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 12:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 12:11:53 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-31 12:03:00 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 12:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 12:02:06 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:01:04 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:00:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:03:17 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:04:28 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:00:13 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:03:02 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:05:41 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:07:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:04:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:02:41 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:05:40 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:02:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:08:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:02:39 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:09:38 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:01:25 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:05:06 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:01:08 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 12:06:13 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-07-31 12:06:36 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-07-31 12:00:51 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-31 12:04:57 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-07-31 12:02:53 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-07-31 12:06:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.050 |  |
| 2026-07-31 12:03:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.131 |  |
| 2026-07-31 12:02:10 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)