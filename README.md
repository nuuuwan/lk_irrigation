# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_16:02:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,976 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 16:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 16:02:35 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-23 16:01:41 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-02-23 16:01:38 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:51:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-23 15:51:26 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-23 15:51:23 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-23 15:13:34 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-02-23 15:11:34 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-02-23 15:09:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:08:34 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 15:04:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-23 16:02:35 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-23 15:02:28 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-23 16:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 15:02:52 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-23 16:01:38 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:11:07 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:01:26 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:09:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:02:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 15:08:34 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-23 14:06:15 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-02-23 14:08:45 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 15:04:02 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:08 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:48 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:16 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:02 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:00:40 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-02-23 15:05:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-02-23 15:00:08 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.012 |  |
| 2026-02-23 14:02:33 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 16:01:41 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-02-23 15:02:12 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:05:44 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:01:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 15:11:34 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-02-23 15:13:34 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-02-23 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-23 15:05:15 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-02-23 15:06:27 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-02-23 14:10:34 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-02-23 15:03:04 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-02-23 15:02:43 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.056 |  |
| 2026-02-23 13:02:06 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.061 |  |
| 2026-02-23 15:02:53 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.109 |  |
| 2026-02-23 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.128 |  |
| 2026-02-23 15:00:42 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -198.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)