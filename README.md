# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_09:00:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 09:00:57 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:21:31 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.016 |  |
| 2026-02-21 08:16:17 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 08:14:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.082 |  |
| 2026-02-21 08:13:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.054 |  |
| 2026-02-21 08:10:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:09:43 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | -0.036 |  |
| 2026-02-21 08:07:49 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-21 08:07:04 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-02-21 08:06:48 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:06:37 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:06:05 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-21 08:05:47 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-21 08:05:14 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-02-21 08:05:12 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:04:58 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.129 |  |
| 2026-02-21 08:04:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 08:04:52 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -38.400 |  |
| 2026-02-21 08:04:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:04:51 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 08:07:49 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-21 08:01:01 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-02-21 08:05:47 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-21 09:00:57 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 08:03:28 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 08:04:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 08:03:38 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 08:16:17 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 08:02:47 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 07:02:25 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:04:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:00:31 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:02:16 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:10:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:06:48 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:03:38 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:06:37 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:03:57 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:05:12 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:04:51 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 08:06:05 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-21 08:03:00 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-21 08:04:08 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.011 |  |
| 2026-02-21 08:07:04 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-02-21 08:21:31 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.016 |  |
| 2026-02-21 08:03:17 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-21 08:04:21 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-02-21 08:02:17 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-21 08:09:43 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | -0.036 |  |
| 2026-02-21 08:01:24 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.050 |  |
| 2026-02-21 08:13:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.054 |  |
| 2026-02-21 08:05:14 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-02-21 08:14:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.082 |  |
| 2026-02-21 08:00:27 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.121 |  |
| 2026-02-21 08:04:58 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.129 |  |
| 2026-02-21 08:04:52 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -38.400 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)