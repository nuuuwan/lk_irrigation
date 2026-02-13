# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_00:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 00:18:41 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:10:06 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.084 |  |
| 2026-02-14 00:09:21 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:09:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:08:19 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-14 00:07:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:07:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-02-14 00:06:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-02-14 00:06:07 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:06:05 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-14 00:06:02 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:31 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:05:15 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:12 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:05:04 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:04:32 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:04:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:03:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:03:50 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-14 00:03:33 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 00:03:08 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.040 |  |
| 2026-02-14 00:03:03 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:02:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:02:46 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:02:38 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 00:02:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:21 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:07 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:00:42 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:44:21 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 00:06:05 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-14 00:08:19 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-13 23:01:06 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-13 23:41:49 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-14 00:03:33 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 00:02:38 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 00:03:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:02:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:05:12 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 00:02:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:07:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:03:03 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:03:25 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:09:59 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:15 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:18:41 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:04 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:07 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:00:42 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:06:07 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:02:21 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:06:02 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:04:32 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:09:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:09:21 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:31 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:02:46 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-02-14 00:03:50 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-14 00:07:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-02-14 00:06:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-02-14 00:03:08 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.040 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-14 00:10:06 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.084 |  |
| 2026-02-13 23:04:23 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)