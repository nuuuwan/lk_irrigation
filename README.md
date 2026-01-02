# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_04:06:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 04:06:26 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-03 04:05:31 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:05:24 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:05:06 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.060 |  |
| 2026-01-03 04:04:49 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -2.769 |  |
| 2026-01-03 04:04:23 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -2.769 |  |
| 2026-01-03 04:04:20 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:03:58 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-03 04:03:53 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-01-03 04:03:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:03:40 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:03:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-01-03 04:03:13 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:03:12 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:02:56 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:02:43 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:02:41 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-03 04:02:22 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:02:09 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.042 |  |
| 2026-01-03 04:01:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:01:28 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-01-03 04:01:06 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.069 |  |
| 2026-01-03 04:01:05 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:00:17 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:53:22 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-03 03:24:26 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.037 |  |
| 2026-01-03 03:15:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.007 |  |
| 2026-01-03 03:12:20 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-01-03 03:11:47 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 5.455 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 03:12:20 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-01-03 01:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-01-03 04:02:41 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-03 03:02:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-03 04:06:26 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-03 04:03:58 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-03 04:03:13 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:03:12 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:02:22 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:03:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 02:05:15 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:02:43 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:05:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:01:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:04:20 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:04:35 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:06:22 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 03:15:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.007 |  |
| 2026-01-03 04:03:40 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:05:24 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:02:56 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:01:05 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:05:31 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:00:17 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 03:04:48 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 04:01:28 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-01-03 03:53:22 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-03 04:03:53 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-03 03:24:26 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.037 |  |
| 2026-01-03 04:02:09 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.042 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-03 04:05:06 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.060 |  |
| 2026-01-03 04:01:06 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.069 |  |
| 2026-01-03 04:03:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-01-03 04:04:49 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)