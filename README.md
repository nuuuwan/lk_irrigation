# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_00:04:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 00:04:19 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-21 00:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:04:11 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 00:04:10 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:03:48 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-21 00:03:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:03:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:02:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:54 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-21 00:01:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:35 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.062 |  |
| 2026-05-21 00:01:32 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:26 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:18 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:15 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-21 00:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:54:13 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:21:48 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-20 23:18:49 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-20 23:15:29 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-20 23:14:03 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 23:21:48 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-20 23:09:15 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-21 00:01:15 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-21 00:04:19 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-21 00:03:48 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-21 00:01:54 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-21 00:04:11 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 23:02:54 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 22:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 00:01:32 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:18 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:01:46 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:26 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:02:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:08:15 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:02:29 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:05:36 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:01:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:03:05 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:03:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:44:55 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:00:45 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:04:05 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:03:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:31 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:02:19 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-20 23:09:43 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-20 23:06:33 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 23:06:13 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-05-20 23:02:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-20 23:03:22 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-05-20 23:08:04 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-05-20 23:03:46 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.061 |  |
| 2026-05-21 00:01:35 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)