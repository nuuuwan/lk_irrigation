# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_05:33:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 05:33:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.013 |  |
| 2026-01-13 05:17:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-01-13 05:16:53 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:16:30 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-13 05:10:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:10:01 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:09:33 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-01-13 05:09:16 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-01-13 05:08:29 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.032 |  |
| 2026-01-13 05:07:47 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:07:23 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 05:07:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-13 05:06:03 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 05:05:33 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-01-13 05:05:15 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.065 |  |
| 2026-01-13 05:05:11 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:04:57 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.088 |  |
| 2026-01-13 05:04:05 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 05:03:22 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-01-13 05:02:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:02:57 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:02:51 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:02:50 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 05:02:46 | Horowpothana (Yan Oya) | 3.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-13 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.213 |  |
| 2026-01-13 05:01:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:01:41 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-13 05:01:11 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 05:01:02 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-01-13 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:00:55 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:00:27 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:47:56 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:37:36 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.088 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 05:07:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-13 05:07:23 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 05:02:46 | Horowpothana (Yan Oya) | 3.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-13 05:04:05 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 05:06:03 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 05:02:50 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:01:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:00:55 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:10:44 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:47:56 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:01:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:02:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:16:53 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:05:11 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:10:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:00:27 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:07:47 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:02:51 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:01:11 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 04:03:01 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-13 05:01:41 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-13 05:01:02 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-01-13 05:33:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.013 |  |
| 2026-01-13 05:16:30 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-13 05:09:33 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-01-13 05:05:33 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-01-13 05:09:16 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-01-13 05:08:29 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.032 |  |
| 2026-01-13 05:17:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-01-13 05:03:22 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-01-13 04:11:23 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-01-13 05:05:15 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.065 |  |
| 2026-01-13 05:04:57 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.088 |  |
| 2026-01-13 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)