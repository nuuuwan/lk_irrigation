# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_16:15:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 16:15:22 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-02-13 16:13:38 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:13:26 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:13:00 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:10:20 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-02-13 16:09:58 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | 0.830 | 🔺 Rising |
| 2026-02-13 16:09:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-02-13 16:08:25 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 16:08:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.037 |  |
| 2026-02-13 16:06:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:06:26 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-02-13 16:04:39 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 16:04:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:04:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:58 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:48 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:45 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-02-13 16:03:27 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:24 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:01 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:02:54 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-13 16:02:49 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:02:44 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 16:02:33 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:02:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-13 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-13 16:02:24 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-02-13 16:02:02 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 16:02:00 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:57 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:57 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.011 |  |
| 2026-02-13 16:01:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-02-13 16:01:16 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-13 16:01:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:09 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:00:33 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:00:30 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-13 16:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.096 |  |
| 2026-02-13 16:00:22 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 16:00:21 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.070 |  |
| 2026-02-13 16:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 16:09:58 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | 0.830 | 🔺 Rising |
| 2026-02-13 16:01:16 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-13 16:02:02 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 16:02:44 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 16:00:22 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 16:04:39 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 16:08:25 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 16:02:33 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:27 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:13:00 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:57 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:02:49 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:13:26 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:24 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:13:38 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:00:33 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:03:01 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:04:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:06:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:04:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:09 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:02:00 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:01:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 16:09:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-02-13 16:10:20 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-02-13 16:01:57 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.011 |  |
| 2026-02-13 16:01:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-02-13 16:02:54 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-13 16:02:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-13 16:06:26 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-02-13 16:02:24 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-02-13 16:00:30 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-13 16:15:22 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-02-13 16:08:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.037 |  |
| 2026-02-13 16:03:45 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-02-13 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-13 16:00:21 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.070 |  |
| 2026-02-13 16:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)