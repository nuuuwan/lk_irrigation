# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_03:25:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 03:25:06 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-27 03:20:31 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 03:13:21 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-04-27 03:11:20 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 03:06:39 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:06:24 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:06:01 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 2.647 | 🔺 Rising |
| 2026-04-27 03:05:33 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-27 03:05:14 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-04-27 03:04:53 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 2.647 | 🔺 Rising |
| 2026-04-27 03:04:49 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:04:25 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-27 03:04:24 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:04:19 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.078 |  |
| 2026-04-27 03:04:07 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:03:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 03:03:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:03:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-04-27 03:03:00 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 03:02:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:02:13 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 03:01:59 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:01:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:01:41 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:01:01 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:00:14 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-27 02:57:47 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.039 |  |
| 2026-04-27 02:45:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 03:06:01 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 2.647 | 🔺 Rising |
| 2026-04-27 03:05:14 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-04-27 02:08:24 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-27 03:04:25 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-27 03:20:31 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 03:05:33 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-27 03:25:06 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-27 03:02:13 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 03:11:20 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 03:03:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 03:03:00 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:23 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:01:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:04:49 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:01:01 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:04:07 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:01:59 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:02:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:14:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:06:39 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:04:24 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 01:25:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-27 00:23:01 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-27 02:09:22 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-27 03:03:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:01:41 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:00:14 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:06:24 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-27 03:03:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-04-27 03:13:21 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-04-27 03:04:19 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.078 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-27 02:20:00 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -1.204 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)