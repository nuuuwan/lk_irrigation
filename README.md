# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_00:29:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 00:29:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:14:03 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-06-19 00:12:35 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:09:01 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:08:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:07:41 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:07:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:07:17 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-06-19 00:06:55 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.018 |  |
| 2026-06-19 00:06:19 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 00:06:17 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 00:05:25 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 00:05:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:05:20 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:05:13 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-19 00:04:42 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -193.714 |  |
| 2026-06-19 00:04:40 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 00:04:00 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | -193.714 |  |
| 2026-06-19 00:03:42 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:03:22 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-19 00:03:11 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-06-19 00:02:42 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:02:31 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.022 |  |
| 2026-06-19 00:02:12 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 00:01:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:56 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:50 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:48 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 2.009 | 🔺 Rising |
| 2026-06-19 00:01:35 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:31 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:26 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-06-19 00:01:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:00:34 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2026-06-18 23:48:25 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 00:01:48 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 2.009 | 🔺 Rising |
| 2026-06-19 00:05:13 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-19 00:03:22 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-19 00:05:25 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 00:02:12 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 00:06:17 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 00:06:19 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 00:04:40 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 00:01:31 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:12:35 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:07:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:35 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:08:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:09:01 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:07:41 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:05:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:56 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:29:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:01:50 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 00:05:20 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:02:42 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:03:42 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 00:03:11 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-06-18 23:48:25 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.012 |  |
| 2026-06-19 00:14:03 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-06-19 00:06:55 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.018 |  |
| 2026-06-18 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-06-19 00:01:26 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-06-19 00:02:31 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.022 |  |
| 2026-06-19 00:07:17 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-06-19 00:00:34 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-18 22:14:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.076 |  |
| 2026-06-19 00:04:42 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -193.714 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)