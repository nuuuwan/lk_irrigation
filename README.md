# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_02:29:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,059 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 02:29:09 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:23:40 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-27 02:23:26 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-27 02:17:50 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-27 02:16:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-02-27 02:09:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:08:23 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-27 02:07:52 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-27 02:07:14 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 02:06:22 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:05:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 02:04:53 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:04:33 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.189 |  |
| 2026-02-27 02:04:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 02:03:20 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:12 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:11 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:02:31 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-02-27 02:02:19 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 02:02:07 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.756 |  |
| 2026-02-27 02:02:04 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 02:01:32 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-02-27 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.407 |  |
| 2026-02-27 02:01:04 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:00:18 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.162 |  |
| 2026-02-27 01:58:09 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.756 |  |
| 2026-02-27 01:56:36 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.162 |  |
| 2026-02-27 01:54:01 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.003 |  |
| 2026-02-27 01:46:19 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:36:45 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 02:23:40 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-27 01:03:42 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.506 | 🔺 Rising |
| 2026-02-27 01:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-27 02:17:50 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-27 02:05:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 02:03:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 02:02:04 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 02:02:19 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 02:07:14 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 01:02:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:04:53 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:51 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:01:04 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:02:26 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:09:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:20 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:29:09 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:12 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:03:11 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:03:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:04:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:08 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:54:01 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.003 |  |
| 2026-02-27 02:01:32 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-02-27 02:16:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-02-27 01:05:31 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-27 02:08:23 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-27 02:07:52 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-27 01:08:57 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-02-27 01:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-02-27 02:02:31 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-02-27 02:00:18 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.162 |  |
| 2026-02-27 02:04:33 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.189 |  |
| 2026-02-27 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.407 |  |
| 2026-02-27 02:02:07 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.756 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)