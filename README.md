# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_03:15:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 03:15:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.007 |  |
| 2026-01-03 03:12:20 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-01-03 03:11:47 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-01-03 03:07:30 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 03:06:37 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-03 03:06:33 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:06:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.086 |  |
| 2026-01-03 03:06:22 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:05:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:05:11 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-01-03 03:04:48 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:04:35 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:34 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:34 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-01-03 03:04:33 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:32 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:20 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-01-03 03:04:12 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:04:12 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:10 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:03:37 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.003 |  |
| 2026-01-03 03:03:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:03:15 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-03 03:02:56 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:02:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-03 03:02:24 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:01:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:01:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-03 03:01:44 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:01:21 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:01:12 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 03:00:38 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.242 |  |
| 2026-01-03 03:00:37 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:00:23 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-01-03 02:55:41 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.242 |  |
| 2026-01-03 02:20:24 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 03:12:20 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-01-03 03:01:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-03 01:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-01-03 03:02:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-03 03:03:15 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-03 02:20:24 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-03 03:01:12 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 03:07:30 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 03:00:23 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:06:33 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:02:56 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:03:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 02:05:15 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:12 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:01:21 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:05:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:01:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:00:37 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:35 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:06:22 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:03:37 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.003 |  |
| 2026-01-03 03:15:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.007 |  |
| 2026-01-03 03:04:12 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:01:44 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:02:24 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:04:48 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:04:20 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-01-03 03:06:37 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-03 03:04:34 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-03 03:05:11 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-03 02:07:05 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.050 |  |
| 2026-01-03 03:06:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.086 |  |
| 2026-01-03 02:03:12 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.089 |  |
| 2026-01-03 03:00:38 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)