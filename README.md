# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19_12:23:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **210,445 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 12:23:15 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-07-19 12:10:43 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:09:32 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:07:54 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.089 |  |
| 2026-07-19 12:07:16 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:06:20 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:05:28 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-19 12:05:00 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-07-19 12:04:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-19 12:04:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:04:01 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:53 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:34 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 12:03:12 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 12:02:54 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-19 12:02:53 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:52 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:51 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:38 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-19 12:02:29 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:26 | Putupaula (Kalu Ganga) | 0.13 | 🟢 Normal | -0.079 |  |
| 2026-07-19 12:02:25 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 12:02:20 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:19 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:01 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.089 |  |
| 2026-07-19 12:01:47 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:47 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:45 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:34 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:20 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-07-19 12:01:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:00:59 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.040 |  |
| 2026-07-19 12:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-19 12:00:20 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 12:05:28 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-19 12:03:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 12:04:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-19 12:02:38 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-19 12:03:12 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 12:02:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 12:01:34 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:45 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:53 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:29 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:47 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:09:32 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:52 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:01:47 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:23:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:00:20 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:04:01 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:04:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:19 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:20 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:51 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:02:25 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:06:20 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:10:43 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:07:16 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:03:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:05:00 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 12:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-19 12:02:54 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-19 12:01:20 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-07-19 12:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-07-19 12:23:15 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-07-19 12:00:59 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.040 |  |
| 2026-07-19 12:02:26 | Putupaula (Kalu Ganga) | 0.13 | 🟢 Normal | -0.079 |  |
| 2026-07-19 12:07:54 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.089 |  |
| 2026-07-19 12:02:01 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)