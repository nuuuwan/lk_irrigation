# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_03:11:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,780 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 03:11:46 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:11:29 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:11:09 | Kithulgala (Kelani Ganga) | 0.31 | 🟢 Normal | -10.871 |  |
| 2026-02-11 03:10:26 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:10:15 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:09:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-11 03:06:20 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:06:19 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:06:18 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:06:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-02-11 03:04:32 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:25 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -10.871 |  |
| 2026-02-11 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:08 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:54 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-11 03:03:50 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:11 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-02-11 03:03:00 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-11 03:02:20 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-11 03:02:12 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:28 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:23 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:20 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:18 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.357 |  |
| 2026-02-11 03:01:16 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:39:17 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:31:55 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 18:04:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-11 03:09:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-11 03:02:20 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-11 03:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:28 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:02:12 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:11 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 18:03:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:06:20 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:01:36 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:08 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:32 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:20 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:10:15 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:23 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:06:18 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:01:49 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:11:46 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:06:47 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:03:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 01:26:11 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:04:46 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:11:29 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:01:42 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-11 02:01:52 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:01:16 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-11 03:10:26 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-11 00:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.006 |  |
| 2026-02-11 02:07:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-11 03:03:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-02-11 03:03:54 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-11 03:03:00 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-11 03:06:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-02-11 00:11:25 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.039 |  |
| 2026-02-11 03:01:18 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.357 |  |
| 2026-02-11 03:11:09 | Kithulgala (Kelani Ganga) | 0.31 | 🟢 Normal | -10.871 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)