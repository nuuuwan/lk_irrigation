# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_01:30:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 01:30:14 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:23:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-21 01:08:05 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-21 01:07:09 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-21 01:06:51 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:06:24 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-07-21 01:05:34 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:20 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:56 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:35 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:32 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-07-21 01:04:25 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:09 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:03 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-07-21 01:04:02 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-21 01:03:32 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.249 |  |
| 2026-07-21 01:03:28 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:03:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:03:15 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-21 01:02:33 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-21 01:02:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:02:24 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:02:03 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:00:17 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:46:26 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:42:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 01:07:09 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-21 01:03:15 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-21 01:23:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-21 01:04:02 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-21 00:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 01:03:28 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:02:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:00:17 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:09 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:00:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:06:24 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 23:30:18 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:35 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:25 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:34 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:04:56 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:20 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:02:03 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:04:57 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:03:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:30:14 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:06:51 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:01:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:02:24 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 01:05:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-07-21 01:08:05 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-21 01:02:33 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-21 01:04:32 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-07-21 01:04:03 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-21 00:02:32 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.050 |  |
| 2026-07-20 21:00:29 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.111 |  |
| 2026-07-21 01:03:32 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.249 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)