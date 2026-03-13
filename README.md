# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_04:25:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 04:25:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-14 04:21:31 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:21:29 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:11:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 04:11:21 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 04:09:02 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-03-14 04:08:12 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.065 |  |
| 2026-03-14 04:08:06 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:06:44 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:06:23 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-03-14 04:05:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-14 04:05:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:04:57 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.268 |  |
| 2026-03-14 04:04:43 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-14 04:03:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:43 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-03-14 04:03:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:14 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-14 04:03:14 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:12 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 04:02:52 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-14 04:02:43 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:02:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:02:10 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.040 |  |
| 2026-03-14 04:01:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.003 |  |
| 2026-03-14 04:01:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 04:01:25 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-14 04:01:12 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-03-14 04:01:02 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:00:57 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:00:14 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-14 03:49:45 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.065 |  |
| 2026-03-14 03:40:01 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 04:03:14 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-14 04:05:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-14 04:00:14 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-14 04:25:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-14 04:11:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 04:01:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 03:40:01 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-14 04:03:12 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 03:03:03 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 04:11:21 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 04:01:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.003 |  |
| 2026-03-14 04:02:43 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:01:02 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:00:57 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:02:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:21:31 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:06:44 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:01:12 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:14 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:05:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:03:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:05:16 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:08:06 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:07:47 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:02:52 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-14 04:04:43 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-14 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-03-14 04:01:25 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-14 04:06:23 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-03-14 04:03:43 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-03-14 04:09:02 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-03-14 04:02:10 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.040 |  |
| 2026-03-14 04:08:12 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.065 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 04:04:57 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.268 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)