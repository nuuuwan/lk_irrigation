# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_11:23:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,955 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 11:23:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:16:34 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2026-06-06 11:14:44 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:10:07 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-06-06 11:09:18 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-06 11:09:05 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-06-06 11:08:25 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:07:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-06 11:07:30 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-06 11:06:46 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.065 |  |
| 2026-06-06 11:06:20 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-06-06 11:06:18 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:05:36 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2026-06-06 11:04:55 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:04:54 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-06-06 11:04:49 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:04:44 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.038 |  |
| 2026-06-06 11:04:08 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:03:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.014 |  |
| 2026-06-06 11:03:50 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.050 |  |
| 2026-06-06 11:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:03:00 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:54 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:02:47 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-06-06 11:02:38 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:02:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:02:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:14 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.060 |  |
| 2026-06-06 11:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 11:02:01 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-06 11:02:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:01:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:01:35 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:01:34 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:01:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 11:09:18 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-06 11:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-06 11:07:30 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-06 11:07:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-06 11:02:01 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-06 11:08:25 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:02:54 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:01:35 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:06:18 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 11:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 11:04:08 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:03:00 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:00:35 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:01:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:23:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:21 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:04:49 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:14:44 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:01:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 11:16:34 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2026-06-06 11:04:54 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-06-06 11:00:53 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:01:34 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:02:38 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:02:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-06 11:05:36 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2026-06-06 11:03:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.014 |  |
| 2026-06-06 11:10:07 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-06-06 11:09:05 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-06-06 11:02:47 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-06-06 11:06:20 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-06-06 11:04:44 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.038 |  |
| 2026-06-06 11:03:50 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.050 |  |
| 2026-06-06 11:02:14 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.060 |  |
| 2026-06-06 11:06:46 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)