# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_09:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,458 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 09:18:49 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.028 |  |
| 2026-06-19 09:18:20 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:09:39 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 09:08:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:08:35 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:07:54 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-06-19 09:07:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:06:57 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:06:31 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 09:06:17 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:06:09 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-19 09:06:01 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.049 |  |
| 2026-06-19 09:05:14 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:05:04 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:03:55 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-06-19 09:03:45 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:03:43 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:03:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:03:30 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-06-19 09:03:24 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-06-19 09:03:02 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 09:02:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:02:42 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 09:02:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:13 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:13 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-06-19 09:02:12 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -55.636 |  |
| 2026-06-19 09:01:45 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:01:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:01:24 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-06-19 09:01:18 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-19 09:01:17 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -55.636 |  |
| 2026-06-19 09:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:00:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:00:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:00:19 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.031 |  |
| 2026-06-19 09:00:12 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 09:01:18 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-19 09:06:09 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-19 09:03:02 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 09:02:42 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 09:06:31 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 09:02:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:00:12 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:00:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:08:35 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:05:04 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:05:14 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:01:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:00:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:03:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:18:20 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:13 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:01:45 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:08:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 08:02:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 09:03:30 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-06-19 09:06:17 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:03:43 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:03:45 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:07:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:06:57 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:02:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-19 09:01:24 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-06-19 09:02:13 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-06-19 09:09:39 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 09:07:54 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-06-19 09:18:49 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.028 |  |
| 2026-06-19 09:00:19 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.031 |  |
| 2026-06-19 09:03:24 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-06-19 09:03:55 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-06-19 09:06:01 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.049 |  |
| 2026-06-19 09:02:12 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -55.636 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)