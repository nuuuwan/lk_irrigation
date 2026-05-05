# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_02:17:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,005 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 02:17:00 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.048 |  |
| 2026-05-06 02:10:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:07:57 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.005 |  |
| 2026-05-06 02:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:07:01 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-06 02:06:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -1.029 |  |
| 2026-05-06 02:05:55 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:05:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:05:42 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-05-06 02:05:29 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.057 |  |
| 2026-05-06 02:05:15 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 02:05:05 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:05:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -1.029 |  |
| 2026-05-06 02:05:01 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-05-06 02:04:51 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:04:48 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-05-06 02:04:39 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-06 02:03:59 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:03:39 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.183 |  |
| 2026-05-06 02:03:28 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:03:12 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:03:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:02:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:43 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:01:34 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:01:33 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.031 |  |
| 2026-05-06 02:00:14 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 01:05:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-06 02:04:39 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-06 02:07:01 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 01:03:26 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 02:05:15 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 02:07:57 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.005 |  |
| 2026-05-06 02:02:43 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 01:00:46 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:05:55 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 01:02:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:03:28 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:10:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:03:29 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:05:05 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:01:34 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:03:12 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:21:50 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.007 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:03:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:04:51 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 01:05:26 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:03:59 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-06 02:05:01 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-05-06 01:05:59 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-05-06 02:01:33 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.031 |  |
| 2026-05-06 02:05:42 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-05-06 02:00:14 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.041 |  |
| 2026-05-06 02:04:48 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-05-06 02:17:00 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.048 |  |
| 2026-05-06 02:05:29 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.057 |  |
| 2026-05-06 02:03:39 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.183 |  |
| 2026-05-06 02:06:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -1.029 |  |
| 2026-05-06 01:14:29 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)