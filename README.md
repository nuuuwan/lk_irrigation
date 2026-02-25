# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_04:27:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 04:27:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 2.512 | 🔺 Rising |
| 2026-02-26 04:26:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | 2.512 | 🔺 Rising |
| 2026-02-26 04:26:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.007 |  |
| 2026-02-26 04:24:50 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-26 04:24:28 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:22:58 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:22:57 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:22:33 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.004 |  |
| 2026-02-26 04:22:11 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-02-26 04:20:06 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-26 04:10:13 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:06:24 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.139 |  |
| 2026-02-26 04:06:18 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:06:10 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:05:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-26 04:05:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:03:48 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:03:13 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 04:02:35 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 04:02:27 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:19 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:02:11 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:01 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-02-26 04:01:32 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:32 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.042 |  |
| 2026-02-26 04:01:22 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:01:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.065 |  |
| 2026-02-26 04:01:16 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:06 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:00:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:00:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 04:00:10 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 03:58:08 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.027 |  |
| 2026-02-26 03:54:20 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-26 03:49:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-02-26 03:46:37 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.027 |  |
| 2026-02-26 03:37:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.027 |  |
| 2026-02-26 03:36:25 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 04:27:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 2.512 | 🔺 Rising |
| 2026-02-26 04:01:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-02-26 04:05:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-26 04:02:35 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 04:00:10 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 03:01:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-26 04:03:13 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 04:00:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 04:22:57 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:32 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:01 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:06:18 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:24:28 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:06 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:03:48 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:22:58 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:00:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 03:05:53 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:01:16 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:06:10 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:02:27 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-26 03:02:01 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-26 04:22:11 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-02-26 04:22:33 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.004 |  |
| 2026-02-26 04:26:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.007 |  |
| 2026-02-26 04:24:50 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-26 04:05:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:02:19 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:01:22 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-26 04:20:06 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-26 04:01:32 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.042 |  |
| 2026-02-26 03:03:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-02-26 04:01:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.065 |  |
| 2026-02-26 02:02:53 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.138 |  |
| 2026-02-26 04:06:24 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)