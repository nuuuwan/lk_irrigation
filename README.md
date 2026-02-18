# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_16:35:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 16:35:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2026-02-18 16:26:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:16:40 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:15:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-02-18 16:09:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:06:22 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:06:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:55 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:45 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-18 16:05:24 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:20 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 16:05:07 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:48 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:05 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-18 16:04:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:40 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:34 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:32 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-02-18 16:03:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.077 |  |
| 2026-02-18 16:03:23 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:57 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 16:02:55 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-18 16:02:51 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:46 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | -288.000 |  |
| 2026-02-18 16:02:45 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -288.000 |  |
| 2026-02-18 16:02:44 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-18 16:02:39 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 16:02:32 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:10 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:01:56 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:01:30 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:01:21 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-18 16:01:11 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.030 |  |
| 2026-02-18 16:00:56 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.003 |  |
| 2026-02-18 16:00:19 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 15:59:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 16:01:21 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-18 16:02:55 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-18 16:04:05 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-18 16:02:44 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-18 16:05:20 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 16:00:19 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 16:02:39 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 16:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 16:02:57 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:34 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 15:59:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:23 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:26:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:55 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:07 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:06:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:06:22 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:16:40 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:40 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:48 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:05:24 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:04:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:01:56 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:10 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:02:32 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:09:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 15:05:11 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:00:56 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.003 |  |
| 2026-02-18 16:15:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-02-18 16:05:45 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-18 16:03:32 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-02-18 16:01:11 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.030 |  |
| 2026-02-18 16:35:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2026-02-18 16:03:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.077 |  |
| 2026-02-18 16:02:46 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)