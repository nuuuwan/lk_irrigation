# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_23:33:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 23:33:00 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.007 |  |
| 2026-06-24 23:32:22 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.034 |  |
| 2026-06-24 23:20:34 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:12:04 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2026-06-24 23:10:42 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-06-24 23:10:35 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-06-24 23:09:17 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:09:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:08:14 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-06-24 23:06:28 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-06-24 23:05:31 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:05:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:04:52 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-06-24 23:04:52 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-24 23:03:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-24 23:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:19 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:32 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-06-24 23:02:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:16 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-06-24 23:02:11 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-24 23:01:48 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 23:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.022 |  |
| 2026-06-24 23:01:27 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.060 |  |
| 2026-06-24 23:01:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:21 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-24 23:01:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:06 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:00 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-24 23:03:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-24 23:01:48 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 23:03:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:09:17 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:20:34 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:09:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:01:06 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:19 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:05:31 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:05:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:03:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:02:11 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:33:00 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.007 |  |
| 2026-06-24 23:10:35 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-06-24 23:10:42 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 23:01:21 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-24 23:04:52 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-24 23:04:52 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-06-24 23:01:00 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-06-24 22:01:16 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-06-24 23:08:14 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-06-24 23:02:16 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-06-24 23:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.022 |  |
| 2026-06-24 23:06:28 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-06-24 23:32:22 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.034 |  |
| 2026-06-24 23:02:32 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-06-24 23:12:04 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2026-06-24 23:01:27 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)