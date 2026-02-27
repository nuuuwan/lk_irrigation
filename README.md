# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_13:39:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,485 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 13:39:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:30:50 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.007 |  |
| 2026-02-27 13:21:11 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:15:55 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:13:16 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:09:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-02-27 13:08:59 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:06:54 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:06:46 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:06:40 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:05:03 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 13:04:49 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:04:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-27 13:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:04:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:47 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 13:03:31 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 13:03:29 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:14 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:05 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-27 13:02:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:02:35 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:02:35 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 13:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 13:02:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:02:11 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:02:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:01:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:39 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.060 |  |
| 2026-02-27 13:01:38 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:35 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:35 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:13 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 13:00:59 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:00:54 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:00:42 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-27 12:59:46 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 13:04:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-27 13:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 13:03:47 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 13:02:35 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 13:01:13 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 13:03:31 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 13:05:03 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 13:00:42 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:02:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:39:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:29 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:38 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:00:59 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:14 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:13:16 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:21:11 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:08:59 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:35 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:06:54 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:04:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:00:54 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:01:35 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:06:40 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:15:55 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:30:50 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.007 |  |
| 2026-02-27 13:09:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-02-27 11:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:04:49 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:06:46 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:02:11 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-27 13:03:05 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-27 13:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:02:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:02:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:02:35 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-27 13:01:39 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)