# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_00:02:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 00:02:26 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:02:19 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:02:00 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.070 |  |
| 2026-02-18 00:01:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:35 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:34 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:33 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 00:01:24 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-17 23:21:38 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:17:58 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-17 23:09:46 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.058 |  |
| 2026-02-17 23:07:27 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 23:01:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-17 23:17:58 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-17 23:01:01 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-18 00:01:33 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 00:01:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:02:26 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:03:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:35 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:03:34 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:05:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:03:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:02:25 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 22:02:33 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 22:22:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:02:01 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:02:19 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:01:32 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:04:28 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-17 22:03:40 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:06:22 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:04:35 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:21:38 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:01:36 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:01:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 23:07:27 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 00:02:00 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-17 23:00:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-17 23:02:17 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:24 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-02-18 00:01:34 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 23:01:11 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-02-17 21:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-02-17 23:09:46 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.058 |  |
| 2026-02-18 00:01:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)