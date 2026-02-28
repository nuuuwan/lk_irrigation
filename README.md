# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_15:16:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,460 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 15:16:07 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:15:04 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:14:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-28 15:10:35 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:09:54 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:09:32 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:08:56 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-02-28 15:08:19 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:27 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:25 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:05:23 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:05:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:56 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 15:04:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:06 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:04 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.026 |  |
| 2026-02-28 15:03:40 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-28 15:03:37 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:03:32 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:03:16 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.006 |  |
| 2026-02-28 15:03:00 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:02:34 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:02:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 15:02:23 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:22 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:02:18 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:05 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:53 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.111 |  |
| 2026-02-28 15:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:37 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:01:30 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:53 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-28 15:00:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:13 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:00 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 14:25:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 15:00:53 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-28 15:14:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-28 15:02:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 15:00:00 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 15:04:56 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 15:02:23 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:09:32 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:16:07 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:18 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 14:00:36 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:25 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:06 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:08:19 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:15:04 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:09:54 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:30 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:05:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:04:04 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:01:37 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:02:05 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:06:27 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:00:13 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 15:03:16 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.006 |  |
| 2026-02-28 15:03:37 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:02:34 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:03:00 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-28 15:08:56 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-02-28 15:03:40 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-28 15:02:22 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:03:32 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:01:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-02-28 15:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.026 |  |
| 2026-02-28 15:01:53 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)