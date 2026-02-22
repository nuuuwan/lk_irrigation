# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_09:06:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 09:06:32 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:26 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-22 09:06:05 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:01 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | -0.037 |  |
| 2026-02-22 09:05:24 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-02-22 09:05:11 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-02-22 09:05:02 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.057 |  |
| 2026-02-22 09:04:51 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:04:07 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.108 |  |
| 2026-02-22 09:04:04 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:03:35 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-02-22 09:03:24 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-02-22 09:03:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-22 09:03:11 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.198 |  |
| 2026-02-22 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-02-22 09:02:55 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.196 |  |
| 2026-02-22 09:02:45 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.095 |  |
| 2026-02-22 09:02:36 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-22 09:02:24 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:01:45 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:01:40 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-02-22 09:01:05 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-22 09:01:03 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-02-22 09:01:02 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-02-22 09:00:46 | Manampitiya (Mahaweli Ganga) | 4.43 | 🟠 Minor Flood | -0.021 |  |
| 2026-02-22 09:00:43 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-22 09:00:12 | Weraganthota (Mahaweli Ganga) | -0.88 | 🟢 Normal | -0.021 |  |
| 2026-02-22 08:33:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-22 08:18:28 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:11:41 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 09:00:46 | Manampitiya (Mahaweli Ganga) | 4.43 | 🟠 Minor Flood | -0.021 |  |
| 2026-02-22 09:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-22 08:02:28 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-22 09:01:05 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-22 09:02:36 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-22 08:03:54 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-22 08:01:11 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-22 08:10:26 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-22 08:03:08 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 09:01:45 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:05 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:04:51 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:02:24 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:26 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:06:32 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-22 09:03:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-22 09:01:02 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-02-22 08:05:56 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:04:50 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-02-22 09:00:12 | Weraganthota (Mahaweli Ganga) | -0.88 | 🟢 Normal | -0.021 |  |
| 2026-02-22 09:05:24 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-02-22 09:01:03 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-02-22 09:00:43 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-22 09:01:40 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-02-22 09:06:01 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | -0.037 |  |
| 2026-02-22 09:03:24 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-02-22 08:09:07 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-02-22 09:05:11 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-02-22 09:05:02 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.057 |  |
| 2026-02-22 09:03:35 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-02-22 08:04:05 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-02-22 08:05:19 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.084 |  |
| 2026-02-22 09:02:45 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.095 |  |
| 2026-02-22 09:04:07 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.108 |  |
| 2026-02-22 08:05:25 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.111 |  |
| 2026-02-22 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-02-22 08:03:11 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.185 |  |
| 2026-02-22 09:02:55 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.196 |  |
| 2026-02-22 09:03:11 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)