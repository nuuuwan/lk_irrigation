# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_05:03:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,725 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 05:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:02:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:41 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:39 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:36 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-23 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:54 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:30 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 05:01:20 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-07-23 05:01:15 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:00:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:00:09 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:48:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:48:30 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:36:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -1152.000 |  |
| 2026-07-23 04:36:08 | Nakkala (Kumbukkan Oya) | 8.51 | 🔴 Major Flood | -1152.000 |  |
| 2026-07-23 04:31:15 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.004 |  |
| 2026-07-23 04:28:42 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:27:54 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:21:18 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 05:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 05:02:36 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-23 04:07:04 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-23 04:05:04 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 04:01:53 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 04:48:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:05:08 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:02:21 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:00:09 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-22 18:12:41 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 02:04:59 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:28:42 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:41 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:12:46 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:39 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:54 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:01:58 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:04:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:03:48 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:15 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:07:17 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:01:30 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:03:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:21:18 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:02:33 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-23 04:31:15 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.004 |  |
| 2026-07-23 04:08:18 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:00:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-23 05:01:20 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-07-22 18:02:13 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-07-23 04:07:00 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.023 |  |
| 2026-07-22 18:02:46 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.039 |  |
| 2026-07-23 04:11:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.043 |  |
| 2026-07-23 04:01:40 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.150 |  |
| 2026-07-23 04:36:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -1152.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)