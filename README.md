# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_03:18:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 03:18:26 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:17:02 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-17 03:09:42 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:07:59 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:07:58 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-17 03:07:06 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-02-17 03:06:47 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-02-17 03:06:24 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.149 |  |
| 2026-02-17 03:06:18 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -72.000 |  |
| 2026-02-17 03:06:17 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -72.000 |  |
| 2026-02-17 03:06:06 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:05:59 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:04:58 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.005 |  |
| 2026-02-17 03:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-17 03:04:30 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.010 |  |
| 2026-02-17 03:04:18 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:04:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-17 03:02:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-02-17 03:02:00 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-17 03:01:58 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:47 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:00:13 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.054 |  |
| 2026-02-17 02:49:03 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.054 |  |
| 2026-02-17 02:45:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 03:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-02-17 01:15:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-17 03:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-17 03:17:02 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-17 03:01:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 02:00:39 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:58 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:09:42 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:47 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:07:59 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:58 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:18:26 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:03:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:04:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:06:06 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 01:00:43 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 01:05:54 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:05:59 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:04:58 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.005 |  |
| 2026-02-17 03:07:58 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-17 03:06:47 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-02-17 03:04:30 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.010 |  |
| 2026-02-17 00:01:50 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-02-17 03:02:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-17 03:02:00 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-17 02:12:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.024 |  |
| 2026-02-17 03:00:13 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.054 |  |
| 2026-02-17 03:07:06 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-02-16 18:00:50 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |
| 2026-02-17 03:06:24 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.149 |  |
| 2026-02-17 03:06:18 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)