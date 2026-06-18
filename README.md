# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_01:23:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 01:23:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.015 |  |
| 2026-06-19 01:23:46 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-06-19 01:23:38 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-19 01:18:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.007 |  |
| 2026-06-19 01:18:14 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-19 01:15:41 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:08:37 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.045 |  |
| 2026-06-19 01:08:10 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 01:07:32 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-19 01:06:44 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 01:06:37 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:05:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:05:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-19 01:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:04:19 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:04:13 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:52 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:49 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2026-06-19 01:03:36 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:03:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 01:03:26 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-06-19 01:03:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 01:02:45 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.063 |  |
| 2026-06-19 01:02:36 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:02:34 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:02:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:01:35 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -2.007 |  |
| 2026-06-19 01:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:00:45 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 01:07:32 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-19 01:08:10 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 01:03:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 01:06:44 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 01:23:38 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-19 01:03:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 01:18:14 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-19 00:01:31 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:00:45 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:52 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:05:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:02:34 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:02:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:05:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:04:13 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:15:41 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:18:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.007 |  |
| 2026-06-19 01:23:46 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-06-19 01:06:37 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:03:36 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:04:19 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-19 01:23:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.015 |  |
| 2026-06-19 01:05:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-19 01:03:26 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-06-18 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-06-19 00:07:17 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-06-19 00:00:34 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2026-06-19 01:03:49 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-19 01:08:37 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.045 |  |
| 2026-06-19 01:02:45 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.063 |  |
| 2026-06-19 01:01:35 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -2.007 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)