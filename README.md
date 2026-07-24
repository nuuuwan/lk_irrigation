# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_19:05:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 19:05:15 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.030 |  |
| 2026-07-24 19:05:05 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:04:55 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:03:05 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:53 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-07-24 19:02:51 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 23.143 | 🔺 Rising |
| 2026-07-24 19:02:41 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-24 19:02:37 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 23.143 | 🔺 Rising |
| 2026-07-24 19:02:27 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:08 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:00:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:00:38 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:00:07 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 19:02:51 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 23.143 | 🔺 Rising |
| 2026-07-24 18:03:39 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-07-24 19:02:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-24 18:00:11 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-24 18:00:52 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:02:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:01:43 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:27 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:00:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:08:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:07:00 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:04:21 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:03:05 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:01:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:14:34 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:11:36 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:05:05 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:00:38 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:41 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:08:06 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:04:55 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:03:00 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:08:12 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:04:12 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:01:18 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:08 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-24 19:02:53 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-07-24 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-24 18:03:44 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.011 |  |
| 2026-07-24 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.011 |  |
| 2026-07-24 19:00:07 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.022 |  |
| 2026-07-24 19:05:15 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.030 |  |
| 2026-07-24 18:08:50 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.059 |  |
| 2026-07-24 18:01:11 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -1.333 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)